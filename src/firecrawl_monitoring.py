"""Firecrawl Monitoring: create, list, fetch, and parse monitor results."""

import logging
import os
from dataclasses import dataclass, field

import httpx

logger = logging.getLogger(__name__)

BASE_URL = "https://api.firecrawl.dev/v2"


def _api_key() -> str:
    return os.environ.get("FIRECRAWL_API_KEY", "")


def _headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {_api_key()}",
        "Content-Type": "application/json",
    }


# ---------------------------------------------------------------------------
# Data classes for parsed monitor results
# ---------------------------------------------------------------------------


@dataclass
class MonitorPageResult:
    """A single page result from a Firecrawl monitor check."""

    url: str
    status: str  # same | new | changed | removed | error
    diff_text: str = ""
    is_meaningful: bool | None = None
    judgment_reason: str = ""
    judgment_confidence: str = ""
    meaningful_changes: list[dict] = field(default_factory=list)
    error: str | None = None


@dataclass
class MonitorCheckResult:
    """Parsed result of a single monitor check."""

    check_id: str
    monitor_id: str
    status: str  # queued | running | completed | failed | partial
    summary: dict = field(default_factory=dict)
    pages: list[MonitorPageResult] = field(default_factory=list)

    @property
    def changed_pages(self) -> list[MonitorPageResult]:
        return [p for p in self.pages if p.status == "changed"]

    @property
    def new_pages(self) -> list[MonitorPageResult]:
        return [p for p in self.pages if p.status == "new"]

    @property
    def removed_pages(self) -> list[MonitorPageResult]:
        return [p for p in self.pages if p.status == "removed"]

    @property
    def error_pages(self) -> list[MonitorPageResult]:
        return [p for p in self.pages if p.status == "error"]

    @property
    def meaningful_pages(self) -> list[MonitorPageResult]:
        return [p for p in self.pages if p.is_meaningful is True]


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------


def parse_page_result(raw: dict) -> MonitorPageResult:
    """Parse a single page from a monitor check response or webhook payload."""
    judgment = raw.get("judgment") or {}
    diff = raw.get("diff") or {}

    return MonitorPageResult(
        url=raw.get("url", ""),
        status=raw.get("status", "unknown"),
        diff_text=diff.get("text", ""),
        is_meaningful=raw.get("isMeaningful"),
        judgment_reason=judgment.get("reason", ""),
        judgment_confidence=judgment.get("confidence", ""),
        meaningful_changes=judgment.get("meaningfulChanges", []),
        error=raw.get("error"),
    )


def parse_check_result(raw: dict) -> MonitorCheckResult:
    """Parse a full monitor check response (from GET check endpoint)."""
    data = raw.get("data", raw)

    pages_raw = data.get("pages", [])
    pages = [parse_page_result(p) for p in pages_raw]

    return MonitorCheckResult(
        check_id=data.get("id", ""),
        monitor_id=data.get("monitorId", ""),
        status=data.get("status", "unknown"),
        summary=data.get("summary", {}),
        pages=pages,
    )


def parse_webhook_payload(raw: dict) -> list[MonitorPageResult]:
    """Parse a Firecrawl monitor webhook payload.

    Webhook payloads have type 'monitor.page' or 'monitor.check.completed'.
    The 'data' field is a list of page results.
    """
    data = raw.get("data", [])
    if isinstance(data, dict):
        data = [data]
    return [parse_page_result(p) for p in data]


# ---------------------------------------------------------------------------
# API interactions
# ---------------------------------------------------------------------------


def create_monitor(source: dict) -> dict:
    """Create a Firecrawl monitor from a source definition.

    The source dict should have:
      - name: str
      - url: str
      - mode: "monitor"
      - monitor config: schedule, goal, target_type, etc.
    """
    key = _api_key()
    if not key:
        logger.warning("FIRECRAWL_API_KEY not set, cannot create monitor")
        return {}

    monitor_config = source.get("monitor", {})
    target_type = monitor_config.get("target_type", "crawl")

    target: dict = {"type": target_type}
    if target_type == "scrape":
        target["urls"] = [source["url"]]
    else:
        target["url"] = source["url"]
        crawl_opts: dict = {}
        if "crawl_limit" in monitor_config:
            crawl_opts["limit"] = monitor_config["crawl_limit"]
        if "max_discovery_depth" in monitor_config:
            crawl_opts["maxDiscoveryDepth"] = monitor_config["max_discovery_depth"]
        if "include_paths" in monitor_config:
            crawl_opts["includePaths"] = monitor_config["include_paths"]
        if crawl_opts:
            target["crawlOptions"] = crawl_opts

    body: dict = {
        "name": source.get("name", ""),
        "targets": [target],
    }

    # Schedule
    schedule = monitor_config.get("schedule", {})
    if isinstance(schedule, str):
        schedule = {"text": schedule, "timezone": "UTC"}
    if schedule:
        body["schedule"] = schedule
        if "timezone" not in body["schedule"]:
            body["schedule"]["timezone"] = monitor_config.get("timezone", "UTC")

    # Goal
    if "goal" in monitor_config:
        body["goal"] = monitor_config["goal"]

    # Notification
    notification_mode = monitor_config.get("notification", "none")
    if notification_mode == "webhook":
        webhook_url = monitor_config.get("webhook_url", "")
        if webhook_url:
            body["webhook"] = {
                "url": webhook_url,
                "events": ["monitor.page", "monitor.check.completed"],
            }
    elif notification_mode == "email":
        recipients = monitor_config.get("email_recipients", [])
        if recipients:
            body["notification"] = {
                "email": {
                    "enabled": True,
                    "recipients": recipients,
                    "includeDiffs": True,
                }
            }

    resp = httpx.post(
        f"{BASE_URL}/monitor",
        headers=_headers(),
        json=body,
        timeout=30,
    )
    resp.raise_for_status()
    result = resp.json()
    logger.info("Created monitor '%s': %s", source.get("name"), result.get("data", {}).get("id", ""))
    return result.get("data", {})


def list_monitors() -> list[dict]:
    """List all configured Firecrawl monitors."""
    key = _api_key()
    if not key:
        logger.warning("FIRECRAWL_API_KEY not set, cannot list monitors")
        return []

    resp = httpx.get(
        f"{BASE_URL}/monitor",
        headers=_headers(),
        timeout=30,
    )
    resp.raise_for_status()
    result = resp.json()
    return result.get("data", [])


def get_latest_check(monitor_id: str) -> MonitorCheckResult | None:
    """Get the latest completed check for a monitor."""
    key = _api_key()
    if not key:
        return None

    # List checks, filter to completed, take most recent
    resp = httpx.get(
        f"{BASE_URL}/monitor/{monitor_id}/checks",
        headers=_headers(),
        params={"limit": 1, "status": "completed"},
        timeout=30,
    )
    resp.raise_for_status()
    result = resp.json()
    checks = result.get("data", [])

    if not checks:
        return None

    check_id = checks[0].get("id", "")
    return get_check_detail(monitor_id, check_id)


def get_check_detail(monitor_id: str, check_id: str) -> MonitorCheckResult:
    """Get detailed results for a specific monitor check, with pagination."""
    all_pages: list[MonitorPageResult] = []
    check_data: dict = {}
    url: str | None = f"{BASE_URL}/monitor/{monitor_id}/checks/{check_id}"

    while url:
        resp = httpx.get(url, headers=_headers(), timeout=30)
        resp.raise_for_status()
        raw = resp.json()

        if not check_data:
            check_data = raw.get("data", {})

        pages_raw = check_data.get("pages", []) if not all_pages else raw.get("data", {}).get("pages", [])
        all_pages.extend(parse_page_result(p) for p in pages_raw)

        url = raw.get("next")

    return MonitorCheckResult(
        check_id=check_data.get("id", check_id),
        monitor_id=check_data.get("monitorId", monitor_id),
        status=check_data.get("status", "unknown"),
        summary=check_data.get("summary", {}),
        pages=all_pages,
    )


def run_monitor_check(monitor_id: str) -> dict:
    """Trigger a manual run of a monitor. Returns the check info."""
    key = _api_key()
    if not key:
        logger.warning("FIRECRAWL_API_KEY not set, cannot run monitor")
        return {}

    resp = httpx.post(
        f"{BASE_URL}/monitor/{monitor_id}/run",
        headers=_headers(),
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json().get("data", {})


def fetch_monitor_results(sources: list[dict]) -> dict[str, MonitorCheckResult]:
    """Fetch latest check results for all monitor-mode sources.

    Returns {source_name: MonitorCheckResult}.
    Sources must have a 'monitor_id' field set.
    """
    results = {}
    for source in sources:
        if source.get("mode") != "monitor":
            continue
        monitor_id = source.get("monitor_id", "")
        if not monitor_id:
            logger.warning("Source '%s' has mode=monitor but no monitor_id", source.get("name"))
            continue

        try:
            check = get_latest_check(monitor_id)
            if check:
                results[source["name"]] = check
                logger.info(
                    "Fetched monitor results for %s: %d pages (%d changed)",
                    source["name"],
                    len(check.pages),
                    len(check.changed_pages),
                )
        except Exception as exc:
            logger.error("Failed to fetch monitor results for %s: %s", source.get("name"), exc)

    return results

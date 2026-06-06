"""Diff engine: compare snapshots, detect changes, score importance, classify."""

import json
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path

from .normalize import normalize_markdown, strip_frontmatter

logger = logging.getLogger(__name__)

SNAPSHOTS_DIR = Path("90 - Raw Snapshots")

# Change categories for classification
CHANGE_CATEGORIES = [
    "product",
    "pricing",
    "security",
    "deployment",
    "integration",
    "competitor",
    "docs-only",
    "minor wording",
    "unknown",
]

# Keywords for heuristic classification
_CATEGORY_KEYWORDS: dict[str, list[str]] = {
    "pricing": ["price", "pricing", "plan", "tier", "cost", "billing", "subscription", "credit", "free", "enterprise plan", "pro plan"],
    "security": ["security", "auth", "sso", "rbac", "permission", "encryption", "compliance", "audit", "vulnerability", "cve"],
    "deployment": ["deploy", "install", "setup", "self-host", "on-prem", "cloud", "docker", "kubernetes", "infrastructure"],
    "integration": ["integrat", "plugin", "extension", "api", "sdk", "mcp", "webhook", "connect", "third-party"],
    "competitor": ["vs", "versus", "compared", "alternative", "switch", "migrat"],
    "product": ["feature", "launch", "release", "new", "update", "capability", "agent", "model", "performance", "benchmark"],
}


@dataclass
class PageChange:
    """A detected change in a single page."""

    source: str
    page_file: str
    url: str
    score: int  # 1 (trivial) to 5 (major)
    old_snippet: str
    new_snippet: str
    change_summary: str
    category: str = "unknown"


@dataclass
class DiffReport:
    """Aggregated diff report for a source."""

    source: str
    old_date: str
    new_date: str
    mode: str = "local"  # "local" or "monitor"
    changes: list[PageChange] = field(default_factory=list)
    new_pages: list[str] = field(default_factory=list)
    removed_pages: list[str] = field(default_factory=list)

    @property
    def significant_changes(self) -> list[PageChange]:
        """Return changes with score >= 3."""
        return [c for c in self.changes if c.score >= 3]


def get_snapshot_dates(source_name: str) -> list[str]:
    """List available snapshot dates for a source, sorted ascending."""
    source_dir = SNAPSHOTS_DIR / source_name
    if not source_dir.exists():
        return []
    dates = sorted(
        d.name
        for d in source_dir.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    )
    return dates


def load_snapshot_pages(source_name: str, snapshot_date: str) -> dict[str, str]:
    """Load all pages from a snapshot as {filename: normalized_content}."""
    snap_dir = SNAPSHOTS_DIR / source_name / snapshot_date
    pages = {}
    for f in snap_dir.glob("*.md"):
        raw = f.read_text(errors="replace")
        content = strip_frontmatter(raw)
        pages[f.name] = normalize_markdown(content)
    return pages


def score_change(old_text: str, new_text: str) -> int:
    """Score a change from 1 (trivial) to 5 (major).

    Heuristics:
    - Tiny changes (< 50 chars diff) -> 1
    - Small changes (< 200 chars diff) -> 2
    - Medium changes (< 500 chars diff) -> 3
    - Large changes (< 2000 chars diff) -> 4
    - Very large changes -> 5
    """
    if old_text == new_text:
        return 0

    # Simple character-level diff size
    len_diff = abs(len(new_text) - len(old_text))

    # Line-level diff
    old_lines = set(old_text.splitlines())
    new_lines = set(new_text.splitlines())
    added_lines = new_lines - old_lines
    removed_lines = old_lines - new_lines
    changed_line_count = len(added_lines) + len(removed_lines)

    # Combined heuristic
    diff_size = len_diff + (changed_line_count * 20)

    if diff_size < 50:
        return 1
    elif diff_size < 200:
        return 2
    elif diff_size < 500:
        return 3
    elif diff_size < 2000:
        return 4
    else:
        return 5


def extract_diff_snippet(old_text: str, new_text: str, max_lines: int = 20) -> tuple[str, str]:
    """Extract the most relevant changed portion for display."""
    old_lines = old_text.splitlines()
    new_lines = new_text.splitlines()

    # Find first differing line
    start = 0
    found_diff = False
    for i, (ol, nl) in enumerate(zip(old_lines, new_lines)):
        if ol != nl:
            start = max(0, i - 2)
            found_diff = True
            break

    # If no inline diff found, the change is appended/removed at the end
    if not found_diff and len(old_lines) != len(new_lines):
        start = max(0, min(len(old_lines), len(new_lines)) - 2)

    old_snippet = "\n".join(old_lines[start : start + max_lines])
    new_snippet = "\n".join(new_lines[start : start + max_lines])
    return old_snippet, new_snippet


def diff_source(source_name: str, old_date: str | None = None, new_date: str | None = None) -> DiffReport | None:
    """Compare two snapshots of a source. Uses the two most recent if dates not given."""
    dates = get_snapshot_dates(source_name)
    if len(dates) < 2:
        logger.info("Not enough snapshots for %s to diff (have %d)", source_name, len(dates))
        return None

    if old_date is None:
        old_date = dates[-2]
    if new_date is None:
        new_date = dates[-1]

    old_pages = load_snapshot_pages(source_name, old_date)
    new_pages = load_snapshot_pages(source_name, new_date)

    report = DiffReport(source=source_name, old_date=old_date, new_date=new_date)

    # Detect new and removed pages
    old_names = set(old_pages.keys())
    new_names = set(new_pages.keys())
    report.new_pages = sorted(new_names - old_names)
    report.removed_pages = sorted(old_names - new_names)

    # Diff common pages
    common = old_names & new_names
    for page_name in sorted(common):
        old_text = old_pages[page_name]
        new_text = new_pages[page_name]

        if old_text == new_text:
            continue

        score = score_change(old_text, new_text)
        if score == 0:
            continue

        old_snippet, new_snippet = extract_diff_snippet(old_text, new_text)

        change = PageChange(
            source=source_name,
            page_file=page_name,
            url="",  # Could be extracted from frontmatter
            score=score,
            old_snippet=old_snippet,
            new_snippet=new_snippet,
            change_summary=f"Score {score} change in {page_name}",
            category=classify_change(old_snippet + " " + new_snippet),
        )
        report.changes.append(change)

    return report


def run_diff(source_names: list[str] | None = None) -> list[DiffReport]:
    """Run diffs for all sources (or given list). Returns list of reports."""
    if source_names is None:
        # Discover from snapshot directory
        if not SNAPSHOTS_DIR.exists():
            return []
        source_names = sorted(
            d.name for d in SNAPSHOTS_DIR.iterdir() if d.is_dir() and not d.name.startswith(".")
        )

    reports = []
    for name in source_names:
        report = diff_source(name)
        if report and (report.changes or report.new_pages or report.removed_pages):
            reports.append(report)

    return reports


# ---------------------------------------------------------------------------
# Change classification
# ---------------------------------------------------------------------------


def classify_change(text: str) -> str:
    """Classify a change into a category based on keyword heuristics.

    Returns one of the CHANGE_CATEGORIES values.
    """
    text_lower = text.lower()

    scores: dict[str, int] = {}
    for category, keywords in _CATEGORY_KEYWORDS.items():
        count = sum(1 for kw in keywords if kw in text_lower)
        if count > 0:
            scores[category] = count

    if not scores:
        # Check for minor wording vs docs-only
        word_count = len(text.split())
        if word_count < 30:
            return "minor wording"
        return "docs-only"

    return max(scores, key=scores.get)  # type: ignore[arg-type]


def score_firecrawl_diff(diff_text: str, judgment: dict | None = None) -> int:
    """Score a Firecrawl monitor diff.

    Uses Firecrawl judgment when available, falls back to diff size heuristic.
    """
    if judgment:
        meaningful = judgment.get("meaningful", False)
        confidence = judgment.get("confidence", "low")

        if not meaningful:
            return 1

        if confidence == "high":
            changes = judgment.get("meaningfulChanges", [])
            if len(changes) >= 3:
                return 5
            if len(changes) >= 2:
                return 4
            return 3
        elif confidence == "medium":
            return 3
        else:
            return 2

    # Fallback: score by diff text size
    if not diff_text:
        return 0

    lines = [l for l in diff_text.splitlines() if l.startswith("+") or l.startswith("-")]
    changed_lines = len(lines)

    if changed_lines < 3:
        return 1
    elif changed_lines < 10:
        return 2
    elif changed_lines < 25:
        return 3
    elif changed_lines < 80:
        return 4
    else:
        return 5


def build_monitor_diff_report(
    source_name: str,
    check_result: "MonitorCheckResult",
) -> DiffReport:
    """Build a DiffReport from Firecrawl monitor check results.

    Scores and classifies Firecrawl-reported changes rather than
    duplicating the diff that Firecrawl already computed.
    """
    from .firecrawl_monitoring import MonitorCheckResult

    report = DiffReport(
        source=source_name,
        old_date="(monitor-previous)",
        new_date="(monitor-latest)",
        mode="monitor",
    )

    for page in check_result.new_pages:
        report.new_pages.append(page.url)

    for page in check_result.removed_pages:
        report.removed_pages.append(page.url)

    for page in check_result.changed_pages:
        judgment = None
        if page.meaningful_changes:
            judgment = {
                "meaningful": page.is_meaningful,
                "confidence": page.judgment_confidence,
                "meaningfulChanges": page.meaningful_changes,
            }

        score = score_firecrawl_diff(page.diff_text, judgment)

        # Build a summary from judgment or diff
        summary = page.judgment_reason or f"Changed page: {page.url}"
        diff_content = page.diff_text or summary

        change = PageChange(
            source=source_name,
            page_file=page.url,
            url=page.url,
            score=score,
            old_snippet="",
            new_snippet=page.diff_text[:500] if page.diff_text else "",
            change_summary=summary,
            category=classify_change(diff_content),
        )
        report.changes.append(change)

    return report

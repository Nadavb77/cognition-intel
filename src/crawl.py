"""Crawl sources using Firecrawl or Tavily APIs."""

import os
import json
import logging
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import httpx
import yaml

logger = logging.getLogger(__name__)

SNAPSHOTS_DIR = Path("90 - Raw Snapshots")
SOURCES_FILE = Path("03 - Sources/sources.yaml")


def load_sources(path: Path | None = None) -> list[dict]:
    """Load source definitions from sources.yaml."""
    path = path or SOURCES_FILE
    with open(path) as f:
        data = yaml.safe_load(f)
    return data.get("sources", [])


def crawl_firecrawl(url: str) -> list[dict]:
    """Crawl a URL using the Firecrawl API. Returns a list of pages."""
    api_key = os.environ.get("FIRECRAWL_API_KEY", "")
    if not api_key:
        logger.warning("FIRECRAWL_API_KEY not set, skipping %s", url)
        return []

    base_url = os.environ.get("FIRECRAWL_API_URL", "https://api.firecrawl.dev/v1")

    # Start a crawl job
    resp = httpx.post(
        f"{base_url}/crawl",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "url": url,
            "limit": 50,
            "scrapeOptions": {"formats": ["markdown"]},
        },
        timeout=60,
    )
    resp.raise_for_status()
    job = resp.json()

    if not job.get("success"):
        logger.error("Firecrawl crawl failed for %s: %s", url, job)
        return []

    job_id = job.get("id")
    if not job_id:
        # Synchronous response with data directly
        return job.get("data", [])

    # Poll for completion
    import time

    for _ in range(60):
        time.sleep(5)
        status_resp = httpx.get(
            f"{base_url}/crawl/{job_id}",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30,
        )
        status_resp.raise_for_status()
        status = status_resp.json()
        if status.get("status") == "completed":
            return status.get("data", [])
        if status.get("status") == "failed":
            logger.error("Firecrawl job failed for %s", url)
            return []

    logger.warning("Firecrawl job timed out for %s", url)
    return []


def crawl_tavily(url: str) -> list[dict]:
    """Crawl a URL using the Tavily Extract API. Returns a list of pages."""
    api_key = os.environ.get("TAVILY_API_KEY", "")
    if not api_key:
        logger.warning("TAVILY_API_KEY not set, skipping %s", url)
        return []

    resp = httpx.post(
        "https://api.tavily.com/extract",
        json={"api_key": api_key, "urls": [url]},
        timeout=60,
    )
    resp.raise_for_status()
    data = resp.json()

    pages = []
    for result in data.get("results", []):
        pages.append(
            {
                "url": result.get("url", url),
                "markdown": result.get("raw_content", ""),
                "metadata": {"title": result.get("url", "")},
            }
        )
    return pages


def crawl_source(source: dict) -> list[dict]:
    """Crawl a single source using the configured method."""
    method = source.get("crawl_method", "firecrawl")
    url = source["url"]
    logger.info("Crawling %s via %s", url, method)

    if method == "firecrawl":
        return crawl_firecrawl(url)
    elif method == "tavily":
        return crawl_tavily(url)
    else:
        logger.error("Unknown crawl method: %s", method)
        return []


def save_snapshot(source_name: str, pages: list[dict], snapshot_date: str | None = None) -> Path:
    """Save crawled pages as Markdown files under 90 - Raw Snapshots."""
    snapshot_date = snapshot_date or date.today().isoformat()
    out_dir = SNAPSHOTS_DIR / source_name / snapshot_date
    out_dir.mkdir(parents=True, exist_ok=True)

    for i, page in enumerate(pages):
        url = page.get("url", f"page-{i}")
        slug = urlparse(url).path.strip("/").replace("/", "_") or f"page-{i}"
        slug = slug[:80]  # Truncate long slugs

        md_content = page.get("markdown", "")
        title = page.get("metadata", {}).get("title", slug)

        filepath = out_dir / f"{slug}.md"
        filepath.write_text(
            f"---\nurl: {url}\ntitle: {title}\ndate: {snapshot_date}\n---\n\n{md_content}\n"
        )

    # Write manifest
    manifest = {
        "source": source_name,
        "date": snapshot_date,
        "page_count": len(pages),
        "pages": [p.get("url", f"page-{i}") for i, p in enumerate(pages)],
    }
    (out_dir / "_manifest.json").write_text(json.dumps(manifest, indent=2))

    logger.info("Saved %d pages for %s to %s", len(pages), source_name, out_dir)
    return out_dir


def run_crawl(sources: list[dict] | None = None) -> dict[str, Path]:
    """Crawl all sources and save snapshots. Returns {source_name: snapshot_dir}."""
    if sources is None:
        sources = load_sources()

    results = {}
    for source in sources:
        name = source["name"]
        try:
            pages = crawl_source(source)
            if pages:
                results[name] = save_snapshot(name, pages)
            else:
                logger.warning("No pages returned for %s", name)
        except Exception:
            logger.exception("Failed to crawl %s", name)

    return results

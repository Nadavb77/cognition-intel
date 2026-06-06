"""Create Firecrawl monitors for all monitor-mode sources and save IDs back to sources.yaml."""

import argparse
import logging
import sys
import time
from pathlib import Path

import yaml

from .crawl import load_sources
from .firecrawl_monitoring import create_monitor, list_monitors

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

SOURCES_FILE = Path("03 - Sources/sources.yaml")


def _save_sources(sources: list[dict], path: Path | None = None) -> None:
    """Write sources back to sources.yaml preserving structure."""
    path = path or SOURCES_FILE
    data = {"sources": sources}
    with open(path, "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    logger.info("Saved sources to %s", path)


def setup_monitors(dry_run: bool = False) -> dict[str, str]:
    """Create Firecrawl monitors for all sources with mode=monitor.

    Skips sources that already have a monitor_id set.
    Returns {source_name: monitor_id} for created monitors.
    """
    sources = load_sources()
    created: dict[str, str] = {}
    skipped: list[str] = []

    for source in sources:
        if source.get("mode") != "monitor":
            continue

        name = source["name"]

        # Skip if already has a monitor_id
        if source.get("monitor_id"):
            logger.info("Skipping %s (already has monitor_id=%s)", name, source["monitor_id"])
            skipped.append(name)
            continue

        if dry_run:
            logger.info("[DRY RUN] Would create monitor for %s (%s)", name, source["url"])
            continue

        logger.info("Creating monitor for %s (%s)...", name, source["url"])
        for attempt in range(5):
            try:
                result = create_monitor(source)
                monitor_id = result.get("id", "")
                if monitor_id:
                    source["monitor_id"] = monitor_id
                    created[name] = monitor_id
                    logger.info("Created monitor for %s: %s", name, monitor_id)
                else:
                    logger.error("No monitor ID returned for %s: %s", name, result)
                break
            except Exception as exc:
                if "429" in str(exc) and attempt < 4:
                    wait = 5 * (2 ** attempt)  # 5, 10, 20, 40s
                    logger.info("Rate limited, retrying in %ds...", wait)
                    time.sleep(wait)
                else:
                    logger.error("Failed to create monitor for %s: %s", name, exc)
                    break
        # Pause between sources to avoid rate limits
        time.sleep(3)

    if created and not dry_run:
        _save_sources(sources)
        logger.info("Saved %d monitor IDs to sources.yaml", len(created))

    # Summary
    logger.info("=== Monitor Setup Summary ===")
    logger.info("Created: %d", len(created))
    logger.info("Skipped (already configured): %d", len(skipped))
    for name, mid in created.items():
        logger.info("  %s -> %s", name, mid)

    return created


def verify_monitors() -> None:
    """List all Firecrawl monitors and verify they match sources.yaml."""
    sources = load_sources()
    monitor_sources = {s["name"]: s.get("monitor_id") for s in sources if s.get("mode") == "monitor"}

    logger.info("Fetching monitors from Firecrawl API...")
    monitors = list_monitors()

    logger.info("Found %d monitors in Firecrawl account", len(monitors))
    for m in monitors:
        mid = m.get("id", "")
        mname = m.get("name", "unknown")
        status = m.get("status", "unknown")
        logger.info("  [%s] %s (id=%s)", status, mname, mid)

    # Check which sources have valid monitor IDs
    logger.info("=== Source → Monitor Mapping ===")
    api_ids = {m.get("id") for m in monitors}
    for name, mid in monitor_sources.items():
        if not mid:
            logger.warning("  %s: NO monitor_id configured", name)
        elif mid in api_ids:
            logger.info("  %s: %s (verified)", name, mid)
        else:
            logger.warning("  %s: %s (NOT FOUND in Firecrawl account!)", name, mid)


def cli() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Create and manage Firecrawl monitors")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    create_parser = subparsers.add_parser("create", help="Create monitors for all monitor-mode sources")
    create_parser.add_argument("--dry-run", action="store_true", help="Show what would be created without making API calls")

    subparsers.add_parser("verify", help="Verify monitors match sources.yaml")
    subparsers.add_parser("list", help="List all Firecrawl monitors")

    args = parser.parse_args()

    if args.command == "create":
        setup_monitors(dry_run=args.dry_run)
    elif args.command == "verify":
        verify_monitors()
    elif args.command == "list":
        monitors = list_monitors()
        for m in monitors:
            logger.info("[%s] %s (id=%s)", m.get("status", "?"), m.get("name", "?"), m.get("id", "?"))
    else:
        parser.print_help()


if __name__ == "__main__":
    cli()

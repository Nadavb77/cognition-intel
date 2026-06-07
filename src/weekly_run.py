"""Weekly pipeline orchestrator: crawl/monitor -> diff -> summarize -> write."""

import argparse
import logging
import sys
from datetime import date
from pathlib import Path

from .crawl import load_sources, run_crawl
from .diff_engine import DiffReport, build_monitor_diff_report, run_diff
from .firecrawl_monitoring import fetch_monitor_results
from .summarize import summarize_all
from .write_markdown import write_digest, write_questions

SNAPSHOTS_DIR = Path("90 - Raw Snapshots")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def main(skip_crawl: bool = False) -> None:
    """Run the full weekly pipeline."""
    today = date.today().isoformat()
    logger.info("=== Weekly Intel Run: %s ===", today)

    sources = load_sources()
    crawl_sources = [s for s in sources if s.get("mode", "crawl") in ("crawl", "scrape")]
    monitor_sources = [s for s in sources if s.get("mode") == "monitor"]

    all_reports: list[DiffReport] = []

    # Track per-source status for the digest
    source_statuses: dict[str, str] = {}
    for s in sources:
        source_statuses[s["name"]] = "pending"

    # Step 1a: Crawl non-monitor sources
    if not skip_crawl and crawl_sources:
        logger.info("Step 1a: Crawling %d sources...", len(crawl_sources))
        snapshot_dirs = run_crawl(crawl_sources)
        logger.info("Crawled %d sources", len(snapshot_dirs))
        for s in crawl_sources:
            if s["name"] in snapshot_dirs:
                source_statuses[s["name"]] = "checked"
            else:
                source_statuses[s["name"]] = "crawl failed or returned no pages"
    elif crawl_sources:
        logger.info("Step 1a: Skipping crawl (--skip-crawl)")
        for s in crawl_sources:
            source_statuses[s["name"]] = "skipped (--skip-crawl)"

    # Step 1b: Fetch Firecrawl monitor results
    if monitor_sources:
        logger.info("Step 1b: Fetching monitor results for %d sources...", len(monitor_sources))
        monitor_results = fetch_monitor_results(monitor_sources)
        logger.info("Got monitor results for %d sources", len(monitor_results))

        for s in monitor_sources:
            name = s["name"]
            if name in monitor_results:
                source_statuses[name] = "checked"
            elif not s.get("monitor_id"):
                source_statuses[name] = "missing monitor_id"
            else:
                source_statuses[name] = "no completed checks yet"

        for source_name, check_result in monitor_results.items():
            report = build_monitor_diff_report(source_name, check_result)
            if report.changes or report.new_pages or report.removed_pages:
                all_reports.append(report)
                logger.info(
                    "Monitor %s: %d changes, %d new, %d removed",
                    source_name,
                    len(report.changes),
                    len(report.new_pages),
                    len(report.removed_pages),
                )
    else:
        logger.info("Step 1b: No monitor sources configured")

    # Step 2: Diff local snapshots (for crawl-mode sources)
    logger.info("Step 2: Running local diffs...")
    local_reports = run_diff()
    all_reports.extend(local_reports)
    logger.info("Found %d sources with local changes", len(local_reports))

    significant_count = sum(len(r.significant_changes) for r in all_reports)
    logger.info("Total significant changes (score >= 3): %d", significant_count)

    # Determine if this is a baseline run: true only when no source has
    # prior snapshots to compare against (first-ever run).
    def _is_first_run() -> bool:
        if all_reports:
            return False
        for s in sources:
            snap_dir = SNAPSHOTS_DIR / s["name"]
            if snap_dir.exists() and len(list(snap_dir.iterdir())) >= 2:
                return False  # has 2+ snapshots → not baseline
        # Also false if any source failed
        if any("failed" in v or "missing" in v for v in source_statuses.values()):
            return False
        return True

    is_baseline = _is_first_run()

    if not all_reports:
        logger.info("No changes detected. Writing digest with source status.")
        write_digest(
            {},
            digest_date=today,
            source_statuses=source_statuses,
            is_baseline=is_baseline,
        )
        return

    # Step 3: Summarize via OpenAI
    logger.info("Step 3: Summarizing changes...")
    summaries = summarize_all(all_reports)
    logger.info("Generated summaries for %d sources", len(summaries))

    # Mark sources with significant changes
    for source_name in summaries:
        source_statuses[source_name] = "significant changes detected"

    # Step 4: Write Markdown output
    logger.info("Step 4: Writing Markdown...")
    digest_path = write_digest(
        summaries,
        digest_date=today,
        reports=all_reports,
        source_statuses=source_statuses,
        is_baseline=is_baseline,
    )
    questions_path = write_questions(summaries, digest_date=today)

    logger.info("=== Done ===")
    logger.info("Digest: %s", digest_path)
    if questions_path:
        logger.info("Questions: %s", questions_path)


def cli() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Run the weekly intel pipeline")
    parser.add_argument(
        "--skip-crawl",
        action="store_true",
        help="Skip the crawl step (use existing snapshots)",
    )
    args = parser.parse_args()
    main(skip_crawl=args.skip_crawl)


if __name__ == "__main__":
    cli()

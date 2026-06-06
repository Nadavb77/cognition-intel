"""Weekly pipeline orchestrator: crawl -> diff -> summarize -> write."""

import argparse
import logging
import sys
from datetime import date

from .crawl import load_sources, run_crawl
from .diff_engine import run_diff
from .summarize import summarize_all
from .write_markdown import write_digest, write_questions

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def main(skip_crawl: bool = False) -> None:
    """Run the full weekly pipeline."""
    today = date.today().isoformat()
    logger.info("=== Weekly Intel Run: %s ===", today)

    # Step 1: Crawl sources
    if not skip_crawl:
        logger.info("Step 1: Crawling sources...")
        sources = load_sources()
        snapshot_dirs = run_crawl(sources)
        logger.info("Crawled %d sources", len(snapshot_dirs))
    else:
        logger.info("Step 1: Skipping crawl (--skip-crawl)")

    # Step 2: Diff against previous snapshots
    logger.info("Step 2: Running diffs...")
    diff_reports = run_diff()
    logger.info("Found %d sources with changes", len(diff_reports))

    significant_count = sum(len(r.significant_changes) for r in diff_reports)
    logger.info("Total significant changes (score >= 3): %d", significant_count)

    if not diff_reports:
        logger.info("No changes detected. Writing empty digest.")
        write_digest({}, digest_date=today)
        return

    # Step 3: Summarize via OpenAI
    logger.info("Step 3: Summarizing changes...")
    summaries = summarize_all(diff_reports)
    logger.info("Generated summaries for %d sources", len(summaries))

    # Step 4: Write Markdown output
    logger.info("Step 4: Writing Markdown...")
    digest_path = write_digest(summaries, digest_date=today)
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

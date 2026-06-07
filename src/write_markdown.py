"""Write weekly digest and related Markdown notes."""

import logging
from datetime import date
from pathlib import Path

from .diff_engine import DiffReport

logger = logging.getLogger(__name__)

DIGESTS_DIR = Path("01 - Weekly Digests")
QUESTIONS_DIR = Path("07 - Questions to Validate")

# Map common concept names to wiki-link targets
CONCEPT_LINKS = {
    "Agent Harness": "[[Agent Harness]]",
    "Devin Harness": "[[Devin Harness]]",
    "Devin": "[[Devin]]",
    "Claude Code": "[[Claude Code]]",
    "GitHub Copilot": "[[GitHub Copilot]]",
    "Cursor": "[[Cursor]]",
    "Factory": "[[Factory]]",
    "CodeRabbit": "[[CodeRabbit]]",
    "Enterprise Deployment": "[[Enterprise Deployment]]",
    "Verification Loop": "[[Verification Loop]]",
    "MCP": "[[MCP]]",
    "DeepWiki": "[[DeepWiki]]",
    "Devbox": "[[Devbox]]",
}


def concept_to_link(name: str) -> str:
    """Convert a concept name to a wiki link."""
    return CONCEPT_LINKS.get(name, f"[[{name}]]")


def format_source_section(source_name: str, summaries: list[dict]) -> str:
    """Format summaries for a single source into a Markdown section."""
    lines = [f"### {source_name}", ""]

    for i, s in enumerate(summaries, 1):
        what = s.get("what_changed", "Unknown change")
        why = s.get("why_it_matters", "")
        bias = s.get("bias_risk", "")
        sales = s.get("sales_implication", "")
        question = s.get("question_to_validate", "")
        concepts = s.get("related_concepts", [])
        category = s.get("category", "")

        lines.append(f"#### {i}. {what}")
        lines.append("")
        if category:
            lines.append(f"**Category:** `{category}`")
            lines.append("")
        if why:
            lines.append(f"**Why it matters:** {why}")
            lines.append("")
        if bias:
            lines.append(f"**Bias risk:** {bias}")
            lines.append("")
        if sales:
            lines.append(f"**Sales implication:** {sales}")
            lines.append("")
        if question:
            lines.append(f"**Question to validate:** {question}")
            lines.append("")
        if concepts:
            links = ", ".join(concept_to_link(c) for c in concepts)
            lines.append(f"**Related:** {links}")
            lines.append("")

    return "\n".join(lines)


def _group_sources_by_mode(
    summaries_by_source: dict[str, list[dict]],
    reports: list[DiffReport] | None = None,
) -> dict[str, dict[str, list[dict]]]:
    """Group sources into sections by mode (monitor / tavily / crawl).

    Returns {"monitor": {...}, "tavily": {...}, "crawl": {...}}.
    """
    mode_map: dict[str, str] = {}
    if reports:
        for r in reports:
            if r.mode == "monitor":
                mode_map[r.source] = "monitor"

    groups: dict[str, dict[str, list[dict]]] = {
        "monitor": {},
        "tavily": {},
        "crawl": {},
    }

    for source_name, summaries in summaries_by_source.items():
        mode = mode_map.get(source_name, "crawl")
        groups[mode][source_name] = summaries

    return groups


def _write_minor_changes_section(
    lines: list[str],
    reports: list[DiffReport],
) -> None:
    """Append a section listing minor changes that were ignored."""
    lines.append("## Minor Changes Ignored")
    lines.append("")
    for report in reports:
        lines.append(f"### {report.source}")
        lines.append("")
        if report.changes:
            for change in report.changes:
                lines.append(
                    f"- **{change.url or change.page_file}** "
                    f"(score {change.score}, {change.category}): "
                    f"{change.change_summary}"
                )
        if report.new_pages:
            for page in report.new_pages:
                lines.append(f"- **New page**: {page}")
        if report.removed_pages:
            for page in report.removed_pages:
                lines.append(f"- **Removed page**: {page}")
        lines.append("")


def _write_source_status_section(
    lines: list[str],
    source_statuses: dict[str, str],
) -> None:
    """Append the Sources Checked section."""
    lines.append("## Sources Checked")
    lines.append("")
    for name, status in source_statuses.items():
        lines.append(f"- **{name}**: {status}")
    lines.append("")


def _write_system_status_section(
    lines: list[str],
    source_statuses: dict[str, str],
) -> None:
    """Append the System Status section."""
    total = len(source_statuses)
    checked = sum(1 for v in source_statuses.values() if v.startswith("checked") or v == "significant changes detected")
    failed = sum(1 for v in source_statuses.values() if "failed" in v or "missing" in v)
    skipped = sum(1 for v in source_statuses.values() if "skipped" in v)

    lines.append("## System Status")
    lines.append("")
    lines.append(f"- {checked}/{total} sources checked successfully")
    if failed:
        lines.append(f"- {failed} failed source{'s' if failed != 1 else ''}")
    else:
        lines.append("- 0 failed sources")
    if skipped:
        lines.append(f"- {skipped} skipped source{'s' if skipped != 1 else ''}")
    lines.append("- No secrets printed")
    lines.append("- Digest generated successfully")
    lines.append("")


def write_digest(
    summaries_by_source: dict[str, list[dict]],
    digest_date: str | None = None,
    reports: list[DiffReport] | None = None,
    source_statuses: dict[str, str] | None = None,
    is_baseline: bool = False,
) -> Path:
    """Write the weekly digest note.

    If reports are provided, the digest separates changes by source mode:
    - Firecrawl monitored changes
    - Tavily-discovered external updates
    - Manual/source-list crawl changes

    source_statuses maps source name -> status string for audit trail.
    is_baseline indicates this is the first run with no prior data.
    """
    digest_date = digest_date or date.today().isoformat()
    DIGESTS_DIR.mkdir(parents=True, exist_ok=True)

    filename = f"{digest_date} - Weekly AI Coding Agents Digest.md"
    filepath = DIGESTS_DIR / filename

    lines = [
        "# Weekly AI Coding Agents Digest",
        "",
        f"**Date:** {digest_date}",
        "",
        "---",
        "",
    ]

    has_minor_changes = not summaries_by_source and reports

    if not summaries_by_source:
        # Rich "no changes" / "minor changes only" digest
        lines.append("## Executive Summary")
        lines.append("")
        if is_baseline:
            lines.append(
                "Baseline run — monitors were checked for the first time. "
                "No previous snapshots to compare against. Future runs will "
                "detect changes relative to this baseline."
            )
        elif has_minor_changes:
            lines.append(
                "Minor changes were detected but none scored high enough "
                "(score \u2265 3) to warrant summarization. Details below."
            )
        else:
            lines.append("No significant changes detected this week.")
        lines.append("")

        if source_statuses:
            _write_source_status_section(lines, source_statuses)
            _write_system_status_section(lines, source_statuses)

        if has_minor_changes:
            _write_minor_changes_section(lines, reports)

        lines.append("## Sales / Learning Impact")
        lines.append("")
        lines.append("No talk track updates needed this week.")
        lines.append("")

        lines.append("## Next Recommended Action")
        lines.append("")
        if is_baseline:
            lines.append(
                "Wait for the next scheduled run. Monitors will compare against "
                "this week's baseline and report any meaningful changes."
            )
        elif has_minor_changes:
            lines.append(
                "Review the minor changes above if any look relevant. "
                "No action required otherwise."
            )
        else:
            lines.append(
                "No action required. Review again next week."
            )
        lines.append("")
    else:
        groups = _group_sources_by_mode(summaries_by_source, reports)

        # Table of contents
        lines.append("## Sources with changes")
        lines.append("")
        for source_name in sorted(summaries_by_source.keys()):
            count = len(summaries_by_source[source_name])
            lines.append(f"- **{source_name}** ({count} change{'s' if count != 1 else ''})")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Firecrawl monitored changes
        if groups["monitor"]:
            lines.append("## Firecrawl Monitored Changes")
            lines.append("")
            lines.append("> These changes were detected by Firecrawl Monitoring, which compares ")
            lines.append("> recurring crawl/scrape snapshots and provides diffs and judgments.")
            lines.append("")
            for source_name in sorted(groups["monitor"].keys()):
                section = format_source_section(source_name, groups["monitor"][source_name])
                lines.append(section)
            lines.append("---")
            lines.append("")

        # Tavily-discovered updates
        if groups["tavily"]:
            lines.append("## Tavily-Discovered Updates")
            lines.append("")
            lines.append("> These changes were discovered via Tavily search/extract and diffed locally.")
            lines.append("")
            for source_name in sorted(groups["tavily"].keys()):
                section = format_source_section(source_name, groups["tavily"][source_name])
                lines.append(section)
            lines.append("---")
            lines.append("")

        # Manual crawl changes
        if groups["crawl"]:
            lines.append("## Crawl-Based Changes")
            lines.append("")
            lines.append("> These changes were detected by crawling sources and comparing local snapshots.")
            lines.append("")
            for source_name in sorted(groups["crawl"].keys()):
                section = format_source_section(source_name, groups["crawl"][source_name])
                lines.append(section)
            lines.append("---")
            lines.append("")

        # Audit trail: source + system status
        if source_statuses:
            _write_source_status_section(lines, source_statuses)
            _write_system_status_section(lines, source_statuses)

    content = "\n".join(lines)
    filepath.write_text(content)
    logger.info("Wrote digest to %s", filepath)
    return filepath


def write_questions(summaries_by_source: dict[str, list[dict]], digest_date: str | None = None) -> Path | None:
    """Extract and write questions to validate."""
    digest_date = digest_date or date.today().isoformat()
    questions = []

    for source, summaries in summaries_by_source.items():
        for s in summaries:
            q = s.get("question_to_validate", "")
            if q:
                questions.append({"source": source, "question": q})

    if not questions:
        return None

    QUESTIONS_DIR.mkdir(parents=True, exist_ok=True)
    filepath = QUESTIONS_DIR / f"{digest_date} - Questions.md"

    lines = [
        f"# Questions to Validate",
        f"",
        f"**Generated:** {digest_date}",
        f"",
        f"---",
        f"",
    ]

    for i, q in enumerate(questions, 1):
        lines.append(f"{i}. **[{q['source']}]** {q['question']}")

    filepath.write_text("\n".join(lines))
    logger.info("Wrote %d questions to %s", len(questions), filepath)
    return filepath

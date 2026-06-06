"""Write weekly digest and related Markdown notes."""

import logging
from datetime import date
from pathlib import Path

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
    lines = [f"## {source_name}", ""]

    for i, s in enumerate(summaries, 1):
        what = s.get("what_changed", "Unknown change")
        why = s.get("why_it_matters", "")
        bias = s.get("bias_risk", "")
        sales = s.get("sales_implication", "")
        question = s.get("question_to_validate", "")
        concepts = s.get("related_concepts", [])

        lines.append(f"### {i}. {what}")
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


def write_digest(
    summaries_by_source: dict[str, list[dict]],
    digest_date: str | None = None,
) -> Path:
    """Write the weekly digest note."""
    digest_date = digest_date or date.today().isoformat()
    DIGESTS_DIR.mkdir(parents=True, exist_ok=True)

    filename = f"{digest_date} - Weekly AI Coding Agents Digest.md"
    filepath = DIGESTS_DIR / filename

    lines = [
        f"# Weekly AI Coding Agents Digest",
        f"",
        f"**Date:** {digest_date}",
        f"",
        f"---",
        f"",
    ]

    if not summaries_by_source:
        lines.append("No significant changes detected this week.")
    else:
        # Table of contents
        lines.append("## Sources with changes")
        lines.append("")
        for source_name in sorted(summaries_by_source.keys()):
            count = len(summaries_by_source[source_name])
            lines.append(f"- **{source_name}** ({count} change{'s' if count != 1 else ''})")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Detailed sections
        for source_name in sorted(summaries_by_source.keys()):
            section = format_source_section(source_name, summaries_by_source[source_name])
            lines.append(section)
            lines.append("---")
            lines.append("")

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

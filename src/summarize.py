"""Summarize changes using the OpenAI API."""

import json
import logging
import os

import httpx

from .diff_engine import DiffReport, PageChange

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a competitive intelligence analyst focused on the AI coding-agent market.
Given a set of documentation changes, produce a structured summary.

For each significant change, output a JSON object with these fields:
- what_changed: One-sentence description of the change
- why_it_matters: Why this matters competitively (1-2 sentences)
- bias_risk: Any vendor bias or spin to watch for (1 sentence)
- sales_implication: How this could affect sales positioning (1 sentence)
- question_to_validate: A question worth investigating further (1 sentence)
- related_concepts: List of related concept names for wiki linking (e.g. ["Agent Harness", "MCP"])

Return a JSON array of these objects. Be concise and high-signal."""


def build_change_prompt(report: DiffReport) -> str:
    """Build a prompt from a diff report's significant changes."""
    parts = [f"Source: {report.source}"]
    parts.append(f"Compared: {report.old_date} -> {report.new_date}")

    if report.new_pages:
        parts.append(f"\nNew pages added: {', '.join(report.new_pages)}")
    if report.removed_pages:
        parts.append(f"\nPages removed: {', '.join(report.removed_pages)}")

    for change in report.significant_changes:
        parts.append(f"\n--- Change in {change.page_file} (score: {change.score}) ---")
        parts.append(f"Old content:\n{change.old_snippet[:500]}")
        parts.append(f"New content:\n{change.new_snippet[:500]}")

    return "\n".join(parts)


def call_openai(prompt: str) -> list[dict]:
    """Call OpenAI API to summarize changes. Returns list of summary dicts."""
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        logger.warning("OPENAI_API_KEY not set, returning empty summary")
        return []

    base_url = os.environ.get("OPENAI_API_URL", "https://api.openai.com/v1")
    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    resp = httpx.post(
        f"{base_url}/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.3,
            "response_format": {"type": "json_object"},
        },
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()

    content = data["choices"][0]["message"]["content"]
    parsed = json.loads(content)

    # Handle both {"changes": [...]} and [...] formats
    if isinstance(parsed, list):
        return parsed
    if isinstance(parsed, dict) and "changes" in parsed:
        return parsed["changes"]
    if isinstance(parsed, dict) and "summaries" in parsed:
        return parsed["summaries"]
    # Return as single-item list if it's a single dict
    if isinstance(parsed, dict):
        return [parsed]

    return []


def summarize_report(report: DiffReport) -> list[dict]:
    """Summarize a diff report's significant changes via OpenAI."""
    significant = report.significant_changes
    if not significant and not report.new_pages:
        logger.info("No significant changes for %s", report.source)
        return []

    prompt = build_change_prompt(report)
    logger.info("Summarizing %d changes for %s", len(significant), report.source)
    return call_openai(prompt)


def summarize_all(reports: list[DiffReport]) -> dict[str, list[dict]]:
    """Summarize all diff reports. Returns {source_name: [summaries]}."""
    results = {}
    for report in reports:
        summaries = summarize_report(report)
        if summaries:
            results[report.source] = summaries
    return results

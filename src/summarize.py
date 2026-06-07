"""Summarize changes using the OpenAI API."""

import json
import logging
import os
import time

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
- category: One of: product, pricing, security, deployment, integration, competitor, docs-only, minor wording, unknown

Return a JSON object with a single key "changes" containing an array of these objects. Be concise and high-signal."""


def build_change_prompt(report: DiffReport) -> str:
    """Build a prompt from a diff report's significant changes."""
    parts = [f"Source: {report.source}"]

    if report.mode == "monitor":
        parts.append("Data source: Firecrawl Monitoring")
        parts.append(f"Compared: previous snapshot -> latest check")
    else:
        parts.append(f"Compared: {report.old_date} -> {report.new_date}")

    if report.new_pages:
        parts.append(f"\nNew pages added: {', '.join(report.new_pages)}")
    if report.removed_pages:
        parts.append(f"\nPages removed: {', '.join(report.removed_pages)}")

    for change in report.significant_changes:
        parts.append(f"\n--- Change in {change.page_file} (score: {change.score}, category: {change.category}) ---")
        if change.old_snippet:
            parts.append(f"Old content:\n{change.old_snippet[:500]}")
        if change.new_snippet:
            parts.append(f"New content / diff:\n{change.new_snippet[:500]}")
        if change.change_summary and change.change_summary != f"Score {change.score} change in {change.page_file}":
            parts.append(f"Firecrawl judgment: {change.change_summary}")

    return "\n".join(parts)


def build_monitor_prompt(report: DiffReport) -> str:
    """Build a prompt specifically optimized for Firecrawl monitor results.

    Uses Firecrawl judgment and diff text directly.
    """
    parts = [
        f"Source: {report.source}",
        "Data source: Firecrawl Monitoring (diffs and judgments provided by Firecrawl)",
    ]

    if report.new_pages:
        parts.append(f"\nNew pages detected: {', '.join(report.new_pages)}")
    if report.removed_pages:
        parts.append(f"\nPages removed: {', '.join(report.removed_pages)}")

    for change in report.significant_changes:
        parts.append(f"\n--- {change.url} (score: {change.score}, category: {change.category}) ---")
        if change.change_summary:
            parts.append(f"Judgment: {change.change_summary}")
        if change.new_snippet:
            parts.append(f"Diff:\n{change.new_snippet[:800]}")

    return "\n".join(parts)


def call_openai(prompt: str) -> list[dict]:
    """Call OpenAI API to summarize changes. Returns list of summary dicts."""
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        logger.warning("OPENAI_API_KEY not set, returning empty summary")
        return []

    base_url = os.environ.get("OPENAI_API_URL", "https://api.openai.com/v1")
    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    max_retries = 3
    for attempt in range(max_retries):
        try:
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
            break
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 429 and attempt < max_retries - 1:
                wait = 2 ** (attempt + 1)
                logger.warning("OpenAI rate limited (429), retrying in %ds...", wait)
                time.sleep(wait)
                continue
            logger.error("OpenAI API error: %s", exc)
            return []
        except httpx.HTTPError as exc:
            logger.error("OpenAI request failed: %s", exc)
            return []

    data = resp.json()

    content = data["choices"][0]["message"]["content"]
    parsed = json.loads(content)

    # Extract the array from the response object
    if isinstance(parsed, list):
        return parsed
    if isinstance(parsed, dict):
        # Check known keys first, then scan for any list value
        for key in ("changes", "summaries", "items", "data", "results"):
            if key in parsed and isinstance(parsed[key], list):
                return parsed[key]
        for v in parsed.values():
            if isinstance(v, list):
                return v
        return [parsed]

    return []


def summarize_report(report: DiffReport) -> list[dict]:
    """Summarize a diff report's significant changes via OpenAI."""
    significant = report.significant_changes
    if not significant and not report.new_pages and not report.removed_pages:
        logger.info("No significant changes for %s", report.source)
        return []

    # Use monitor-optimized prompt for Firecrawl monitor reports
    if report.mode == "monitor":
        prompt = build_monitor_prompt(report)
    else:
        prompt = build_change_prompt(report)

    logger.info("Summarizing %d changes for %s (mode=%s)", len(significant), report.source, report.mode)
    return call_openai(prompt)


def summarize_all(
    reports: list[DiffReport],
) -> tuple[dict[str, list[dict]], list[str]]:
    """Summarize all diff reports.

    Returns (summaries_by_source, failed_sources) where failed_sources
    lists source names where OpenAI summarization failed.
    """
    results = {}
    failed: list[str] = []
    for report in reports:
        if not report.significant_changes and not report.new_pages and not report.removed_pages:
            continue
        summaries = summarize_report(report)
        if summaries:
            results[report.source] = summaries
        else:
            logger.warning(
                "Summarization returned no results for %s — "
                "changes were detected but not summarized",
                report.source,
            )
            failed.append(report.source)
    return results, failed

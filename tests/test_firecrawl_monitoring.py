"""Tests for Firecrawl monitoring parsing and scoring."""

import json
from pathlib import Path

from src.diff_engine import (
    build_monitor_diff_report,
    classify_change,
    score_firecrawl_diff,
)
from src.firecrawl_monitoring import (
    MonitorCheckResult,
    MonitorPageResult,
    parse_check_result,
    parse_page_result,
    parse_webhook_payload,
)

FIXTURES = Path(__file__).parent / "fixtures"


def _load_fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text())


# ---------------------------------------------------------------------------
# Parsing tests
# ---------------------------------------------------------------------------


class TestParsePageResult:
    def test_changed_page_with_judgment(self):
        fixture = _load_fixture("monitor_webhook_page.json")
        raw = fixture["data"][0]
        page = parse_page_result(raw)

        assert page.url == "https://docs.devin.ai/getting-started"
        assert page.status == "changed"
        assert page.is_meaningful is True
        assert page.judgment_confidence == "high"
        assert page.judgment_reason == "New MCP integration documentation added to getting started guide."
        assert len(page.meaningful_changes) == 2
        assert "previous" in page.diff_text
        assert "current" in page.diff_text

    def test_not_meaningful_page(self):
        fixture = _load_fixture("monitor_webhook_not_meaningful.json")
        raw = fixture["data"][0]
        page = parse_page_result(raw)

        assert page.status == "changed"
        assert page.is_meaningful is False
        assert page.judgment_confidence == "high"
        assert "copyright" in page.judgment_reason.lower()
        assert len(page.meaningful_changes) == 0

    def test_page_without_judgment(self):
        fixture = _load_fixture("monitor_check_detail.json")
        same_page = fixture["data"]["pages"][1]  # status: same
        page = parse_page_result(same_page)

        assert page.status == "same"
        assert page.is_meaningful is None
        assert page.judgment_reason == ""
        assert page.diff_text == ""

    def test_new_page(self):
        fixture = _load_fixture("monitor_check_detail.json")
        new_page = fixture["data"]["pages"][2]  # status: new
        page = parse_page_result(new_page)

        assert page.status == "new"
        assert page.url == "https://docs.example.com/new-feature"

    def test_removed_page(self):
        fixture = _load_fixture("monitor_check_detail.json")
        removed_page = fixture["data"]["pages"][3]  # status: removed
        page = parse_page_result(removed_page)

        assert page.status == "removed"
        assert page.url == "https://docs.example.com/deprecated-page"


class TestParseCheckResult:
    def test_full_check_result(self):
        fixture = _load_fixture("monitor_check_detail.json")
        check = parse_check_result(fixture)

        assert check.check_id == "019df960-5f2a-75fb-a98b-bd2d32ca67d4"
        assert check.monitor_id == "019df960-06e7-7383-9d89-82c0113dc31a"
        assert check.status == "completed"
        assert len(check.pages) == 5
        assert check.summary["totalPages"] == 5

    def test_check_filters(self):
        fixture = _load_fixture("monitor_check_detail.json")
        check = parse_check_result(fixture)

        assert len(check.changed_pages) == 1
        assert len(check.new_pages) == 1
        assert len(check.removed_pages) == 1
        assert len(check.error_pages) == 0
        assert len(check.meaningful_pages) == 1

    def test_check_no_judgment(self):
        fixture = _load_fixture("monitor_check_no_judgment.json")
        check = parse_check_result(fixture)

        assert check.status == "completed"
        assert len(check.pages) == 3
        assert len(check.changed_pages) == 1
        assert len(check.new_pages) == 1
        # Page without judgment should still be parseable
        changed = check.changed_pages[0]
        assert changed.is_meaningful is None
        assert changed.diff_text != ""


class TestParseWebhookPayload:
    def test_page_webhook(self):
        fixture = _load_fixture("monitor_webhook_page.json")
        pages = parse_webhook_payload(fixture)

        assert len(pages) == 1
        assert pages[0].status == "changed"
        assert pages[0].is_meaningful is True

    def test_not_meaningful_webhook(self):
        fixture = _load_fixture("monitor_webhook_not_meaningful.json")
        pages = parse_webhook_payload(fixture)

        assert len(pages) == 1
        assert pages[0].is_meaningful is False

    def test_empty_data(self):
        pages = parse_webhook_payload({"data": []})
        assert len(pages) == 0

    def test_single_dict_data(self):
        """Webhook data can be a single dict instead of a list."""
        payload = {
            "data": {
                "url": "https://example.com",
                "status": "changed",
            }
        }
        pages = parse_webhook_payload(payload)
        assert len(pages) == 1
        assert pages[0].url == "https://example.com"


# ---------------------------------------------------------------------------
# Scoring tests
# ---------------------------------------------------------------------------


class TestScoreFirecrawlDiff:
    def test_high_confidence_meaningful(self):
        judgment = {
            "meaningful": True,
            "confidence": "high",
            "meaningfulChanges": [
                {"type": "added", "reason": "New feature"},
                {"type": "modified", "reason": "Updated API"},
            ],
        }
        assert score_firecrawl_diff("some diff", judgment) == 4

    def test_high_confidence_single_change(self):
        judgment = {
            "meaningful": True,
            "confidence": "high",
            "meaningfulChanges": [{"type": "added", "reason": "One change"}],
        }
        assert score_firecrawl_diff("some diff", judgment) == 3

    def test_high_confidence_many_changes(self):
        judgment = {
            "meaningful": True,
            "confidence": "high",
            "meaningfulChanges": [
                {"type": "added", "reason": "1"},
                {"type": "added", "reason": "2"},
                {"type": "added", "reason": "3"},
            ],
        }
        assert score_firecrawl_diff("some diff", judgment) == 5

    def test_medium_confidence(self):
        judgment = {
            "meaningful": True,
            "confidence": "medium",
            "meaningfulChanges": [{"type": "modified"}],
        }
        assert score_firecrawl_diff("some diff", judgment) == 3

    def test_low_confidence(self):
        judgment = {
            "meaningful": True,
            "confidence": "low",
            "meaningfulChanges": [{"type": "modified"}],
        }
        assert score_firecrawl_diff("some diff", judgment) == 2

    def test_not_meaningful(self):
        judgment = {
            "meaningful": False,
            "confidence": "high",
            "meaningfulChanges": [],
        }
        assert score_firecrawl_diff("some diff", judgment) == 1

    def test_no_judgment_small_diff(self):
        diff = "+added line\n-removed line"
        assert score_firecrawl_diff(diff) == 1

    def test_no_judgment_medium_diff(self):
        diff = "\n".join(f"+added line {i}" for i in range(15))
        assert score_firecrawl_diff(diff) == 3

    def test_no_judgment_large_diff(self):
        diff = "\n".join(f"+added line {i}" for i in range(50))
        assert score_firecrawl_diff(diff) == 4

    def test_no_judgment_empty(self):
        assert score_firecrawl_diff("") == 0


# ---------------------------------------------------------------------------
# Classification tests
# ---------------------------------------------------------------------------


class TestClassifyChange:
    def test_pricing_change(self):
        text = "Updated pricing tiers: Pro plan now costs $50/month with new billing cycle"
        assert classify_change(text) == "pricing"

    def test_security_change(self):
        text = "Added SSO authentication support with RBAC permissions for enterprise"
        assert classify_change(text) == "security"

    def test_deployment_change(self):
        text = "New Docker deployment guide for self-hosted installations on Kubernetes"
        assert classify_change(text) == "deployment"

    def test_integration_change(self):
        text = "Added MCP plugin integration with webhook support for third-party tools"
        assert classify_change(text) == "integration"

    def test_product_change(self):
        text = "New agent feature launched with improved model performance benchmarks"
        assert classify_change(text) == "product"

    def test_competitor_change(self):
        text = "Comparison table: Devin vs Cursor alternative products"
        assert classify_change(text) == "competitor"

    def test_minor_wording(self):
        text = "Fixed a typo in the docs"
        assert classify_change(text) == "minor wording"

    def test_docs_only(self):
        text = "This is a paragraph about some general documentation restructuring and reorganization of content across multiple pages to improve readability and navigation for visitors who want to find information more easily in the revised layout of the help center"
        assert classify_change(text) == "docs-only"

    def test_unknown_with_no_keywords(self):
        text = "The quick brown fox jumps over the lazy dog and other animals in the forest"
        category = classify_change(text)
        assert category in ("docs-only", "minor wording", "unknown")


# ---------------------------------------------------------------------------
# Monitor diff report building
# ---------------------------------------------------------------------------


class TestBuildMonitorDiffReport:
    def test_builds_from_check_result(self):
        fixture = _load_fixture("monitor_check_detail.json")
        check = parse_check_result(fixture)
        report = build_monitor_diff_report("test-source", check)

        assert report.source == "test-source"
        assert report.mode == "monitor"
        assert len(report.new_pages) == 1
        assert len(report.removed_pages) == 1
        assert len(report.changes) == 1

        change = report.changes[0]
        assert change.url == "https://docs.example.com/getting-started"
        assert change.score >= 3  # High confidence meaningful
        assert change.category != "unknown"

    def test_builds_from_no_judgment_check(self):
        fixture = _load_fixture("monitor_check_no_judgment.json")
        check = parse_check_result(fixture)
        report = build_monitor_diff_report("no-judge-source", check)

        assert report.mode == "monitor"
        assert len(report.new_pages) == 1
        assert len(report.changes) == 1
        # Without judgment, score is based on diff size
        assert report.changes[0].score >= 1

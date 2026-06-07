"""Tests for the summarize module — focusing on retry, failure, and guard logic."""

import json
from unittest.mock import patch, MagicMock

import httpx
import pytest

from src.diff_engine import DiffReport, PageChange
from src.summarize import call_openai, summarize_report, summarize_all


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_report(
    source: str = "test-source",
    changes: list[PageChange] | None = None,
    new_pages: list[str] | None = None,
    removed_pages: list[str] | None = None,
    mode: str = "monitor",
) -> DiffReport:
    return DiffReport(
        source=source,
        old_date="2026-01-01",
        new_date="2026-01-08",
        mode=mode,
        changes=changes or [],
        new_pages=new_pages or [],
        removed_pages=removed_pages or [],
    )


def _significant_change(score: int = 4) -> PageChange:
    return PageChange(
        source="test-source",
        page_file="page.md",
        url="https://example.com/page",
        score=score,
        old_snippet="old text",
        new_snippet="new text",
        change_summary="Something important changed",
        category="product",
    )


def _minor_change() -> PageChange:
    return PageChange(
        source="test-source",
        page_file="page.md",
        url="https://example.com/page",
        score=1,
        old_snippet="old",
        new_snippet="new",
        change_summary="Trivial wording fix",
        category="minor wording",
    )


def _openai_success_response(summaries: list[dict]) -> httpx.Response:
    """Build a mock httpx.Response that looks like a successful OpenAI response."""
    body = {
        "choices": [
            {"message": {"content": json.dumps({"changes": summaries})}}
        ]
    }
    return httpx.Response(200, json=body, request=httpx.Request("POST", "https://api.openai.com/v1/chat/completions"))


def _openai_429_response() -> httpx.Response:
    return httpx.Response(429, text="rate limited", request=httpx.Request("POST", "https://api.openai.com/v1/chat/completions"))


def _openai_500_response() -> httpx.Response:
    return httpx.Response(500, text="server error", request=httpx.Request("POST", "https://api.openai.com/v1/chat/completions"))


# ---------------------------------------------------------------------------
# call_openai tests
# ---------------------------------------------------------------------------

class TestCallOpenai:
    @patch.dict("os.environ", {"OPENAI_API_KEY": ""})
    def test_no_api_key_returns_empty(self):
        assert call_openai("test prompt") == []

    @patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"})
    @patch("src.summarize.httpx.post")
    def test_success(self, mock_post):
        summaries = [{"what_changed": "New feature added"}]
        mock_post.return_value = _openai_success_response(summaries)
        result = call_openai("test prompt")
        assert result == summaries

    @patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"})
    @patch("src.summarize.httpx.post")
    @patch("src.summarize.time.sleep")
    def test_429_retries_then_succeeds(self, mock_sleep, mock_post):
        summaries = [{"what_changed": "Feature X"}]
        mock_post.side_effect = [
            httpx.HTTPStatusError("429", request=MagicMock(), response=_openai_429_response()),
            _openai_success_response(summaries),
        ]
        result = call_openai("test prompt")
        assert result == summaries
        assert mock_sleep.call_count == 1
        mock_sleep.assert_called_with(2)  # first retry: 2^1

    @patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"})
    @patch("src.summarize.httpx.post")
    @patch("src.summarize.time.sleep")
    def test_429_exhausts_retries_returns_empty(self, mock_sleep, mock_post):
        mock_post.side_effect = httpx.HTTPStatusError(
            "429", request=MagicMock(), response=_openai_429_response()
        )
        result = call_openai("test prompt")
        assert result == []
        assert mock_sleep.call_count == 2  # retried twice before giving up

    @patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"})
    @patch("src.summarize.httpx.post")
    def test_500_returns_empty_no_retry(self, mock_post):
        mock_post.side_effect = httpx.HTTPStatusError(
            "500", request=MagicMock(), response=_openai_500_response()
        )
        result = call_openai("test prompt")
        assert result == []
        assert mock_post.call_count == 1  # no retry for non-429

    @patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"})
    @patch("src.summarize.httpx.post")
    def test_network_error_returns_empty(self, mock_post):
        mock_post.side_effect = httpx.ConnectError("connection refused")
        result = call_openai("test prompt")
        assert result == []


# ---------------------------------------------------------------------------
# summarize_report tests
# ---------------------------------------------------------------------------

class TestSummarizeReport:
    def test_no_significant_changes_skips_openai(self):
        """Reports with only new_pages but no significant changes skip OpenAI."""
        report = _make_report(new_pages=["page1.md", "page2.md"])
        with patch("src.summarize.call_openai") as mock:
            result = summarize_report(report)
        assert result == []
        mock.assert_not_called()

    def test_only_minor_changes_skips_openai(self):
        """Reports with changes below score 3 skip OpenAI."""
        report = _make_report(changes=[_minor_change()])
        with patch("src.summarize.call_openai") as mock:
            result = summarize_report(report)
        assert result == []
        mock.assert_not_called()

    def test_significant_changes_calls_openai(self):
        """Reports with significant changes call OpenAI."""
        report = _make_report(changes=[_significant_change()])
        with patch("src.summarize.call_openai", return_value=[{"what_changed": "test"}]) as mock:
            result = summarize_report(report)
        assert result == [{"what_changed": "test"}]
        mock.assert_called_once()

    def test_empty_report_skips_openai(self):
        report = _make_report()
        with patch("src.summarize.call_openai") as mock:
            result = summarize_report(report)
        assert result == []
        mock.assert_not_called()


# ---------------------------------------------------------------------------
# summarize_all tests
# ---------------------------------------------------------------------------

class TestSummarizeAll:
    def test_baseline_new_pages_only_skips_openai(self):
        """Baseline run with only new pages should not call OpenAI at all."""
        reports = [
            _make_report(source="source-a", new_pages=["p1", "p2"]),
            _make_report(source="source-b", new_pages=["p3"]),
        ]
        with patch("src.summarize.call_openai") as mock:
            summaries, failed = summarize_all(reports)
        assert summaries == {}
        assert failed == []
        mock.assert_not_called()

    def test_significant_changes_summarized(self):
        reports = [
            _make_report(source="source-a", changes=[_significant_change()]),
        ]
        with patch("src.summarize.call_openai", return_value=[{"what_changed": "test"}]):
            summaries, failed = summarize_all(reports)
        assert "source-a" in summaries
        assert failed == []

    def test_openai_failure_tracked(self):
        """When OpenAI returns [] for a source with significant changes, it's tracked as failed."""
        reports = [
            _make_report(source="source-a", changes=[_significant_change()]),
        ]
        with patch("src.summarize.call_openai", return_value=[]):
            summaries, failed = summarize_all(reports)
        assert summaries == {}
        assert failed == ["source-a"]

    def test_mixed_success_and_failure(self):
        """One source succeeds, another fails."""
        reports = [
            _make_report(source="source-ok", changes=[_significant_change()]),
            _make_report(source="source-fail", changes=[_significant_change()]),
        ]
        with patch("src.summarize.call_openai") as mock:
            mock.side_effect = [
                [{"what_changed": "good"}],
                [],  # failure
            ]
            summaries, failed = summarize_all(reports)
        assert "source-ok" in summaries
        assert failed == ["source-fail"]

    def test_only_minor_changes_no_openai(self):
        """Reports with only minor changes (score < 3) skip OpenAI entirely."""
        reports = [
            _make_report(source="source-a", changes=[_minor_change()]),
        ]
        with patch("src.summarize.call_openai") as mock:
            summaries, failed = summarize_all(reports)
        assert summaries == {}
        assert failed == []
        mock.assert_not_called()

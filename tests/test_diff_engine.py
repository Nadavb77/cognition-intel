"""Tests for the diff engine module."""

from src.diff_engine import score_change, extract_diff_snippet, PageChange, DiffReport


class TestScoreChange:
    def test_identical_texts(self):
        assert score_change("hello", "hello") == 0

    def test_trivial_change(self):
        old = "hello world"
        new = "hello world!"
        score = score_change(old, new)
        assert score == 1

    def test_small_change(self):
        old = "line1\nline2\nline3"
        new = "line1\nline2 modified with some extra text\nline3"
        score = score_change(old, new)
        assert score in (1, 2)

    def test_medium_change(self):
        old = "original content\n" * 10
        new = "completely different content with new information\n" * 10
        score = score_change(old, new)
        assert score >= 3

    def test_large_change(self):
        old = "old line\n" * 5
        new = "brand new content that is very different\n" * 50
        score = score_change(old, new)
        assert score >= 4

    def test_very_large_change(self):
        old = "x\n" * 10
        new = "completely new and very different lengthy content here\n" * 100
        score = score_change(old, new)
        assert score == 5

    def test_score_range(self):
        """All scores should be 0-5."""
        pairs = [
            ("", ""),
            ("a", "b"),
            ("hello", "hello world this is a test"),
            ("x" * 100, "y" * 500),
            ("short", "a" * 5000),
        ]
        for old, new in pairs:
            score = score_change(old, new)
            assert 0 <= score <= 5, f"Score {score} out of range for ({old[:20]}..., {new[:20]}...)"


class TestExtractDiffSnippet:
    def test_basic_snippet(self):
        old = "line1\nline2\nline3\nline4"
        new = "line1\nline2 changed\nline3\nline4"
        old_snip, new_snip = extract_diff_snippet(old, new)
        assert "line2" in old_snip
        assert "line2 changed" in new_snip

    def test_max_lines(self):
        old = "\n".join(f"line{i}" for i in range(100))
        new = "\n".join(f"line{i}" for i in range(100))
        old_snip, new_snip = extract_diff_snippet(old, new, max_lines=5)
        assert old_snip.count("\n") <= 4  # 5 lines = 4 newlines

    def test_empty_texts(self):
        old_snip, new_snip = extract_diff_snippet("", "")
        assert old_snip == ""
        assert new_snip == ""

    def test_appended_content(self):
        """Snippet should show the boundary where content was appended."""
        old = "\n".join(f"line{i}" for i in range(20))
        new = old + "\nnew_line20\nnew_line21\nnew_line22"
        old_snip, new_snip = extract_diff_snippet(old, new)
        # The new snippet should contain the appended lines
        assert "new_line20" in new_snip

    def test_removed_content_at_end(self):
        """Snippet should show the boundary where content was removed."""
        old = "\n".join(f"line{i}" for i in range(25))
        new = "\n".join(f"line{i}" for i in range(20))
        old_snip, new_snip = extract_diff_snippet(old, new)
        # The old snippet should contain lines near the removal point
        assert "line19" in old_snip or "line18" in old_snip


class TestDiffReport:
    def test_significant_changes_filter(self):
        report = DiffReport(source="test", old_date="2026-01-01", new_date="2026-01-08")
        report.changes = [
            PageChange(
                source="test", page_file="a.md", url="",
                score=1, old_snippet="", new_snippet="",
                change_summary="trivial",
            ),
            PageChange(
                source="test", page_file="b.md", url="",
                score=3, old_snippet="", new_snippet="",
                change_summary="medium",
            ),
            PageChange(
                source="test", page_file="c.md", url="",
                score=5, old_snippet="", new_snippet="",
                change_summary="major",
            ),
        ]

        significant = report.significant_changes
        assert len(significant) == 2
        assert all(c.score >= 3 for c in significant)

    def test_no_significant_changes(self):
        report = DiffReport(source="test", old_date="2026-01-01", new_date="2026-01-08")
        report.changes = [
            PageChange(
                source="test", page_file="a.md", url="",
                score=1, old_snippet="", new_snippet="",
                change_summary="trivial",
            ),
            PageChange(
                source="test", page_file="b.md", url="",
                score=2, old_snippet="", new_snippet="",
                change_summary="small",
            ),
        ]

        assert len(report.significant_changes) == 0

    def test_empty_report(self):
        report = DiffReport(source="test", old_date="2026-01-01", new_date="2026-01-08")
        assert len(report.significant_changes) == 0
        assert len(report.changes) == 0
        assert len(report.new_pages) == 0
        assert len(report.removed_pages) == 0

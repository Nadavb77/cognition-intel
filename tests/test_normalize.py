"""Tests for the normalize module."""

from src.normalize import normalize_markdown, extract_sections, strip_frontmatter


class TestNormalizeMarkdown:
    def test_collapses_blank_lines(self):
        text = "line1\n\n\n\n\nline2"
        assert normalize_markdown(text) == "line1\n\nline2"

    def test_strips_trailing_whitespace(self):
        text = "hello   \nworld  "
        result = normalize_markdown(text)
        assert "   " not in result

    def test_removes_html_comments(self):
        text = "before <!-- hidden --> after"
        assert normalize_markdown(text) == "before  after"

    def test_removes_multiline_html_comments(self):
        text = "before\n<!-- \nhidden\n-->\nafter"
        assert normalize_markdown(text) == "before\n\nafter"

    def test_removes_utm_params(self):
        text = "Visit https://example.com/page?utm_source=twitter&utm_medium=social"
        result = normalize_markdown(text)
        assert "utm_source" not in result
        assert "utm_medium" not in result
        assert "https://example.com/page" in result

    def test_removes_fbclid_param(self):
        text = "https://example.com/page?fbclid=abc123"
        result = normalize_markdown(text)
        assert "fbclid" not in result

    def test_normalizes_list_markers(self):
        text = "* item1\n* item2\n* item3"
        result = normalize_markdown(text)
        assert result == "- item1\n- item2\n- item3"

    def test_preserves_content(self):
        text = "# Hello\n\nThis is a paragraph.\n\n- item 1\n- item 2"
        result = normalize_markdown(text)
        assert result == text

    def test_normalizes_crlf(self):
        text = "line1\r\nline2\r\nline3"
        result = normalize_markdown(text)
        assert "\r" not in result
        assert result == "line1\nline2\nline3"

    def test_empty_input(self):
        assert normalize_markdown("") == ""

    def test_strips_leading_trailing_whitespace(self):
        text = "  \n\nhello\n\n  "
        result = normalize_markdown(text)
        assert result == "hello"


class TestExtractSections:
    def test_splits_by_heading(self):
        text = "# Heading 1\ncontent1\n## Heading 2\ncontent2"
        sections = extract_sections(text)
        assert "Heading 1" in sections
        assert "Heading 2" in sections
        assert sections["Heading 1"] == "content1"
        assert sections["Heading 2"] == "content2"

    def test_preamble(self):
        text = "some preamble\n# Heading\ncontent"
        sections = extract_sections(text)
        assert "_preamble" in sections
        assert sections["_preamble"] == "some preamble"

    def test_no_headings(self):
        text = "just some text\nwith no headings"
        sections = extract_sections(text)
        assert "_preamble" in sections

    def test_empty_preamble_removed(self):
        text = "# Heading\ncontent"
        sections = extract_sections(text)
        assert "_preamble" not in sections

    def test_multiple_heading_levels(self):
        text = "# H1\n## H2\n### H3\ncontent"
        sections = extract_sections(text)
        assert "H1" in sections
        assert "H2" in sections
        assert "H3" in sections


class TestStripFrontmatter:
    def test_strips_yaml_frontmatter(self):
        text = "---\ntitle: test\ndate: 2026-01-01\n---\n\n# Hello"
        result = strip_frontmatter(text)
        assert result == "# Hello"
        assert "title:" not in result

    def test_no_frontmatter(self):
        text = "# Hello\n\nworld"
        result = strip_frontmatter(text)
        assert result == text

    def test_frontmatter_only(self):
        text = "---\ntitle: test\n---"
        result = strip_frontmatter(text)
        assert result == ""

    def test_dashes_not_at_start(self):
        text = "hello\n---\nworld"
        result = strip_frontmatter(text)
        assert result == text

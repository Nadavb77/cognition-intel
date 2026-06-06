"""Normalize Markdown content for reliable diffing."""

import re


def normalize_markdown(text: str) -> str:
    """Normalize Markdown text to reduce noise in diffs.

    - Strip excessive whitespace
    - Normalize line endings
    - Remove tracking parameters from URLs
    - Collapse multiple blank lines
    - Strip HTML comments
    - Normalize list markers
    """
    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove HTML comments
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

    # Remove common tracking params from URLs
    text = re.sub(r"(\?|&)(utm_\w+|ref|source|mc_\w+|fbclid|gclid)=[^&\s)]*", "", text)
    # Clean up trailing ? or & after param removal
    text = re.sub(r"\?(&|$)", "", text)
    text = re.sub(r"&(&|$)", "", text)

    # Normalize list markers (- or * to -)
    text = re.sub(r"^(\s*)\*(\s)", r"\1-\2", text, flags=re.MULTILINE)

    # Collapse multiple blank lines to at most two
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Strip trailing whitespace per line
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)

    # Strip leading/trailing whitespace from the whole document
    text = text.strip()

    return text


def extract_sections(text: str) -> dict[str, str]:
    """Split Markdown into sections by heading. Returns {heading: content}."""
    sections: dict[str, str] = {}
    current_heading = "_preamble"
    current_lines: list[str] = []

    for line in text.split("\n"):
        heading_match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading_match:
            # Save previous section
            sections[current_heading] = "\n".join(current_lines).strip()
            current_heading = heading_match.group(2).strip()
            current_lines = []
        else:
            current_lines.append(line)

    # Save last section
    sections[current_heading] = "\n".join(current_lines).strip()

    # Remove empty preamble
    if "_preamble" in sections and not sections["_preamble"]:
        del sections["_preamble"]

    return sections


def strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter from Markdown."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3 :].strip()
    return text

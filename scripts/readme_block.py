"""Replace a generated block in the README between its start and end markers."""

from pathlib import Path


def replace_block(readme: Path, start_marker: str, end_marker: str, body: str) -> bool:
    """Write body between the markers and return whether the README changed."""
    text = readme.read_text(encoding="utf-8")
    start, end = text.find(start_marker), text.find(end_marker)
    if start == -1 or end == -1 or end < start:
        raise ValueError(f"{readme} needs {start_marker!r} before {end_marker!r}")
    updated = f"{text[:start]}{start_marker}\n\n{body}\n\n{text[end:]}"
    if updated == text:
        return False
    readme.write_text(updated, encoding="utf-8")
    return True

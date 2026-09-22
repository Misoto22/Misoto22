"""Generate the themed Toolbox SVGs used in the profile README.

Icons come from Simple Icons (CC0), pinned to one release so a rerun
reproduces the same output. Run from the repository root:

    python3 scripts/toolbox.py
"""

import argparse
import colorsys
import math
import re
import urllib.error
import urllib.request
from pathlib import Path

ICON_URL = "https://cdn.jsdelivr.net/npm/simple-icons@{version}/icons/{slug}.svg"
ICON_VERSION = "16.32.0"
# Simple Icons later dropped these glyphs; pin the last release that shipped each.
PINNED_VERSIONS = {"openai": "15.22.0", "amazonwebservices": "14.15.0"}

# (row label, [(display name, simple-icons slug, brand hex)])
GROUPS = [
    (
        "Agents",
        [
            ("Claude Code", "claude", "D97757"),
            ("Codex", "openai", "000000"),
            ("MCP", "modelcontextprotocol", "000000"),
            ("LangGraph", "langgraph", "7FC8FF"),
        ],
    ),
    (
        "Languages",
        [
            ("Python", "python", "3776AB"),
            ("TypeScript", "typescript", "3178C6"),
            ("Rust", "rust", "000000"),
            ("Swift", "swift", "F05138"),
        ],
    ),
    (
        "Frontend",
        [
            ("React", "react", "61DAFB"),
            ("Next.js", "nextdotjs", "000000"),
            ("Tailwind CSS", "tailwindcss", "06B6D4"),
        ],
    ),
    (
        "Backend",
        [
            ("Django", "django", "092E20"),
            ("FastAPI", "fastapi", "009688"),
            ("PostgreSQL", "postgresql", "4169E1"),
            ("Redis", "redis", "FF4438"),
        ],
    ),
    (
        "Infra",
        [
            ("Docker", "docker", "2496ED"),
            ("GitHub Actions", "githubactions", "2088FF"),
            ("AWS", "amazonwebservices", "FF9900"),
            ("Cloudflare", "cloudflare", "F38020"),
        ],
    ),
]

# GitHub Primer tokens, so the card sits on the README like native UI.
THEMES = {
    "light": {
        "fg": "#1f2328",
        "muted": "#59636e",
        "chip": "#f6f8fa",
        "border": "#d1d9e0",
    },
    "dark": {
        "fg": "#f0f6fc",
        "muted": "#9198a1",
        "chip": "#151b23",
        "border": "#3d444d",
    },
}

# Arial advance widths (per 1000 em) for ASCII 32-126. Viewers render with the
# system UI font, so widths get SAFETY headroom instead of exact metrics.
ARIAL_WIDTHS = [
    278, 278, 355, 556, 556, 889, 667, 191, 333, 333, 389, 584, 278, 333, 278, 278,
    556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 278, 278, 584, 584, 584, 556,
    1015, 667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778,
    667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 278, 278, 278, 469, 556,
    333, 556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833, 556, 556,
    556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500, 334, 260, 334, 584,
]  # fmt: skip
SAFETY = 1.03

MAX_WIDTH = 840
LABEL_WIDTH = 124
ROW_HEIGHT = 46
CHIP_HEIGHT = 34
CHIP_GAP = 10
ICON_SIZE = 16
FONT_SIZE = 13
FONT_STACK = (
    '-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif'
)


def text_width(text: str, size: float) -> float:
    units = sum(ARIAL_WIDTHS[ord(c) - 32] if 32 <= ord(c) < 127 else 600 for c in text)
    return units * size / 1000 * SAFETY


def fetch_icon(slug: str) -> str:
    """Return the single path of a Simple Icons glyph."""
    version = PINNED_VERSIONS.get(slug, ICON_VERSION)
    url = ICON_URL.format(version=version, slug=slug)
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            svg = response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        raise ValueError(
            f"Simple Icons {version} has no glyph {slug!r}: {error}"
        ) from error
    match = re.search(r'<path d="([^"]+)"', svg)
    if match is None:
        raise ValueError(f"No path in Simple Icons glyph {slug!r}")
    return match.group(1)


def luminance(hex_color: str) -> float:
    def channel(value: int) -> float:
        c = value / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (int(hex_color.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def contrast(a: str, b: str) -> float:
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def icon_color(brand: str, theme: dict[str, str]) -> str:
    """Keep the brand's hue and saturation, moving only lightness until it reads (3:1).

    Black or white marks carry no hue to keep, so they take the text colour.
    """
    r, g, b = (int(brand[i : i + 2], 16) / 255 for i in (0, 2, 4))
    hue, light, sat = colorsys.rgb_to_hls(r, g, b)
    if sat < 0.1 or light < 0.02 or light > 0.98:
        return theme["fg"]
    toward_light = luminance(theme["chip"]) < 0.5
    for step in range(51):
        shift = step / 50
        lightness = light + (1 - light) * shift if toward_light else light * (1 - shift)
        rgb = colorsys.hls_to_rgb(hue, lightness, sat)
        candidate = "#" + "".join(f"{round(c * 255):02x}" for c in rgb)
        if contrast(candidate, theme["chip"]) >= 3:
            return candidate
    return theme["fg"]


def chip(x: int, name: str, path: str, color: str) -> tuple[str, int]:
    width = math.ceil(12 + ICON_SIZE + 8 + text_width(name, FONT_SIZE) + 14)
    scale = ICON_SIZE / 24
    icon_y = (CHIP_HEIGHT - ICON_SIZE) / 2
    markup = (
        f'<g transform="translate({x} 0)">'
        f'<rect x=".5" y=".5" width="{width - 1}" height="{CHIP_HEIGHT - 1}" rx="9"/>'
        f'<path transform="translate(12 {icon_y}) scale({scale:.4f})" fill="{color}" d="{path}"/>'
        f'<text x="{12 + ICON_SIZE + 8}" y="{CHIP_HEIGHT / 2}">{name}</text>'
        "</g>"
    )
    return markup, width


def render(icons: dict[str, str], theme: dict[str, str]) -> str:
    rows, width_used = [], 0
    for row, (label, tools) in enumerate(GROUPS):
        x, chips = LABEL_WIDTH, []
        for name, slug, brand in tools:
            markup, width = chip(x, name, icons[slug], icon_color(brand, theme))
            chips.append(markup)
            x += width + CHIP_GAP
        if x - CHIP_GAP > MAX_WIDTH:
            raise ValueError(f"Row {label!r} overflows the {MAX_WIDTH}px canvas")
        width_used = max(width_used, x - CHIP_GAP)
        y = row * ROW_HEIGHT + (ROW_HEIGHT - CHIP_HEIGHT) / 2
        rows.append(
            f'<g transform="translate(0 {y:.1f})">'
            f'<text class="l" y="{CHIP_HEIGHT / 2}">{label.upper()}</text>{"".join(chips)}</g>'
        )
    height = len(GROUPS) * ROW_HEIGHT
    names = ", ".join(name for _, tools in GROUPS for name, _, _ in tools)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width_used}" height="{height}" '
        f'viewBox="0 0 {width_used} {height}" role="img" aria-label="Toolbox: {names}">\n'
        f"<title>Toolbox: {names}</title>\n<style>\n"
        f"text{{font-family:{FONT_STACK};font-size:{FONT_SIZE}px;fill:{theme['fg']};"
        "dominant-baseline:central}\n"
        f".l{{font-size:11px;font-weight:600;letter-spacing:.08em;fill:{theme['muted']}}}\n"
        f"rect{{fill:{theme['chip']};stroke:{theme['border']};stroke-width:1}}\n"
        "</style>\n" + "\n".join(rows) + "\n</svg>\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", default="assets", type=Path)
    args = parser.parse_args()

    icons = {slug: fetch_icon(slug) for _, tools in GROUPS for _, slug, _ in tools}
    args.out.mkdir(parents=True, exist_ok=True)
    for name, theme in THEMES.items():
        target = args.out / f"toolbox-{name}.svg"
        target.write_text(render(icons, theme), encoding="utf-8")
        print(f"wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

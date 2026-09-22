"""Generate the animated handwritten signature SVGs used in the profile README.

The glyphs come from a single-stroke (centre-line) SVG font, so every letter can
be "written" with a stroke-dashoffset animation instead of fading in a filled
outline. Run from the repository root:

    python3 scripts/signature.py
"""

import argparse
import itertools
import math
import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

# EMS Allure: single-stroke derivative of Allura, SIL Open Font License.
FONT_URL = "https://gitlab.com/inkscape/extensions/-/raw/master/svg_fonts/EMSAllure.svg"
SVG_NS = "{http://www.w3.org/2000/svg}"
THEMES = {"light": "#1f2328", "dark": "#e6edf3"}

CYCLE_MS = 9000
DRAW_END = 0.55  # fraction of the cycle spent writing
ERASE_START = 0.86  # hold the finished signature until here
ERASE_END = 0.92
STROKE_WIDTH = 26
PADDING = 40
JOIN_TOLERANCE = 15  # font units; merges strokes that visually continue
CORNER_DEGREES = 100  # sharper turns stay pointed instead of being smoothed


def load_glyphs(font_source: str) -> tuple[dict[str, tuple[float, str]], float]:
    """Return {char: (advance, path_data)} and the default advance of the font."""
    if font_source.startswith("http"):
        with urllib.request.urlopen(font_source, timeout=30) as response:
            raw = response.read()
    else:
        raw = Path(font_source).read_bytes()
    font = ET.fromstring(raw).find(f".//{SVG_NS}font")
    if font is None:
        raise ValueError(f"No <font> element in {font_source}")
    default_adv = float(font.get("horiz-adv-x", "500"))
    glyphs = {}
    for glyph in font.iter(f"{SVG_NS}glyph"):
        char = glyph.get("unicode")
        if char:
            adv = float(glyph.get("horiz-adv-x", default_adv))
            glyphs[char] = (adv, glyph.get("d", ""))
    return glyphs, default_adv


def cubic(p0, p1, p2, p3, steps=12):
    for i in range(1, steps + 1):
        t = i / steps
        u = 1 - t
        yield (
            u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
            u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1],
        )


def parse_strokes(d: str, dx: float) -> list[list[tuple[float, float]]]:
    """Flatten absolute M/L/C path data into polylines, shifted by dx and y-flipped."""
    tokens = re.findall(r"[MLC]|-?\d*\.?\d+(?:e-?\d+)?", d)
    strokes, current, i = [], [], 0
    while i < len(tokens):
        cmd = tokens[i]
        i += 1
        if cmd == "M":
            if len(current) > 1:
                strokes.append(current)
            current = [(float(tokens[i]), float(tokens[i + 1]))]
            i += 2
        elif cmd == "L":
            current.append((float(tokens[i]), float(tokens[i + 1])))
            i += 2
        elif cmd == "C":
            pts = [(float(tokens[i + k]), float(tokens[i + k + 1])) for k in (0, 2, 4)]
            current.extend(cubic(current[-1], *pts))
            i += 6
        else:
            raise ValueError(f"Unsupported path command {cmd!r}")
    if len(current) > 1:
        strokes.append(current)
    return [[(x + dx, -y) for x, y in stroke] for stroke in strokes]


def layout(text: str, glyphs, default_adv: float) -> list[list[tuple[float, float]]]:
    strokes, pen_x = [], 0.0
    for char in text:
        adv, d = glyphs.get(char, (default_adv, ""))
        strokes.extend(parse_strokes(d, pen_x))
        pen_x += adv
    return merge_continuations(strokes)


def merge_continuations(strokes):
    """Join a stroke to the previous one when the pen would not lift between them."""
    merged = [strokes[0]]
    for stroke in strokes[1:]:
        if math.dist(merged[-1][-1], stroke[0]) <= JOIN_TOLERANCE:
            merged[-1] = merged[-1] + stroke[1:]
        else:
            merged.append(stroke)
    return merged


def turn_angle(a, b, c) -> float:
    v1 = (b[0] - a[0], b[1] - a[1])
    v2 = (c[0] - b[0], c[1] - b[1])
    n1, n2 = math.hypot(*v1), math.hypot(*v2)
    if n1 == 0 or n2 == 0:
        return 0.0
    cos = max(-1.0, min(1.0, (v1[0] * v2[0] + v1[1] * v2[1]) / (n1 * n2)))
    return math.degrees(math.acos(cos))


def catmull_rom(points, samples=6):
    """Centripetal Catmull-Rom through points; avoids overshoot at tight turns."""
    if len(points) < 3:
        return points
    padded = [points[0], *points, points[-1]]
    out = [points[0]]
    for i in range(1, len(padded) - 2):
        p0, p1, p2, p3 = padded[i - 1 : i + 3]
        t0 = 0.0
        t1 = t0 + max(math.dist(p0, p1), 1e-6) ** 0.5
        t2 = t1 + max(math.dist(p1, p2), 1e-6) ** 0.5
        t3 = t2 + max(math.dist(p2, p3), 1e-6) ** 0.5
        for s in range(1, samples + 1):
            t = t1 + (t2 - t1) * s / samples
            out.append(_barry_goldman(p0, p1, p2, p3, t0, t1, t2, t3, t))
    return out


def _barry_goldman(p0, p1, p2, p3, t0, t1, t2, t3, t):
    def lerp(a, b, ta, tb):
        if tb == ta:
            return a
        w = (t - ta) / (tb - ta)
        return (a[0] + (b[0] - a[0]) * w, a[1] + (b[1] - a[1]) * w)

    a1, a2, a3 = lerp(p0, p1, t0, t1), lerp(p1, p2, t1, t2), lerp(p2, p3, t2, t3)
    b1, b2 = lerp(a1, a2, t0, t2), lerp(a2, a3, t1, t3)
    return lerp(b1, b2, t1, t2)


def smooth(stroke):
    """Smooth each run between sharp corners so cusps stay crisp."""
    runs, run = [], [stroke[0]]
    for a, b, c in zip(stroke, stroke[1:], stroke[2:]):
        run.append(b)
        if turn_angle(a, b, c) >= CORNER_DEGREES:
            runs.append(run)
            run = [b]
    run.append(stroke[-1])
    runs.append(run)
    out = []
    for r in runs:
        pts = catmull_rom(r)
        out.extend(pts if not out else pts[1:])
    return out


def length(stroke) -> float:
    return sum(math.dist(a, b) for a, b in itertools.pairwise(stroke))


def pct(fraction: float) -> str:
    return f"{fraction * 100:.2f}%"


def keyframes(index: int, dash: int, start: float, end: float) -> str:
    erase = ERASE_START + (ERASE_END - ERASE_START) * (1 - end / DRAW_END)
    return (
        f".s{index}{{stroke-dasharray:{dash} {dash + 4};"
        f"animation:w{index} {CYCLE_MS}ms ease-in-out infinite both}}\n"
        f"@keyframes w{index}{{0%,{pct(start)}{{stroke-dashoffset:{dash}}}"
        f"{pct(end)},{pct(erase)}{{stroke-dashoffset:0}}"
        f"{pct(min(erase + 0.03, 1))},100%{{stroke-dashoffset:{dash}}}}}\n"
    )


def render(strokes, color: str, title: str) -> str:
    xs = [x for s in strokes for x, _ in s]
    ys = [y for s in strokes for _, y in s]
    min_x, min_y = min(xs) - PADDING, min(ys) - PADDING
    width, height = max(xs) - min_x + PADDING, max(ys) - min_y + PADDING
    lengths = [length(s) for s in strokes]
    total = sum(lengths)
    css, paths, cursor = [], [], 0.0
    for i, (stroke, size) in enumerate(zip(strokes, lengths)):
        start = DRAW_END * cursor / total
        cursor += size
        dash = math.ceil(size)
        css.append(keyframes(i, dash, start, DRAW_END * cursor / total))
        d = "M" + "L".join(f"{x - min_x:.1f},{y - min_y:.1f}" for x, y in stroke)
        paths.append(f'<path class="s{i}" d="{d}"/>')
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height:.0f}" '
        f'role="img" aria-label="{title}">\n<title>{title}</title>\n<style>\n'
        f"path{{fill:none;stroke:{color};stroke-width:{STROKE_WIDTH};"
        "stroke-linecap:round;stroke-linejoin:round}\n"
        + "".join(css)
        + "@media (prefers-reduced-motion:reduce){path{animation:none!important}}\n"
        "</style>\n" + "\n".join(paths) + "\n</svg>\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--text", default="Henry Chen")
    parser.add_argument("--font", default=FONT_URL, help="URL or path of an SVG font")
    parser.add_argument("--out", default="assets", type=Path)
    args = parser.parse_args()

    glyphs, default_adv = load_glyphs(args.font)
    strokes = [smooth(s) for s in layout(args.text, glyphs, default_adv)]
    args.out.mkdir(parents=True, exist_ok=True)
    for theme, color in THEMES.items():
        target = args.out / f"signature-{theme}.svg"
        target.write_text(render(strokes, color, args.text), encoding="utf-8")
        print(f"wrote {target} ({target.stat().st_size} bytes, {len(strokes)} strokes)")


if __name__ == "__main__":
    main()

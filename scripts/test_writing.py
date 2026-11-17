"""Run: python3 -m unittest scripts/test_writing.py"""

import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from writing import render, tag_source  # noqa: E402


class TagSourceTest(unittest.TestCase):
    def test_routes_a_post_through_the_github_source_link(self):
        self.assertEqual(
            tag_source("https://misoto22.com/blog/where-should-my-data-live"),
            "https://misoto22.com/r/github/blog/where-should-my-data-live",
        )

    def test_render_uses_the_tagged_link(self):
        line = render([(datetime(2026, 7, 31, tzinfo=timezone.utc), "A [post]", "https://misoto22.com/blog/a")])
        self.assertEqual(line, "- [A \\[post\\]](https://misoto22.com/r/github/blog/a) <sub>Jul 2026</sub>")


if __name__ == "__main__":
    unittest.main()

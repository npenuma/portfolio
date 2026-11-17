"""
Blog posts stored as Markdown files in the posts/ folder.

Each file starts with a small header between --- lines, for example:

    ---
    title: My first post
    date: 2026-11-17
    summary: One sentence shown on the post list.
    tags: AI, Learning
    draft: false
    ---

The file name (without .md) becomes the post's URL: /blog/<file-name>.
Posts are re-read on every request, so a new or edited file shows up
without restarting the server.
"""

import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import markdown

POSTS_DIR = Path(__file__).parent / "posts"
WORDS_PER_MINUTE = 200
_SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass
class Post:
    slug: str
    title: str
    date: date
    summary: str = ""
    tags: list[str] = field(default_factory=list)
    html: str = ""
    minutes: int = 1

    @property
    def date_label(self) -> str:
        return f"{self.date:%B} {self.date.day}, {self.date.year}"


def _parse(path: Path) -> Post | None:
    text = path.read_text(encoding="utf-8")
    meta: dict[str, str] = {}
    body = text
    if text.startswith("---"):
        _, header, body = text.split("---", 2)
        for line in header.strip().splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip().lower()] = value.strip()

    if meta.get("draft", "").lower() == "true" or "title" not in meta:
        return None
    try:
        post_date = date.fromisoformat(meta.get("date", ""))
    except ValueError:
        post_date = date.fromtimestamp(path.stat().st_mtime)

    return Post(
        slug=path.stem,
        title=meta["title"],
        date=post_date,
        summary=meta.get("summary", ""),
        tags=[t.strip() for t in meta.get("tags", "").split(",") if t.strip()],
        html=markdown.markdown(body, extensions=["fenced_code", "tables", "sane_lists"]),
        minutes=max(1, round(len(body.split()) / WORDS_PER_MINUTE)),
    )


def all_posts() -> list[Post]:
    """Published posts, newest first."""
    if not POSTS_DIR.is_dir():
        return []
    posts = [p for f in POSTS_DIR.glob("*.md") if _SLUG_RE.match(f.stem) and (p := _parse(f))]
    return sorted(posts, key=lambda p: p.date, reverse=True)


def get_post(slug: str) -> Post | None:
    if not _SLUG_RE.match(slug):
        return None
    path = POSTS_DIR / f"{slug}.md"
    return _parse(path) if path.is_file() else None

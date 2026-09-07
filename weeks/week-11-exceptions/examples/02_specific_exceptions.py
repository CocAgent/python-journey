"""Handle only expected failures."""

from pathlib import Path


def read_count(path: Path) -> int | None:
    try:
        return int(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except ValueError:
        return None

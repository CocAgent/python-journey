"""Reference Lab 01: explicit UTF-8 read/write, working-directory independent."""

from pathlib import Path


def save_notes(path: Path, lines: list[str]) -> Path:
    """Save lines, returning the exact path supplied by caller."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as stream:
        if lines:
            stream.write("\n".join(lines) + "\n")
    return path


def load_notes(path: Path) -> list[str]:
    """A missing file raises FileNotFoundError instead of claiming success."""
    with path.open("r", encoding="utf-8") as stream:
        return stream.read().splitlines()


if __name__ == "__main__":
    print("Run practice/checks/check_practice.py --solutions")

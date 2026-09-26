"""Official solution for pathlib text persistence."""

from pathlib import Path


def save_text(path: Path, lines: list[str]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def load_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()

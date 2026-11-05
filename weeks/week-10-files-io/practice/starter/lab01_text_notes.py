"""Lab 01: write and read UTF-8 lines at an explicit Path.

Starter functions must work inside any temporary directory.
See practice/README.md. Do not hardcode cwd or sample output paths.
"""

from pathlib import Path


def save_notes(path: Path, lines: list[str]) -> Path:
    """Create parent folders, save each note on its own line; return path."""
    # TODO: path.parent.mkdir(...); with path.open("w", encoding="utf-8") ...
    # TODO: write a final newline for nonempty notes, no newline for [].
    raise NotImplementedError("Hoàn thiện save_notes")


def load_notes(path: Path) -> list[str]:
    """Read UTF-8 notes. Missing file must raise FileNotFoundError."""
    # TODO: with path.open("r", encoding="utf-8") then splitlines().
    raise NotImplementedError("Hoàn thiện load_notes")


if __name__ == "__main__":
    print("Hoàn thiện hai hàm trước khi chạy self-check.")

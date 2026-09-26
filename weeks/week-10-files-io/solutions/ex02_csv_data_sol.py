"""Official solution for CSV persistence."""

import csv
from pathlib import Path


def save_rows(path: Path, rows: list[dict[str, object]]) -> Path:
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["bot", "wins"])
        writer.writeheader()
        writer.writerows(rows)
    return path


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as stream:
        return list(csv.DictReader(stream))

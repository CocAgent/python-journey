"""Lab 02: CSV score table, explicit schema, parse numeric text."""

import csv
from pathlib import Path


def save_scores(path: Path, rows: list[dict[str, object]]) -> Path:
    """Write name,score columns; names nonempty, score real int 0..10."""
    # TODO: validate all rows BEFORE writing; invalid => ValueError.
    # TODO: mkdir parent; with open(newline="", encoding="utf-8"),
    #       csv.DictWriter(fieldnames=["name","score"]), header, rows.
    raise NotImplementedError("Hoàn thiện save_scores")


def load_scores(path: Path) -> list[dict[str, object]]:
    """Read CSV; validate exact header and rows; scores return as int."""
    # TODO: with open(newline="", encoding="utf-8"), csv.DictReader.
    # TODO: header must be ["name","score"], rows nonempty name and
    #       score int in 0..10. Missing file -> FileNotFoundError;
    #       bad schema/value -> ValueError.
    raise NotImplementedError("Hoàn thiện load_scores")


if __name__ == "__main__":
    print("Hoàn thiện TODO rồi kiểm CSV round-trip.")

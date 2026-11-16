"""Reference Lab 02: CSV round-trip with explicit strict schema."""

import csv
from pathlib import Path


def check_score(name: object, score: object) -> None:
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Thiếu tên học viên")
    if type(score) is not int or not 0 <= score <= 10:
        raise ValueError("Điểm phải là số nguyên 0..10")


def save_scores(path: Path, rows: list[dict[str, object]]) -> Path:
    """Validate before opening file, preventing invalid partial writes."""
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"name", "score"}:
            raise ValueError("Sai cấu trúc cột")
        check_score(row["name"], row["score"])
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerows(rows)
    return path


def load_scores(path: Path) -> list[dict[str, object]]:
    """CSV cells are text, so convert and validate scores."""
    results: list[dict[str, object]] = []
    with path.open("r", newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ["name", "score"]:
            raise ValueError("Thiếu hoặc sai header")
        for row in reader:
            if None in row or set(row) != {"name", "score"}:
                raise ValueError("Sai số cột CSV")
            name = row["name"]
            score_text = row["score"]
            if not isinstance(score_text, str):
                raise ValueError("Thiếu cột điểm")
            try:
                score = int(score_text)
            except ValueError as error:
                raise ValueError("Điểm CSV không phải số nguyên") from error
            check_score(name, score)
            results.append({"name": name, "score": score})
    return results


if __name__ == "__main__":
    print("Run practice/checks/check_practice.py --solutions")

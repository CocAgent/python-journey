"""Student Manager business logic and persistence."""

import json
import math
from pathlib import Path


def validate_scores(scores: list[float]) -> list[float]:
    if not isinstance(scores, list) or not scores:
        raise ValueError("scores must be a non-empty list")
    checked = []
    for score in scores:
        if (
            isinstance(score, bool)
            or not isinstance(score, (int, float))
            or not math.isfinite(score)
            or not 0 <= score <= 10
        ):
            raise ValueError("each score must be a number between 0 and 10")
        checked.append(float(score))
    return checked


def calculate_average(scores: list[float]) -> float:
    values = validate_scores(scores)
    return sum(values) / len(values)


def classify_student(average: float) -> str:
    if not math.isfinite(average) or not 0 <= average <= 10:
        raise ValueError("invalid average")
    if average >= 8:
        return "Excellent"
    if average >= 6.5:
        return "Good"
    if average >= 5:
        return "Average"
    return "Needs improvement"


def find_student(students: list[dict], student_id: str) -> dict | None:
    return next((s for s in students if s["id"] == student_id.strip()), None)


def add_student(
    students: list[dict], student_id: str, name: str, scores: list[float]
) -> list[dict]:
    student_id, name = student_id.strip(), name.strip()
    if not student_id or not name:
        raise ValueError("ID and name are required")
    if find_student(students, student_id):
        raise ValueError("duplicate student ID")
    return [
        *students,
        {"id": student_id, "name": name, "scores": validate_scores(scores)},
    ]


def validate_students(data: object) -> list[dict]:
    if not isinstance(data, list):
        raise ValueError("expected list of students")
    checked: list[dict] = []
    for student in data:
        if not isinstance(student, dict):
            raise ValueError("invalid student")
        try:
            checked = add_student(
                checked, student["id"], student["name"], student["scores"]
            )
        except (KeyError, AttributeError, TypeError) as error:
            raise ValueError("invalid student record") from error
    return checked


def load_students(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError("invalid JSON data") from error
    return validate_students(data)


def save_students(path: Path, students: list[dict]) -> None:
    checked = validate_students(students)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(checked, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

"""Reference 02 — UTF-8 JSON report with schema checks and temp-file testing."""

import json
from pathlib import Path

FORMAT = "PYTHON JOURNEY REVIEW V1"


def validate_report(report: object) -> bool:
    """Contract for local review report, not a production file format."""
    if not isinstance(report, dict):
        return False
    if set(report) != {"format", "count", "average", "passed"}:
        return False
    if report["format"] != FORMAT:
        return False
    count = report["count"]
    average = report["average"]
    passed = report["passed"]
    if type(count) is not int or count < 0:
        return False
    if not isinstance(passed, list) or len(passed) > count:
        return False
    if any(not isinstance(name, str) or not name.strip() for name in passed):
        return False
    if len({name.strip().casefold() for name in passed}) != len(passed):
        return False
    if count == 0:
        return average is None and not passed
    return type(average) in (int, float) and 0 <= average <= 10


def save_report(path: Path, report: dict[str, object]) -> Path:
    """Reject before overwrite. Atomicity/multiuser locking is out of scope."""
    if not validate_report(report):
        raise ValueError("Report schema không hợp lệ")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as stream:
        json.dump(report, stream, ensure_ascii=False, indent=2)
    return path


def load_report(path: Path) -> dict[str, object]:
    with path.open("r", encoding="utf-8") as stream:
        report = json.load(stream)
    if not validate_report(report):
        raise ValueError("Report schema không hợp lệ")
    return report


if __name__ == "__main__":
    print("Run review/practice/checks/check_review.py --solutions")

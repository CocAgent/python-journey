"""Exercise 01: pathlib and UTF-8 text."""

from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "week10.txt"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text("Học Python tuần 10\nĐọc và ghi tập tin", encoding="utf-8")

for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
    print(f"{number}. {line}")

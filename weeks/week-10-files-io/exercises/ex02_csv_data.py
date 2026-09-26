"""Exercise 02: CSV match summary."""

import csv
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "match_summary.csv"
rows = [{"bot": "student", "wins": 2}, {"bot": "wait", "wins": 0}]
# TODO: tạo thư mục cha trước khi mở file.
# TODO: ghi header và rows bằng csv.DictWriter.
# TODO: tải rows bằng csv.DictReader rồi in kết quả.
print(csv.__name__, path, rows)

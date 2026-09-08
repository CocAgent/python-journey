"""Exercise 01: pathlib and UTF-8 text."""

from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "week10.txt"
# TODO: tạo thư mục cha.
# TODO: ghi hai dòng với encoding="utf-8".
# TODO: đọc text và in từng dòng với số thứ tự bắt đầu từ 1.
print(path)

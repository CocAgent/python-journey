"""Exercise 01: pathlib and UTF-8 text."""

from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "week10.txt"
# TODO: tạo thư mục cha.
path.parent.mkdir(parents=True, exist_ok=True)
# TODO: ghi hai dòng với encoding="utf-8".
content = "Dòng thứ nhất: Học thông qua làm\nDòng thứ hai: Cố gắng lên!"
path.write_text(content, encoding="utf-8")
# TODO: đọc text và in từng dòng với số thứ tự bắt đầu từ 1.
text_data = path.read_text(encoding="utf-8")

lines = text_data.splitlines()

for index, line in enumerate(lines, start=1):
    print(f"{index}. {line}")
print(f"\n[Đường dẫn file]: {path}")




"""Exercise 01: pathlib and UTF-8 text."""

from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "week10.txt"

# Tao thu muc cha
path.parent.mkdir(parents=True, exist_ok=True)

# Ghi hai dong UTF-8
with path.open("w", encoding="utf-8") as file:
    file.write("Xin chào Python\n")
    file.write("Đây là bài tập tuần 10\n")

# Doc va in cac dong co so thu tu
with path.open("r", encoding="utf-8") as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line.strip()}")

print(path)

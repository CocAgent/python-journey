"""Exercise 02: CSV match summary."""

import csv
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "match_summary.csv"
rows = [{"bot": "student", "wins": 2}, {"bot": "wait", "wins": 0}]
# TODO: tạo thư mục cha trước khi mở file.
path.parent.mkdir(parents=True, exist_ok=True)
# TODO: ghi header và rows bằng csv.DictWriter.
with path.open("w", newline="", encoding="utf-8") as stream:
    writer = csv.DictWriter(stream, fieldnames=["bot", "wins"])

    writer.writeheader()

    writer.writerows(rows)

    print("✓ Đã ghi dữ liệu vào file CSV thành công.\n")
# TODO: tải rows bằng csv.DictReader rồi in kết quả.
print("--- DỮ LIỆU ĐỌC TỪ FILE CSV ---")
with path.open("r", newline="", encoding="utf-8") as stream:
    reader = csv.DictReader(stream)

    for row in reader:
        bot_name = row["bot"]
        wins_count = int(row["wins"])
print(f"Bot: {bot_name:<10} | Số trận thắng: {wins_count} (Kiểu dữ liệu: {type(wins_count).__name__})")

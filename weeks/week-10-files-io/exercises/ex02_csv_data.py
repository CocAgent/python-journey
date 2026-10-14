"""Exercise 02: CSV match summary."""

import csv
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / "data" / "match_summary.csv"
rows = [{"bot": "student", "wins": 2}, {"bot": "wait", "wins": 0}]

# Tao thu muc cha
path.parent.mkdir(parents=True, exist_ok=True)

# Ghi CSV
with path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["bot", "wins"])
    writer.writeheader()
    writer.writerows(rows)

# Doc CSV
with path.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Bot: {row['bot']}, Wins: {row['wins']}")

print(csv.__name__, path, rows)

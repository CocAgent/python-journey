"""Exercise 03: JSON-compatible replay data."""

import json
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "replay.json"
replay = {
    "format": "COURSE LOCAL FORMAT",
    "production_compatibility": "NOT VUACOC PRODUCTION FORMAT",
    "turns": [],
}

# Tao thu muc cha
path.parent.mkdir(parents=True, exist_ok=True)

# Ghi JSON
with path.open("w", encoding="utf-8") as file:
    json.dump(replay, file, ensure_ascii=False, indent=2)

# Tai lai va kiem tra nhan
with path.open("r", encoding="utf-8") as file:
    data = json.load(file)

if (
    isinstance(data, dict)
    and data.get("format") == "COURSE LOCAL FORMAT"
    and data.get("production_compatibility") == "NOT VUACOC PRODUCTION FORMAT"
):
    print("Dữ liệu hợp lệ")
    print("Danh sách lượt chơi:", data["turns"])
else:
    print("Dữ liệu không hợp lệ")

print(json.__name__, path, replay)

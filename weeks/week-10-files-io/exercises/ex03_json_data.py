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
# TODO: tạo thư mục cha trước khi ghi file.
# TODO: lưu replay với ensure_ascii=False và indent=2.
# TODO: tải lại và kiểm tra cả hai nhãn trước khi đọc turns.
print(json.__name__, path, replay)

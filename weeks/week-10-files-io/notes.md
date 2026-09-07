# Week 10 — Data persistence

## pathlib và text

```python
from pathlib import Path

path = Path("evidence") / "note.txt"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text("Learn → Build → Test", encoding="utf-8")
text = path.read_text(encoding="utf-8")
```

## CSV

CSV là bảng: mỗi row có cùng nhóm column. Mở file với `newline=""` và
`encoding="utf-8"`.

```python
import csv

with Path("scores.csv").open("w", newline="", encoding="utf-8") as stream:
    writer = csv.DictWriter(stream, fieldnames=["bot", "wins"])
    writer.writeheader()
    writer.writerow({"bot": "student", "wins": 2})
```

## JSON và serialization

JSON hỗ trợ object/map, array/list, string, number, Boolean và null. Một Python
object tùy ý không tự động serialize; chuyển nó thành dict/list chứa giá trị
JSON-compatible trước.

```python
import json

payload = {"format": "COURSE LOCAL FORMAT", "turns": [{"action": "wait"}]}
encoded = json.dumps(payload, ensure_ascii=False, indent=2)
```

## Replay course-local

```text
in-memory MatchResult
→ JSON-compatible dict
→ explicit save
→ explicit load
→ inspect labels and turns
```

Không suy luận schema production từ ví dụ này.

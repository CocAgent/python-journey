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

## Đường dẫn tương đối và working directory

`Path("data.json")` được tính từ thư mục terminal đang đứng, không phải từ file
Python. Vì vậy cùng một script có thể ghi file ở hai nơi khác nhau nếu bạn chạy
nó từ hai working directory khác nhau.

Khi bài học cần output nằm cạnh nội dung tuần, hãy neo đường dẫn theo file:

```python
week_root = Path(__file__).resolve().parents[1]
output = week_root / ".learner-output" / "result.json"
output.parent.mkdir(parents=True, exist_ok=True)
```

Các exercise của tuần này dùng `.learner-output/`. Thư mục này bị Git bỏ qua để
việc luyện tập không vô tình tạo file cần commit.

## Đọc dữ liệu không có nghĩa là dữ liệu hợp lệ

File tồn tại vẫn có thể chứa dữ liệu sai. Tách ba bước để dễ debug:

```text
read text/bytes → parse CSV/JSON → validate fields and values
```

Với JSON, `json.loads()` có thể raise `json.JSONDecodeError`. Với CSV,
`DictReader` trả giá trị dạng chuỗi; chương trình phải chuyển kiểu và kiểm tra
range trước khi tính toán.

```python
try:
    data = json.loads(path.read_text(encoding="utf-8"))
except FileNotFoundError:
    print("Chưa có dữ liệu")
except json.JSONDecodeError as error:
    print(f"JSON không hợp lệ: {error}")
```

Chỉ bắt lỗi bạn có thể xử lý có ý nghĩa. Không dùng `except Exception: pass`.

## Checklist evidence

- file được ghi đúng thư mục và dùng UTF-8;
- CSV mở với `newline=""`;
- JSON giữ đúng kiểu dữ liệu tương thích;
- file thiếu và JSON lỗi có hành vi quan sát được;
- replay vẫn mang đủ hai nhãn course-local.

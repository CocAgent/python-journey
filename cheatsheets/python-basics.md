# Python Basics Cheat Sheet

## Kiểu dữ liệu
| Kiểu | Ví dụ | Mô tả |
|------|-------|-------|
| `int` | `42` | Số nguyên |
| `float` | `3.14` | Số thập phân |
| `str` | `"hello"` | Chuỗi |
| `bool` | `True` | Đúng/Sai |
| `list` | `[1,2,3]` | Danh sách |
| `dict` | `{"a":1}` | Từ điển |

## Input / Output
```python
name = input("Tên: ")
age = int(input("Tuổi: "))
print(f"Xin chào {name}, {age} tuổi!")
print(f"{3.14159:.2f}")       # 3.14
print(f"{1000000:,}")         # 1,000,000
```

## Toán tử: `+` `-` `*` `/` `//` `%` `**`
## So sánh: `==` `!=` `>` `<` `>=` `<=`
## Logic: `and` `or` `not`

## Điều kiện
```python
if x > 0:
    print("Dương")
elif x == 0:
    print("Zero")
else:
    print("Âm")
```

## Vòng lặp
```python
for i in range(5):        # 0..4
for item in my_list:      # duyệt list
while condition:          # lặp theo dk
```

## Hàm
```python
def greet(name, lang="vi"):
    return f"Xin chào {name}!"
```

## Collections

```python
topics = ["loops", "functions"]
point = (3, 7)
profile = {"name": "An", "week": 8}
unique_topics = {"loops", "functions"}

for index, topic in enumerate(topics, start=1):
    print(index, topic)
```

## File, CSV và JSON

```python
import json
from pathlib import Path

path = Path("data.json")
path.write_text(json.dumps({"week": 10}), encoding="utf-8")
data = json.loads(path.read_text(encoding="utf-8"))
```

## Try/Except
```python
try:
    risky_code()
except ValueError:
    handle_error()
```

## Pytest

```python
def test_total():
    assert sum([2, 3]) == 5
```

```bash
pytest -q
```

## Module và main guard

```python
from pathlib import Path


def main() -> None:
    print(Path.cwd())


if __name__ == "__main__":
    main()
```

## OOP vừa đủ

```python
class Progress:
    def __init__(self, completed: int, total: int):
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100
```

Ưu tiên function và dữ liệu đơn giản. Dùng class khi state và behavior thật sự
thuộc cùng một trách nhiệm; ưu tiên composition trước inheritance.

# Week 11 — Debugging và defensive coding

## Traceback anatomy

Đọc từ dòng cuối: exception type và message. Sau đó đi ngược lên frame gần code
của mình nhất để tìm file, line và operation gây lỗi.

## Expected bad input và programming bug

```python
try:
    age = int(raw_age)
except ValueError:
    print("Tuổi phải là số nguyên")
```

`ValueError` ở đây là input dự kiến có thể sai. `NameError`, invariant sai
hoặc typo thường là bug cần sửa, không nên bị che bởi broad exception.

## Raise và validation

```python
def validate_action(action: str) -> str:
    if action not in {"left", "right", "wait"}:
        raise ValueError(f"illegal local action: {action!r}")
    return action
```

## Debugging loop

```text
Reproduce
→ Read traceback
→ Isolate
→ Fix
→ Re-test
```

Giữ minimal failing input, sửa một nguyên nhân nhỏ rồi thêm regression check.

## Bot robustness

```text
strategy loss   → bot chạy đúng contract nhưng quyết định yếu
software defect → crash, malformed replay hoặc illegal local action
```

Arena course-local ghi rõ bot failure; nó không im lặng nuốt exception.

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

## `else` và `finally`

`else` chỉ chạy khi khối `try` không raise exception. Đặt success path ở đây
giúp `try` chỉ bao quanh operation có thể thất bại.

`finally` luôn chạy trước khi rời cấu trúc, kể cả khi function `return` hoặc có
exception. Nó phù hợp cho cleanup hoặc ghi nhận attempt; không dùng nó để che
exception.

```python
def parse_score(raw: str, audit_log: list[str]) -> int | None:
    try:
        score = int(raw)
    except ValueError:
        return None
    else:
        return score if 0 <= score <= 10 else None
    finally:
        audit_log.append(f"parsed={raw!r}")
```

Trong thực tế, context manager thường là cách rõ hơn để đóng file. `finally`
vẫn quan trọng khi bạn phải đảm bảo một bước kết thúc luôn diễn ra.

## Dự đoán luồng exception trước khi chạy

Trong [WORKED-EXAMPLES.md](WORKED-EXAMPLES.md), thực hành
ba tình huống: (1) lỗi logic không tạo traceback;
(2) `FileNotFoundError`/`ValueError` có thể xử lý
theo contract nhưng bug khác phải hiện rõ;
(3) `finally` vẫn chạy khi hàm return hoặc exception
không bị bắt.

Sau đó làm [4 lab tương tự](practice/README.md)
và chạy checker `--starter`. Bài kiểm thử theo dõi
type/message của exception, không chỉ in một dòng
`PASS`. Đây là bài đệm để tự viết `pytest` Week 12.

**Phân biệt contract hai tuần:** Lab 01 Week 10 chủ động
cho `FileNotFoundError` nổi lên; Lab 02 Week 11 chọn
trả `None` khi thiếu file điểm. Cả hai đều có thể hợp
lý khi được **công bố trước trong contract**.

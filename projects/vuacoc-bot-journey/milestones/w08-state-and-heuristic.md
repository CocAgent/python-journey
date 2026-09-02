# W08 — State + Heuristic

## Python focus

`dict`, `set`, nested data và data modeling.

## Milestone

Nâng state chuỗi của W07 thành dữ liệu có cấu trúc. Bot đọc một vài field cần
thiết và dùng heuristic ngắn, có thứ tự ưu tiên rõ.

```text
TEACHING MODEL — NOT VUACOC PRODUCTION CONTRACT
```

```python
teaching_state = {
    "status": "danger",
    "energy": 3,
    "available_actions": {"defend", "wait"},
}
```

Ví dụ trên chỉ là course-local data model. Nó không mô tả state schema, legal
actions hoặc protocol thật của VuaCóc.

## Learning moves

1. Chọn field thật sự cần cho quyết định.
2. Dùng `set` để biểu diễn teaching actions không trùng.
3. Viết heuristic từ đơn giản đến cụ thể.
4. Trả action thuộc teaching action set.

## Evidence

- State có cấu trúc và được giải thích.
- Heuristic có rules đọc được, không phụ thuộc thứ tự dictionary.
- Có normal state, boundary state và state thiếu dữ liệu theo course contract.
- Commit mô tả năng lực mới so với W07.

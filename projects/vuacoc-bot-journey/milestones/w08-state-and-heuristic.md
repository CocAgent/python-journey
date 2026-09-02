# W08 — State + Heuristic

## Python focus

`dict`, `set`, nested data và data modeling.

## Milestone

Nâng safe default của W07 thành reasoning từ structured course-local state. Bot
đọc một vài field cần thiết và dùng heuristic ngắn, có thứ tự ưu tiên rõ.

```text
TEACHING MODEL — NOT VUACOC PRODUCTION CONTRACT
```

```python
teaching_state = {
    "position": 1,
    "opponent_position": 3,
    "goal": 4,
    "turn": 2,
    "max_turns": 6,
    "min_position": 0,
    "max_position": 4,
}
```

Ví dụ trên chỉ là course-local data model. Nó không mô tả state schema, legal
actions hoặc protocol thật của VuaCóc.

## Learning moves

1. Chọn field thật sự cần cho quyết định.
2. Dùng `set` để biểu diễn local actions không trùng khi cần validate.
3. Viết heuristic từ đơn giản đến cụ thể.
4. Trả action thuộc teaching action set.

## Evidence

- State có cấu trúc và được giải thích.
- Heuristic có rules đọc được, không phụ thuộc thứ tự dictionary.
- Có normal state, boundary state và state thiếu dữ liệu theo course contract.
- Replay cho thấy state trước, action và state sau transition.
- Commit mô tả năng lực mới so với W07.

Chạy official learning check từ repository root:

```bash
python weeks/week-08-dicts-sets/checks/check_solutions.py
```

Sau khi đưa heuristic của bạn vào `student_bot/bot.py`, chạy một local match:

```bash
python projects/vuacoc-bot-journey/local_arena/cli.py --bot-a student --bot-b wait --replay
```

Match hoàn tất và action hợp lệ là evidence cho milestone này; không yêu cầu bot
phải thắng.

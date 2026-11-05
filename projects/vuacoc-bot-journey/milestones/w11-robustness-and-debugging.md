# W11 — Robustness + Debugging

## Python focus

Exceptions, tracebacks, debugging và defensive coding.

## Milestone

Bot xử lý các bad inputs đã biết trong course-local model và cung cấp evidence
cho quá trình sửa lỗi. Người học phải phân biệt hai loại thất bại:

```text
strategy loss
vs
software defect
```

Thua vì rule chưa tốt không giống crash, đọc sai dữ liệu hoặc trả giá trị ngoài
contract local. Chỉ software defect mới cần fix để khôi phục hành vi đã định.

## Debugging loop

```text
Reproduce → Read → Isolate → Fix → Re-test
```

## Evidence

- Minimal failing input cho ít nhất một bug.
- Traceback hoặc thông báo lỗi được đọc và giải thích.
- Fix nhỏ, không dùng bare `except:` để che lỗi.
- Case đã sửa được chạy lại thành công.
- Known strategy weakness vẫn được ghi riêng nếu chưa cải tiến.

## Course-local negative controls

- invalid local state: validation phải từ chối;
- illegal local action: match trả `bot_failure`;
- bot exception: type và message được ghi vào reason;
- malformed replay: loader raise `ValueError`;
- known failure regression: giữ minimal input và chạy lại sau fix.

```bash
pytest projects/vuacoc-bot-journey/tests/test_local_arena.py -q
pytest projects/vuacoc-bot-journey/tests/test_replay.py -q
```

# Mini-project — Robust Bot Debugging Note

Chạy negative controls của local arena và ghi evidence cho một software defect.

```bash
pytest projects/vuacoc-bot-journey/tests/test_local_arena.py -q
pytest projects/vuacoc-bot-journey/tests/test_replay.py -q
```

Evidence cần có:

- minimal failing input;
- exception type/message hoặc explicit failure reason;
- nguyên nhân đã isolate;
- fix nhỏ và regression check;
- strategy weakness, nếu có, ghi riêng với software defect.

Arena bắt exception tại boundary để ghi failure có quan sát được; learner code
không được dùng exception swallowing.

## Bài đệm trước Robust Bot Debugging Note

Học [ba ví dụ giải thích từng bước](../WORKED-EXAMPLES.md)
rồi tự làm [bốn lab](../practice/README.md) để phân biệt
**expected bad input** với **programming bug** và luyện
Reproduce → Read traceback → Isolate → Fix → Re-test.

Không dùng broad except để chuyển crash thành "match thua".
Nếu local arena báo `bot_failure`, ghi rõ failure reason
và regression evidence; không tuyên bố production integration.

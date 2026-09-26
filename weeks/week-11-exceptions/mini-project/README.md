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

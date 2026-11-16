# Ví dụ OOP qua nhiều module

- [bot.py](bot.py): định nghĩa class `Bot` và gọi `self.strategy(state)`.
- [strategies.py](strategies.py): định nghĩa hai hàm chiến lược độc lập.
- [test_oop_team.py](../test_oop_team.py): kiểm tra luồng hoạt động qua cả hai module.

```bash
python -m pytest weeks/week-14-oop-essentials/examples/test_oop_team.py -q
```

**Quan sát:** cùng một object Bot có thể đổi `strategy` khi chạy;
không phải tạo hai class kế thừa. Đây là ví dụ *tham chiếu*, không chấm
bài tập sinh viên.

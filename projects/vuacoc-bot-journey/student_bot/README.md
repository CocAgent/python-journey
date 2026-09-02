# Student Bot

Chỉnh [`bot.py`](bot.py) để phát triển cùng một decision policy qua khóa học.
Starter luôn trả local action an toàn `wait`, vì vậy có thể tham gia match ngay
trước khi bạn thêm rules.

> This is a Python Journey teaching contract. It is not the production
> contract of vuacoc.com.

## Progression

```text
W07: edit decision function
W08: reason from structured state
W09: compare with all three baselines
later: tests, replay analysis, adapter boundary, strategies
```

## Interface

```python
def choose_action(state):
    ...
```

Đọc [`../local_arena/CONTRACT.md`](../local_arena/CONTRACT.md) trước khi dùng
fields hoặc actions. Đây là course-local contract, không phải VuaCóc production
schema.

## Run a match

Từ repository root:

```bash
python projects/vuacoc-bot-journey/local_arena/cli.py --bot-a student --bot-b wait --replay
```

W07 evidence cần bot chạy, trả local legal action, giải thích được decision và
match hoàn tất. Không yêu cầu Student Bot phải thắng.

> Local Arena is not a security sandbox. Do not run untrusted Python code.

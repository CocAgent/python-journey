# Track A — VuaCóc Bot V1

Xây một bot nhỏ dùng structured course-local state và heuristic dễ giải thích.

```text
COURSE_LOCAL_ONLY = YES
VUACOC_PRODUCTION_COMPATIBILITY = NOT_CLAIMED
```

## Interface

```python
def choose_action(state):
    ...
```

Bot trả một trong `left`, `right`, `wait`. Đây là action set của Local Arena,
không phải production contract của VuaCóc.

## Required behavior

- Bot chạy local.
- Match hoàn tất trong giới hạn của arena.
- Action luôn thuộc course-local set.
- Rules đọc structured state và giải thích được.
- Không dùng global state không cần thiết.
- Không có win-rate bắt buộc.

## Build path

1. Copy [`../starter/vuacoc_bot_v1.py`](../starter/vuacoc_bot_v1.py).
2. Viết 2–4 rules theo thứ tự ưu tiên.
3. Thử normal, goal boundary và opponent-near states.
4. Đưa `choose_action` vào Student Bot của project.
5. Chạy lần lượt với WaitBot, ForwardBot và CautiousBot.
6. Điền kết quả vào [`../evidence-template.md`](../evidence-template.md).

Reference evaluator:

```bash
python weeks/week-09-midterm-project/reference/evaluate_baselines.py
```

Mỗi baseline record cần opponent, result, turn count, một observed strength và
một observed weakness. Không dùng Elo, Glicko hoặc statistical claims.

## Definition of done

```text
BOT_RUNS_LOCALLY = YES
MATCH_COMPLETES = YES
LOCAL_ACTIONS_VALID = YES
STRUCTURED_STATE_USED = YES
RULES_EXPLAINABLE = YES
NO_UNNECESSARY_GLOBAL_STATE = YES
GIT_EVIDENCE = PRESENT
KNOWN_WEAKNESS = DOCUMENTED
```

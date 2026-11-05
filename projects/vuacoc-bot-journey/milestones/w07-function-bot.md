# W07 — Function Bot

## Python focus

Functions, decomposition, scope và basic type hints.

## Milestone

Người học tạo một decision function nhỏ:

```python
def choose_action(state):
    ...
```

Ở local arena, starter có thể chưa đọc structured state và chỉ trả một safe
default action. Teaching action set là `left`, `right`, `wait`. Policy có tối đa
3–5 rules, deterministic và mỗi rule có thể giải thích bằng một câu.

```text
TEACHING MODEL — NOT VUACOC PRODUCTION CONTRACT
```

## Constraints

- Không server.
- Không OOP hoặc class hierarchy.
- Không network/API.
- Không machine learning.
- Không state schema production.

## Evidence

- Cùng state được gọi nhiều lần cho cùng action.
- Bot chạy và trả một local legal action.
- Match với baseline hoàn tất trong `max_turns`.
- Người học giải thích được `state → function → action`.
- Commit chứa decision function và ghi chú ngắn.

W07 **không yêu cầu bot thắng**. Kết quả match là feedback, không phải điều kiện
hoàn thành tuần.

Week 07 lesson hiện có tại
[`weeks/week-07-functions`](../../../weeks/week-07-functions/README.md).

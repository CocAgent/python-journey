# W07 — Function Bot

## Python focus

Functions, decomposition, scope và basic type hints.

## Milestone

Người học tạo một decision function nhỏ:

```python
def choose_action(state: str) -> str:
    ...
```

State là một input nhỏ dạng chuỗi. Teaching action set cũng nhỏ, ví dụ
`defend`, `advance`, `wait`. Policy có tối đa 3–5 rules, deterministic và mỗi
rule có thể giải thích bằng một câu.

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
- Các teaching states mẫu đều có output.
- Người học giải thích được `state → function → action`.
- Commit chứa decision function và ghi chú ngắn.

Week 07 lesson hiện có tại
[`weeks/week-07-functions`](../../../weeks/week-07-functions/README.md).

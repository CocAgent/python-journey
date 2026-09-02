# W14 — Strategy Composition

## Python focus

Class, object, composition và basic inheritance chỉ khi được chứng minh là hữu
ích.

## Milestone

Bot nhận strategy từ bên ngoài để có thể đổi policy mà không viết lại bot core:

```python
class Bot:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state):
        return self.strategy(state)
```

Preferred rule:

```text
COMPOSITION BEFORE INHERITANCE
```

## Learning moves

1. Giữ các strategy nhỏ và test được độc lập.
2. Truyền strategy vào `Bot` thay vì hardcode policy.
3. Chạy cùng state qua hai strategy local để so sánh.
4. Chỉ dùng basic inheritance nếu có quan hệ “is-a” tự nhiên và rõ hơn.

## Evidence

- Swap strategy không cần sửa method điều phối chính.
- Mỗi strategy có tests hành vi.
- Người học giải thích vì sao composition phù hợp.
- Không có class hierarchy hoặc design pattern phức tạp không cần thiết.

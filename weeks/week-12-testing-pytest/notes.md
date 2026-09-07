# Week 12 — pytest foundation

## Discovery và assert

Pytest tìm file `test_*.py` và function `test_*`. Một assertion so sánh
actual behavior với expected behavior.

## Arrange → Act → Assert

```python
def test_wait_action_is_legal():
    # Arrange
    state = {"position": 2}

    # Act
    action = choose_action(state)

    # Assert
    assert action in {"left", "right", "wait"}
```

## Case selection

- normal: input điển hình;
- edge: biên hợp lệ như list rỗng hoặc turn cuối;
- invalid: input ngoài contract và expected exception;
- regression: input nhỏ từng làm code sai.

Fixture nhỏ chỉ dùng khi setup chung thực sự làm test rõ hơn. Tuần này không
cần mock framework, patch-heavy tests hay test architecture.

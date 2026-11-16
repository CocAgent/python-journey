# W12 — Testing with pytest

## Python focus

Test functions, `assert`, Arrange → Act → Assert và đọc test failure.

## Milestone

Tạo regression suite cho bot core. Tests gọi decision logic trực tiếp, không
cần server, network hoặc production adapter.

## Test coverage tối thiểu

```text
normal decision
boundary state
invalid input
never return illegal local action
regression for previously fixed bug
```

“Illegal” ở đây chỉ có nghĩa ngoài teaching action set do course local định
nghĩa.

## Constraints

- Không mocking nâng cao.
- Không integration-test architecture phức tạp.
- Không test chi tiết implementation khi behavior là điều cần chứng minh.

## Evidence

- Test suite chạy được bằng `pytest`.
- Có ít nhất một test từng fail trước fix và pass sau fix.
- Tên test mô tả hành vi.
- Người học giải thích được failure message quan trọng.
Week 12 learner tests nằm trong week directory; root `tests/` là maintainer
invariants và không phải bài tập learner.

Tối thiểu có normal, edge, invalid và regression cases theo
Arrange → Act → Assert. Không cần mocking framework.

```bash
pytest weeks/week-12-testing-pytest/tests -q
pytest projects/vuacoc-bot-journey/tests -q
```

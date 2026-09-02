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

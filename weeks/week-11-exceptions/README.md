# Tuần 11 — Exceptions · Tracebacks · Debugging · Defensive coding

Tuần này bạn đọc lỗi trước khi sửa, bắt đúng lỗi dự kiến và để programming bug
tiếp tục hiện rõ.

## Outcomes

- đọc exception type, message và vị trí cuối traceback;
- phân biệt expected bad input với programming bug;
- dùng `try/except` cho exception cụ thể và `raise` khi contract bị vi phạm;
- áp dụng `Reproduce → Read traceback → Isolate → Fix → Re-test`;
- phân biệt strategy loss với software defect trong bot local.

Đi theo [notes](notes.md), [examples](examples/), [exercises](exercises/),
[hints](hints.md), [machine check](checks/README.md) và
[mini-project](mini-project/README.md).

Không dùng `except Exception: pass` để tạo cảm giác “robust”.

# Tuần 11 — Exceptions · Tracebacks · Debugging · Defensive coding

Tuần này bạn đọc lỗi trước khi sửa, bắt đúng lỗi dự kiến và để programming bug
tiếp tục hiện rõ.

## Outcomes

- đọc exception type, message và vị trí cuối traceback;
- phân biệt expected bad input với programming bug;
- dùng `try/except/else/finally` đúng vai trò và `raise` khi contract bị vi phạm;
- áp dụng `Reproduce → Read traceback → Isolate → Fix → Re-test`;
- phân biệt strategy loss với software defect trong bot local.

Đi theo [notes](notes.md), [examples](examples/), [exercises](exercises/),
[hints](hints.md), [machine check](checks/README.md) và
[mini-project](mini-project/README.md).

Không dùng `except Exception: pass` để tạo cảm giác “robust”.

## Ví dụ có hướng dẫn và bốn bài tự luyện

Học tiếp theo phương pháp **Dự đoán → Chạy → Đọc lỗi →
Tái hiện → Sửa nguyên nhân → Regression check**.
Bắt đầu tại [WORKED-EXAMPLES.md](WORKED-EXAMPLES.md):

```bash
python weeks/week-11-exceptions/examples/05_predict_traceback_regression.py
python weeks/week-11-exceptions/examples/06_predict_specific_exceptions.py
python weeks/week-11-exceptions/examples/07_predict_else_finally.py
```

Sau khi dự đoán output của từng ví dụ, tự làm
[4 lab](practice/README.md) về exception cụ thể, file lỗi,
raise có thông tin, `except/else/finally`.

```bash
python weeks/week-11-exceptions/practice/checks/check_practice.py --starter
python weeks/week-11-exceptions/practice/checks/check_practice.py --solutions
```

`--starter` **ban đầu FAIL (0/4)** vì TODO chưa hoàn thiện;
`--solutions` chỉ kiểm lời giải tham khảo. Bộ checker
kiểm trực tiếp `return`, exception type, error message,
và audit event order, không chấp nhận broad catch che bug.
Đây là bài bổ sung, **không thay official exercises,
mini-project hoặc rubric**.

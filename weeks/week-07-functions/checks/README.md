# Week 07 machine check

Machine check này dùng Python standard library để kiểm tra hành vi của official
solutions. Người học chưa cần biết cú pháp `pytest`; testing với `pytest` thuộc
Week 12.

Chạy từ repository root:

```bash
python weeks/week-07-functions/checks/check_solutions.py
```

Kết quả thành công:

```text
Week 07 solution checks: PASS
```

Nếu có lỗi, output nêu case không đạt và process trả exit code khác 0. Đây là
check cho reference artifacts, không tự chấm starter code của người học.

## Bộ tự kiểm bài Functions tương tự

Chạy từ gốc `python-journey`:

```bash
# Gọi chính các function trong practice/starter: chưa làm TODO -> FAIL
python weeks/week-07-functions/practice/checks/check_practice.py --starter

# Dùng trong maintainer CI để xác nhận lời giải tham khảo
python weeks/week-07-functions/practice/checks/check_practice.py --solutions
```

Khác với machine check so output đơn giản, checker này
**import và gọi hàm thật**, kiểm `return`, input biên,
`ValueError`, trạng thái local và khả năng tái sử dụng hàm con.
Nó chỉ dùng standard library; sinh viên chưa cần biết `pytest`.

**Không nhầm:** `Week 07 reference practice: PASS (4/4)`
không phải bằng chứng student starter đã hoàn tất.
Xem [sổ tay hướng dẫn](../WORKED-EXAMPLES.md).

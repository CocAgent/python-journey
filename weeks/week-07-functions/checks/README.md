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

# Week 06 machine check

```bash
python weeks/week-06-loops/checks/check_solutions.py
```

## Bài tương tự — kiểm code sinh viên, tách khỏi official check

Từ **gốc repository**:

```bash
# Kiểm code đã viết trong practice/starter; trước khi hoàn thiện sẽ FAIL
python weeks/week-06-loops/practice/checks/check_practice.py --starter

# Kiểm lời giải tham khảo, maintainer CI dùng chế độ này
python weeks/week-06-loops/practice/checks/check_practice.py --solutions
```

Checker dùng thư viện chuẩn, không cần `pytest` ở Week06.
`--solutions` PASS không chứng minh `--starter` đã hoàn thành.
Xem [WORKED-EXAMPLES.md](../WORKED-EXAMPLES.md) để dự đoán trace.

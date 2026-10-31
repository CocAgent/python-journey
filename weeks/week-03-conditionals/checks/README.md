# Week 03 machine check

```bash
python weeks/week-03-conditionals/checks/check_solutions.py
```

Check dùng standard library và kiểm tra official decision functions.

## Tự kiểm ba lab bổ sung

Từ gốc repository:

```bash
# Kiểm code sinh viên đang viết; ban đầu FAIL vì starter chứa TODO
python weeks/week-03-conditionals/practice/checks/check_practice.py --starter

# Kiểm lời giải mẫu; maintainer CI chỉ chạy chế độ này
python weeks/week-03-conditionals/practice/checks/check_practice.py --solutions
```

Hai chế độ này **không đồng nghĩa**. `--solutions` PASS không
chứng minh sinh viên đã hoàn thành starter. Có nhiều case thường,
biên và lỗi; tất cả chạy offline, không cần pytest ở Week03.
Xem [sổ tay dự đoán kết quả](../WORKED-EXAMPLES.md).

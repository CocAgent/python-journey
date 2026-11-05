# Week 02 machine check

Chạy từ repository root:

```bash
python weeks/week-02-variables-types/checks/check_solutions.py
```

Check dùng standard library và chỉ kiểm tra official solutions.

## Kiểm thêm ba bài tương tự

Chạy từ **repository root**:

```bash
# Kiểm chính mã sinh viên trong practice/starter (ban đầu FAIL đúng thiết kế)
python weeks/week-02-variables-types/practice/checks/check_practice.py --starter

# Kiểm đáp án tham khảo trong practice/solutions (CI chỉ dùng chế độ này)
python weeks/week-02-variables-types/practice/checks/check_practice.py --solutions
```

Đây là kiểm tra đầu ra và trường hợp sai theo [WORKED-EXAMPLES.md](../WORKED-EXAMPLES.md);
không yêu cầu pytest ở Week02. **Official check** `check_solutions.py`
vẫn chỉ kiểm lời giải ba bài gốc, không chấm starter TODO.

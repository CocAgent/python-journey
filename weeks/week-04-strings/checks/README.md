# Week 04 machine check

```bash
python weeks/week-04-strings/checks/check_solutions.py
```

Check bao gồm string processing và regex mini-lab official solutions.

## Bộ bài tương tự (không thay official solutions)

Chạy từ **repository root**:

```bash
# Kiểm chính file trong practice/starter — ban đầu FAIL đúng thiết kế
python weeks/week-04-strings/practice/checks/check_practice.py --starter

# Kiểm reference trong practice/solutions — maintainer CI dùng chế độ này
python weeks/week-04-strings/practice/checks/check_practice.py --solutions
```

Bộ kiểm dùng standard library để chạy nhiều input/edge/no-match case,
không cần `pytest` trong bài W04. `--solutions` PASS **không phải**
chứng cứ sinh viên đã hoàn thành starter.
Xem [WORKED-EXAMPLES.md](../WORKED-EXAMPLES.md).

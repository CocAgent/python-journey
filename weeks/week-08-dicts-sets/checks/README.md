# Week 08 machine check

Machine check dùng Python standard library để kiểm tra hành vi của official
solutions. Nó không chấm strategy của learner và không yêu cầu kiến thức về
testing framework.

Chạy từ repository root:

```bash
python weeks/week-08-dicts-sets/checks/check_solutions.py
```

Kết quả thành công:

```text
Week 08 solution checks: PASS
```

Nếu thất bại, output nêu case cần xem lại và process trả exit code khác 0.

## Self-check bốn bài tự luyện mới

Từ repository root:

```bash
# Kiểm các function trong practice/starter (chưa hoàn thành: FAIL)
python weeks/week-08-dicts-sets/practice/checks/check_practice.py --starter

# Chỉ kiểm reference, maintainer CI dùng mode này
python weeks/week-08-dicts-sets/practice/checks/check_practice.py --solutions
```

Bộ checker mới dùng Python standard library để import và gọi trực tiếp
các function, kiểm return, schema, dữ liệu không hợp lệ, không sửa
input, set/list order và tính tất định của heuristic.

Nó không thay official check trong file hiện tại; không cần
`pytest` ở Week08. `--solutions` PASS **không có nghĩa**
sinh viên đã giải được các TODO starter.

Xem [WORKED-EXAMPLES.md](../WORKED-EXAMPLES.md).

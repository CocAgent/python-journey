# Week 15 capstone readiness check

Readiness checker tự kiểm tra **submission của chính bạn** trước khi handoff.

Nó đo evidence cơ học, không chấm chất lượng thiết kế và không thay rubric.
Rubric duy nhất nằm tại
[FINAL_PROJECT.md](../../../FINAL_PROJECT.md).

## Mặc định

```bash
python weeks/week-15-capstone-project/checks/check_capstone_readiness.py path/to/my-project
```

Checker kiểm:

- README có nội dung về problem/scope, chức năng, chạy, test và thiết kế;
- có `AI_USAGE.md`;
- có Python source và source parse được;
- có ít nhất 5 test function;
- pytest collect được;
- không có bare `except:`.

Checker **không ép quota số hàm/class/module**.

## Chạy tests thật

Với project của chính bạn:

```bash
python weeks/week-15-capstone-project/checks/check_capstone_readiness.py \
  path/to/my-project --run-tests
```

`--run-tests` chạy code qua pytest. Không dùng tùy chọn này với code không tin
cậy.

## Kết quả

PASS:

```text
Week 15 capstone readiness: PASS
```

FAIL sẽ liệt kê từng evidence còn thiếu. Sửa rồi chạy lại trước demo/review.

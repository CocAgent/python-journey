# Week 01 AutoGrade — tự đánh giá 5 điểm thực hành

Bản AG-01 dùng chính ba file starter sẵn có: `exercises/ex01_hello.py` (2 điểm), `exercises/ex02_calculator.py` (2 điểm), `mini-project/starter_basic.py` (1 điểm). Điều kiện được khai báo trong [`rubric.json`](rubric.json).

Ở **thư mục gốc** `python-journey`, sau khi học viên viết code:

```bash
python -m assessment grade --week 01 --acknowledge-local-code
```

Báo cáo JSON riêng tư (không upload):

```bash
python -m assessment grade --week 01 --acknowledge-local-code --json-out .learner-output/week01.json
```

Trong thang điểm 10 của Week 01, **máy chỉ tự kiểm 5 điểm**. Giảng viên đánh giá thêm: môi trường/terminal/REPL (2), minh chứng một lỗi được sửa (1), Git commit/hướng dẫn/evidence (2). Không dùng `--mode reference` làm bằng chứng đã nộp bài; đó là bài mẫu của bộ chấm.

`ex03_input.py` và mini-project dùng `input()` thuộc Week 02 nên không tính điểm bắt buộc. Kết quả kiểm tra stdout/AST chỉ là gợi ý học tập, không thay xác minh của giảng viên.

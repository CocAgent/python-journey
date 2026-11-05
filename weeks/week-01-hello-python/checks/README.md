# Machine checks Tuần 01

Có **hai loại xác nhận khác nhau**:

1. **Sinh viên tự kiểm tra**: chạy chính `exercises/ex01_hello.py`,
   `ex02_calculator.py`, nhìn output và đối chiếu
   [đề](../exercises/README.md), rồi điền
   [minh chứng](../evidence-template.md).
2. **Maintainer kiểm tra chất lượng giáo trình**: chạy lệnh:

```bash
# Không cần pytest, không chạy student starter:
python weeks/week-01-hello-python/checks/check_week.py

# Nếu đã cài pytest trong dev environment:
python -m pytest weeks/week-01-hello-python/tests -q
```

`check_week.py` gọi `check_solutions.py` + `check_examples.py`.
Các test pytest của tuần thử lời giải ở dữ liệu thường/biên và
mini-project **tham chiếu**. Root CI gọi chúng qua
`tests/test_week_owned_checks.py`, nhưng không thu `exercises/`
hoặc starter mini-project.

**PASS của giảng viên không phải điểm bài tập sinh viên.** Việc
`ex01` chạy mà không in gì trước khi hoàn thành TODO là bình thường.

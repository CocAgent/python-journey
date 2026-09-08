# Chạy exercises Week 13

Các exercise import package `bot_course`, vì vậy hãy chạy chúng theo module
mode từ thư mục của tuần:

```bash
cd weeks/week-13-modules-cli-api
python -m exercises.ex01_modules
python -m exercises.ex02_cli --turn 3
python -m exercises.ex03_http
```

Module mode đặt week root vào import path. Nếu chạy trực tiếp
`python exercises/ex03_http.py`, Python chỉ nhìn thấy thư mục `exercises/` và
không tìm được package sibling `bot_course`.

Sau khi hoàn thành, quay về repository root trước khi tiếp tục các command ở
tài liệu chính.

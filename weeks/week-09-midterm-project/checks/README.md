# Week 09 reference check

Machine check xác nhận reference Bot V1 có callable, trả course-local action và
hoàn tất match với đúng ba baseline. Nó không chấm strategy và không yêu cầu bot
thắng.

Chạy từ repository root:

```bash
python weeks/week-09-midterm-project/checks/check_midterm_reference.py
```

Kết quả thành công:

```text
Week 09 midterm reference checks: PASS
```

## Kiểm tra danh mục dự án tham khảo

Danh mục Track C có công cụ **kiểm tra tài liệu giáo trình** (không phải chấm bài sinh viên):

```bash
python weeks/week-09-midterm-project/checks/check_project_catalog.py
```

Lệnh này kiểm tra 20 mục, 20 URL GitHub, tiêu chí rubric và liên kết nội bộ. `PASS` không có nghĩa một nhóm sinh viên đã làm đúng. Track C phải được đánh giá theo [rubric 10 điểm](../project-ideas/rubric-10-diem.md) và bằng chứng bài nộp.

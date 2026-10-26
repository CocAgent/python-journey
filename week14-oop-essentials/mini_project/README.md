# Mini Project — Student Manager OOP

## Mục tiêu

Áp dụng class, object, methods, `__str__`, composition và basic inheritance vào một bài toán gần thực tế.

## Mô hình

```text
StudentManager
    │
    ├── Student
    │      └── courses → Course
    │
    └── Course
```

`Student` có nhiều `Course`, đây là ví dụ về composition: một object sử dụng và quản lý các object khác.

## Chức năng

- Hiển thị danh sách sinh viên.
- Tìm sinh viên theo mã.
- Thêm môn học cho sinh viên.
- Tính tổng số tín chỉ.
- Kiểm tra input số tín chỉ.

## Chạy

Từ thư mục repository:

```bash
python week14-oop-essentials/mini_project/student_manager.py
```

## Bài nâng cấp

1. Thêm chức năng thêm sinh viên.
2. Không cho phép trùng mã sinh viên.
3. Xóa sinh viên.
4. Xóa môn học.
5. Tính điểm trung bình.
6. Lưu dữ liệu sang JSON ở Tuần 15 hoặc khi ôn tập Tuần 10.
7. Viết test cho `StudentManager`.

# Tuần 14 — OOP: Class, Object, Composition và Kế thừa cơ bản

> **Mục tiêu:** Biết dùng class để gom dữ liệu và hành vi, thay đổi hành vi Bot
> bằng composition, hiểu kế thừa và kiểm thử chương trình OOP.

Bài học tiếp nối hàm, ngoại lệ, module và pytest. Yêu cầu Python 3.12+ và pytest
đã cài theo [SETUP](../../SETUP.md).

## Sau bài học, sinh viên làm được

1. Tạo class và object bằng __init__ và self.
2. Phân biệt thuộc tính, phương thức, return và print.
3. Dùng __str__ để trả chuỗi hiển thị.
4. Kiểm tra dữ liệu đầu vào và báo ValueError khi không hợp lệ.
5. Dùng composition để thay chiến lược cho Bot.
6. Dùng inheritance cho quan hệ “là một”.
7. Viết và chạy pytest cho các trường hợp đúng, sai và biên.

## Lộ trình học

| Bước | Tài liệu / thực hành | Bằng chứng |
|---|---|---|
| 1. Nền tảng | [Bài giảng](notes.md), [Progress](examples/01_class_object.py) | Hiểu self, __init__, __str__ |
| 2. Đối tượng | [DienThoai](examples/04_dien_thoai.py) | Tạo hai điện thoại độc lập |
| 3. Đổi hành vi | [Composition](examples/02_composition.py), [Kế thừa](examples/03_basic_inheritance.py) | Phân biệt “có” và “là một” |
| 4. Bài tập có lời giải | [Bốn bài tập](exercises/README.md) | Đọc, chạy và giải thích code |
| 5. Kiểm tra | [Lệnh kiểm tra](checks/README.md) | Test bài tập và lời giải |
| 6. Vận dụng | [Mini-project Bot nhiều tệp](mini-project/README.md) | Tách Bot khỏi chiến lược |

## Chạy tại thư mục gốc repository

    python weeks/week-14-oop-essentials/examples/01_class_object.py
    python weeks/week-14-oop-essentials/examples/02_composition.py
    python weeks/week-14-oop-essentials/examples/03_basic_inheritance.py
    python weeks/week-14-oop-essentials/examples/04_dien_thoai.py
    python weeks/week-14-oop-essentials/checks/check_student.py
    python weeks/week-14-oop-essentials/checks/check_week.py

- check_student.py kiểm tra bốn bài trong exercises/.
- check_week.py kiểm tra lời giải tham khảo và ví dụ.
- PASS là bằng chứng test đã chạy thành công, không thay thế việc tự giải thích code.

## Quy ước

- Tên class dùng PascalCase như DienThoai; biến và phương thức dùng snake_case.
- self.ma_may là thuộc tính riêng của từng object.
- Comment giải thích lý do kiểm tra và trường hợp biên.
- Đọc [gợi ý](hints.md), [bài tập](exercises/README.md) và [lời giải](solutions/README.md).

## Đánh giá tham khảo / 10 điểm

| Tiêu chí | Điểm |
|---|---:|
| Bài 1: class, phương thức, __str__, dữ liệu hợp lệ | 2 |
| Bài 2: composition, thay chiến lược, hai hướng | 3 |
| Bài 3: kế thừa và quan hệ “là một” | 1 |
| Bài 4: DienThoai, hai object và xác thực | 2 |
| Giải thích thiết kế, test và minh chứng chạy | 2 |
| **Tổng** | **10** |

Rubric chỉ là gợi ý; sinh viên cần hiểu và giải thích được code của mình.

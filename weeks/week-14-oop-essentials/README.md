# Tuần 14 — OOP: Class, Object, Composition và Kế thừa cơ bản

> **Mục tiêu:** Biết khi nào nên dùng class để gom dữ liệu và hành vi,
> biết thay đổi hành vi của Bot bằng composition, và biết kiểm thử bài OOP.

Bài học tiếp nối kiến thức **hàm**, **ngoại lệ**, **module** và **pytest**.
Chỉ yêu cầu Python 3.12+ và pytest đã cài theo [SETUP](../../SETUP.md).

## Sau bài học, sinh viên làm được

1. Tạo `class`, khởi tạo nhiều `object` bằng `__init__` và `self`.
2. Trình bày được vai trò của **thuộc tính** và **phương thức**.
3. Phân biệt `return` (trả dữ liệu) và `print` (hiển thị).
4. Dùng `__str__` để hiển thị thông tin dễ hiểu, không tạo tác dụng phụ.
5. Từ chối dữ liệu đầu vào sai với `ValueError` khi cần.
6. Dùng **composition** để gắn chiến lược cho Bot, đổi chiến lược mà không sửa class.
7. Dùng **inheritance** cho quan hệ “là một”, không lạm dụng kế thừa.
8. Viết và chạy test kiểm chứng hành vi của **chính bài làm sinh viên**.

## Lộ trình học và sản phẩm

| Bước | Tài liệu / thực hành | Bằng chứng |
|---|---|---|
| 1. Nền tảng | [Bài giảng](notes.md) và [ví dụ Progress](examples/01_class_object.py) | Biết `self`, `__init__`, `__str__` |
| 2. Đối tượng thực | [Ví dụ DienThoai](examples/04_dien_thoai.py) | Tạo hai điện thoại độc lập |
| 3. Đổi hành vi | [Composition](examples/02_composition.py), [Kế thừa](examples/03_basic_inheritance.py) | Phân biệt “có” và “là một” |
| 4. Tự làm | [Bốn bài tập](exercises/README.md) | Hoàn thành mã của chính mình |
| 5. Tự kiểm tra | [Hai lệnh kiểm tra khác nhau](checks/README.md) | Phân biệt bài sinh viên và lời giải mẫu |
| 6. Vận dụng | [Mini-project Bot nhiều tệp](mini-project/README.md) | Tách Bot khỏi chiến lược, có test |

## Lệnh chạy — tại thư mục gốc repository

```bash
# Chạy từng ví dụ để quan sát kết quả.
python weeks/week-14-oop-essentials/examples/01_class_object.py
python weeks/week-14-oop-essentials/examples/02_composition.py
python weeks/week-14-oop-essentials/examples/03_basic_inheritance.py
python weeks/week-14-oop-essentials/examples/04_dien_thoai.py

# CHỈ kiểm tra lời giải và ví dụ mẫu.
python weeks/week-14-oop-essentials/checks/check_week.py

# Kiểm tra bài tập DO SINH VIÊN TỰ VIẾT.
python weeks/week-14-oop-essentials/checks/check_student.py
```

**Quan trọng:** starter có `raise NotImplementedError` nên lệnh kiểm tra sinh viên
**FAIL có chủ đích trước khi làm bài**. Đây là điều đúng. Lệnh kiểm tra lời giải
mẫu PASS **không có nghĩa** sinh viên đã hoàn thành bài.

## Quy ước viết code và comment tiếng Việt

- Tên class dùng `PascalCase` như `DienThoai`; tên biến, phương thức dùng `snake_case`.
- `self.ma_may` là thuộc tính của từng điện thoại, không phải biến dùng chung.
- Comment giải thích lý do kiểm tra, trường hợp biên; không phiên dịch từng lệnh.
- Đọc [gợi ý theo cấp độ](hints.md) khi gặp lỗi, tự thử trước khi xem lời giải.
- Không đưa framework, metaclass, nhiều cấp kế thừa hay Bot AI phức tạp vào tuần này.

## Đánh giá tham khảo theo thang điểm 10

| Tiêu chí | Điểm |
|---|---:|
| Bài 1: class, phương thức, `__str__`, dữ liệu hợp lệ | 2 |
| Bài 2: composition, thay chiến lược, hai hướng di chuyển | 3 |
| Bài 3: kế thừa và giải thích quan hệ “là một” | 1 |
| Bài 4: lớp `DienThoai`, hai object và đầu vào sai | 2 |
| Giải thích được quyết định thiết kế, test và minh chứng chạy | 2 |
| **Tổng** | **10** |

Rubric là gợi ý cho **giảng viên**, không phải điểm tự động do máy quyết định.
Sinh viên cần giải thích được code và ghi lại lệnh thực sự đã chạy.

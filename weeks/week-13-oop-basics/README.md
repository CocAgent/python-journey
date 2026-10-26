# Tuần 13: OOP cơ bản — Class & Object 🏗️

Tuần này luyện cách tổ chức dữ liệu và hành vi bằng **lập trình hướng đối tượng (OOP)** trong Python.

## 🎯 Mục tiêu

Sau khi hoàn thành, người học có thể:

- Phân biệt **class** (khuôn mẫu) và **object** (đối tượng được tạo từ class).
- Dùng `__init__()` để khởi tạo object và `self` để truy cập dữ liệu của object hiện tại.
- Viết instance methods và `__str__()` để hiển thị object dễ đọc.
- Dùng class variable và `@classmethod`.
- Thiết kế class đơn giản, kiểm tra dữ liệu đầu vào và xử lý trường hợp không hợp lệ.

## 📚 Kiến thức

Đọc [notes.md](notes.md) trước hoặc trong lúc làm bài.

Các khái niệm chính: `class`, object, `self`, `__init__`, instance variable, class variable, method, `__str__`, `@classmethod`, đóng gói dữ liệu và quan hệ giữa các object.

## ✍️ Bài tập thực hành

Các file trong thư mục [exercises](exercises/) là bản bài tập có thể chạy trực tiếp. Mỗi file có ví dụ trong hàm `main()`.

| File | Nội dung |
|---|---|
| [ex01_classes.py](exercises/ex01_classes.py) | Class `HocSinh`, kiểm tra dữ liệu, xếp loại, `__str__` và đếm số object |
| [ex02_methods.py](exercises/ex02_methods.py) | Tài khoản ngân hàng, lịch sử giao dịch, sản phẩm và giỏ hàng |
| [ex03_design.py](exercises/ex03_design.py) | Theo dõi tiến độ đọc sách, quản lý danh bạ và quản lý quán cà phê |

### Cách chạy bài tập

Mở terminal tại thư mục gốc repository và chạy:

```bash
python weeks/week-13-oop-basics/exercises/ex01_classes.py
python weeks/week-13-oop-basics/exercises/ex02_methods.py
python weeks/week-13-oop-basics/exercises/ex03_design.py
```

Nếu máy dùng lệnh `py` thay cho `python`, có thể thay `python` bằng `py`.

## ✅ Lời giải tham khảo

Thư mục [solutions](solutions/) có lời giải tương ứng:

- [ex01_classes_sol.py](solutions/ex01_classes_sol.py)
- [ex02_methods_sol.py](solutions/ex02_methods_sol.py)
- [ex03_design_sol.py](solutions/ex03_design_sol.py)

Nên tự làm trong `exercises/` trước, sau đó so sánh với `solutions/`. Lời giải bao gồm kiểm tra dữ liệu cơ bản và ví dụ chạy thử.

## 🚀 Mini-project: Hệ thống thư viện

Yêu cầu mini-project nằm tại [mini-project/README.md](mini-project/README.md). Mục tiêu là xây dựng các class `Book` và `Library` để thêm, xóa, tìm, mượn, trả sách và thống kê tình trạng sách.

## 🔎 Tự kiểm tra sau khi học

- [ ] Giải thích được `self` và `__init__`.
- [ ] Tạo được nhiều object có dữ liệu độc lập.
- [ ] Biết khi nào nên viết method thay vì đặt toàn bộ logic ở bên ngoài class.
- [ ] Dùng `__str__` để hiển thị object.
- [ ] Kiểm tra input không hợp lệ.
- [ ] Chạy cả ba file trong `exercises/` và đối chiếu với `solutions/`.
- [ ] Hoàn thành mini-project và cập nhật [PROGRESS.md](../../PROGRESS.md) khi đã tự chạy, hiểu và kiểm tra bài.

## 📖 Đọc thêm

- [Think Python — Chapter 14: Classes and Objects](https://allendowney.github.io/ThinkPython/chap14.html)

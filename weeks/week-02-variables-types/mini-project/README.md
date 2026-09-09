# 🎓 Mini-project — Thẻ sinh viên

Mini-project thuộc **Week 02 — Variables & Data Types**.

Chương trình cho phép người dùng nhập thông tin của một sinh viên, kiểm tra năm nhập học và hiển thị thông tin dưới dạng một thẻ sinh viên đơn giản.

---

## 🎯 Mục tiêu

Thông qua mini-project này, mình thực hành các kiến thức đã học trong Week 02:

* Khai báo và sử dụng biến.
* Nhận dữ liệu từ bàn phím bằng `input()`.
* Làm việc với kiểu dữ liệu `str` và `int`.
* Kiểm tra chuỗi có chứa toàn bộ chữ số bằng `isdigit()`.
* Chuyển đổi dữ liệu từ `str` sang `int`.
* Thực hiện phép tính với số nguyên.
* Hiển thị dữ liệu bằng f-string.
* Sử dụng câu lệnh `if...else` để kiểm tra dữ liệu.

---

## 📌 Yêu cầu bài toán

Chương trình cần nhận 4 thông tin từ người dùng:

1. Họ và tên sinh viên.
2. Mã sinh viên.
3. Ngành học.
4. Năm nhập học.

Ví dụ:

```text
Họ và tên: Bùi Trung Sơn
Mã sinh viên: 25110001
Ngành học: Công nghệ thông tin
Năm nhập học: 2025
```

---

## ⌨️ Nhập dữ liệu

Sử dụng `input()` để nhập đủ 4 giá trị:

```python
name = input("Nhập họ và tên: ")
student_id = input("Nhập mã sinh viên: ")
major = input("Nhập ngành học: ")
year = input("Nhập năm nhập học: ")
```

Dữ liệu nhận từ `input()` mặc định có kiểu `str`.

Ví dụ khi nhập:

```text
2025
```

thì biến `year` lúc này vẫn là chuỗi:

```python
"2025"
```

chứ chưa phải số nguyên `2025`.

---

## 🔍 Kiểm tra năm nhập học

Trước khi sử dụng `int()`, chương trình phải kiểm tra năm nhập học có chỉ gồm chữ số hay không.

Sử dụng:

```python
year.isdigit()
```

Ví dụ:

```python
"2025".isdigit()
```

Kết quả:

```text
True
```

Nhưng:

```python
"20a5".isdigit()
```

Kết quả:

```text
False
```

Vì vậy chương trình kiểm tra:

```python
if year.isdigit():
    year = int(year)
else:
    print("Năm nhập học không hợp lệ!")
```

Việc kiểm tra này giúp chương trình chỉ thực hiện `int()` khi dữ liệu nhập vào hợp lệ.

---

## 🔢 Chuyển đổi kiểu dữ liệu

Sau khi xác nhận năm nhập học chỉ gồm chữ số, chuyển `year` từ `str` sang `int`:

```python
year = int(year)
```

Ví dụ:

```text
"2025" → 2025
```

Sau khi chuyển đổi, chương trình có thể thực hiện phép tính với `year`.

---

## 🎓 Tính năm dự kiến tốt nghiệp

Giả sử chương trình học kéo dài 4 năm.

Năm dự kiến tốt nghiệp được tính bằng:

```python
graduation_year = year + 4
```

Ví dụ:

```text
Năm nhập học: 2025

2025 + 4 = 2029
```

Vậy năm dự kiến tốt nghiệp là `2029`.

---

## 🖨️ Hiển thị thẻ sinh viên

Chương trình sử dụng **f-string** để đưa giá trị của các biến vào nội dung cần in.

Ví dụ:

```python
print(f"Họ và tên: {name}")
print(f"Mã sinh viên: {student_id}")
print(f"Ngành học: {major}")
print(f"Năm nhập học: {year}")
print(f"Năm dự kiến tốt nghiệp: {graduation_year}")
```

---

## 💻 Code chương trình

File:

```text
starter.py
```

Nội dung:

```python
name = input("Nhập họ và tên: ")
student_id = input("Nhập mã sinh viên: ")
major = input("Nhập ngành học: ")
year = input("Nhập năm nhập học: ")

if year.isdigit():
    year = int(year)
    graduation_year = year + 4

    print("\n===== THẺ SINH VIÊN =====")
    print(f"Họ và tên: {name}")
    print(f"Mã sinh viên: {student_id}")
    print(f"Ngành học: {major}")
    print(f"Năm nhập học: {year}")
    print(f"Năm dự kiến tốt nghiệp: {graduation_year}")
else:
    print("Năm nhập học không hợp lệ!")
```

---

## 📂 Cấu trúc thư mục

Mini-project được đặt trong:

```text
python-journey/
└── weeks/
    └── week-02-variables-types/
        └── mini-project/
            ├── README.md
            └── starter.py
```

Trong đó:

* `starter.py`: chứa chương trình Python.
* `README.md`: mô tả mini-project và cách sử dụng.

---

## ▶️ Cách chạy chương trình

### Bước 1: Mở Terminal

Di chuyển đến thư mục gốc của repository `python-journey`.

Ví dụ:

```bash
cd python-journey
```

### Bước 2: Chạy chương trình

```bash
python weeks/week-02-variables-types/mini-project/starter.py
```

---

## 🧪 Ví dụ chạy chương trình

### Trường hợp 1 — Năm nhập học hợp lệ

Nhập:

```text
Nhập họ và tên: Bùi Trung Sơn
Nhập mã sinh viên: 25110001
Nhập ngành học: Công nghệ thông tin
Nhập năm nhập học: 2025
```

Kết quả:

```text
===== THẺ SINH VIÊN =====
Họ và tên: Bùi Trung Sơn
Mã sinh viên: 25110001
Ngành học: Công nghệ thông tin
Năm nhập học: 2025
Năm dự kiến tốt nghiệp: 2029
```

---

### Trường hợp 2 — Năm nhập học không hợp lệ

Nhập:

```text
Nhập họ và tên: Bùi Trung Sơn
Nhập mã sinh viên: 25110001
Nhập ngành học: Công nghệ thông tin
Nhập năm nhập học: 20a5
```

Vì `20a5` chứa chữ cái nên:

```python
year.isdigit()
```

trả về `False`.

Kết quả:

```text
Năm nhập học không hợp lệ!
```

---

## 🔄 Luồng hoạt động

Chương trình hoạt động theo thứ tự:

```text
Nhập họ tên
     ↓
Nhập mã sinh viên
     ↓
Nhập ngành học
     ↓
Nhập năm học
     ↓
Kiểm tra year.isdigit()
     ↓
   Có phải số?
    /       \
  Có        Không
   ↓          ↓
int(year)   Báo lỗi
   ↓
year + 4
   ↓
In thẻ sinh viên
```

---

## 🧠 Kiến thức sử dụng

| Kiến thức   | Mục đích                      |
| ----------- | ----------------------------- |
| `input()`   | Nhận dữ liệu từ người dùng    |
| Biến        | Lưu thông tin sinh viên       |
| `str`       | Lưu dữ liệu dạng chuỗi        |
| `isdigit()` | Kiểm tra chuỗi chỉ gồm chữ số |
| `int()`     | Chuyển chuỗi thành số nguyên  |
| `if...else` | Kiểm tra năm nhập học         |
| `+`         | Tính năm tốt nghiệp           |
| f-string    | Hiển thị giá trị của biến     |

---

## ✅ Checklist

* [x] Nhập họ và tên bằng `input()`.
* [x] Nhập mã sinh viên bằng `input()`.
* [x] Nhập ngành học bằng `input()`.
* [x] Nhập năm nhập học bằng `input()`.
* [x] Kiểm tra năm bằng `isdigit()`.
* [x] Kiểm tra trước khi sử dụng `int()`.
* [x] Tính năm tốt nghiệp bằng năm nhập học + 4.
* [x] Hiển thị kết quả bằng f-string.
* [x] Có xử lý trường hợp năm nhập học không hợp lệ.
* [x] Không sử dụng exception handling.

---

## 📚 Kết quả đạt được

Sau khi hoàn thành mini-project, mình có thể:

* Hiểu rõ dữ liệu từ `input()` mặc định là chuỗi.
* Biết cách kiểm tra dữ liệu trước khi chuyển kiểu.
* Chuyển đổi dữ liệu từ `str` sang `int`.
* Sử dụng biến để lưu trữ thông tin.
* Thực hiện phép tính đơn giản với số nguyên.
* Sử dụng f-string để trình bày output rõ ràng.
* Kết hợp các kiến thức cơ bản để tạo một chương trình Python hoàn chỉnh.


# Tuần 02 — Biến & Kiểu Dữ Liệu

> **Python Journey** — Khóa học Python cơ bản cho người mới bắt đầu  
> Thời lượng: 2h lý thuyết + 2h thực hành

---

## 🎯 Mục Tiêu Tuần Này

Sau buổi học, bạn có thể:
- Khai báo và sử dụng biến trong Python
- Phân biệt 4 kiểu dữ liệu cơ bản: `int`, `float`, `str`, `bool`
- Dùng hàm `input()` để nhận dữ liệu từ người dùng
- Chuyển đổi giữa các kiểu dữ liệu
- Đặt tên biến đúng quy tắc và theo phong cách Python

---

## 1. Biến — Hộp Lưu Trữ Dữ Liệu

### 1.1 Biến Là Gì?

Hãy tưởng tượng biến như những **chiếc hộp có nhãn** trong kho. Bạn đặt tên cho hộp, bỏ dữ liệu vào, và sau đó có thể lấy ra bất cứ lúc nào.

```python
# Tạo biến — đặt tên và gán giá trị
ten = "Nguyễn Văn A"
tuoi = 25
chieu_cao = 1.75
la_sinh_vien = True

# Dùng biến
print("Tên:", ten)
print("Tuổi:", tuoi)
print("Chiều cao:", chieu_cao, "m")
```

**Điều kỳ diệu**: Giá trị của biến có thể **thay đổi** sau khi tạo:

```python
diem = 7
print("Điểm ban đầu:", diem)  # 7

diem = 9                       # Gán lại giá trị mới
print("Điểm sau cập nhật:", diem)  # 9

diem = diem + 1                # Cộng thêm 1 vào diem hiện tại
print("Điểm cuối:", diem)      # 10
```

### 1.2 Quy Tắc Đặt Tên Biến

```python
# ✅ Tên biến HỢP LỆ
ten_hoc_sinh = "An"       # snake_case — chuẩn Python
tuoi = 20
_bia = "private"           # Bắt đầu bằng _ được phép
ketQua = 90                # camelCase (không khuyến khích trong Python)
x = 5                      # Ngắn, nhưng OK cho biến tạm

# ❌ Tên biến KHÔNG HỢP LỆ
2ten = "An"               # Không bắt đầu bằng số
ten-hoc-sinh = "An"       # Không dùng dấu gạch ngang
for = 5                    # Không dùng từ khóa của Python
```

**Từ khóa của Python** (không dùng làm tên biến):
```
if  else  elif  for  while  def  class  return
import  from  and  or  not  in  is  True  False  None
```

### 1.3 Phong Cách Đặt Tên — snake_case

Python khuyến khích dùng **snake_case**: chữ thường, ngăn cách bằng dấu gạch dưới.

```python
# ✅ Pythonic (chuẩn Python)
ten_nguoi_dung = "An"
so_san_pham = 100
gia_ban_le = 25000.5

# ❌ Không Pythonic (nhưng vẫn chạy)
TenNguoiDung = "An"        # PascalCase — dùng cho class
soSanPham = 100             # camelCase — dùng trong Java/JavaScript
```

---

## 2. Bốn Kiểu Dữ Liệu Cơ Bản

### 2.1 `int` — Số Nguyên

```python
tuoi = 25
nam_sinh = 1999
so_am = -10
so_lon = 1_000_000         # Dấu _ giúp dễ đọc (= 1000000)

print(type(tuoi))          # <class 'int'>
print(type(so_am))         # <class 'int'>
```

**Phép toán với int:**
```python
a = 17
b = 5

print(a + b)   # Cộng:          22
print(a - b)   # Trừ:           12
print(a * b)   # Nhân:          85
print(a // b)  # Chia lấy nguyên: 3
print(a % b)   # Chia lấy dư:   2
print(a ** b)  # Lũy thừa:      1419857
```

### 2.2 `float` — Số Thực (Có Phần Thập Phân)

```python
pi = 3.14159
chieu_cao = 1.75
nhiet_do = -5.5
khoa_hoc = 1.5e10          # Ký hiệu khoa học: 15000000000.0

print(type(pi))            # <class 'float'>

# Phép chia thông thường luôn trả về float
print(10 / 2)              # 5.0 (không phải 5!)
print(10 / 3)              # 3.3333333333333335
```

**Cẩn thận với float:**
```python
# Số thực trong máy tính không hoàn toàn chính xác
print(0.1 + 0.2)           # 0.30000000000000004 (!!!)
print(0.1 + 0.2 == 0.3)    # False (!!!)

# Giải pháp: dùng round() khi so sánh
print(round(0.1 + 0.2, 2) == 0.3)  # True
```

### 2.3 `str` — Chuỗi Văn Bản

```python
ten = "Nguyễn Văn A"
dia_chi = 'Hà Nội, Việt Nam'
mo_ta = """Đây là chuỗi
nhiều dòng
dùng ba dấu nháy"""

print(type(ten))           # <class 'str'>

# Một số thao tác cơ bản với chuỗi
print(len(ten))            # Độ dài: 12
print(ten.upper())         # NGUYỄN VĂN A
print(ten.lower())         # nguyễn văn a
print(ten[0])              # N (ký tự đầu tiên, index bắt đầu từ 0)
```

**Nối chuỗi:**
```python
ho = "Nguyễn"
ten = "An"

# Cách 1: Dùng dấu +
ho_ten = ho + " " + ten
print(ho_ten)              # Nguyễn An

# Cách 2: f-string (khuyến nghị — hiện đại, dễ đọc)
ho_ten = f"{ho} {ten}"
print(ho_ten)              # Nguyễn An

# f-string cho phép tính toán trực tiếp
tuoi = 25
print(f"Tôi {tuoi} tuổi, sang năm {tuoi + 1} tuổi.")
```

### 2.4 `bool` — Đúng / Sai

```python
da_dang_nhap = True
con_hang = False

print(type(da_dang_nhap))  # <class 'bool'>

# Phép so sánh trả về bool
print(5 > 3)               # True
print(5 < 3)               # False
print(5 == 5)              # True  (so sánh bằng dùng ==, không phải =)
print(5 != 3)              # True  (khác nhau)
print(5 >= 5)              # True  (lớn hơn hoặc bằng)
print(5 <= 4)              # False (nhỏ hơn hoặc bằng)
```

---

## 3. Chuyển Đổi Kiểu Dữ Liệu

```python
# int() — chuyển thành số nguyên
print(int("42"))           # 42     (chuỗi → int)
print(int(3.9))            # 3      (float → int, CẮT, không làm tròn!)
print(int(True))           # 1
print(int(False))          # 0

# float() — chuyển thành số thực
print(float("3.14"))       # 3.14
print(float(5))            # 5.0

# str() — chuyển thành chuỗi
print(str(42))             # "42"
print(str(3.14))           # "3.14"
print(str(True))           # "True"

# bool() — chuyển thành bool
print(bool(0))             # False  (số 0 là False)
print(bool(1))             # True   (mọi số khác 0 là True)
print(bool(""))            # False  (chuỗi rỗng là False)
print(bool("hello"))       # True   (chuỗi có nội dung là True)
print(bool(None))          # False
```

**Lỗi thường gặp:**
```python
# ❌ Sai — không thể cộng số và chuỗi trực tiếp
tuoi = 25
print("Tuổi tôi là: " + tuoi)   # TypeError!

# ✅ Đúng — chuyển đổi trước
print("Tuổi tôi là: " + str(tuoi))
# Hoặc dùng f-string (tốt hơn)
print(f"Tuổi tôi là: {tuoi}")
```

---

## 4. Nhận Dữ Liệu Từ Người Dùng — `input()`

```python
# input() dừng chương trình, chờ người dùng gõ và nhấn Enter
ten = input("Nhập tên của bạn: ")
print(f"Xin chào, {ten}!")

# ⚠️ QUAN TRỌNG: input() LUÔN trả về kiểu str
tuoi_str = input("Nhập tuổi: ")
print(type(tuoi_str))      # <class 'str'>

# Phải chuyển đổi nếu muốn tính toán
tuoi = int(input("Nhập tuổi: "))
nam_sinh = 2025 - tuoi
print(f"Bạn sinh năm {nam_sinh}")
```

**Ví dụ hoàn chỉnh — Máy tính đơn giản:**
```python
print("=== Máy tính cộng ===")
so_1 = float(input("Nhập số thứ nhất: "))
so_2 = float(input("Nhập số thứ hai: "))
ket_qua = so_1 + so_2
print(f"{so_1} + {so_2} = {ket_qua}")
```

---

## 5. Hàm `type()` và Kiểm Tra Kiểu

```python
# Kiểm tra kiểu dữ liệu
x = 42
print(type(x))             # <class 'int'>
print(type(x) == int)      # True
print(isinstance(x, int))  # True (cách kiểm tra ưa dùng)

# isinstance() hữu ích hơn type() vì hỗ trợ kế thừa
print(isinstance(True, int))   # True (bool là con của int!)
print(isinstance(True, bool))  # True
```

---

## 6. Bài Tập Thực Hành

### Bài 1 — Lý lịch cá nhân (Dễ)
Tạo các biến lưu thông tin cá nhân (họ tên, tuổi, chiều cao, thành phố, là sinh viên hay không) rồi in ra bằng f-string theo format đẹp.

### Bài 2 — Đổi tiền tệ (Dễ)
```python
# Tỷ giá 1 USD = 25,000 VND
# Nhận số USD từ người dùng, in ra số VND tương đương
```

### Bài 3 — Tính BMI (Trung bình)
```
Nhập cân nặng (kg): 70
Nhập chiều cao (m): 1.75
BMI của bạn: 22.86
Phân loại: Bình thường (BMI 18.5 - 24.9)
```
*(Chỉ tính BMI và in ra — phân loại sẽ học ở tuần 5)*

### Bài 4 — Khám phá kiểu dữ liệu (Thử thách)
Thử các phép toán sau và **đoán** kết quả trước khi chạy:
```python
print(type(1 + 1))
print(type(1 + 1.0))
print(type(1 / 1))
print(type(1 // 1))
print(True + True)
print(True * 5)
print("abc" * 3)
print(len("Việt Nam"))
```

---

## 🔑 Những Điều Quan Trọng Nhất Tuần Này

> 1. **Biến** là tên gắn với giá trị — giá trị có thể thay đổi, tên thì không (trừ khi bạn gán lại)
> 2. **`input()` luôn trả về `str`** — phải dùng `int()` hoặc `float()` nếu muốn tính toán
> 3. **f-string** (`f"Xin chào {ten}"`) là cách in đẹp và hiện đại nhất — dùng nó thay vì `+`

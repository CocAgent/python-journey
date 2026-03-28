# Tuần 04 — Chuỗi (Strings) — Từ Cơ Bản Đến Thực Dụng

> **Python Journey** — Khóa học Python cơ bản cho người mới bắt đầu  
> Thời lượng: 2h lý thuyết + 2h thực hành

---

## 🎯 Mục Tiêu Tuần Này

Sau buổi học, bạn có thể:
- Truy cập từng ký tự và cắt chuỗi bằng indexing/slicing
- Dùng thành thạo ≥10 phương thức chuỗi quan trọng
- Định dạng chuỗi đẹp với f-string
- Kiểm tra và thao tác chuỗi từ `input()`

---

## 1. Indexing — Truy Cập Từng Ký Tự

```python
ten = "Python"
#      P  y  t  h  o  n
# idx: 0  1  2  3  4  5    (index dương, từ trái)
# idx:-6 -5 -4 -3 -2 -1    (index âm, từ phải)

print(ten[0])      # P (ký tự đầu)
print(ten[5])      # n (ký tự cuối)
print(ten[-1])     # n (ký tự cuối, cách hay hơn)
print(ten[-2])     # o

# IndexError: index ngoài phạm vi
# print(ten[6])    # ❌ Lỗi! Chỉ có index 0-5
```

## 2. Slicing — Cắt Chuỗi Con

```python
# chuoi[bat_dau:ket_thuc:buoc]
# Kết quả: từ index bat_dau đến ket_thuc-1
s = "Hello, World!"

print(s[0:5])      # Hello   (index 0,1,2,3,4)
print(s[7:12])     # World
print(s[:5])       # Hello   (bỏ qua 0 = từ đầu)
print(s[7:])       # World!  (bỏ qua cuối = đến hết)
print(s[:])        # Hello, World! (toàn bộ)
print(s[::2])      # Hlo ol! (mỗi 2 ký tự)
print(s[::-1])     # !dlroW ,olleH (đảo ngược!)
```

## 3. Phương Thức Chuỗi Quan Trọng

```python
s = "  Xin Chào Python!  "

# Xử lý khoảng trắng
print(s.strip())           # "Xin Chào Python!" (xóa hai đầu)
print(s.lstrip())          # "Xin Chào Python!  " (trái)
print(s.rstrip())          # "  Xin Chào Python!" (phải)

# Thay đổi chữ hoa/thường
s2 = "hello world"
print(s2.upper())          # HELLO WORLD
print(s2.lower())          # hello world
print(s2.title())          # Hello World
print(s2.capitalize())     # Hello world

# Tìm kiếm
s3 = "banana"
print(s3.find("an"))       # 1  (vị trí đầu tiên tìm thấy)
print(s3.count("an"))      # 2  (số lần xuất hiện)
print(s3.startswith("ban"))# True
print(s3.endswith("na"))   # True
print("an" in s3)          # True  (toán tử in)

# Thay thế và tách
print(s3.replace("an", "xx"))     # bxxxxa -> bxxxxa
email = "user@example.com"
print(email.split("@"))           # ['user', 'example.com']
print(",".join(["a", "b", "c"]))  # a,b,c

# Kiểm tra nội dung
print("123".isdigit())    # True
print("abc".isalpha())    # True
print("abc123".isalnum()) # True
print("  ".isspace())     # True
```

## 4. F-String Nâng Cao

```python
ten = "An"
tuoi = 25
diem = 8.567

# Cơ bản
print(f"Tên: {ten}, Tuổi: {tuoi}")

# Căn chỉnh (width = 10)
print(f"{'Trái':<10}|")         # Căn trái
print(f"{'Phải':>10}|")         # Căn phải
print(f"{'Giữa':^10}|")         # Căn giữa

# Số thực: làm tròn
print(f"Điểm: {diem:.2f}")      # 8.57 (2 chữ số thập phân)
print(f"Pi: {3.14159:.4f}")     # 3.1416

# Số nguyên: thêm dấu phân cách nghìn
so_lon = 1234567
print(f"Dân số: {so_lon:,}")    # 1,234,567
```

## 5. Bài Tập Thực Hành

### Bài 1 — Phân tích tên (Dễ)
```python
# Nhận họ tên đầy đủ từ người dùng
# In ra: họ, tên, số ký tự, tên viết hoa, tên đảo ngược
ho_ten = input("Nhập họ tên: ")
# ...
```

### Bài 2 — Kiểm tra palindrome (Trung bình)
Viết code kiểm tra một từ có phải palindrome không
(palindrome đọc xuôi ngược giống nhau: "radar", "madam")

### Bài 3 — Đếm từ trong câu (Trung bình)
```
Nhập câu: Python là ngôn ngữ lập trình tuyệt vời
Số từ: 8
Từ dài nhất: lập (3 ký tự) -> từ này sai, bài toán thú vị hơn
Ký tự đầu mỗi từ: P l n n l t t v
```

---

## 🔑 Những Điều Quan Trọng Nhất Tuần Này

> 1. **Index âm** (`s[-1]`) là cách tiện lợi truy cập từ cuối chuỗi
> 2. **`s[::-1]`** đảo ngược chuỗi — trick hay và Pythonic
> 3. **`.strip()`** luôn dùng khi nhận input từ người dùng để xóa khoảng trắng thừa

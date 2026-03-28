# Tuần 03 — Câu Lệnh Điều Kiện — if / elif / else

> **Python Journey** — Khóa học Python cơ bản cho người mới bắt đầu  
> Thời lượng: 2h lý thuyết + 2h thực hành

---

## 🎯 Mục Tiêu Tuần Này

Sau buổi học, bạn có thể:
- Viết câu lệnh if/elif/else đúng cú pháp
- Dùng toán tử logic: and, or, not
- Viết biểu thức điều kiện một dòng (ternary)
- Tránh lỗi logic phổ biến với điều kiện

---

## 1. Cú Pháp if/elif/else

```python
diem = float(input("Nhập điểm (0-10): "))

if diem >= 9:
    xep_loai = "Xuất sắc"
elif diem >= 8:
    xep_loai = "Giỏi"
elif diem >= 6.5:
    xep_loai = "Khá"
elif diem >= 5:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

print(f"Điểm {diem} → {xep_loai}")
```

> ⚠️ **Quan trọng**: Thứ tự elif quan trọng! Python kiểm tra từ trên xuống, dừng lại ở điều kiện đầu tiên đúng.

## 2. Toán Tử So Sánh

```python
x = 10
print(x == 10)   # True  — bằng
print(x != 5)    # True  — khác
print(x > 5)     # True  — lớn hơn
print(x < 20)    # True  — nhỏ hơn
print(x >= 10)   # True  — lớn hơn hoặc bằng
print(x <= 10)   # True  — nhỏ hơn hoặc bằng
```

## 3. Toán Tử Logic

```python
tuoi = 20
co_bang = True
say = False

# and: CẢ HAI phải đúng
lai_xe_ok = tuoi >= 18 and co_bang and not say
print(lai_xe_ok)   # True

# or: ÍT NHẤT MỘT đúng
cuoi_tuan = True
ngay_le = False
nghi = cuoi_tuan or ngay_le
print(nghi)        # True

# not: đảo ngược
print(not True)    # False
print(not False)   # True

# Kết hợp: and trước or (nhưng dùng ngoặc cho rõ)
# True and False or True  = (True and False) or True = False or True = True
print((True and False) or True)  # True
```

## 4. Ternary — Điều Kiện Một Dòng

```python
# gia_tri_neu_dung if dieu_kien else gia_tri_neu_sai
tuoi = 20
trang_thai = "Người lớn" if tuoi >= 18 else "Trẻ em"
print(trang_thai)   # Người lớn

# Trong f-string
x = -5
print(f"{x} là {'âm' if x < 0 else 'không âm'}")

# Gán giá trị mặc định
ten = input("Tên: ").strip()
ten = ten if ten else "Khách"   # Dùng "Khách" nếu rỗng
```

## 5. Giá Trị Truthy và Falsy

```python
# Trong Python, nhiều thứ có thể dùng như bool
# Falsy (được coi là False):
print(bool(0))       # False
print(bool(0.0))     # False
print(bool(""))      # False (chuỗi rỗng)
print(bool([]))      # False (list rỗng)
print(bool(None))    # False

# Truthy (được coi là True): mọi thứ còn lại
print(bool(1))       # True
print(bool("a"))     # True
print(bool([1]))     # True

# Ứng dụng thực tế
ten = input("Tên: ")
if ten:              # Thay vì if ten != ""
    print(f"Xin chào {ten}")
else:
    print("Bạn chưa nhập tên")
```

## 6. Bài Tập

### Bài 1 — Xếp loại học sinh (Dễ)
Nhận điểm từ người dùng (0-10), xếp loại theo thang Việt Nam với kiểm tra điểm hợp lệ.

### Bài 2 — Máy tính 4 phép (Trung bình)
Nhận 2 số và phép toán (+, -, *, /), trả về kết quả với xử lý chia cho 0.

### Bài 3 — Năm nhuận (Trung bình)
Năm nhuận nếu: chia hết cho 4 VÀ không chia hết cho 100, HOẶC chia hết cho 400.

### Bài 4 — Game đoán số (Thử thách)
Máy sinh số ngẫu nhiên 1-100, người đoán, máy báo cao/thấp đến khi đúng.

---

## 🔑 Những Điều Quan Trọng Nhất Tuần Này

> 1. **Thứ tự elif** quan trọng — kiểm tra từ trên xuống, dừng ở điều kiện đầu tiên đúng
> 2. **and trước or** — dùng ngoặc khi kết hợp để code rõ ràng hơn
> 3. **Falsy values**: 0, '', [], None, False — có thể dùng trực tiếp trong if

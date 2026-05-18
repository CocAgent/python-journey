# Tuần 07 — Hàm (Functions) — Tái Sử Dụng Code

> **Python Journey** — Khóa học Python cơ bản cho người mới bắt đầu  
> Thời lượng: 2h lý thuyết + 2h thực hành

---

## 🎯 Mục Tiêu Tuần Này

Sau buổi học, bạn có thể:
- Định nghĩa và gọi hàm với def
- Hiểu tham số, đối số và return value
- Dùng tham số mặc định và keyword arguments
- Hiểu phạm vi biến (scope)
- Viết docstring chuyên nghiệp

---

## 1. Định Nghĩa và Gọi Hàm

```python
# Hàm cơ bản
def chao(ten):
    print(f"Xin chào, {ten}!")

chao("An")      # Xin chào, An!
chao("Bình")    # Xin chào, Bình!

# Hàm có return
def tinh_dien_tich(dai, rong):
    return dai * rong

dt = tinh_dien_tich(5, 3)
print(f"Diện tích: {dt} m²")   # 15 m²

# Hàm không có return trả về None
def in_khong_tra_ve():
    print("Hello")

ket_qua = in_khong_tra_ve()
print(ket_qua)   # None
```

## 2. Các Loại Tham Số

```python
# Tham số mặc định (phải đặt SAU tham số bắt buộc)
def gioi_thieu(ten, tuoi=18, thanh_pho="Hà Nội"):
    print(f"Tôi là {ten}, {tuoi} tuổi, ở {thanh_pho}")

gioi_thieu("An")                      # Dùng mặc định
gioi_thieu("Bình", 25)               # Ghi đè tuổi
gioi_thieu("Châu", thanh_pho="HCM")  # Keyword argument

# *args — số lượng tham số không xác định
def tinh_tong(*numbers):
    return sum(numbers)

print(tinh_tong(1, 2, 3))         # 6
print(tinh_tong(1, 2, 3, 4, 5))   # 15

# **kwargs — keyword arguments không xác định
def in_thong_tin(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

in_thong_tin(ten="An", tuoi=25, thanh_pho="HCM")
```

## 3. Trả Về Nhiều Giá Trị

```python
def thong_ke(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

nho, lon, tb = thong_ke([7, 9, 5, 8])
print(f"Min: {nho}, Max: {lon}, TB: {tb:.1f}")
# Min: 5, Max: 9, TB: 7.2
```

## 4. Phạm Vi Biến (Scope)

```python
x = 10       # Biến global

def ham():
    y = 20   # Biến local — chỉ sống trong hàm
    print(x) # Đọc global được
    print(y)

ham()
print(x)     # 10
# print(y)   # NameError — y không tồn tại ở đây

# Thay đổi global (hạn chế dùng — gây khó debug)
def tang_x():
    global x
    x += 1

tang_x()
print(x)  # 11
```

## 5. Docstring — Tài Liệu Hàm

```python
def tinh_bmi(can_nang: float, chieu_cao: float) -> float:
    """
    Tính chỉ số BMI (Body Mass Index).

    Args:
        can_nang: Cân nặng tính bằng kilogram (kg)
        chieu_cao: Chiều cao tính bằng mét (m)

    Returns:
        Chỉ số BMI làm tròn 2 chữ số thập phân

    Raises:
        ValueError: Nếu can_nang hoặc chieu_cao <= 0

    Example:
        >>> tinh_bmi(70, 1.75)
        22.86
    """
    if can_nang <= 0 or chieu_cao <= 0:
        raise ValueError("Cân nặng và chiều cao phải > 0")
    return round(can_nang / chieu_cao ** 2, 2)
```

## 6. Bài Tập

### Bài 1 — Bộ công cụ toán (Dễ)
Viết 5 hàm: tinh_chu_vi_hinh_tron, tinh_dien_tich_hinh_tron, doi_do_c_sang_f, doi_do_f_sang_c, tinh_luy_thua.

### Bài 2 — Xử lý chuỗi (Trung bình)
Hàm clean_text: xóa khoảng trắng thừa, viết hoa chữ đầu mỗi từ, đếm từ.

### Bài 3 — Hàm thống kê (Trung bình)
Hàm thong_ke(numbers) trả về dict với min, max, mean, median.

### Bài 4 — Hàm đệ quy (Thử thách)
Viết hàm đệ quy: giai_thua(n), fibonacci(n), luy_thua(base, exp).

---

## 🔑 Những Điều Quan Trọng Nhất Tuần Này

> 1. **Hàm tốt làm đúng một việc** — nếu dài hơn 20 dòng, cân nhắc tách nhỏ
> 2. **Luôn viết docstring** — code không có tài liệu là code khó bảo trì
> 3. **Tránh dùng global** — truyền qua tham số và return là cách Pythonic

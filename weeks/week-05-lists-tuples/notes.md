# Tuần 05 — List (Danh Sách) — Làm Việc Với Tập Hợp Dữ Liệu

> **Python Journey** — Khóa học Python cơ bản cho người mới bắt đầu  
> Thời lượng: 2h lý thuyết + 2h thực hành

---

## 🎯 Mục Tiêu Tuần Này

Sau buổi học, bạn có thể:
- Tạo và thao tác list trong Python
- Dùng indexing và slicing trên list
- Dùng các phương thức: append, insert, remove, sort
- Hiểu list lồng nhau và list comprehension

---

## 1. Tạo và Truy Cập List

```python
# List là tập hợp có THỨ TỰ, có thể THAY ĐỔI
diem = [8, 9, 7, 10, 6]
ten = ["An", "Bình", "Châu"]
hon_hop = [1, "hai", 3.0, True]
rong = []

# Truy cập (giống string)
print(diem[0])     # 8
print(ten[-1])     # Châu
print(diem[1:3])   # [9, 7]
print(len(diem))   # 5
```

## 2. Thay Đổi List

```python
fruits = ["apple", "banana", "cherry"]

# Thêm
fruits.append("date")           # Cuối list
fruits.insert(1, "avocado")     # Vị trí chỉ định

# Xóa
fruits.remove("banana")         # Theo giá trị
del fruits[0]                   # Theo index
last = fruits.pop()             # Xóa và trả về phần tử cuối

# Sắp xếp
nums = [3, 1, 4, 1, 5, 9]
nums.sort()                     # Tại chỗ, tăng dần
nums.sort(reverse=True)         # Giảm dần
new = sorted(nums)              # Trả về list mới

# Tìm kiếm
print(5 in nums)                # True/False
print(nums.index(5))            # Vị trí đầu tiên
print(nums.count(1))            # Số lần xuất hiện
```

## 3. List Comprehension

```python
# Bình thường
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

# List comprehension — Pythonic hơn
squares = [i ** 2 for i in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# Có điều kiện lọc
chan = [x for x in range(20) if x % 2 == 0]
print(chan)      # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Biến đổi chuỗi
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(upper)     # ['HELLO', 'WORLD', 'PYTHON']
```

## 4. List Lồng Nhau

```python
# Ma trận 3x3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])   # 6 (hàng 1, cột 2)

# Duyệt ma trận
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # Xuống dòng
```

## 5. Bài Tập

### Bài 1 — Quản lý danh sách mua hàng (Dễ)
```python
# Cho phép: thêm sản phẩm, xóa, xem, tìm kiếm
gio_hang = []
# Thực hiện: thêm 5 sản phẩm, xóa 1, sắp xếp, in ra
```

### Bài 2 — Thống kê điểm (Trung bình)
```python
diem = [7, 9, 5, 8, 10, 6, 9, 7, 8, 9]
# Tính: min, max, trung bình, số điểm >= 8
```

### Bài 3 — Matrix (Thử thách)
Dùng list lồng nhau tạo và in bảng cửu chương 5×5.

---

## 🔑 Những Điều Quan Trọng Nhất Tuần Này

> 1. **List là mutable** — có thể thay đổi sau khi tạo (khác string)
> 2. **append()** nhanh hơn **insert()** — dùng append khi có thể
> 3. **List comprehension** ngắn hơn và thường nhanh hơn vòng lặp for

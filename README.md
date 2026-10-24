# Tuần 05 — Lists · Tuples · Mutability · Unpacking

Tuần này bạn chọn list cho collection có thể thay đổi và tuple cho một nhóm giá
trị cố định, đồng thời quan sát khác biệt giữa alias và copy.

## Outcomes

### 1. Tạo, đọc, cập nhật, thêm và xóa phần tử list (CRUD)
```python
fruits = ["Táo", "Chuối", "Cam"]
print(fruits[0])        # Đọc phần tử đầu: "Táo"
print(fruits[-1])       # Đọc phần tử cuối: "Cam"
fruits[1] = "Xoài"      # Cập nhật: ["Táo", "Xoài", "Cam"]
fruits.append("Nho")    # Thêm cuối: ["Táo", "Xoài", "Cam", "Nho"]
fruits.insert(1, "Lê")  # Chèn tại index 1: ["Táo", "Lê", "Xoài", "Cam", "Nho"]
fruits.remove("Cam")    # Xóa theo giá trị
last = fruits.pop()     # Lấy ra và xóa phần tử cuối ("Nho")
```

### 2. Dùng indexing và slicing
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
print(numbers[:3])    # 3 phần tử đầu: [0, 1, 2]
print(numbers[-3:])   # 3 phần tử cuối: [5, 6, 7]
print(numbers[2:6])   # Cắt từ index 2 đến trước 6: [2, 3, 4, 5]
print(numbers[1:-1])  # Cắt ở giữa (bỏ đầu và cuối): [1, 2, 3, 4, 5, 6]
# Lưu ý: Slicing luôn tạo ra list mới, không làm thay đổi list gốc.
```

### 3. Tạo tuple, packing và unpacking
```python
# Tạo tuple và packing
point = (3, 7)
profile = "An", 20, "Python"  # Packing thành tuple 3 phần tử

# Unpacking
x, y = point                  # x = 3, y = 7
name, age, topic = profile    # Mở gói tuple thành các biến riêng biệt

# Hoán đổi hai biến nhanh bằng tuple unpacking
left, right = "A", "B"
left, right = right, left     # left = "B", right = "A"
```

### 4. Giải thích list mutable và tuple immutable
```python
# List là mutable (thay đổi được phần tử tại chỗ):
items = [1, 2, 3]
items[0] = 99        # Hợp lệ, items trở thành [99, 2, 3]

# Tuple là immutable (không thể thay đổi sau khi tạo):
fixed = (1, 2, 3)
# fixed[0] = 99      # Báo lỗi: TypeError: 'tuple' object does not support item assignment
```

### 5. Phân biệt hai tên cùng trỏ một list (alias) với shallow copy độc lập
```python
original = [1, 2, 3]
alias = original           # Alias: cùng trỏ chung một list trong bộ nhớ
copied = original.copy()   # Copy: tạo bản sao nông độc lập

alias.append(4)
print(original)  # [1, 2, 3, 4] -> bị thay đổi vì alias trỏ cùng đối tượng!
print(copied)    # [1, 2, 3]    -> không thay đổi, độc lập hoàn toàn
```

Comprehensions được học có hệ thống ở Week 06.

## Learning path

```text
README → notes → examples → exercises → hints
       → machine check → collection workflow → evidence
```

Đi theo [`notes.md`](notes.md), [`examples/`](examples/),
[`exercises/`](exercises/), [`hints.md`](hints.md),
[machine check](checks/README.md) và [mini-project](mini-project/README.md).

## Evidence

- output `Week 05 solution checks: PASS`;
- một ví dụ alias thay đổi cùng list;
- một ví dụ copy không thay đổi source;
- tuple unpacking và một collection workflow đã chạy.

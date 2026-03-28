# Tuần 08 — Dictionary và Set

> **Python Journey** — Khóa học Python cơ bản cho người mới bắt đầu  
> Thời lượng: 2h lý thuyết + 2h thực hành

---

## 🎯 Mục Tiêu Tuần Này

Sau buổi học, bạn có thể:
- Tạo và thao tác dictionary (dict)
- Duyệt dict với keys(), values(), items()
- Dùng set và các phép toán tập hợp
- Chọn đúng cấu trúc dữ liệu cho bài toán

---

## 1. Dictionary — Dữ Liệu Theo Cặp Key-Value

```python
# Dict lưu dữ liệu theo cặp key: value
hoc_sinh = {
    "ten": "Nguyễn An",
    "tuoi": 20,
    "diem": 8.5,
    "la_sinh_vien": True
}

# Truy cập
print(hoc_sinh["ten"])            # Nguyễn An
print(hoc_sinh.get("diem"))       # 8.5
print(hoc_sinh.get("sdt", "N/A")) # N/A (giá trị mặc định nếu key không tồn tại)

# Thêm / Cập nhật
hoc_sinh["sdt"] = "0901234567"   # Thêm key mới
hoc_sinh["tuoi"] = 21            # Cập nhật key có sẵn

# Xóa
del hoc_sinh["sdt"]              # Xóa theo key
tuoi = hoc_sinh.pop("tuoi")     # Xóa và lấy giá trị

# Kiểm tra key
print("ten" in hoc_sinh)         # True
print("sdt" in hoc_sinh)         # False
```

## 2. Duyệt Dictionary

```python
soluong = {"tao": 5, "cam": 3, "chuoi": 8}

# Duyệt keys (mặc định)
for key in soluong:
    print(key)

# Duyệt values
for value in soluong.values():
    print(value)

# Duyệt cả hai — Pythonic nhất
for fruit, qty in soluong.items():
    print(f"{fruit}: {qty} quả")

# Dict comprehension
gia = {"tao": 15000, "cam": 12000, "chuoi": 8000}
gia_usd = {fruit: round(price / 25000, 2) for fruit, price in gia.items()}
print(gia_usd)
```

## 3. Set — Tập Hợp Không Trùng Lặp

```python
# Set: không có thứ tự, không trùng lặp
mau_sac = {"đỏ", "xanh", "vàng", "đỏ"}  # "đỏ" tự động bị xóa trùng
print(mau_sac)  # {'đỏ', 'xanh', 'vàng'}

# Thêm / Xóa
mau_sac.add("tím")
mau_sac.discard("vàng")  # Không lỗi nếu không tồn tại

# Phép toán tập hợp
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)   # Hợp: {1, 2, 3, 4, 5, 6}
print(a & b)   # Giao: {3, 4}
print(a - b)   # Hiệu: {1, 2}
print(a ^ b)   # Đối xứng: {1, 2, 5, 6}

# Ứng dụng: xóa trùng lặp trong list
co_trung = [1, 2, 2, 3, 3, 3, 4]
khong_trung = list(set(co_trung))
print(khong_trung)  # [1, 2, 3, 4]
```

## 4. Bài Tập

### Bài 1 — Từ điển Anh-Việt (Dễ)
```python
# Xây dựng từ điển, tra cứu từ, thêm từ mới
tu_dien = {"hello": "xin chào", "world": "thế giới"}
```

### Bài 2 — Đếm từ (Trung bình)
Đếm số lần xuất hiện của mỗi từ trong một câu văn.

### Bài 3 — Phân tích lớp học (Trung bình)
Dùng dict lưu điểm nhiều môn của học sinh, tính thống kê.

### Bài 4 — Tìm từ chung (Thử thách)
Tìm tất cả từ xuất hiện trong cả hai đoạn văn bản dùng set.

---

## 🔑 Những Điều Quan Trọng Nhất Tuần Này

> 1. **dict.get(key, default)** tốt hơn dict[key] khi key có thể không tồn tại
> 2. **.items()** là cách Pythonic nhất để duyệt dict
> 3. **set** giải quyết bài toán xóa trùng lặp trong một dòng code

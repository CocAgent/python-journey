# Tuần 10 — Đọc và Ghi File

> **Python Journey** — Khóa học Python cơ bản cho người mới bắt đầu  
> Thời lượng: 2h lý thuyết + 2h thực hành

---

## 🎯 Mục Tiêu Tuần Này

Sau buổi học, bạn có thể:
- Đọc và ghi file text với open()
- Dùng context manager (with)
- Xử lý CSV cơ bản
- Xử lý lỗi khi file không tồn tại

---

## 1. Ghi File

```python
# Ghi file — 'w' ghi đè, 'a' thêm vào cuối
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Xin chào!\n")
    f.write("Đây là dòng thứ hai.\n")

# Ghi nhiều dòng cùng lúc
lines = ["Dòng 1\n", "Dòng 2\n", "Dòng 3\n"]
with open("lines.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

# Thêm vào file có sẵn (append)
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("Dòng được thêm vào cuối.\n")
```

> ⚠️ **Luôn dùng `with`** (context manager) — tự động đóng file, tránh rò rỉ tài nguyên.

## 2. Đọc File

```python
# Đọc toàn bộ
with open("hello.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()
print(noi_dung)

# Đọc theo dòng
with open("hello.txt", "r", encoding="utf-8") as f:
    for dong in f:
        print(dong.strip())  # .strip() xóa \n cuối dòng

# Đọc tất cả dòng vào list
with open("hello.txt", "r", encoding="utf-8") as f:
    cac_dong = f.readlines()

# Đọc an toàn — xử lý file không tồn tại
try:
    with open("khong_ton_tai.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("❌ File không tồn tại!")
```

## 3. Làm Việc Với CSV

```python
import csv

# Ghi CSV
hoc_sinh = [
    ["Tên", "Toán", "Văn", "Anh"],
    ["Nguyễn An", 9, 8.5, 9.5],
    ["Trần Bình", 7, 8, 6.5],
]

with open("diem.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(hoc_sinh)

# Đọc CSV
with open("diem.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Tên']}: Toán={row['Toán']}")
```

## 4. Bài Tập

### Bài 1 — Nhật ký cá nhân (Dễ)
Cho phép thêm ghi chú vào file nhật ký, xem nhật ký, xóa tất cả.

### Bài 2 — Lưu danh sách (Trung bình)
Mở rộng dự án tuần 08: lưu danh sách học sinh vào file, đọc lại khi khởi động.

### Bài 3 — Phân tích CSV (Thử thách)
Đọc file CSV điểm học sinh, tính thống kê và ghi báo cáo ra file mới.

---

## 🔑 Những Điều Quan Trọng Nhất Tuần Này

> 1. **Luôn dùng `with open()`** — tự động đóng file, không bao giờ quên
> 2. **`encoding='utf-8'`** luôn chỉ định — tránh lỗi khi đọc file tiếng Việt
> 3. **try/except FileNotFoundError** khi đọc file — file có thể bị xóa, đổi tên

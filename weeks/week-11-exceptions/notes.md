# Tuần 11 — Xử Lý Lỗi — try / except

> **Python Journey** — Khóa học Python cơ bản cho người mới bắt đầu  
> Thời lượng: 2h lý thuyết + 2h thực hành

---

## 🎯 Mục Tiêu Tuần Này

Sau buổi học, bạn có thể:
- Hiểu exception là gì và tại sao cần xử lý
- Dùng try/except/else/finally đúng cách
- Bắt nhiều loại exception khác nhau
- Raise exception tự định nghĩa

---

## 1. Tại Sao Cần Xử Lý Lỗi?

```python
# Không xử lý lỗi — chương trình crash
so = int(input("Nhập số: "))   # Người dùng nhập "abc" → ValueError → crash!
print(10 / so)                 # Người dùng nhập 0 → ZeroDivisionError → crash!

# Có xử lý lỗi — chương trình tiếp tục
try:
    so = int(input("Nhập số: "))
    ket_qua = 10 / so
    print(f"10 / {so} = {ket_qua}")
except ValueError:
    print("❌ Vui lòng nhập số nguyên!")
except ZeroDivisionError:
    print("❌ Không thể chia cho 0!")
```

## 2. Cấu Trúc try/except/else/finally

```python
try:
    # Code có thể lỗi
    f = open("data.txt")
    noi_dung = f.read()
    so = int(noi_dung.strip())
    ket_qua = 100 / so

except FileNotFoundError:
    print("❌ File không tồn tại!")
    so = None

except ValueError:
    print("❌ Nội dung file không phải số!")
    so = None

except ZeroDivisionError:
    print("❌ Số trong file là 0!")
    so = None

except Exception as e:
    # Bắt mọi exception khác
    print(f"❌ Lỗi không xác định: {e}")
    so = None

else:
    # Chỉ chạy khi KHÔNG có lỗi
    print(f"✅ Kết quả: {ket_qua}")

finally:
    # LUÔN chạy, dù có lỗi hay không
    print("Đã hoàn tất xử lý")
    if 'f' in locals():
        f.close()
```

## 3. Các Exception Phổ Biến

| Exception | Khi nào xảy ra |
|-----------|---------------|
| `ValueError` | Giá trị sai kiểu: `int("abc")` |
| `TypeError` | Phép toán sai kiểu: `"a" + 1` |
| `IndexError` | Index ngoài phạm vi: `lst[100]` |
| `KeyError` | Key không tồn tại: `dict["x"]` |
| `FileNotFoundError` | File không tồn tại |
| `ZeroDivisionError` | Chia cho 0 |
| `AttributeError` | Gọi method không tồn tại |
| `NameError` | Dùng biến chưa khai báo |

## 4. Raise — Tự Tạo Exception

```python
def tinh_bmi(can_nang, chieu_cao):
    if can_nang <= 0:
        raise ValueError(f"Cân nặng phải > 0, nhận được {can_nang}")
    if chieu_cao <= 0:
        raise ValueError(f"Chiều cao phải > 0, nhận được {chieu_cao}")
    return can_nang / chieu_cao ** 2

try:
    bmi = tinh_bmi(70, -1.75)
except ValueError as e:
    print(f"❌ Lỗi: {e}")   # ❌ Lỗi: Chiều cao phải > 0, nhận được -1.75

# Custom Exception
class DiemKhongHopLeError(Exception):
    pass

def kiem_tra_diem(diem):
    if not 0 <= diem <= 10:
        raise DiemKhongHopLeError(f"Điểm {diem} không hợp lệ (phải 0-10)")
```

## 5. Bài Tập

### Bài 1 — Máy tính an toàn (Dễ)
Viết hàm tinh_toan(a, op, b) xử lý đầy đủ lỗi: chia 0, sai operator, a/b không phải số.

### Bài 2 — Đọc file an toàn (Trung bình)
Hàm doc_file_diem(filepath) đọc CSV điểm, xử lý tất cả lỗi có thể xảy ra.

### Bài 3 — Retry decorator (Thử thách)
Viết decorator tự động thử lại hàm tối đa N lần khi có exception.

---

## 🔑 Những Điều Quan Trọng Nhất Tuần Này

> 1. **else** trong try/except chạy khi KHÔNG có lỗi — hiếm biết nhưng hữu ích
> 2. **finally** luôn chạy — dùng để dọn dẹp tài nguyên (đóng file, ngắt kết nối)
> 3. **Raise exception** sớm với thông điệp rõ ràng — tốt hơn để lỗi xảy ra âm thầm

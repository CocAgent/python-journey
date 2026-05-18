# Tuần 09 — Dự Án Giữa Kỳ: Hệ Thống Quản Lý Học Sinh

> **Python Journey** — Khóa học Python cơ bản cho người mới bắt đầu  
> Thời lượng: 4h thực hành (không có bài giảng mới)

---

## 🎯 Mục Tiêu Tuần Này

Tuần này không có nội dung lý thuyết mới. Mục tiêu:
- **Tổng hợp** tất cả kiến thức tuần 1–8
- Hoàn thành dự án **Hệ Thống Quản Lý Học Sinh**
- Viết code **sạch, có comment, có xử lý lỗi**
- Thực hành quy trình phát triển: plan → code → test → refine

---

## 1. Ôn Tập Nhanh Tuần 1–7

```
Tuần 1: print(), comment, phép tính cơ bản
Tuần 2: Biến, kiểu dữ liệu, input(), type conversion
Tuần 3: if/elif/else, toán tử logic, ternary
Tuần 4: Chuỗi, indexing, slicing, string methods
Tuần 5: List, append/remove/sort, list comprehension
Tuần 6: for/while, break/continue, enumerate/zip
Tuần 7: Hàm, tham số, return, scope, docstring
Tuần 8: Dictionary, set, phép toán tập hợp
```

---

## 2. Dự Án Giữa Kỳ — Hệ Thống Quản Lý Học Sinh

### 2.1 Yêu Cầu Chức Năng

Xây dựng chương trình quản lý danh sách học sinh với các tính năng:

**Bắt buộc (7 điểm):**
- [x] Thêm học sinh (tên, tuổi, điểm toán, điểm văn, điểm anh)
- [x] Xem danh sách học sinh có định dạng đẹp
- [x] Tìm học sinh theo tên
- [x] Xóa học sinh theo tên
- [x] Tính điểm trung bình mỗi học sinh
- [x] Xếp loại học sinh (Xuất sắc/Giỏi/Khá/TB/Yếu)
- [x] Thống kê lớp (số HS, điểm TB cao nhất/thấp nhất)

**Nâng cao (+3 điểm):**
- [ ] Sắp xếp danh sách theo điểm hoặc tên
- [ ] Xuất báo cáo dạng bảng đẹp
- [ ] Xác thực đầu vào (điểm 0-10, tên không rỗng)
- [ ] Lưu và đọc dữ liệu từ file (nếu đã học tuần 10)

### 2.2 Gợi Ý Cấu Trúc Code

```python
# student_manager.py
# Hệ thống quản lý học sinh
# Tác giả: [Tên bạn]
# Tuần 09 — Dự án giữa kỳ

# ─── DỮ LIỆU ─────────────────────────────────
# Mỗi học sinh là một dict
# Danh sách học sinh là list of dicts

students = []  # Khởi đầu rỗng

# ─── CÁC HÀM CỐT LÕI ────────────────────────

def tinh_diem_tb(hoc_sinh: dict) -> float:
    """Tính điểm trung bình của một học sinh."""
    diem = [hoc_sinh["toan"], hoc_sinh["van"], hoc_sinh["anh"]]
    return round(sum(diem) / len(diem), 2)


def xep_loai(dtb: float) -> str:
    """Xếp loại dựa trên điểm trung bình."""
    if dtb >= 9:
        return "Xuất sắc"
    elif dtb >= 8:
        return "Giỏi"
    elif dtb >= 6.5:
        return "Khá"
    elif dtb >= 5:
        return "Trung bình"
    else:
        return "Yếu"


def them_hoc_sinh():
    """Thêm học sinh mới vào danh sách."""
    print("\n=== THÊM HỌC SINH ===")
    
    ten = input("Tên học sinh: ").strip()
    if not ten:
        print("❌ Tên không được rỗng!")
        return
    
    # Kiểm tra trùng tên
    if any(hs["ten"].lower() == ten.lower() for hs in students):
        print(f"❌ Học sinh '{ten}' đã tồn tại!")
        return
    
    try:
        tuoi = int(input("Tuổi: "))
        toan = float(input("Điểm Toán (0-10): "))
        van  = float(input("Điểm Văn (0-10): "))
        anh  = float(input("Điểm Anh (0-10): "))
    except ValueError:
        print("❌ Điểm phải là số!")
        return
    
    # Kiểm tra giới hạn điểm
    for diem, mon in [(toan, "Toán"), (van, "Văn"), (anh, "Anh")]:
        if not 0 <= diem <= 10:
            print(f"❌ Điểm {mon} phải từ 0 đến 10!")
            return
    
    hoc_sinh = {
        "ten": ten,
        "tuoi": tuoi,
        "toan": toan,
        "van": van,
        "anh": anh,
    }
    students.append(hoc_sinh)
    dtb = tinh_diem_tb(hoc_sinh)
    print(f"✅ Đã thêm {ten} — ĐTB: {dtb} — {xep_loai(dtb)}")


def xem_danh_sach():
    """Hiển thị danh sách học sinh dạng bảng."""
    if not students:
        print("📭 Danh sách trống!")
        return
    
    print(f"\n{'='*72}")
    print(f"{'STT':<5}{'Tên':<15}{'Tuổi':<6}{'Toán':<7}{'Văn':<7}{'Anh':<7}{'ĐTB':<7}{'Xếp loại'}")
    print(f"{'─'*72}")
    
    for i, hs in enumerate(students, 1):
        dtb = tinh_diem_tb(hs)
        loai = xep_loai(dtb)
        print(f"{i:<5}{hs['ten']:<15}{hs['tuoi']:<6}"
              f"{hs['toan']:<7.1f}{hs['van']:<7.1f}{hs['anh']:<7.1f}"
              f"{dtb:<7.2f}{loai}")
    
    print(f"{'='*72}")
    print(f"Tổng: {len(students)} học sinh")


def tim_hoc_sinh():
    """Tìm học sinh theo tên."""
    ten = input("Nhập tên cần tìm: ").strip().lower()
    ket_qua = [hs for hs in students if ten in hs["ten"].lower()]
    
    if not ket_qua:
        print(f"🔍 Không tìm thấy học sinh nào có tên '{ten}'")
        return
    
    print(f"\n🔍 Tìm thấy {len(ket_qua)} kết quả:")
    for hs in ket_qua:
        dtb = tinh_diem_tb(hs)
        print(f"  • {hs['ten']} — {hs['tuoi']} tuổi — ĐTB: {dtb} ({xep_loai(dtb)})")


def xoa_hoc_sinh():
    """Xóa học sinh theo tên."""
    ten = input("Tên học sinh cần xóa: ").strip()
    for i, hs in enumerate(students):
        if hs["ten"].lower() == ten.lower():
            students.pop(i)
            print(f"✅ Đã xóa học sinh '{hs['ten']}'")
            return
    print(f"❌ Không tìm thấy '{ten}'")


def thong_ke():
    """Thống kê toàn lớp."""
    if not students:
        print("📭 Danh sách trống!")
        return
    
    diem_tb_list = [tinh_diem_tb(hs) for hs in students]
    
    print(f"\n{'='*40}")
    print("       THỐNG KÊ TOÀN LỚP")
    print(f"{'─'*40}")
    print(f"  Tổng học sinh:   {len(students)}")
    print(f"  ĐTB cao nhất:    {max(diem_tb_list):.2f}")
    print(f"  ĐTB thấp nhất:   {min(diem_tb_list):.2f}")
    print(f"  ĐTB toàn lớp:    {sum(diem_tb_list)/len(diem_tb_list):.2f}")
    
    # Phân bố xếp loại
    print(f"\n  Phân bố xếp loại:")
    loai_names = ["Xuất sắc", "Giỏi", "Khá", "Trung bình", "Yếu"]
    for loai in loai_names:
        so_hs = sum(1 for dtb in diem_tb_list if xep_loai(dtb) == loai)
        if so_hs > 0:
            bar = "█" * so_hs
            print(f"    {loai:<12}: {bar} ({so_hs})")
    print(f"{'='*40}")


# ─── MENU CHÍNH ───────────────────────────────

def hien_thi_menu():
    print("\n╔══════════════════════════════╗")
    print("║  HỆ THỐNG QUẢN LÝ HỌC SINH  ║")
    print("╠══════════════════════════════╣")
    print("║  1. Thêm học sinh            ║")
    print("║  2. Xem danh sách            ║")
    print("║  3. Tìm học sinh             ║")
    print("║  4. Xóa học sinh             ║")
    print("║  5. Thống kê                 ║")
    print("║  0. Thoát                    ║")
    print("╚══════════════════════════════╝")


def main():
    # Thêm dữ liệu mẫu
    students.extend([
        {"ten": "Nguyễn An", "tuoi": 16, "toan": 9.0, "van": 8.5, "anh": 9.5},
        {"ten": "Trần Bình", "tuoi": 17, "toan": 7.0, "van": 8.0, "anh": 6.5},
        {"ten": "Lê Châu",   "tuoi": 16, "toan": 5.5, "van": 6.0, "anh": 5.0},
    ])
    
    actions = {
        "1": them_hoc_sinh,
        "2": xem_danh_sach,
        "3": tim_hoc_sinh,
        "4": xoa_hoc_sinh,
        "5": thong_ke,
    }
    
    while True:
        hien_thi_menu()
        lua_chon = input("Chọn chức năng: ").strip()
        
        if lua_chon == "0":
            print("👋 Tạm biệt!")
            break
        elif lua_chon in actions:
            actions[lua_chon]()
        else:
            print("⚠️ Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
```

---

## 3. Tiêu Chí Đánh Giá

| Tiêu chí | Điểm |
|---------|------|
| Chức năng thêm/xem/xóa/tìm hoạt động đúng | 4 |
| Tính điểm TB và xếp loại chính xác | 2 |
| Thống kê đầy đủ | 1 |
| Xử lý lỗi input (điểm không hợp lệ, tên rỗng) | 1.5 |
| Code sạch: tên biến rõ, có comment, có docstring | 1 |
| Chức năng nâng cao | +1.5 |
| **Tổng** | **10** |

---

## 4. Gợi Ý Mở Rộng

Nếu hoàn thành sớm, thử thêm:

```python
# Sắp xếp danh sách
def sap_xep():
    tieu_chi = input("Sắp xếp theo (1.tên / 2.điểm TB): ")
    if tieu_chi == "1":
        students.sort(key=lambda hs: hs["ten"])
    elif tieu_chi == "2":
        students.sort(key=tinh_diem_tb, reverse=True)
    print("✅ Đã sắp xếp!")
    xem_danh_sach()
```

---

## 🔑 Những Điều Quan Trọng Nhất Tuần Này

> 1. **Plan trước khi code** — viết ra danh sách chức năng, chia nhỏ từng hàm
> 2. **Test từng hàm riêng** — đừng viết toàn bộ rồi mới test
> 3. **Xử lý lỗi** là bắt buộc — người dùng LUÔN nhập sai, code phải chịu được

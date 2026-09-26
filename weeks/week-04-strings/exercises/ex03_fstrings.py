"""
Bài tập 03: f-string formatting 💅
====================================
Mục tiêu: Định dạng output đẹp với f-string
"""

# =============================================================
# TODO 1: f-string cơ bản — nhúng biến vào chuỗi
# f"..." → f-string: đặt chữ f trước nháy kép để nhúng biến vào
# {bien}      → in giá trị của biến
# {bien:.2f}  → in số thực, làm tròn đến 2 chữ số thập phân
#   Ví dụ: 8.567 → "8.57" (làm tròn, không phải cắt bỏ)
# =============================================================

ten  = "An"
tuoi = 20
diem = 8.567

print(f"Học sinh {ten}, {tuoi} tuổi, điểm TB: {diem:.2f}")
# Kết quả: "Học sinh An, 20 tuổi, điểm TB: 8.57"


# =============================================================
# TODO 2: Căn chỉnh cột trong f-string — bảng cửu chương
# {gia_tri:>N} → căn PHẢI trong N ký tự (thêm khoảng trắng vào bên trái)
#   Ví dụ: f"{3:>4}" → "   3"   (3 khoảng trắng + số 3)
#           f"{10:>4}" → "  10"  (2 khoảng trắng + số 10)
# Mục đích: làm cho các cột thẳng hàng nhau, dễ đọc
# =============================================================

print()     # In một dòng trống để dễ nhìn
for i in range(1, 11):              # range(1, 11) → tạo dãy số 1, 2, 3, ..., 10
    print(f"5 x {i:>2} = {5 * i:>4}")
    # {i:>2}     → số i, căn phải trong 2 ký tự (1 → " 1", 10 → "10")
    # {5 * i:>4} → kết quả, căn phải trong 4 ký tự (5 → "   5", 50 → "  50")


# =============================================================
# TODO 3: In hóa đơn đẹp với căn lề trái/phải
# {ten:<20}  → căn TRÁI trong 20 ký tự (thêm khoảng trắng vào bên phải)
# {gia:>11,} → căn PHẢI trong 11 ký tự, dấu , phân cách nghìn
#   Ví dụ: {35000:>11,} → "     35,000" (khoảng trắng + số + dấu phẩy)
# Kỹ thuật: căn lề tạo ra "cột" trực quan như bảng tính
# =============================================================

san_pham = [
    ("Cà phê", 35_000),     # Tuple: (tên sản phẩm, giá)
    ("Bánh mì", 25_000),    # Danh sách 3 tuple
    ("Nước suối", 10_000),
]
tong = sum(gia for _, gia in san_pham)
# sum(...) → cộng tất cả giá lại
# "for _, gia in san_pham" → lặp qua danh sách, lấy cột giá (bỏ qua tên = _)

print()
print("=" * 31)                             # In 31 dấu "=" liên tiếp
print(f"{'SẢN PHẨM':<20}{'GIÁ (VNĐ)':>11}")  # Tiêu đề cột
print("-" * 31)
for ten_sp, gia in san_pham:
    print(f"{ten_sp:<20}{gia:>11,}")        # Mỗi dòng sản phẩm
print("-" * 31)
print(f"{'TỔNG CỘNG':<20}{tong:>11,}")     # Dòng tổng
print("=" * 31)


# =============================================================
# TODO 4 (Thử thách): Thanh tiến trình (progress bar)
# Ý tưởng: Biến số phần trăm thành thanh đồ họa bằng ký tự
#   40% → [████████░░░░░░░░░░░░] 40%
#   "█" = ô đã đầy,  "░" = ô còn trống
# Công thức: số ô đầy = (phan_tram / 100) × tổng ô
# =============================================================

phan_tram = int(input("\nNhập phần trăm (0-100): "))
phan_tram = max(0, min(100, phan_tram))
# max(0, ...) → đảm bảo không nhỏ hơn 0
# min(100, .) → đảm bảo không lớn hơn 100
# Tóm lại: kẹp giá trị trong khoảng [0, 100]

tong_o = 20                                 # Thanh có 20 ô tổng
day    = int(phan_tram / 100 * tong_o)      # Số ô đã đầy
trong  = tong_o - day                       # Số ô còn trống

thanh = "█" * day + "░" * trong
# "█" * 8  → "████████"  (nhân ký tự với số lần lặp)
# "░" * 12 → "░░░░░░░░░░░░"
# Nối hai phần lại = thanh hoàn chỉnh

print(f"[{thanh}] {phan_tram}%")

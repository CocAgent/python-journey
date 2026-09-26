"""
Bài tập 03: f-string formatting 💅
====================================
Mục tiêu: Định dạng output đẹp với f-string
"""

# TODO 1: Cho ten = "An", tuoi = 20, diem = 8.567
# In ra: "Học sinh An, 20 tuổi, điểm TB: 8.57"
# Gợi ý: dùng :.2f để làm tròn 2 chữ số thập phân
ten = "An"
tuoi = 20
diem = 8.567

print(f"Học sinh {ten}, {tuoi} tuổi, điểm TB: {diem:.2f}")


# TODO 2: In bảng cửu chương 5 với cột thẳng hàng
# Dùng f-string width: f"{value:>4}"
# 5 x  1 =   5
# 5 x  2 =  10
# ...
# 5 x 10 =  50

print("\n=== Bảng cửu chương 5 ===")
for i in range(1, 11):
    print(f"5 x {i:>2} = {5 * i:>3}")


# TODO 3: In hóa đơn mua hàng đẹp
# Dùng f-string để căn lề trái/phải
# ===========================
# SẢN PHẨM          GIÁ (VNĐ)
# ---------------------------
# Cà phê              35,000
# Bánh mì             25,000
# Nước suối            10,000
# ---------------------------
# TỔNG CỘNG           70,000
# ===========================
# Gợi ý: dùng f"{name:<20}{price:>10,}"

san_pham = [
    ("Cà phê", 35_000),
    ("Bánh mì", 25_000),
    ("Nước suối", 10_000),
]
tong = sum(gia for _, gia in san_pham)

print()
print("=" * 31)
print(f"{'SẢN PHẨM':<20}{'GIÁ (VNĐ)':>11}")
print("-" * 31)
for ten_sp, gia in san_pham:
    print(f"{ten_sp:<20}{gia:>11,}")
print("-" * 31)
print(f"{'TỔNG CỘNG':<20}{tong:>11,}")
print("=" * 31)


# TODO 4 (Thử thách): Tạo progress bar bằng f-string
# Nhập phần trăm (0-100)
# In ra: [████████░░░░░░░░░░░░] 40%

print("\n=== TODO 4 (Progress Bar) ===")
phan_tram = int(input("Nhập phần trăm (0-100): "))

# Giới hạn trong khoảng hợp lệ
phan_tram = max(0, min(100, phan_tram))

do_dai = 20  # tổng độ dài thanh progress bar
so_day = round(phan_tram * do_dai / 100)
so_trong = do_dai - so_day

thanh = "█" * so_day + "░" * so_trong
print(f"[{thanh}] {phan_tram}%")

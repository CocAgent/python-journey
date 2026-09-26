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
print("--- 1. Định dạng thông tin học sinh ---")
print(f"Học sinh {ten}, {tuoi} tuổi, điểm TB: {diem:.2f}")


# TODO 2: In bảng cửu chương 5 với cột thẳng hàng
# Dùng f-string width: f"{value:>4}"
# 5 x  1 =   5
# 5 x  2 =  10
# ...
# 5 x 10 =  50
print("\n--- 2. Bảng cửu chương 5 ---")
so = 5
for i in range(1, 11):
    print(f"{so} x {i:>2} = {so * i:>3}")


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
print("\n--- 3. Hóa đơn mua hàng ---")
danh_sach_mon = [
    ("Cà phê", 35000),
    ("Bánh mì", 25000),
    ("Nước suối", 10000),
]
tong_tien = sum(gia for _, gia in danh_sach_mon)

print("=" * 30)
print(f"{'SẢN PHẨM':<20}{'GIÁ (VNĐ)':>10}")
print("-" * 30)
for ten_mon, gia in danh_sach_mon:
    print(f"{ten_mon:<20}{gia:>10,}")
print("-" * 30)
print(f"{'TỔNG CỘNG':<20}{tong_tien:>10,}")
print("=" * 30)


# TODO 4 (Thử thách): Tạo progress bar bằng f-string
# Nhập phần trăm (0-100)
# In ra: [████████░░░░░░░░░░░░] 40%
print("\n--- 4. Thanh tiến trình (Progress bar) ---")
phan_tram = int(input("Nhập phần trăm tiến độ (0-100): "))
phan_tram_chuan = max(0, min(100, phan_tram))
so_o_day = phan_tram_chuan // 5  # Mỗi ô tương ứng 5% (tổng 20 ô)
bar = "█" * so_o_day + "░" * (20 - so_o_day)

print(f"[{bar}] {phan_tram_chuan}%")

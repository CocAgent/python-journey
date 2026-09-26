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
print()
for i in range(1, 11):
    # :>2 căn phải 2 ký tự cho thừa số; :>3 căn phải 3 ký tự cho kết quả
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
    ("Cà phê",    35_000),
    ("Bánh mì",   25_000),
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
phan_tram = int(input("\nNhập phần trăm (0-100): "))
phan_tram = max(0, min(100, phan_tram))     # giới hạn về [0, 100]

# Thanh dài 20 ô: mỗi ô tương ứng 5%
day = phan_tram // 5
thanh = "█" * day + "░" * (20 - day)
print(f"[{thanh}] {phan_tram}%")

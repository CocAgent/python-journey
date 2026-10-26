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
print("=" * 27)
print(f"{'SẢN PHẨM':<17}{'GIÁ (VNĐ)':>10}")
print("-" * 27)
print(f"{'Cà phê':<17}{35000:>10,}")
print(f"{'Bánh mì':<17}{25000:>10,}")
print(f"{'Nước suối':<17}{10000:>10,}")
print("-" * 27)
print(f"{'TỔNG CỘNG':<17}{70000:>10,}")
print("=" * 27)

# TODO 4 (Thử thách): Tạo progress bar bằng f-string
# Nhập phần trăm (0-100)
# In ra: [████████░░░░░░░░░░░░] 40%
percent = int(input("Nhập phần trăm (0-100): "))
filled = int(percent / 100 * 20)
empty = 20 - filled
bar = f"[{'█' * filled}{'░' * empty}] {percent}%"
print(bar)

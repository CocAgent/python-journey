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
# → Học sinh An, 20 tuổi, điểm TB: 8.57


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
products = [
    ("Cà phê",     35000),
    ("Bánh mì",    25000),
    ("Nước suối",  10000),
]
print("===========================")
print(f"{'SẢN PHẨM':<20}{'GIÁ (VNĐ)':>9}")
print("---------------------------")
total = 0
for name, price in products:
    print(f"{name:<20}{price:>10,}")
    total += price
print("---------------------------")
print(f"{'TỔNG CỘNG':<20}{total:>10,}")
print("===========================")


# TODO 4 (Thử thách): Tạo progress bar bằng f-string
# Nhập phần trăm (0-100)
# In ra: [████████░░░░░░░░░░░░] 40%
percent = int(input("Nhập phần trăm (0-100): "))
filled = percent // 5
bar = "█" * filled + "░" * (20 - filled)
print(f"[{bar}] {percent}%")

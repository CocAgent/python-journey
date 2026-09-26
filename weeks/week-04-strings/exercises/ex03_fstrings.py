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
print("--- TODO 1: Định dạng số thực với f-string ---")
print(f"Học sinh {ten}, {tuoi} tuổi, điểm TB: {diem:.2f}")


# TODO 2: In bảng cửu chương 5 với cột thẳng hàng
# Dùng f-string width: f"{value:>4}"
# 5 x  1 =   5
# 5 x  2 =  10
# ...
# 5 x 10 =  50
print("\n--- TODO 2: Bảng cửu chương 5 thẳng hàng ---")
for i in range(1, 11):
    print(f"5 x {i:>2} ={5 * i:>4}")


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
print("\n--- TODO 3: In hóa đơn mua hàng căn chỉnh đẹp ---")
items = [
    ("Cà phê", 35000),
    ("Bánh mì", 25000),
    ("Nước suối", 10000),
]
total = sum(price for _, price in items)

print("=" * 30)
print(f"{'SẢN PHẨM':<20}{'GIÁ (VNĐ)':>10}")
print("-" * 30)
for name, price in items:
    print(f"{name:<20}{price:>10,}")
print("-" * 30)
print(f"{'TỔNG CỘNG':<20}{total:>10,}")
print("=" * 30)


# TODO 4 (Thử thách): Tạo progress bar bằng f-string
# Nhập phần trăm (0-100)
# In ra: [████████░░░░░░░░░░░░] 40%
print("\n--- TODO 4: Thanh tiến trình (Progress Bar) ---")
percent_input = input("Nhập phần trăm (0-100): ").strip()
percent = int(percent_input) if percent_input.isdigit() else 40
percent = max(0, min(100, percent))  # Đảm bảo giá trị nằm trong khoảng 0-100

filled_slots = percent // 5  # 100% ứng với 20 ô (mỗi ô là 5%)
empty_slots = 20 - filled_slots
bar = "█" * filled_slots + "░" * empty_slots
print(f"[{bar}] {percent}%")

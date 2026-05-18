"""Lời giải Bài tập 03: f-string formatting"""

# TODO 1
ten, tuoi, diem = "An", 20, 8.567
print(f"Học sinh {ten}, {tuoi} tuổi, điểm TB: {diem:.2f}")

# TODO 2
for i in range(1, 11):
    print(f"5 x {i:>2} = {5 * i:>3}")

# TODO 3
items = [("Cà phê", 35000), ("Bánh mì", 25000), ("Nước suối", 10000)]
print("=" * 30)
print(f"{'SẢN PHẨM':<20}{'GIÁ (VNĐ)':>10}")
print("-" * 30)
total = 0
for name, price in items:
    print(f"{name:<20}{price:>10,}")
    total += price
print("-" * 30)
print(f"{'TỔNG CỘNG':<20}{total:>10,}")
print("=" * 30)

# TODO 4
pct = int(input("Phần trăm (0-100): "))
filled = int(pct / 5)
bar = "█" * filled + "░" * (20 - filled)
print(f"[{bar}] {pct}%")

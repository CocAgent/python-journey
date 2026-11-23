"""Trusted checker fixture; not a student submission."""

# TODO 1: Tổng, hiệu, tích, thương
so_a = float(input())
so_b = float(input())
print("Tổng:", so_a + so_b)
print("Hiệu:", so_a - so_b)
print("Tích:", so_a * so_b)
print("Thương:", so_a / so_b)

# TODO 2: Diện tích và chu vi
r = float(input())
pi = 3.14159
print(f"Diện tích: {pi * r ** 2:.2f}")
print(f"Chu vi: {2 * pi * r:.2f}")

# TODO 3: Giảm giá
gia_goc = float(input())
phan_tram_giam = float(input())
print(f"Giá sau giảm: {gia_goc * (1 - phan_tram_giam / 100):.2f}")

# TODO 4 (Thử thách): không yêu cầu làm

"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
so_1 = float(input("Nhập số thứ nhất: "))
so_2 = float(input("Nhập số thứ hai: "))

print("Tổng:", so_1 + so_2)
print("Hiệu:", so_1 - so_2)
print("Tích:", so_1 * so_2)
if so_2 != 0:
    print("Thương:", so_1 / so_2)
else:
    print("Thương: không xác định (chia cho 0)")

print("-" * 30)

# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159


pi = 3.14159
r = float(input("Nhập bán kính hình tròn: "))
dien_tich = pi * r ** 2
chu_vi = 2 * pi * r
print(f"Diện tích: {dien_tich:.2f}")
print(f"Chu vi: {chu_vi:.2f}")

print("-" * 30)


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000

gia_goc = float(input("Nhập giá gốc: "))
phan_tram_giam = float(input("Nhập % giảm giá: "))
gia_sau_giam = gia_goc * (1 - phan_tram_giam / 100)
print(f"Giá sau khi giảm: {gia_sau_giam:,.0f}")

print("-" * 30)


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
so_tien_vnd = float(input("Nhập số tiền VNĐ: "))
ty_gia = float(input("Nhập tỷ giá USD/VNĐ (VD: 25000): "))
if ty_gia != 0:
    so_tien_usd = so_tien_vnd / ty_gia
    print(f"Số tiền tương đương: {so_tien_usd:.2f} USD")
else:
    print("Tỷ giá không hợp lệ (không thể là 0)")

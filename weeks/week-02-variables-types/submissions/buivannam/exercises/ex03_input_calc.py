"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
so_a = float(input("Số thứ nhất: "))
so_b = float(input("Số thứ hai: "))
print("Tổng:", so_a + so_b)
print("Hiệu:", so_a - so_b)
print("Tích:", so_a * so_b)
print("Thương:", so_a / so_b)


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
pi = 3.14159
ban_kinh = float(input("Bán kính: "))
dien_tich = pi * ban_kinh ** 2
chu_vi = 2 * pi * ban_kinh
print("Diện tích:", dien_tich)
print("Chu vi:", chu_vi)


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("Giá gốc: "))
phan_tram_giam = float(input("% giảm giá: "))
gia_sau_giam = gia_goc * (1 - phan_tram_giam / 100)
print(f"Giá sau giảm: {gia_sau_giam:.2f}")


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
so_tien_vnd = float(input("Số tiền (VNĐ): "))
ty_gia = float(input("Tỷ giá (VNĐ cho 1 USD): "))
so_usd = so_tien_vnd / ty_gia
print(f"Số USD: {so_usd:.2f}")

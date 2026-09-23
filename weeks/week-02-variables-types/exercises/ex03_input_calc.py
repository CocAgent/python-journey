"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
a=int(input("Nhập số thứ nhất: "))
b=int(input("Nhập số thứ hai: "))
print("Tổng:", a + b)
print("Hiệu:", a - b)
print("Tích:", a * b)
print("Thương:", a / b)

# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
r = float(input("Nhập bán kính hình tròn: "))
pi = 3.14159
dien_tich = pi * r ** 2
chu_vi = 2 * pi * r
print("Diện tích:", dien_tich)
print("Chu vi:", chu_vi)


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("Nhập giá gốc: "))
giam_gia = float(input("Nhập phần trăm giảm giá: "))
gia_sau_giam = gia_goc - (gia_goc * giam_gia / 100)
print("Giá sau khi giảm:", gia_sau_giam)


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
so_tien_vnd = float(input("Nhập số tiền VNĐ: "))
ty_gia = float(input("Nhập tỷ giá USD/VNĐ: "))
so_tien_usd = so_tien_vnd / ty_gia
print("Số USD tương ứng:", round(so_tien_usd, 2))
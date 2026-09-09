"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

print("Tổng:", a + b)
print("Hiệu:", a - b)
print("Tích:", a * b)
print("Thương:", a / b)

# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
pi = 3.14159

r = float(input("Nhập bán kính: "))

dien_tich = pi * r ** 2
chu_vi = 2 * pi * r

print("Diện tích:", dien_tich)
print("Chu vi:", chu_vi)

# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("Nhập giá gốc: "))
phan_tram_giam = float(input("Nhập % giảm giá: "))

tien_giam = gia_goc * phan_tram_giam / 100
gia_sau_giam = gia_goc - tien_giam

print("Giá sau khi giảm:", gia_sau_giam)

# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
vnd = float(input("Nhập số tiền VNĐ: "))
ty_gia = float(input("Nhập tỷ giá USD/VNĐ: "))

usd = vnd / ty_gia

print(f"Số USD tương ứng: {usd:.2f} USD")   
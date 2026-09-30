"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
so1 = float(input("Nhập số thứ nhất: "))
so2 = float(input("Nhập số thứ hai: "))
print(so1 + so2)
print(so1 - so2)
print(so1 * so2)
print(so1 / so2)


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
pi = 3.14159
r = float(input("Nhập bán kính hình tròn: "))
print(pi * (r ** 2))
print(2 * pi * r)




# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("Nhập giá gốc: "))
giam_gia = float(input("Nhập % giảm giá: "))
gia_sau_giam = gia_goc * (1 - giam_gia / 100)
print(gia_sau_giam)



# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
tien_vnd = float(input("Nhập số tiền VNĐ: "))
ty_gia = float(input("Nhập tỷ giá USD/VNĐ: "))
tien_usd = tien_vnd / ty_gia
print(f"{tien_usd:.2f}")
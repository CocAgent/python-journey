"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
so_1 = float(input("So thu nhat: "))
so_2 = float(input("So thu hai: "))
print(f"Tong: {so_1 + so_2}")
print(f"Hieu: {so_1 - so_2}")
print(f"Tich: {so_1 * so_2}")
if so_2 != 0:
    print(f"Thuong: {so_1 / so_2:.2f}")
else:
    print("Thuong: Khong the chia cho 0")


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
pi = 3.14159
ban_kinh = float(input("Ban kinh: "))
dien_tich = pi * (ban_kinh ** 2)
chu_vi = 2 * pi * ban_kinh
print(f"Dien tich: {dien_tich:.2f}")
print(f"Chu vi: {chu_vi:.2f}")


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("Gia goc (VND): "))
phan_tram_giam = float(input("Phan tram giam (%): "))
gia_sau_giam = gia_goc * (1 - phan_tram_giam / 100)
print(f"Gia sau giam: {gia_sau_giam:.2f}")


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
so_tien_vnd = float(input("So tien (VND): "))
ty_gia = float(input("Ty gia USD/VND: "))
if ty_gia != 0:
    so_tien_usd = so_tien_vnd / ty_gia
    print(f"USD: {so_tien_usd:.2f}")
else:
    print("Ty gia phai khac 0")

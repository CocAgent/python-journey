"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
print("--- TODO 1: Bốn phép tính cơ bản ---")
so_1 = float(input("Nhập số thứ nhất: "))
so_2 = float(input("Nhập số thứ hai: "))

tong = so_1 + so_2
hieu = so_1 - so_2
tich = so_1 * so_2

print(f"Tổng: {so_1} + {so_2} = {tong}")
print(f"Hiệu: {so_1} - {so_2} = {hieu}")
print(f"Tích: {so_1} * {so_2} = {tich}")
if so_2 != 0:
    thuong = so_1 / so_2
    print(f"Thương: {so_1} / {so_2} = {thuong}")
else:
    print("Thương: Không thể chia cho 0!")


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
print("\n--- TODO 2: Tính chu vi và diện tích hình tròn ---")
pi = 3.14159
r = float(input("Nhập bán kính hình tròn (r): "))

dien_tich = pi * (r ** 2)
chu_vi = 2 * pi * r

print(f"Diện tích: {dien_tich:.2f}")
print(f"Chu vi   : {chu_vi:.2f}")


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
print("\n--- TODO 3: Tính giá sau giảm ---")
gia_goc = float(input("Nhập giá gốc (VNĐ): "))
phan_tram_giam = float(input("Nhập phần trăm giảm giá (%): "))

gia_sau_giam = gia_goc * (1 - phan_tram_giam / 100)
print(f"Giá sau khi giảm {phan_tram_giam}%: {gia_sau_giam:,.0f} VNĐ")


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
print("\n--- TODO 4: Máy đổi tiền VNĐ sang USD ---")
tien_vnd = float(input("Nhập số tiền VNĐ: "))
ty_gia = float(input("Nhập tỷ giá USD/VNĐ: "))

if ty_gia > 0:
    tien_usd = tien_vnd / ty_gia
    print(f"Số USD tương ứng: {tien_usd:.2f} USD")
else:
    print("Tỷ giá phải lớn hơn 0!")


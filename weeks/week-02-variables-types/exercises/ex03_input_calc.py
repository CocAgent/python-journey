"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
print("--- TODO 1: Tính tổng, hiệu, tích, thương ---")
so_1 = float(input("Nhập số thứ nhất: "))
so_2 = float(input("Nhập số thứ hai: "))

tong = so_1 + so_2
hieu = so_1 - so_2
tich = so_1 * so_2

print(f"Tổng:  {so_1} + {so_2} = {tong}")
print(f"Hiệu:  {so_1} - {so_2} = {hieu}")
print(f"Tích:  {so_1} * {so_2} = {tich}")
if so_2 != 0:
    thuong = so_1 / so_2
    print(f"Thương: {so_1} / {so_2} = {thuong}")
else:
    print("Thương: Không thể chia cho 0!")


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
print("\n--- TODO 2: Chu vi & Diện tích hình tròn ---")
pi = 3.14159
r = float(input("Nhập bán kính hình tròn (r): "))

dien_tich = pi * (r ** 2)
chu_vi = 2 * pi * r

print(f"Diện tích hình tròn (π × r²): {dien_tich:.2f}")
print(f"Chu vi hình tròn (2 × π × r): {chu_vi:.2f}")


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
print("\n--- TODO 3: Tính giá sau giảm ---")
gia_goc = float(input("Nhập giá gốc sản phẩm (VNĐ): "))
phan_tram_giam = float(input("Nhập % giảm giá (ví dụ 20): "))

so_tien_giam = gia_goc * (phan_tram_giam / 100)
gia_sau_giam = gia_goc - so_tien_giam
# Hoặc công thức rút gọn: gia_sau_giam = gia_goc * (1 - phan_tram_giam / 100)

print(f"Số tiền được giảm: {so_tien_giam:,.0f} VNĐ")
print(f"Giá sau khi giảm:  {gia_sau_giam:,.0f} VNĐ")


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
print("\n--- TODO 4: Đổi tiền VNĐ sang USD ---")
tien_vnd = float(input("Nhập số tiền VNĐ: "))
ty_gia = float(input("Nhập tỷ giá (VNĐ/USD, ví dụ 25000): "))

if ty_gia > 0:
    so_usd = tien_vnd / ty_gia
    print(f"{tien_vnd:,.0f} VNĐ tương đương: {so_usd:.2f} USD")
else:
    print("Lỗi: Tỷ giá phải lớn hơn 0!")

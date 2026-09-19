"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
print("--- TODO 1: Máy tính 4 phép toán cơ bản ---")
so_a = float(input("Nhập số thứ nhất: "))
so_b = float(input("Nhập số thứ hai: "))

tong = so_a + so_b
hieu = so_a - so_b
tich = so_a * so_b
print(f"Tổng: {so_a} + {so_b} = {tong}")
print(f"Hiệu: {so_a} - {so_b} = {hieu}")
print(f"Tích: {so_a} * {so_b} = {tich}")

if so_b != 0:
    thuong = so_a / so_b
    print(f"Thương: {so_a} / {so_b} = {thuong}")
else:
    print("Không thể chia cho 0!")


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
print("\n--- TODO 2: Chu vi và diện tích hình tròn ---")
pi = 3.14159
r = float(input("Nhập bán kính r: "))

dien_tich = pi * (r ** 2)
chu_vi = 2 * pi * r
print(f"Diện tích: {dien_tich:.2f}")
print(f"Chu vi: {chu_vi:.2f}")


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
print("\n--- TODO 3: Tính giá sau khuyến mãi ---")
gia_goc = float(input("Nhập giá gốc (VNĐ): "))
phan_tram_giam = float(input("Nhập % giảm giá (ví dụ 20): "))

gia_sau_giam = gia_goc * (1 - phan_tram_giam / 100)
print(f"Giá sau khi giảm {phan_tram_giam:.0f}%: {gia_sau_giam:,.0f} VNĐ")


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
print("\n--- TODO 4: Đổi tiền VNĐ sang USD ---")
tien_vnd = float(input("Nhập số tiền VNĐ: "))
ty_gia = float(input("Nhập tỷ giá USD/VNĐ (ví dụ 25000): "))

if ty_gia > 0:
    so_usd = tien_vnd / ty_gia
    print(f"{tien_vnd:,.0f} VNĐ = {so_usd:.2f} USD")
else:
    print("Tỷ giá phải lớn hơn 0!")

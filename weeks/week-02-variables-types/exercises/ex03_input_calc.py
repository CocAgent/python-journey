"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
so_a = float(input("Nhap so thu nhat: "))
so_b = float(input("Nhap so thu hai: "))

print(f"Tong:   {so_a} + {so_b} = {so_a + so_b}")
print(f"Hieu:   {so_a} - {so_b} = {so_a - so_b}")
print(f"Tich:   {so_a} x {so_b} = {so_a * so_b}")
# Kiểm tra chia cho 0 trước khi thực hiện
if so_b != 0:
    print(f"Thuong: {so_a} / {so_b} = {so_a / so_b:.2f}")
else:
    print("Thuong: Khong the chia cho 0!")


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
pi = 3.14159
ban_kinh = float(input("Nhap ban kinh hinh tron: "))

dien_tich = pi * ban_kinh ** 2
chu_vi = 2 * pi * ban_kinh

print(f"Dien tich = {dien_tich:.2f}")
print(f"Chu vi    = {chu_vi:.2f}")


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("Nhap gia goc (VND): "))
phan_tram_giam = float(input("Nhap % giam gia (vi du 20): "))

so_tien_giam = gia_goc * phan_tram_giam / 100
gia_sau_giam = gia_goc - so_tien_giam

print(f"Gia goc:      {gia_goc:,.0f} VND")
print(f"Giam:         {so_tien_giam:,.0f} VND ({phan_tram_giam}%)")
print(f"Gia sau giam: {gia_sau_giam:,.0f} VND")


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
so_tien_vnd = float(input("Nhap so tien VND: "))
ty_gia = float(input("Nhap ty gia (1 USD = ? VND), vi du 25000: "))

so_usd = so_tien_vnd / ty_gia
print(f"{so_tien_vnd:,.0f} VND = {so_usd:.2f} USD")

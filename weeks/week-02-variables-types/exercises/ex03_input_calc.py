"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
num1 = float(input("Nhap so thu nhat: "))
num2 = float(input("Nhap so thu hai: "))

tong = num1 + num2
hieu = num1 - num2
tich = num1 * num2
thuong = num1 / num2  # Lưu ý: num2 phải khác 0

print(f"Tong: {tong}")
print(f"Hieu: {hieu}")
print(f"Tich: {tich}")
print(f"Thuong: {thuong}")


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
r = float(input("\nNhap ban kinh hinh tron (r): "))
pi = 3.14159

dien_tich = pi * (r ** 2)
chu_vi = 2 * pi * r

print(f"Dien tich: {dien_tich:.2f}")
print(f"Chu vi: {chu_vi:.2f}")


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("\nNhap gia goc: "))
phan_tram_giam = float(input("Nhap % giam gia: "))

gia_sau_giam = gia_goc * (1 - phan_tram_giam / 100)

print(f"Gia sau khi giam: {gia_sau_giam:,.0f}")


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
tien_vnd = float(input("\nNhap so tien VND: "))
ty_gia = float(input("Nhap ty gia USD/VND: "))

so_usd = tien_vnd / ty_gia

print(f"So USD tuong ung: {so_usd:.2f}")
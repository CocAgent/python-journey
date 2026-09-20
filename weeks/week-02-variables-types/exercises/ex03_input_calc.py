"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
a = float(input('Nhập số thứ 1:'))
b = float(input('Nhập số thứ 2:'))
print(f'Tổng: {a + b}')
print(f'Hiệu: {a - b}')
print(f'Tích: {a * b}')
print(f'Thương: {a / b}')
# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
r = float(input('Nhập bán kính:'))
pi = 3.14159
s = pi * r ** 2
c = 2 * pi * r
print(f'Diện tích hình tròn: {s}')
print(f'Chu vi hình tròn: {c}')
# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
m = float(input('Nhập giá bán:'))
n = float(input('Nhập (%) giảm giá:'))
o =  m - (m * (n / 100))
print(f'Giá gốc {m}, giảm {n}% -> {o}')
# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
vnd = float(input('Nhập số tiền VNĐ:'))
ti_gia = float(input('Nhập tỉ giá USĐ/VNĐ:'))
usd = vnd / ti_gia
print(f'Số tiền USĐ tương ứng: {usd:.2f}')
"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
input_num1=float(input("nhap so thu nhat: "))
input_num2=float(input("nhap so thu hai: "))

print(f"Tong: {input_num1 + input_num2}")
print(f"Hieu: {input_num1 - input_num2}")
print(f"Tich: {input_num1 * input_num2}")
print(f"Thuong: {input_num1 / input_num2}")

# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
pi = 3.14159
radius = float(input("Nhập bán kính hình tròn: "))
area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"Diện tích: {area}")
print(f"Chu vi: {circumference}")

# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
original_price = float(input("Nhập giá gốc: "))
discount_percentage = float(input("Nhập phần trăm giảm giá: "))
discount_amount = original_price * discount_percentage / 100
final_price = original_price - discount_amount
print(f"Giá sau khi giảm: {final_price}")

# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
vnd_amount = float(input("Nhập số tiền VNĐ: "))
exchange_rate = float(input("Nhập tỷ giá USD/VNĐ: "))
usd_amount = vnd_amount / exchange_rate
print(f"Số USD tương ứng: {usd_amount:.2f}")
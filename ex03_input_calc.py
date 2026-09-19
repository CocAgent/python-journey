"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
print("--- TODO 1: 4 phép tính cơ bản ---")
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))

tong = num1 + num2
hieu = num1 - num2
tich = num1 * num2
thuong = num1 / num2 if num2 != 0 else "Không thể chia cho 0"

print(f"Tổng: {num1} + {num2} = {tong}")
print(f"Hiệu: {num1} - {num2} = {hieu}")
print(f"Tích: {num1} * {num2} = {tich}")
print(f"Thương: {num1} / {num2} = {thuong}")


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
print("\n--- TODO 2: Chu vi & Diện tích hình tròn ---")
pi = 3.14159
r = float(input("Nhập bán kính r: "))

dien_tich = pi * (r ** 2)
chu_vi = 2 * pi * r

print(f"Diện tích = {dien_tich:.2f}")
print(f"Chu vi = {chu_vi:.2f}")


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
print("\n--- TODO 3: Tính giá sau khi giảm giá ---")
gia_goc = float(input("Nhập giá gốc: "))
phan_tram_giam = float(input("Nhập % giảm giá: "))

gia_sau_giam = gia_goc * (1 - phan_tram_giam / 100)
print(f"Giá sau khi giảm {phan_tram_giam}%: {gia_sau_giam:,.0f} VNĐ")


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
print("\n--- TODO 4: Máy đổi tiền VNĐ sang USD ---")
tien_vnd = float(input("Nhập số tiền VNĐ: "))
ty_gia = float(input("Nhập tỷ giá USD/VNĐ: "))

if ty_gia != 0:
    tien_usd = tien_vnd / ty_gia
    print(f"{tien_vnd:,.0f} VNĐ = {tien_usd:.2f} USD")
else:
    print("Lỗi: Tỷ giá phải khác 0")


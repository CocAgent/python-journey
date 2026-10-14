"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
print(f"Tổng: {a + b}")
print(f"Hiệu: {a - b}")
print(f"Tích: {a * b}")
if b != 0:
    print(f"Thương: {a / b:.2f}")
else:
    print("Không thể chia cho 0!")

# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
r = float(input("Nhập bán kính: "))
pi = 3.14159
print(f"Diện tích: {pi * r**2:.2f}")
print(f"Chu vi: {2 * pi * r:.2f}")

# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("Nhập giá gốc: "))
giam_gia = float(input("Nhập % giảm giá: "))
gia_sau_giam = gia_goc - (gia_goc * giam_gia / 100)
print(f"Giá sau khi giảm: {gia_sau_giam:.0f} VNĐ")


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
vnđ = float(input("Nhập số tiền VNĐ: "))
tỷ_giá = float(input("Nhập tỷ giá USD/VNĐ: "))
usd = vnđ / tỷ_giá
print(f"Số USD tương ứng: {usd:.2f} USD")

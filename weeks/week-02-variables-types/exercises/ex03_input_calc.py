"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
a = float(input("Số thứ nhất: "))
b = float(input("Số thứ hai: "))
print(f"Tổng: {a + b}")
print(f"Hiệu: {a - b}")
print(f"Tích: {a * b}")
if b != 0:
    print(f"Thương: {a / b}")
else:
    print("Không thể chia cho 0")


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
pi = 3.14159
ban_kinh = float(input("Bán kính: "))
if ban_kinh >= 0:
    print(f"Diện tích: {pi * ban_kinh ** 2}")
    print(f"Chu vi: {2 * pi * ban_kinh}")
else:
    print("Bán kính không được âm")


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("Giá gốc: "))
giam_gia = float(input("Phần trăm giảm giá: "))
if gia_goc >= 0 and 0 <= giam_gia <= 100:
    gia_sau_giam = gia_goc * (1 - giam_gia / 100)
    print(f"Giá sau giảm: {gia_sau_giam}")
else:
    print("Giá phải không âm; phần trăm giảm từ 0 đến 100")


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
tien_vnd = float(input("Số tiền VNĐ: "))
ty_gia = float(input("Tỷ giá (VNĐ cho 1 USD): "))
if tien_vnd >= 0 and ty_gia > 0:
    print(f"USD: {tien_vnd / ty_gia:.2f}")
else:
    print("Tiền phải không âm và tỷ giá phải lớn hơn 0")

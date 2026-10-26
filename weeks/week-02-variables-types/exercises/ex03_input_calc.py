"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
so_1 = float(input("Nhập số thứ nhất: "))
so_2 = float(input("Nhập số thứ hai: "))

print(f"Tổng: {so_1 + so_2}")
print(f"Hiệu: {so_1 - so_2}")
print(f"Tích: {so_1 * so_2}")
if so_2 == 0:
    print("Không thể chia vì mẫu số bằng 0")
else:
    print(f"Thương: {so_1 / so_2}")


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
pi = 3.14159
ban_kinh = float(input("Nhập bán kính hình tròn: "))
diện_tích = pi * (ban_kinh ** 2)
chu_vi = 2 * pi * ban_kinh
print(f"Diện tích: {diện_tích:.2f}")
print(f"Chu vi: {chu_vi:.2f}")


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("Nhập giá gốc: "))
phan_tram_giam = float(input("Nhập % giảm giá: "))
so_tien_giam = gia_goc * (phan_tram_giam / 100)
gia_sau_khi_giam = gia_goc - so_tien_giam
print(f"Giá sau khi giảm: {gia_sau_khi_giam:,.0f}")


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
so_tien_vnd = float(input("Nhập số tiền VNĐ: "))
ty_gia = float(input("Nhập tỷ giá USD/VNĐ (ví dụ: 25000): "))
if ty_gia == 0:
    print("Tỷ giá không được bằng 0")
else:
    so_usd = so_tien_vnd / ty_gia
    print(f"Số USD tương ứng: {so_usd:.2f}")

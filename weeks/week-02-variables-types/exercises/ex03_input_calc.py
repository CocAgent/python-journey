"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
so_thu_nhat = float(input("Số thứ nhất: "))
so_thu_hai = float(input("Số thứ hai: "))
print(f"Tổng: {so_thu_nhat + so_thu_hai}")
print(f"Hiệu: {so_thu_nhat - so_thu_hai}")
print(f"Tích: {so_thu_nhat * so_thu_hai}")
if so_thu_hai != 0:
	print(f"Thương: {so_thu_nhat / so_thu_hai}")
else:
	print("Không thể chia cho 0")


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
ban_kinh = float(input("Bán kính: "))
pi = 3.14159
dien_tich = pi * ban_kinh**2
chu_vi = 2 * pi * ban_kinh
print(f"Diện tích: {dien_tich}")
print(f"Chu vi: {chu_vi}")


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("Giá gốc: "))
phan_tram_giam = float(input("Phần trăm giảm giá: "))
gia_sau_khi_giam = gia_goc * (1 - phan_tram_giam / 100)
print(f"Giá sau khi giảm: {gia_sau_khi_giam}")


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
so_tien_vnd = float(input("Số tiền VNĐ: "))
ty_gia = float(input("Tỷ giá USD/VNĐ: "))
if ty_gia != 0:
	so_tien_usd = so_tien_vnd / ty_gia
	print(f"Số USD: {so_tien_usd:.2f}")
else:
	print("Tỷ giá phải khác 0")

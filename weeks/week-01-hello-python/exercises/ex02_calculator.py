"""
Bài tập 02: Máy tính Python 🧮
================================
Mục tiêu: Sử dụng các phép tính cơ bản trong Python
"""

# ============================================================
# TODO 1: Tính và in ra kết quả của 2024 + 1000
# ============================================================

# dấu +
# dùng để cộng

ket_qua = 2024 + 1000

print("2024 + 1000 =", ket_qua)


# ============================================================
# TODO 2: Tính số tiền còn lại
# ============================================================

# tạo biến lưu dữ liệu

tien_hien_co = 150000

gia_ca_phe = 35000

so_ly = 3

# *
# phép nhân

tong_tien = gia_ca_phe * so_ly

# -
# phép trừ

tien_con_lai = tien_hien_co - tong_tien

print("Số tiền còn lại =", tien_con_lai, "VNĐ")


# ============================================================
# TODO 3: Tính diện tích hình tròn
# ============================================================

# bán kính

ban_kinh = 7

# **
# phép lũy thừa

# ban_kinh ** 2
# nghĩa là 7 mũ 2

dien_tich = 3.14159 * ban_kinh ** 2

print("Diện tích hình tròn =", dien_tich)


# ============================================================
# TODO 4: Chia kẹo
# ============================================================

keo = 100

nguoi = 7

# //
# chia lấy nguyên

moi_nguoi = keo // nguoi

# %
# chia lấy dư

con_du = keo % nguoi

print("Mỗi người được", moi_nguoi, "viên")

print("Còn dư", con_du, "viên")


# ============================================================
# TODO 5: Đổi độ C sang độ F
# ============================================================

c = 37

# công thức:
# F = C * 9/5 + 32

f = c * 9 / 5 + 32

# f-string
# dùng để chèn biến vào chuỗi

print(f"{c}°C = {f}°F")


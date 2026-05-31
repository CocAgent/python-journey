"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# ============================================================
# TODO 1: Nhập 2 số từ người dùng
# ============================================================

# input()
# dùng để nhập dữ liệu

# float()
# đổi chuỗi thành số thực

a = float(input("Nhập số thứ nhất: "))

b = float(input("Nhập số thứ hai: "))

# +
# phép cộng

print("Tổng =", a + b)

# -
# phép trừ

print("Hiệu =", a - b)

# *
# phép nhân

print("Tích =", a * b)

# /
# phép chia

print("Thương =", a / b)


# ============================================================
# TODO 2: Tính diện tích và chu vi hình tròn
# ============================================================

# số pi

pi = 3.14159

# nhập bán kính

r = float(input("Nhập bán kính hình tròn: "))

# **
# lũy thừa

# r²

dien_tich = pi * (r ** 2)

# 2 × π × r

chu_vi = 2 * pi * r

# :.2f
# làm tròn 2 chữ số thập phân

print(f"Diện tích = {dien_tich:.2f}")

print(f"Chu vi = {chu_vi:.2f}")


# ============================================================
# TODO 3: Tính giá sau khi giảm
# ============================================================

gia_goc = float(input("Nhập giá gốc: "))

giam_gia = float(input("Nhập phần trăm giảm giá: "))

# công thức:
# giá giảm = giá gốc × % giảm / 100

gia_sau_giam = gia_goc - (gia_goc * giam_gia / 100)

# :,.0f
# thêm dấu phẩy
# bỏ phần thập phân

print(f"Giá sau giảm = {gia_sau_giam:,.0f} VNĐ")


# ============================================================
# TODO 4: Máy đổi tiền
# ============================================================

# nhập số tiền VNĐ

vnd = float(input("Nhập số tiền VNĐ: "))

# nhập tỷ giá

ty_gia = float(input("Nhập tỷ giá USD/VNĐ: "))

# USD = VND / tỷ giá

usd = vnd / ty_gia

# :.2f
# làm tròn 2 chữ số

print(f"Số USD tương ứng: {usd:.2f} USD")

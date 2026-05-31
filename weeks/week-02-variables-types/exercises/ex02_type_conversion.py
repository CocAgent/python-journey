"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# ============================================================
# TODO 1: Chuyển str sang int
# ============================================================

# "42" là chuỗi (str)
# vì nằm trong dấu ""

so_text = "42"

# int()
# đổi chuỗi thành số nguyên

so = int(so_text)

# cộng thêm 8

ket_qua = so + 8

print("Kết quả:", ket_qua)


# ============================================================
# TODO 2: Chuyển float sang int
# ============================================================

# float = số thực

pi = 3.14159

# int()
# sẽ bỏ phần thập phân

pi_int = int(pi)

print("Sau khi chuyển sang int:", pi_int)

# kết quả là:
# 3


# ============================================================
# TODO 3: Kiểm tra bool()
# ============================================================

# bool()
# chuyển dữ liệu thành True hoặc False

# Falsy (được xem là False)

print(bool(0))

print(bool(""))

print(bool([]))

# Truthy (được xem là True)

print(bool(1))

print(bool("hello"))

print(bool([1, 2]))


# ============================================================
# TODO 4: Tính BMI
# ============================================================

# input()
# dùng để nhập dữ liệu

# float()
# đổi dữ liệu sang số thực

chieu_cao = float(input("Nhập chiều cao (m): "))

can_nang = float(input("Nhập cân nặng (kg): "))

# **
# lũy thừa

# BMI = cân nặng / chiều cao²

bmi = can_nang / (chieu_cao ** 2)

# :.1f
# làm tròn 1 số thập phân

print(f"BMI của bạn là: {bmi:.1f}")


# ============================================================
# TODO 5: Đổi giây sang giờ : phút : giây
# ============================================================

tong_giay = int(input("Nhập số giây: "))

# //
# chia lấy nguyên

gio = tong_giay // 3600

# %
# chia lấy dư

# lấy phần còn lại sau khi tính giờ

phut = (tong_giay % 3600) // 60

# lấy số giây còn lại

giay = tong_giay % 60

print(f"{gio} giờ {phut} phút {giay} giây")

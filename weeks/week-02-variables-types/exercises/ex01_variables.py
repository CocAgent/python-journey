"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# ============================================================
# TODO 1: Tạo 4 biến lưu thông tin cá nhân
# ============================================================

# str (string)
# dùng để lưu chữ

ten = "Dương Khánh Băng"

# int (integer)
# dùng để lưu số nguyên

tuoi = 20

# float
# dùng để lưu số thực

diem_tb = 8.5

# bool (boolean)
# chỉ có True hoặc False

dang_hoc = True

# type()
# dùng để xem kiểu dữ liệu

print(ten, type(ten))
print(tuoi, type(tuoi))
print(diem_tb, type(diem_tb))
print(dang_hoc, type(dang_hoc))


# ============================================================
# TODO 2: Hoán đổi giá trị 2 biến
# ============================================================

a = 10
b = 20

print("Trước hoán đổi:")
print("a =", a)
print("b =", b)

# Python cho phép đổi chỗ trực tiếp

a, b = b, a

print("Sau hoán đổi:")
print("a =", a)
print("b =", b)


# ============================================================
# TODO 3: Augmented Assignment
# ============================================================

# Augmented Assignment
# là vừa tính toán vừa gán lại giá trị

x = 100

# x = x + 50

x += 50
print("Sau += :", x)

# x = x - 20

x -= 20
print("Sau -= :", x)

# x = x * 2

x *= 2
print("Sau *= :", x)

# x = x // 5

x //= 5
print("Sau //= :", x)


# ============================================================
# TODO 4: Multiple Assignment
# ============================================================

# gán nhiều biến trên cùng một dòng

ho, ten, tuoi = "Dương", "Khánh Băng", 20

# f-string
# dùng để chèn biến vào chuỗi

print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")


# ============================================================
# KIẾN THỨC TRONG BÀI
# ============================================================

# BIẾN (variable)
# dùng để lưu dữ liệu

# cú pháp:
# ten_bien = gia_tri

# ví dụ:
# tuoi = 20

# ============================================================
# CÁC KIỂU DỮ LIỆU
# ============================================================

# str
# chuỗi ký tự
# ví dụ:
# "Python"

# int
# số nguyên
# ví dụ:
# 10

# float
# số thực
# ví dụ:
# 8.5

# bool
# True hoặc False

# ============================================================
# NHỮNG ĐIỀU KHÔNG ĐƯỢC LÀM
# ============================================================

# Sai:
# 1ten = "Bang"
# không được bắt đầu tên biến bằng số

# Sai:
# ten hoc sinh = "Bang"
# không được có khoảng trắng

# Sai:
# true
# false

# Python yêu cầu:
# True
# False

# ============================================================
# PYTHON PHÂN BIỆT HOA THƯỜNG
# ============================================================

# ten khác Ten

ten = "Bang"

Ten = "Minh"

print(ten)
print(Ten)


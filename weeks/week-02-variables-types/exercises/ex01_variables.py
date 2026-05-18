"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân
ten = "Lê Văn Cường"
tuoi = 20
diem_tb = 9.5
dang_hoc = True

print(f"ten: {ten} -> {type(ten)}")
print(f"tuoi: {tuoi} -> {type(tuoi)}")
print(f"diem_tb: {diem_tb} -> {type(diem_tb)}")
print(f"dang_hoc: {dang_hoc} -> {type(dang_hoc)}")

# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
a = 10
b = 20
a, b = b, a
print(f"Sau hoán đổi: a = {a}, b = {b}")

# TODO 3: Augmented assignment
x = 100
x += 50
print(f"x sau khi += 50: {x}")
x -= 20
print(f"x sau khi -= 20: {x}")
x *= 2
print(f"x sau khi *= 2: {x}")
x //= 5
print(f"x sau khi //= 5: {x}")

# TODO 4 (Thử thách): Multiple assignment
ho, ten, tuoi = "Lê Văn", "Cường", 20
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")

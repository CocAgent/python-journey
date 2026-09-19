"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân
# ten = ???       (str)
# tuoi = ???      (int)
# diem_tb = ???   (float)
# dang_hoc = ???  (bool)
# In ra giá trị và kiểu dữ liệu của mỗi biến bằng type()
ten = "An"
tuoi = 20
diem_tb = 8.5
dang_hoc = True

print(f"Tên: {ten} - Kiểu dữ liệu: {type(ten)}")
print(f"Tuổi: {tuoi} - Kiểu dữ liệu: {type(tuoi)}")
print(f"Điểm TB: {diem_tb} - Kiểu dữ liệu: {type(diem_tb)}")
print(f"Đang học: {dang_hoc} - Kiểu dữ liệu: {type(dang_hoc)}")


# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a
a = 10
b = 20
print(f"Trước hoán đổi: a = {a}, b = {b}")

a, b = b, a
print(f"Sau hoán đổi: a = {a}, b = {b}")


# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước
x = 100
print(f"Ban đầu: x = {x}")

x += 50   # Cộng thêm 50 -> 150
print(f"Sau bước 1 (+= 50): x = {x}")

x -= 30   # Trừ đi 30 -> 120
print(f"Sau bước 2 (-= 30): x = {x}")

x *= 2    # Nhân với 2 -> 240
print(f"Sau bước 3 (*= 2): x = {x}")

x //= 4   # Chia lấy nguyên cho 4 -> 60
print(f"Sau bước 4 (//= 4): x = {x}")


# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"
ho, ten, tuoi = "Nguyễn", "An", 20
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")


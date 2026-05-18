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
name = "DO MINH KIET"
age = 20
average_score = 8.5
is_studying = True

print(f"Tên: {name}, Kiểu: {type(name)}")
print(f"Tuổi: {age}, Kiểu: {type(age)}")
print(f"Điểm trung bình: {average_score}, Kiểu: {type(average_score)}")
print(f"Đang học: {is_studying}, Kiểu: {type(is_studying)}")

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
print(f"Giá trị ban đầu của x: {x}")
x += 50
print(f"Sau x += 50: {x}")
x -= 30
print(f"Sau x -= 30: {x}")
x *= 2
print(f"Sau x *= 2: {x}")
x //= 7
print(f"Sau x //= 7: {x}")

# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"
ho, ten, tuoi = "DO", "MINH KIET", 20
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")

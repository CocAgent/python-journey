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

ten = "Phan Văn Lực" 
tuoi = 20 
diem_tb = 9 
dang_hoc = True 
print(f"ten = {ten}, type: {type(ten)}") 
print(f"tuoi = {tuoi}, type: {type(tuoi)}") 
print(f"diem_tb = {diem_tb}, type: {type(diem_tb)}")
print(f"dang_hoc = {dang_hoc}, type: {type(dang_hoc)}")

# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a
a = 10
b = 20 
a, b = b, a 
print(f"a = {a}, b = {b}")

# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước
x = 100
x += 10; print(f"x += 10 → {x}") #110 
x -= 20; print(f"x -= 20 → {x}") #90 
x *= 3; print(f"x *= 3 → {x}") #270 
x //= 8; print(f"x //= 8 → {x}") #33

# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"
ho = "Phan"
ten = "Lực"
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")

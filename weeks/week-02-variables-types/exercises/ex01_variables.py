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
ten="kiet"
tuoi =20
diem_tb= 8.4
dang_hoc=True
print(ten, type(ten))
print(tuoi, type(tuoi))
print(diem_tb, type(diem_tb))
print(dang_hoc, type(dang_hoc))


# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a
a=10
b=20
a, b = b, a
print("Sau hoán đổi: a =", a, ", b =", b)


# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước
x= 100
x += 10
print("Sau bước 1: x =", x)
x -= 20
print("Sau bước 2: x =", x)
x *= 3
print("Sau bước 3: x =", x)
x //= 4
print("Sau bước 4: x =", x)


# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"

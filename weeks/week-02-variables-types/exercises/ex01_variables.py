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
print("TODO 1: Tao 4 bien luu thong tin ca nhan")
ten = "Tran Ngoc Bao"
tuoi = 20
diem_tb = 8.1
dang_hoc = True
print(ten, type(ten))
print(tuoi, type(tuoi))
print(diem_tb, type(diem_tb))
print(dang_hoc, type(dang_hoc))
print("")

# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a
print("TODO 2: Hoan doi gia tri 2 bien khong dung bien tam")
a = 10
b = 20
print("Truoc khi hoan doi:")
print(f"a = {a}, b = {b}")
a, b = b, a
print("Sau khi hoan doi:")
print(f"a = {a}, b = {b}")


# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước
print("TODO 3: Augmented assignment")
x = 100
print("x = 100")
x += 100
print(x)
x -= 100
print(x)
x *= 100
print(x)
x //= 100
print(x)
print("")

# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"
print("TODO 4 (Thử thách): Multiple assignment")
ho, ten, tuoi = "Tran", "Ngoc Bao", 20
print(f"Ho ten: {ho} {ten}, {tuoi} tuoi")


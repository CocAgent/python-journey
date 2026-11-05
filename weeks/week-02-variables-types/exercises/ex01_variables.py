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
Ten = "Nguyen Huu Tai"
Tuoi = 21
Diem_tb = 8.7
Dang_hoc = True
print("Ten:", Ten)
print("Tuoi:", Tuoi)
print("Diem_tb:", Diem_tb)
print("Dang_hoc:", Dang_hoc)
print("Type of ten:", type(Ten))
print("Type of tuoi:", type(Tuoi))
print("Type of diem_tb:", type(Diem_tb))
print("Type of dang_hoc:", type(Dang_hoc))
# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a
a = 10
b = 20
a, b = b, a
print("a:", a)
print("b:", b)

# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước
x = 100
print("x = 100")
x += 50
print("x = x + 50 =", x)
x -= 30
print("x = x - 30 =", x)
x *= 2
print("x = x * 2 =", x)
x //= 4
print("x = x // 4 =", x)


# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"
ho, ten, tuoi = "Nguyễn", "Hữu Tài", 21
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")
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
tên = "Bùi Anh Khoa"
tuổi = 22
diem_tb = 8.3
đang_học = True

print(tên, type(tên))
print(tuổi, type(tuổi))
print(diem_tb, type(diem_tb))
print(đang_học, type(đang_học))

# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a
a = 10
b = 20
print(f"Trước: a= {a}, b={b}")
a,b = b,a
print(f"Sau: a={a}, b={b}")


# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước
x = 100
print(f"x={x}")
x += 50
print(f"x={x}")
x -= 10
print(f"x={x}")
x *= 5
print(f"x={x}")
x //= 3
print(f"x={x}")

# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"
họ, tên, tuổi = "Bùi", "Khoa",22
print(f"Họ tên: {họ},{tên},{tuổi} tuổi")

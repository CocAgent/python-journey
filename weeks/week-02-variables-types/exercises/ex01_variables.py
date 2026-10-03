"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân
ten = "Nguyen Tan Dung"     #(str)
tuoi = 19      #(int)
diem_tb = 7.5   #(float)
dang_hoc = True  #(bool)
# In ra giá trị và kiểu dữ liệu của mỗi biến bằng type()

print("ten:", ten, type(ten))
print("tuoi:", tuoi, type(tuoi))
print("diem_tb:", diem_tb, type(diem_tb))
print("dang_hoc:", dang_hoc, type(dang_hoc))

# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
a = 10
b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a
a, b = b, a

print(f"Sau hoan doi: a = {a}, b = {b}")

# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước

x = 100

x += 50
print("Sau step 1 (+=):", x)
x -= 25
print("sau step 2 (-=)", x)
x *= 2
print("sau step 3 (*=)", x)
x //= 5
print("sau step 4 (//=)", x)

# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"

ho, ten, tuoi = "Nguyen Tan", "Dung", 19
print(f"Ho ten: {ho} {ten}, {tuoi} tuoi")

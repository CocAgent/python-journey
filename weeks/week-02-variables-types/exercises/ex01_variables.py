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
ten = "Phương"
tuoi = 23
diem_tb = 8.5
dang_hoc = True
print(f"ten= {ten},type: {type(ten)}")
print(f"tuoi= {tuoi},type: {type(tuoi)}")
print(f"diem_tb= {diem_tb},type: {type(diem_tb)}")
print(f"dang_hoc= {dang_hoc},type: {type(dang_hoc)}")


# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a
a= 10
b= 20   
a, b = b, a
print(f"a = {a}, b = {b}")  

# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước
x=100
x+=20; print(f"x+=20={x}")
x-=30; print(f"x-=30={x}")
x*=2; print(f"x*=2={x}")    
x//=7; print(f"x//=7={x}")

# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"
ho = "Tran" ; ten = "Phuong" ; tuoi = 23
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")
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
ten = "Ho Van Nam"
tuoi = 20
diem_tb= 8.1
dang_hoc = True

values = (ten, tuoi, diem_tb, dang_hoc)
for value in values:
    print(f"value={value}, type={type(value).__name__}")

#print(type(ten), type(tuoi), type(diem_tb), type(dang_hoc))

# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a
a = 10
b = 20
a, b = b, a

print(f"a= {a}, b= {b}")


# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước
x= 100
x+= 10
x-= 30
#x*=2
#x//=50

print(f"x+= {x}, x-={x},")
print(f"x*= {x*2}, x//= {x//20} ")


# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"
ho, ten, tuoi = "Vo", "Nam", 20
ho_ten = ho + " " + ten
print(f"ho ten: {ho_ten}, {tuoi} tuoi")


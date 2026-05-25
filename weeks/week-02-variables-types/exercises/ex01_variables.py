"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân
# ten = Phạm Văn Thiện       (str)
# tuoi = 20      (int)
# diem_tb = 7.0   (float)
# dang_hoc = true  (bool)
# In ra giá trị và kiểu dữ liệu của mỗi biến bằng type()
print(ten, type(ten))
print(tuoi, type(tuoi))
print(diem_tb, type(diem_tb))
print(dang_hoc, type(dang_hoc))


# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a
print("a =", b)
print("b =", a)


# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước
x += 10
print("Sau x += 10:", x)

x -= 5
print("Sau x -= 5:", x)

x *= 2
print("Sau x *= 2:", x)

x //= 3
print("Sau x //= 3:", x)

# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi"

ho, ten, tuoi = "Phạm", "Thiện", 20
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")

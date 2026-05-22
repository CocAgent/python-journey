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
# In ra giá trị và kiểu dữ liệu của mỗi biến bằng type().
# Viết code ở đây:
ten = "Nguyễn Trung Tín"
tuoi = 21
diem_tb = 8.75
dang_hoc = True

print(f"Tên: {ten}, Kiểu: {type(ten)}")
print(f"Tuổi: {tuoi}, Kiểu: {type(tuoi)}")
print(f"Điểm TB: {diem_tb}, Kiểu: {type(diem_tb)}")
print(f"Đang học: {dang_hoc}, Kiểu: {type(dang_hoc)}")

print("-" * 30) # Dòng phân cách


# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
# a = 10
# b = 20
# Sau hoán đổi: a = 20, b = 10
# Gợi ý: Python cho phép a, b = b, a.
# Viết code ở đây:
a = 10
b = 20
print(f"Trước hoán đổi: a = {a}, b = {b}")
a, b = b, a
print(f"Sau hoán đổi: a = {a}, b = {b}")

print("-" * 30) # Dòng phân cách


# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
# In ra x sau mỗi bước.
# Viết code ở đây:
x = 100
print(f"Giá trị ban đầu của x: {x}")

x += 5 # x = x + 5
print(f"Sau x += 5: {x}") # 105

x -= 10 # x = x - 10
print(f"Sau x -= 10: {x}") # 95

x *= 2 # x = x * 2
print(f"Sau x *= 2: {x}") # 190

x //= 3 # x = x // 3
print(f"Sau x //= 3: {x}") # 63

print("-" * 30) # Dòng phân cách


# TODO 4 (Thử thách): Multiple assignment
# Gán 3 biến trên 1 dòng: ho, ten, tuoi = ???.
# In ra: "Họ tên: [ho] [ten], [tuoi] tuổi".
# Viết code ở đây:
ho, ten, tuoi = "Nguyễn", "Trung Tín", 21
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")

print("\n🎉 Chúc mừng! Bạn đã hoàn thành bài tập về biến!")

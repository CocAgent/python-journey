"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo biến và in type
ten = "Nguyễn Tấn Vũ"
tuoi = 20
diem_tb = 3.6
dang_hoc = True

print("ten =", ten, "| type:", type(ten))
print("tuoi =", tuoi, "| type:", type(tuoi))
print("diem_tb =", diem_tb, "| type:", type(diem_tb))
print("dang_hoc =", dang_hoc, "| type:", type(dang_hoc))


# TODO 2: Hoán đổi giá trị 2 biến
a = 10
b = 20

a, b = b, a

print("\nSau hoán đổi:")
print("a =", a)
print("b =", b)


# TODO 3: Augmented assignment
x = 100

x += 50
print("x += 50 →", x)

x -= 30
print("x -= 30 →", x)

x *= 2
print("x *= 2 →", x)

x //= 7
print("x //= 7 →", x)


# TODO 4: Multiple assignment
ho, ten, tuoi = "Nguyễn", "Tấn Vũ", 20

print("\nHọ tên:", ho, ten, ",", tuoi, "tuổi")

"""Lời giải Bài tập 01: Biến trong Python"""

# TODO 1
ten = "Trần Minh Khang"
tuoi = 22
diem_tb = 7.8
dang_hoc = True

print(f"ten = {ten}, type: {type(ten)}")
print(f"tuoi = {tuoi}, type: {type(tuoi)}")
print(f"diem_tb = {diem_tb}, type: {type(diem_tb)}")
print(f"dang_hoc = {dang_hoc}, type: {type(dang_hoc)}")

# TODO 2
a = 15
b = 35

a, b = b, a

print(f"a = {a}, b = {b}")  # a = 35, b = 15

# TODO 3
x = 200

x += 25
print(f"x += 25  → {x}")   # 225

x -= 40
print(f"x -= 40  → {x}")   # 185

x *= 3
print(f"x *= 3   → {x}")   # 555

x //= 5
print(f"x //= 5  → {x}")   # 111

# TODO 4
ho, ten, tuoi = "Lê", "Gia Huy", 19

print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")

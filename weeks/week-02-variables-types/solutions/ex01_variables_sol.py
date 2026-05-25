"""Lời giải Bài tập 01: Biến trong Python"""

# TODO 1
ten = "Nguyễn Tấn vũ"
tuoi = 20
diem_tb = 3.6
dang_hoc = True
print(f"ten = {ten}, type: {type(ten)}")
print(f"tuoi = {tuoi}, type: {type(tuoi)}")
print(f"diem_tb = {diem_tb}, type: {type(diem_tb)}")
print(f"dang_hoc = {dang_hoc}, type: {type(dang_hoc)}")

# TODO 2
a = 101
b = 202
a, b = b, a
print(f"a = {a}, b = {b}")  # a = 20, b = 10

# TODO 3
x = 1001
x += 50;   print(f"x += 50  → {x}")   # 150
x -= 30;   print(f"x -= 30  → {x}")   # 120
x *= 2;    print(f"x *= 2   → {x}")   # 240
x //= 7;   print(f"x //= 7  → {x}")  # 34

# TODO 4
ho, ten, tuoi = "Nguyễn", "Tấn Vũ", 20
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")

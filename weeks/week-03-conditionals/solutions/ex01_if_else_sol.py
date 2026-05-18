"""Lời giải Bài tập 01: if/elif/else cơ bản"""

# TODO 1
tuoi = int(input("Nhập tuổi: "))
if tuoi < 13:
    print("Thiếu nhi")
elif tuoi <= 17:
    print("Thiếu niên")
elif tuoi <= 64:
    print("Người lớn")
else:
    print("Người cao tuổi")

# TODO 2
diem = float(input("Nhập điểm (0-10): "))
if diem >= 9:
    print("Xuất sắc")
elif diem >= 8:
    print("Giỏi")
elif diem >= 6.5:
    print("Khá")
elif diem >= 5:
    print("Trung bình")
else:
    print("Yếu")

# TODO 3
nam = int(input("Nhập năm: "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(f"{nam} là năm nhuận")
else:
    print(f"{nam} không phải năm nhuận")

# TODO 4
a = float(input("Số thứ nhất: "))
b = float(input("Số thứ hai: "))
c = float(input("Số thứ ba: "))
if a >= b and a >= c:
    print(f"Số lớn nhất: {a}")
elif b >= a and b >= c:
    print(f"Số lớn nhất: {b}")
else:
    print(f"Số lớn nhất: {c}")

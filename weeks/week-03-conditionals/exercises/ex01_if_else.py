"""
Bài tập 01: if/elif/else cơ bản 🔀
====================================
Mục tiêu: Viết câu lệnh điều kiện đúng cú pháp
"""

# TODO 1: Nhập tuổi, in ra nhóm tuổi
# < 13: "Thiếu nhi"
# 13-17: "Thiếu niên"
# 18-64: "Người lớn"
# >= 65: "Người cao tuổi"
age = int(input("Nhập tuổi: "))

if age < 13:
    print("Thiếu nhi")
elif age <= 17:
    print("Thiếu niên")
elif age <= 64:
    print("Người lớn")
else:
    print("Người cao tuổi")


# TODO 2: Nhập điểm (0-10), xếp loại:
# >= 9: Xuất sắc, >= 8: Giỏi, >= 6.5: Khá, >= 5: TB, < 5: Yếu
diem = float(input("Nhập điểm (0-10): "))

if diem < 0 or diem > 10:
    print("Điểm không hợp lệ")
elif diem >= 9:
    print("Xuất sắc")
elif diem >= 8:
    print("Giỏi")
elif diem >= 6.5:
    print("Khá")
elif diem >= 5:
    print("TB")
else:
    print("Yếu")


# TODO 3: Nhập năm, kiểm tra năm nhuận
# Năm nhuận: chia hết cho 4, NHƯNG không chia hết cho 100,
# TRỪ KHI chia hết cho 400
# 2000 → nhuận, 1900 → không, 2024 → nhuận
year = int(input("Nhập năm: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} là năm nhuận")
else:
    print(f"{year} không phải là năm nhuận")


# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"Số lớn nhất là: {largest}")

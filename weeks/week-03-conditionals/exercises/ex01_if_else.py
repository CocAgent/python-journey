"""
Bài tập 01: if/elif/else cơ bản 🔀
====================================
Mục tiêu: Viết câu lệnh điều kiện đúng cú pháp
"""
# TODO 1: Nhập tuổi, in ra nhóm tuổi
# < 13: "Thiếu nhi"
tuoi = int(input("Nhập tuổi: "))
if tuoi < 13:
    print("Thiếu nhi")
# 13-17: "Thiếu niên"
elif tuoi <= 17:
    print("Thiếu niên")
# 18-64: "Người lớn"
elif tuoi <= 64:
    print("Người lớn")
# >= 65: "Người cao tuổi"
else:
    print("Người cao tuổi")
# TODO 2: Nhập điểm (0-10), xếp loại
diem = float(input("Nhập điểm: "))
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
# TODO 3: Nhập năm, kiểm tra năm nhuận
nam = int(input("Nhập năm: "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print("Năm nhuận")
else:
    print("Không phải năm nhuận")
# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
if a >= b and a >= c:
    print("Số lớn nhất là:", a)
elif b >= a and b >= c:
    print("Số lớn nhất là:", b)
else:
    print("Số lớn nhất là:", c)

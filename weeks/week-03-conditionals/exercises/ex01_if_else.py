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
tuoi = int(input("Nhập tuổi: "))

if tuoi < 13:
    print("Thiếu nhi")
elif tuoi <= 17:
    print("Thiếu niên")
elif tuoi <= 64:
    print("Người lớn")
else:
    print("Người cao tuổi")
# TODO 2: Nhập điểm (0-10), xếp loại:
# >= 9: Xuất sắc, >= 8: Giỏi, >= 6.5: Khá, >= 5: TB, < 5: Yếu
diem= float(input("Nhập điểm (0-10): "))

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
# Năm nhuận: chia hết cho 4, NHƯNG không chia hết cho 100,
# TRỪ KHI chia hết cho 400
# 2000 → nhuận, 1900 → không, 2024 → nhuận
nam = int(input("Nhập năm: "))

if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print("Năm nhuận")
else:
    print("Không phải năm nhuận")

# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else
nhap_1 = float(input("Nhập số thứ nhất: "))
nhap_2 = float(input("Nhập số thứ hai: "))  
nhap_3 = float(input("Nhập số thứ ba: "))
if nhap_1 >= nhap_2 and nhap_1 >= nhap_3:
    print("Số lớn nhất là:", nhap_1)
elif nhap_2 >= nhap_1 and nhap_2 >= nhap_3:
    print("Số lớn nhất là:", nhap_2)
else:
    print("Số lớn nhất là:", nhap_3)
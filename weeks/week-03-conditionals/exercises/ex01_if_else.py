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
tuoi=int(input("Tuoi cua ban la: "))
if tuoi<13:
    print("Thieu nhi")
elif tuoi<=17:
    print("Thieu nien")
elif tuoi<=64:
    print("Nguoi lon")
else:
    print("Nguoi cao tuoi")



# TODO 2: Nhập điểm (0-10), xếp loại:
# >= 9: Xuất sắc, >= 8: Giỏi, >= 6.5: Khá, >= 5: TB, < 5: Yếu

diem = float(input("Nhập điểm (0-10): "))

if diem < 0 or diem > 10:
    print("Điểm không hợp lệ!")
elif diem >= 9:
    print("Xếp loại: Xuất sắc")
elif diem >= 8:
    print("Xếp loại: Giỏi")
elif diem >= 6.5:
    print("Xếp loại: Khá")
elif diem >= 5:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")


# TODO 3: Nhập năm, kiểm tra năm nhuận
# Năm nhuận: chia hết cho 4, NHƯNG không chia hết cho 100,
# TRỪ KHI chia hết cho 400
# 2000 → nhuận, 1900 → không, 2024 → nhuận
nam = int(input("Nhập năm: "))

if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print(nam, "là năm nhuận")
else:
    print(nam, "không phải là năm nhuận")

# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

if a >= b and a >= c:
    print("Số lớn nhất là:", a)
elif b >= a and b >= c:
    print("Số lớn nhất là:", b)
else:
    print("Số lớn nhất là:", c)

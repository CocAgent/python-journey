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
    print("Nhóm tuổi: Thiếu nhi")
elif tuoi <= 17:
    print("Nhóm tuổi: Thiếu niên")
elif tuoi <= 64:
    print("Nhóm tuổi: Người lớn")
else:
    print("Nhóm tuổi: Người cao tuổi")


# TODO 2: Nhập điểm (0-10), xếp loại:
# >= 9: Xuất sắc, >= 8: Giỏi, >= 6.5: Khá, >= 5: TB, < 5: Yếu
diem = float(input("Nhập điểm (0-10): "))
if diem < 0 or diem > 10:
    print("Xếp loại: Điểm không hợp lệ")
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
# Năm nhuận: (chia hết cho 4 và không chia hết cho 100) hoặc chia hết cho 400
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(f"Năm {nam} là năm nhuận")
else:
    print(f"Năm {nam} không phải là năm nhuận")


# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else
so1 = float(input("Nhập số thứ nhất: "))
so2 = float(input("Nhập số thứ hai: "))
so3 = float(input("Nhập số thứ ba: "))

if so1 >= so2 and so1 >= so3:
    so_lon_nhat = so1
elif so2 >= so1 and so2 >= so3:
    so_lon_nhat = so2
else:
    so_lon_nhat = so3

print(f"Số lớn nhất là: {so_lon_nhat}")

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
print("--- TODO 1: Phân loại nhóm tuổi ---")
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
print("\n--- TODO 2: Xếp loại học tập ---")
diem = float(input("Nhập điểm (0-10): "))
if diem >= 9.0:
    print("Xuất sắc")
elif diem >= 8.0:
    print("Giỏi")
elif diem >= 6.5:
    print("Khá")
elif diem >= 5.0:
    print("Trung bình")
else:
    print("Yếu")


# TODO 3: Nhập năm, kiểm tra năm nhuận
# Năm nhuận: chia hết cho 4, NHƯNG không chia hết cho 100,
# TRỪ KHI chia hết cho 400
# 2000 → nhuận, 1900 → không, 2024 → nhuận
print("\n--- TODO 3: Kiểm tra năm nhuận ---")
nam = int(input("Nhập năm: "))
if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print(f"Năm {nam} là năm nhuận.")
else:
    print(f"Năm {nam} không phải là năm nhuận.")


# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else
print("\n--- TODO 4: Tìm số lớn nhất trong 3 số ---")
a = float(input("Nhập số thứ nhất (a): "))
b = float(input("Nhập số thứ hai (b): "))
c = float(input("Nhập số thứ ba (c): "))

if a >= b and a >= c:
    so_lon_nhat = a
elif b >= a and b >= c:
    so_lon_nhat = b
else:
    so_lon_nhat = c

print(f"Số lớn nhất là: {so_lon_nhat}")

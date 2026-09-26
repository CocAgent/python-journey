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
print("--- 1. Phân loại nhóm tuổi ---")
tuoi = int(input("Nhập tuổi: "))

if tuoi < 0:
    print("Tuổi không hợp lệ")
elif tuoi < 13:
    print("Nhóm tuổi: Thiếu nhi")
elif tuoi < 18:
    print("Nhóm tuổi: Thiếu niên")
elif tuoi < 65:
    print("Nhóm tuổi: Người lớn")
else:
    print("Nhóm tuổi: Người cao tuổi")


# TODO 2: Nhập điểm (0-10), xếp loại:
# >= 9: Xuất sắc, >= 8: Giỏi, >= 6.5: Khá, >= 5: TB, < 5: Yếu
print("\n--- 2. Xếp loại học lực ---")
diem = float(input("Nhập điểm (0-10): "))

if diem < 0 or diem > 10:
    print("Điểm không hợp lệ (phải từ 0 đến 10)")
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
print("\n--- 3. Kiểm tra năm nhuận ---")
nam = int(input("Nhập năm cần kiểm tra: "))

if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(f"Năm {nam} là NĂM NHUẬN")
else:
    print(f"Năm {nam} KHÔNG PHẢI là năm nhuận")


# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else
print("\n--- 4. Tìm số lớn nhất trong 3 số ---")
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

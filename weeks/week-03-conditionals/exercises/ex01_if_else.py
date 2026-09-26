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
tuoi=int(input("Nhập tuổi: "))
if tuoi < 13:
    nhom_tuoi = "Thiếu nhi"
elif tuoi >= 13 and tuoi <=17:
    nhom_tuoi = "Thiếu niên"
elif tuoi >= 18 and tuoi <=64:
    nhom_tuoi = "Người lớn"
else:
    nhom_tuoi = "Người cao tuổi"
print(f"Tuổi: {tuoi} - {nhom_tuoi}\n")

# TODO 2: Nhập điểm (0-10), xếp loại:
# >= 9: Xuất sắc, >= 8: Giỏi, >= 6.5: Khá, >= 5: TB, < 5: Yếu
diem = float(input("Nhập điểm (0-10): "))
if diem >= 9:
    xep_loai = "Xuất sắc"
elif diem >= 8:
    xep_loai = "Giỏi"
elif diem >= 6.5:
    xep_loai = "Khá"
elif diem >= 5:
    xep_loai = "TB"
else:
    xep_loai = "Yếu"
print(f"Điểm: {diem} - Xếp loại: {xep_loai}\n")

# TODO 3: Nhập năm, kiểm tra năm nhuận
# Năm nhuận: chia hết cho 4, NHƯNG không chia hết cho 100,
# TRỪ KHI chia hết cho 400
# 2000 → nhuận, 1900 → không, 2024 → nhuận
nam = int(input("Nhập năm: "))
if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
    print(f"Năm {nam} nhuận")
else:
    print(f"Năm {nam} không nhuận\n")

# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

if a >= b and a >= c:
    print(f"Số lớn nhất là: {a}")
elif b >= a and b >= c:
    print(f"Số lớn nhất là: {b}")
else:
    print(f"Số lớn nhất là: {c}")
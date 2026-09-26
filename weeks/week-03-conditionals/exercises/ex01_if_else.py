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
age = int(input('Nhap tuoi:'))
if age < 0 or age > 120:
    print('Tuoi khong hop le')
elif age < 13:
    print('Thieu nhi')
elif age <= 17:
    print('Thieu nien')
elif age <= 64:
    print('Nguoi lon')
else:
    print('Nguoi cao tuoi')
# TODO 2: Nhập điểm (0-10), xếp loại:
# >= 9: Xuất sắc, >= 8: Giỏi, >= 6.5: Khá, >= 5: TB, < 5: Yếu
score = float(input('Nhap diem:'))
if score < 0 or score > 10:
    print('Diem khong hop le')
elif score >= 9:
    print('Xuat sac')
elif score >= 8:
    print('Gioi')
elif score >= 6.5:
    print('Kha')
elif score >= 5:
    print('Trung binh')
else:
    print('Yeu')
# TODO 3: Nhập năm, kiểm tra năm nhuận
# Năm nhuận: chia hết cho 4, NHƯNG không chia hết cho 100,
# TRỪ KHI chia hết cho 400
# 2000 → nhuận, 1900 → không, 2024 → nhuận
year = int(input('Nhap nam:'))
if year % 4 == 0 and year % 100 != 0:
    print('Nam nhuan')
elif year % 400:
    print('Nam nhuan')
else:
    print('Nam khong nhuan')
# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else
a = int(input('Nhap so thu 1:'))
b = int(input('Nhap so thu 2:'))
c = int(input('Nhap so thu 3:'))
if a >= b and a >= c:
    print('So lon nhat la:', a)
elif b >= a and b >= c:
    print('So lon nhat la:', b)
else:
    print('So lon nhat la:', c)
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
tuoi = int(input("Nhap tuoi: "))
if tuoi < 13:
    print("Thieu nhi")
elif tuoi >= 13 and tuoi <= 17:
    print("Thieu nien")
elif tuoi >= 18 and tuoi <= 64:
    print("Nguoi lon")
else:
    print("Nguoi cao tuoi")

# TODO 2: Nhập điểm (0-10), xếp loại:
# >= 9: Xuất sắc, >= 8: Giỏi, >= 6.5: Khá, >= 5: TB, < 5: Yếu
diem = float(input("Nhap diem (0-10): "))
if diem >= 9:
    print("Xuat sac")
elif diem >= 8:
    print("Gioi")
elif diem >= 6.5:
    print("Kha")
elif diem >= 5:
    print("TB")
else:
    print("Yeu")

# TODO 3: Nhập năm, kiểm tra năm nhuận
# Năm nhuận: chia hết cho 4, NHƯNG không chia hết cho 100,
# TRỪ KHI chia hết cho 400
# 2000 → nhuận, 1900 → không, 2024 → nhuận

nam = int(input("Nhap nam: "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print("Nam nhuan")
else:
    print("Khong phai nam nhuan")

# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else
so_1 = int(input("Nhap so thu nhat: "))
so_2 = int(input("Nhap so thu hai: "))
so_3 = int(input("Nhap so thu ba: "))
if so_1 >= so_2 and so_1 >= so_3:
    print(f"so lon nhat: {so_1}")
elif so_2 >= so_1 and so_2 >= so_3:
    print(f"so lon nhat: {so_2}")
else:
    print(f"so lon nhat: {so_3}")

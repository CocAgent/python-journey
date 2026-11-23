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
print("=== TODO 1: Phân loại nhóm tuổi ===")
tuoi = int(input("Nhập tuổi của bạn: "))
if tuoi < 0:
    print("Tuổi không hợp lệ!")
elif tuoi < 13:
    print("Thiếu nhi")
elif tuoi <= 17:
    print("Thiếu niên")
elif tuoi <= 64:
    print("Người lớn")
else:
    print("Người cao tuổi")


# TODO 2: Nhập điểm (0-10), xếp loại:
# >= 9: Xuất sắc, >= 8: Giỏi, >= 6.5: Khá, >= 5: TB, < 5: Yếu
print("\n=== TODO 2: Xếp loại học lực ===")
diem = float(input("Nhập điểm (0 - 10): "))
if diem < 0 or diem > 10:
    print("Điểm không hợp lệ! Vui lòng nhập từ 0 đến 10.")
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
print("\n=== TODO 3: Kiểm tra năm nhuận ===")
nam = int(input("Nhập năm cần kiểm tra: "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(f"Năm {nam} là năm nhuận.")
else:
    print(f"Năm {nam} không phải là năm nhuận.")


# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else
print("\n=== TODO 4: Tìm số lớn nhất trong 3 số ===")
so_1 = float(input("Nhập số thứ nhất: "))
so_2 = float(input("Nhập số thứ hai: "))
so_3 = float(input("Nhập số thứ ba: "))

if so_1 >= so_2 and so_1 >= so_3:
    lon_nhat = so_1
elif so_2 >= so_1 and so_2 >= so_3:
    lon_nhat = so_2
else:
    lon_nhat = so_3

print(f"Số lớn nhất là: {lon_nhat:g}")

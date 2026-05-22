# GPA Calculator

n = int(input("Nhập số lượng môn học: "))

tong_diem = 0
tong_tin_chi = 0

for i in range(n):
    ten_mon = input("Tên môn: ")
    tin_chi = int(input("Số tín chỉ: "))
    diem_10 = float(input("Điểm hệ 10: "))

    diem_4 = diem_10 * 4 / 10

    tong_diem += diem_4 * tin_chi
    tong_tin_chi += tin_chi

gpa = tong_diem / tong_tin_chi

if gpa >= 3.6:
    xep_loai = "Xuất sắc"
elif gpa >= 3.2:
    xep_loai = "Giỏi"
elif gpa >= 2.5:
    xep_loai = "Khá"
elif gpa >= 2.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

print("GPA:", round(gpa, 2))
print("Xếp loại:", xep_loai)
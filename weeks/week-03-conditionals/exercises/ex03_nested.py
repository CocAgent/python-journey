"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
So_du = int(input('Nhap so du hien tai:'))
So_tien = int(input('Nhap so tien muon rut:'))
if So_tien > 0:
    if So_tien <= So_du:
        if So_tien % 50000 == 0:
            So_du_moi = So_du - So_tien
            print('Rut tien thanh cong!')
            print(f'So du con lai: {So_du_moi}')
        else:
            print('So tien can rut it nhat la: 50.000')
    else:
        print('So du khong du')
else:
    print('Vui long nhap lai so tien muon rut')
# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
Chieu_cao = float(input('Nhap chieu cao (m):'))
Can_nang = float(input('Nhap can nang (kg):'))
Bmi = Can_nang / (Chieu_cao ** 2)
print(f'BMI cua ban: {Bmi:.2f}')
if Bmi < 18.5:
    print('Thieu can')
elif Bmi < 24.9:
    print('Binh thuong')
elif Bmi < 29.9:
    print('Thua can')
else:
    print('Beo phi')
# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
Loai_ve = input('Loai ve (thuong/vip):').lower()
Ngay = input('Ngay (thuong/cuoi_tuan):').lower()
tuoi = int(input('Tuoi:'))
if Loai_ve == 'thuong':
    gia = 80000
elif Loai_ve == 'vip':
    gia = 120000
else:
    print('Loai ve khong hop le! Vui long nhap lai')
    gia = 0
if gia > 0:
    if Ngay == 'cuoi_tuan':
        gia *= 1.3
    if tuoi < 12 or tuoi >= 65:
        gia *= 0.5
    elif tuoi >= 18 and tuoi <= 25:
        gia *= 0.8
    print(f'Gia ve: {gia:.0f} VND')
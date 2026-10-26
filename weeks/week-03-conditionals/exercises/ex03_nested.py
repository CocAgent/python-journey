"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
so_du = float(input("Nhap so du hien tai: "))
so_tien_rut = float(input("Nhap so tien muon rut: "))
if so_tien_rut <= 0:
    print("So tien rut phai lon hon 0")
elif so_tien_rut > so_du:
    print("khong du so du de rut")
elif so_tien_rut % 50000 != 0:
    print("so tien rut phai la boi so cua 50,000")
else:
    print(f"rut tien thanh cong: {so_tien_rut} VND, so du con lai: {so_du - so_tien_rut} VND")

# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
chieu_cao = float(input("Nhap chieu cao (m): "))
can_nang = float(input("Nhap can nang (kg): "))
BMI = can_nang / (chieu_cao ** 2)
if BMI < 18.5:
    print(f"chi so BMI: {BMI:.1f}, thieu can, nen tang can")
elif 18.5 <= BMI <= 24.9:
    print(f"chi so BMI: {BMI:.1f}, binh thuong")
elif 25 <= BMI <= 29.9:
    print(f"chi so BMI: {BMI:.1f}, thua can, can can thap")
else:
    print(f"chi so BMI: {BMI:.1f}, beo phi, nen gap bac si")

# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
loai_ve = input("Nhap loai ve (thuong/vip): ")
ngay = input("nhap ngay (thuong/cuoi_tuan): ")
tuoi = int(input("Nhap tuoi: "))
if loai_ve == "thuong":
    gia_co_ban = 80000
elif loai_ve == "vip":
    gia_co_ban = 120000
if ngay == "cuoi_tuan":
    gia_co_ban *= 1.3
if tuoi < 12 or tuoi >= 65:
    gia_co_ban *= 0.5
elif tuoi >= 18 and tuoi <= 25:
    gia_co_ban *= 0.8
print(f"gia ve cuoi cung: {gia_co_ban:.0f} VND")

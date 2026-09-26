"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp

so_du = float(input("nhap so du hien tai: "))
tien_rut = float(input("nhap so tien muon rut: "))

if tien_rut > 0:
    if tien_rut <= so_du:
        if tien_rut % 50000 == 0:
            so_du -= tien_rut
            print(f"rut tien thanh cong! so du con lai: {so_du:,.0f} vnd")
        else:
            print("so tien rut phai la boi cua 50000 vnd!")
    else:
        print("so du khong du de thuc hien giao dich!")
else:
    print("so tien rut phai lon hon 0!")  


# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ

height = float(input("nhap chieu cao (m): "))
height = float(input("nhap can nang (kg): "))

bmi = weight / (heighht ** 2)
print(f"chi so bmi cua ban: {bmi:.2f}")

if bmi < 18.5:
    print("thieu can -> ban nen chu y an uong day du de tang can.")
elif bmi <= 24.9:
    print("binh thuong -> the trang tot hay tiep tuc duy tri nhe.")
elif bmi <= 29.9:
    print("thua can -> ban nen chu y tap the duc thuong xuyen hon.")
else:
    print("beo phi -> ban nen gap bac si de tu van suc khoe.")

# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng

loai_ve = input("nhap loai ve (thuong/vip): ").strip().lower()
ngay = input("nhap ngay (thuong/cuoi_tuan): ").strip().lower()
tuoi = int(input("nhaptuoi: "))

if loai_ve == "vip":
    gia_ve = 120000
else:
    gia_ve = 80000

if ngay == "cuoi_tuan":
    gia_ve *= 1.30

if tuoi < 12 or tuoi >= 65:
    gia_ve *= 0.50
elif 18 <= tuoi <= 25:
    gia_ve *= 0.80 

print(f"gia ve cuoi cung cua ban la: {gia_ve:,.0f} vnd")
"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
sodu = float(input("Số dư hiện tại: "))
sotien = float(input("Số tiền muốn rút: "))

if sotien > 0:
    if sotien <= sodu:
        if sotien % 50000 == 0:
            print("Rút tiền thành công!")
        else:
            print("Số tiền rút phải là bội số của 50,000")
    else:
        print("Không đủ số dư")
else:
    print("Số tiền rút phải lớn hơn 0")

# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
cc= float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))
BMI = can_nang / (cc ** 2)
print(f"BMI = {BMI:.1f}")
if BMI < 18.5:
    print("Thiếu cân — nên tăng cân hợp lý")
elif BMI < 25:
    print("Bình thường — tuyệt vời!")   
elif BMI < 30:
    print("Thừa cân — nên điều chỉnh chế độ ăn")
else:
    print("Béo phì — khuyến nghị gặp bác sĩ")

# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
loai_ve = input("Loại vé (thuong/vip): ").lower()
ngay = input("Ngày (thuong/cuoi_tuan): ").lower()
tuoi = int(input("Tuổi: "))

gia = 80000 if loai_ve == "thuong" else 120000
if ngay == "cuoi_tuan":
    gia *= 1.3
if tuoi < 12 or tuoi >= 65:
    gia *= 0.5
elif 18 <= tuoi <= 25:
    gia *= 0.8
print(f"Giá vé: {gia:,.0f} VNĐ")

"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
so_du = float(input("Nhập số dư hiện tại: "))
so_tien_rut = float(input("Nhập số tiền muốn rút: "))
if so_du > 0:
    if so_tien_rut <= so_du:
        if so_tien_rut % 50000 == 0:
            print("Rút tiền thành công")
        else:
            print("Số tiền rút phải là bội số của 50,000")
    else:
        print("Không đủ số dư")

# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))

bmi = can_nang / (chieu_cao ** 2)

print(f"BMI của bạn là: {bmi:.2f}")

if bmi < 18.5:
    print("Thiếu cân - Bạn nên tăng cân")
elif bmi < 25:
    print("Bình thường - Thể trạng tốt")
elif bmi < 30:
    print("Thừa cân - Nên chú ý cân nặng")
else:
    print("Béo phì - Nên tham khảo ý kiến bác sĩ")

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

if loai_ve == "thuong":
    gia = 80000
elif loai_ve == "vip":
    gia = 120000
else:
    gia = 0
    print("Loại vé không hợp lệ")

if gia > 0:
    if ngay == "cuoi_tuan":
        gia = gia * 1.3

    if tuoi < 12 or tuoi >= 65:
        gia = gia * 0.5
    elif 18 <= tuoi <= 25:
        gia = gia * 0.8

    print(f"Giá vé cuối cùng: {gia:.0f} đồng")
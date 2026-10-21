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

if so_tien_rut > 0:
    if so_tien_rut <= so_du:
        if so_tien_rut % 50000 == 0:
            print("Rút thành công.")
        else:
            print("Số tiền rút phải là bội số 50,000.")
    else:
        print("Số dư không đủ.")
else:
    print("Số tiền rút phải > 0.")         

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

if bmi < 18.5:
    print("Thiếu cân.")
elif 18.5 <= bmi <= 24.9:
    print("Bình thường.")
elif 25 <= bmi <= 29.9:
    print("Thừa cân.")
else:
    print("Béo phì.")


# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
loai_ve = input("Nhập loại vé (thuong/vip): ").lower()
ngay = input("Nhập ngày (thuong/cuoi_tuan): ").lower()  
tuoi = int(input("Nhập tuổi: "))

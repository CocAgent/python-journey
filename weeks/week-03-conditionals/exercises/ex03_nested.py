"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
so_du = float(input("Số dư hiện tại: "))
so_tien_rut = float(input("Số tiền muốn rút: "))
if so_tien_rut > 0:
    if so_tien_rut <= so_du:
        if so_tien_rut % 50000 == 0:
            so_du_moi = so_du - so_tien_rut
            print(f"Rút thành công. Số dư còn lại: {so_du_moi}")
        else:
            print("Số tiền phải là bội số của 50,000")
    else:
        print("Số dư không đủ")
else:
    print("Số tiền rút phải lớn hơn 0")


# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
height = float(input("Chiều cao (m): "))
weight = float(input("Cân nặng (kg): "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print(f"BMI = {bmi:.1f} → Thiếu cân. Gợi ý: tăng cân đều đặn.")
elif bmi < 25:
    print(f"BMI = {bmi:.1f} → Bình thường. Tốt lắm, giữ vậy!")
elif bmi < 30:
    print(f"BMI = {bmi:.1f} → Thừa cân. Cần chú ý ăn uống.")
else:
    print(f"BMI = {bmi:.1f} → Béo phì. Nên gặp bác sĩ chuyên khoa.")


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
if loai_ve == "vip":
    gia_ve = 120000
else:
    gia_ve = 80000
if ngay == "cuoi_tuan":
    gia_ve *= 1.3
if tuoi < 12 or tuoi >= 65:
    gia_ve *= 0.5
elif 18 <= tuoi <= 25:
    gia_ve *= 0.8
print(f"Giá vé cuối cùng: {gia_ve:.0f}k")

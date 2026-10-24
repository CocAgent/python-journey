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

if so_tien_rut <= 0:
    print("Số tiền không hợp lệ")
elif so_tien_rut > so_du:
    print("Không đủ số dư")
elif so_tien_rut % 50_000 != 0:
    print("Cần là bội số 50,000")
else:
    so_du -= so_tien_rut
    print(f"Rút tiền thành công: {so_tien_rut:,.0f} đ. Số dư còn lại: {so_du:,.0f} đ")


# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))

if chieu_cao <= 0 or can_nang <= 0:
    print("Chiều cao và cân nặng không hợp lệ")
else:
    bmi = can_nang / (chieu_cao ** 2)
    print(f"Chỉ số BMI: {bmi:.1f}")
    if bmi < 18.5:
        print("Xếp loại: Thiếu cân → Gợi ý: Bạn nên tăng cân.")
    elif bmi <= 24.9:
        print("Xếp loại: Bình thường → Khen: Thể trạng rất cân đối và khỏe mạnh!")
    elif bmi <= 29.9:
        print("Xếp loại: Thừa cân → Cảnh báo nhẹ: Nên kiểm soát chế độ ăn uống.")
    else:
        print("Xếp loại: Béo phì → Khuyến nghị: Bạn nên gặp bác sĩ để được tư vấn.")


# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
loai_ve = input("Loại vé (thuong/vip): ").strip().lower()
ngay = input("Ngày xem (thuong/cuoi_tuan): ").strip().lower()
tuoi = int(input("Nhập tuổi: "))

# 1. Giá cơ bản
if loai_ve == "vip":
    gia = 120_000
else:
    gia = 80_000

# 2. Phụ thu cuối tuần
if ngay == "cuoi_tuan":
    gia *= 1.3

# 3. Giảm giá theo độ tuổi
if tuoi < 12 or tuoi >= 65:
    gia *= 0.5
elif 18 <= tuoi <= 25:
    gia *= 0.8

gia_cuoi_cung = int(gia)
print(f"Giá vé cuối cùng: {gia_cuoi_cung:,.0f} đ")

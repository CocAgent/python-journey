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
    print("Số tiền rút phải lớn hơn 0")
elif so_tien_rut > so_du:
    print("Số dư không đủ để thực hiện giao dịch")
elif so_tien_rut % 50_000 != 0:
    print("Số tiền rút phải là bội số của 50,000")
else:
    so_du -= so_tien_rut
    print(f"Rút tiền thành công! Số dư còn lại: {so_du:,.0f} VNĐ")


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
    print("Chiều cao và cân nặng phải lớn hơn 0")
else:
    bmi = can_nang / (chieu_cao ** 2)
    print(f"Chỉ số BMI của bạn là: {bmi:.2f}")
    if bmi < 18.5:
        print("Thiếu cân → Bạn nên bổ sung dinh dưỡng để tăng cân.")
    elif bmi <= 24.9:
        print("Bình thường → Tuyệt vời, hãy tiếp tục duy trì thể trạng này!")
    elif bmi <= 29.9:
        print("Thừa cân → Cảnh báo nhẹ: nên chú ý chế độ ăn uống và vận động.")
    else:
        print("Béo phì → Khuyến nghị nên thăm khám bác sĩ hoặc chuyên gia dinh dưỡng.")


# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
loai_ve = input("Loại vé (thuong/vip): ").strip().lower()
ngay = input("Ngày (thuong/cuoi_tuan): ").strip().lower()
tuoi = int(input("Nhập tuổi: "))

gia_co_ban = 120_000 if loai_ve == "vip" else 80_000

# Cuối tuần: +30%
if ngay == "cuoi_tuan":
    gia_sau_ngay = gia_co_ban * 1.3
else:
    gia_sau_ngay = gia_co_ban

# Giảm giá theo độ tuổi
if tuoi < 12 or tuoi >= 65:
    gia_ve_cuoi = gia_sau_ngay * 0.5
elif 18 <= tuoi <= 25:
    gia_ve_cuoi = gia_sau_ngay * 0.8
else:
    gia_ve_cuoi = gia_sau_ngay

print(f"Giá vé cuối cùng: {int(gia_ve_cuoi):,} VNĐ")

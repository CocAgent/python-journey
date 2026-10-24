"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
so_du = float(input("Nhập số dư hiện tại (VNĐ): "))
so_tien_rut = float(input("Nhập số tiền muốn rút (VNĐ): "))

if so_tien_rut <= 0:
    print("Giao dịch thất bại: Số tiền rút phải lớn hơn 0.")
elif so_tien_rut > so_du:
    print("Giao dịch thất bại: Số dư tài khoản không đủ.")
elif so_tien_rut % 50_000 != 0:
    print("Giao dịch thất bại: Số tiền rút phải là bội số của 50,000 VNĐ.")
else:
    so_du -= so_tien_rut
    print(f"Rút tiền thành công! Số dư còn lại: {int(so_du):,} VNĐ")


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
    print("Chiều cao và cân nặng phải là số dương hợp lệ!")
else:
    bmi = can_nang / (chieu_cao ** 2)
    print(f"Chỉ số BMI của bạn: {bmi:.2f}")

    if bmi < 18.5:
        print("Xếp loại: Thiếu cân → Gợi ý: Bạn nên tăng cường dinh dưỡng để tăng cân.")
    elif bmi <= 24.9:
        print("Xếp loại: Bình thường → Khen: Thể trạng rất cân đối, hãy tiếp tục duy trì!")
    elif bmi <= 29.9:
        print("Xếp loại: Thừa cân → Cảnh báo: Bạn nên chú ý chế độ ăn và vận động nhẹ.")
    else:
        print("Xếp loại: Béo phì → Khuyến nghị: Bạn nên thăm khám bác sĩ hoặc chuyên gia dinh dưỡng.")


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

# 1. Xác định giá cơ bản
if loai_ve == "vip":
    gia = 120_000
else:
    gia = 80_000

# 2. Phụ thu ngày cuối tuần (+30%)
if ngay == "cuoi_tuan":
    gia *= 1.3

# 3. Ưu đãi theo độ tuổi
if tuoi < 12 or tuoi >= 65:
    gia *= 0.5  # Giảm 50%
elif 18 <= tuoi <= 25:
    gia *= 0.8  # Giảm 20%

print(f"Giá vé cuối cùng: {int(gia):,} VNĐ")

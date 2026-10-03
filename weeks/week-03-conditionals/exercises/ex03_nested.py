"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
print("--- TODO 1: ATM rút tiền ---")
so_du = float(input("Nhập số dư hiện tại (VNĐ): "))
so_tien_rut = float(input("Nhập số tiền muốn rút (VNĐ): "))

if so_tien_rut > 0:
    if so_tien_rut % 50000 == 0:
        if so_tien_rut <= so_du:
            so_du -= so_tien_rut
            print(f"Rút tiền thành công: {so_tien_rut:,.0f} VNĐ. Số dư còn lại: {so_du:,.0f} VNĐ.")
        else:
            print("Giao dịch thất bại: Số dư không đủ để thực hiện giao dịch.")
    else:
        print("Giao dịch thất bại: Số tiền rút phải là bội số của 50,000 VNĐ.")
else:
    print("Giao dịch thất bại: Số tiền rút phải lớn hơn 0.")


# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
print("\n--- TODO 2: Xếp loại BMI ---")
chieu_cao = float(input("Nhập chiều cao (m, ví dụ 1.70): "))
can_nang = float(input("Nhập cân nặng (kg, ví dụ 65): "))

if chieu_cao > 0 and can_nang > 0:
    bmi = can_nang / (chieu_cao ** 2)
    print(f"Chỉ số BMI: {bmi:.2f}")
    if bmi < 18.5:
        print("Thiếu cân: Bạn nên bổ sung dinh dưỡng và tập luyện để tăng cân.")
    elif bmi <= 24.9:
        print("Bình thường: Thân hình rất cân đối, hãy tiếp tục duy trì nhé! 🎉")
    elif bmi <= 29.9:
        print("Thừa cân: Cảnh báo nhẹ, nên kiểm soát calo và tăng cường vận động.")
    else:
        print("Béo phì: Khuyến nghị bạn nên thăm khám bác sĩ hoặc chuyên gia dinh dưỡng.")
else:
    print("Chiều cao và cân nặng phải là số dương hợp lệ.")


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

gia = 120_000 if loai_ve == "vip" else 80_000

if ngay == "cuoi_tuan":
    gia = gia * 1.3

if tuoi < 12 or tuoi >= 65:
    gia = gia * 0.5
elif 18 <= tuoi <= 25:
    gia = gia * 0.8

print(f"Giá vé cuối cùng: {int(gia):,} VNĐ")
print("\n--- TODO 3: Máy bán vé xem phim ---")
loai_ve = input("Loại vé (thuong/vip): ").strip().lower()
ngay = input("Ngày (thuong/cuoi_tuan): ").strip().lower()
tuoi = int(input("Nhập tuổi: "))

# Xác định giá cơ bản
if loai_ve == "vip":
    gia = 120000
else:
    gia = 80000

# Phụ thu cuối tuần (+30%)
if ngay == "cuoi_tuan":
    gia = gia * 1.3

# Giảm giá theo độ tuổi
if tuoi < 12 or tuoi >= 65:
    gia = gia * 0.5
    print("Ưu đãi: Giảm 50% (Trẻ em / Người cao tuổi)")
elif 18 <= tuoi <= 25:
    gia = gia * 0.8
    print("Ưu đãi: Giảm 20% (Sinh viên)")
else:
    print("Ưu đãi: Không giảm giá")

print(f"Giá vé cuối cùng: {gia:,.0f} VNĐ")

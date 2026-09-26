"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
print("--- 1. ATM rút tiền ---")
so_du = float(input("Nhập số dư hiện tại (VNĐ): "))
so_tien_rut = float(input("Nhập số tiền muốn rút (VNĐ): "))

if so_tien_rut <= 0:
    print("Lỗi: Số tiền rút không hợp lệ (phải lớn hơn 0)")
elif so_tien_rut > so_du:
    print("Lỗi: Số dư không đủ để thực hiện giao dịch")
elif so_tien_rut % 50_000 != 0:
    print("Lỗi: Số tiền rút cần là bội số của 50,000 VNĐ")
else:
    so_du -= so_tien_rut
    print(f"Rút tiền thành công: {so_tien_rut:,.0f} VNĐ")
    print(f"Số dư còn lại: {so_du:,.0f} VNĐ")


# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
print("\n--- 2. Xếp loại chỉ số BMI ---")
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))

if chieu_cao <= 0 or can_nang <= 0:
    print("Chiều cao và cân nặng phải lớn hơn 0")
else:
    bmi = can_nang / (chieu_cao ** 2)
    print(f"Chỉ số BMI của bạn: {bmi:.2f}")
    if bmi < 18.5:
        print("Xếp loại: Thiếu cân → Gợi ý: Bạn nên bổ sung dinh dưỡng và ăn uống điều độ để tăng cân.")
    elif bmi <= 24.9:
        print("Xếp loại: Bình thường → Rất tốt! Cơ thể bạn đang ở trạng thái cân đối.")
    elif bmi <= 29.9:
        print("Xếp loại: Thừa cân → Cảnh báo nhẹ: Bạn nên kiểm soát chế độ ăn và tập thể dục thường xuyên.")
    else:
        print("Xếp loại: Béo phì → Khuyến nghị: Bạn nên gặp bác sĩ hoặc chuyên gia dinh dưỡng để được tư vấn.")


# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
print("\n--- 3. Máy bán vé xem phim ---")
loai_ve = input("Loại vé (thuong/vip): ").strip().lower()
ngay = input("Ngày xem (thuong/cuoi_tuan): ").strip().lower()
tuoi = int(input("Nhập tuổi của bạn: "))

# Xác định giá cơ bản
gia_ve = 120_000 if loai_ve == "vip" else 80_000

# Phụ thu cuối tuần (+30%)
if ngay == "cuoi_tuan":
    gia_ve *= 1.3

# Áp dụng giảm giá theo đối tượng
if tuoi < 12 or tuoi >= 65:
    gia_ve *= 0.5
    print("Ưu đãi áp dụng: Giảm 50% (Trẻ em / Người cao tuổi)")
elif 18 <= tuoi <= 25:
    gia_ve *= 0.8
    print("Ưu đãi áp dụng: Giảm 20% (Sinh viên)")
else:
    print("Ưu đãi áp dụng: Giá tiêu chuẩn")

gia_ve_cuoi = int(gia_ve)
print(f"Giá vé cuối cùng: {gia_ve_cuoi:,.0f} VNĐ")

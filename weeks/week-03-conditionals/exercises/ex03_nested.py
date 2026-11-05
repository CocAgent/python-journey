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
    print("Số tiền rút không hợp lệ (phải lớn hơn 0)")
elif so_tien_rut % 50000 != 0:
    print("Số tiền rút phải là bội số của 50,000 VNĐ")
elif so_tien_rut > so_du:
    print("Số dư trong tài khoản không đủ")
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

bmi = can_nang / (chieu_cao ** 2)
print(f"Chỉ số BMI của bạn: {bmi:.1f}")

if bmi < 18.5:
    print("Thiếu cân → Bạn nên ăn uống bồi bổ để tăng cân nhé!")
elif bmi <= 24.9:
    print("Bình thường → Tuyệt vời! Bạn có thân hình rất cân đối.")
elif bmi <= 29.9:
    print("Thừa cân → Bạn nên chú ý ăn uống lành mạnh và tập luyện nhẹ nhàng.")
else:
    print("Béo phì → Khuyến nghị bạn nên tham khảo ý kiến bác sĩ hoặc chuyên gia dinh dưỡng.")


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

# 2. Phụ thu cuối tuần (+30%)
if ngay == "cuoi_tuan":
    gia *= 1.3

# 3. Giảm giá theo tuổi
if tuoi < 12 or tuoi >= 65:
    gia *= 0.5   # Giảm 50%
elif 18 <= tuoi <= 25:
    gia *= 0.8   # Giảm 20%

print(f"Giá vé cuối cùng: {int(gia):,} VNĐ")

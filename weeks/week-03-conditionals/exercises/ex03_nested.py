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
    print("Lỗi: Số tiền rút phải lớn hơn 0!")
else:
    if so_tien_rut > so_du:
        print("Lỗi: Số dư không đủ!")
    else:
        if so_tien_rut % 50_000 != 0:
            print("Lỗi: Số tiền rút phải là bội số của 50,000!")
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
print(f"Chỉ số BMI: {bmi:.1f}")

if bmi < 18.5:
    print("Xếp loại: Thiếu cân → Bạn nên bổ sung thêm dinh dưỡng để tăng cân nhé!")
elif bmi < 25:
    print("Xếp loại: Bình thường → Tuyệt vời, vóc dáng rất cân đối!")
elif bmi < 30:
    print("Xếp loại: Thừa cân → Chú ý điều chỉnh khẩu phần ăn và tăng cường vận động!")
else:
    print("Xếp loại: Béo phì → Khuyến nghị nên thăm khám hoặc gặp bác sĩ tư vấn!")


# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
loai_ve = input("Loại vé (thuong/vip): ").strip().lower()
ngay = input("Ngày xem (thuong/cuoi_tuan): ").strip().lower()
tuoi = int(input("Tuổi: "))

# 1. Xác định giá cơ bản
if loai_ve == "vip":
    gia_ve = 120_000
else:
    gia_ve = 80_000

# 2. Phụ thu cuối tuần (+30%)
if ngay == "cuoi_tuan":
    gia_ve *= 1.3

# 3. Giảm giá theo độ tuổi
if tuoi < 12 or tuoi >= 65:
    gia_ve *= 0.5
elif 18 <= tuoi <= 25:
    gia_ve *= 0.8

# 4. In giá vé cuối cùng
print(f"Giá vé cuối cùng: {gia_ve:,.0f} VNĐ")


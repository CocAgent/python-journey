"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
print("=== TODO 1: ATM rút tiền ===")
so_du = int(input("Nhập số dư hiện tại (VNĐ): "))
so_tien_rut = int(input("Nhập số tiền muốn rút (VNĐ): "))

if so_tien_rut <= 0:
    print("Lỗi: Số tiền rút phải lớn hơn 0.")
else:
    if so_tien_rut % 50_000 != 0:
        print("Lỗi: Số tiền rút phải là bội số của 50,000 VNĐ.")
    else:
        if so_tien_rut > so_du:
            print("Lỗi: Số dư không đủ để thực hiện giao dịch.")
        else:
            so_du -= so_tien_rut
            print(f"Rút thành công {so_tien_rut:,} VNĐ! Số dư còn lại: {so_du:,} VNĐ.")


# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
print("\n=== TODO 2: Xếp loại BMI ===")
chieu_cao = float(input("Nhập chiều cao (m, ví dụ 1.70): "))
can_nang = float(input("Nhập cân nặng (kg, ví dụ 65): "))

if chieu_cao <= 0 or can_nang <= 0:
    print("Lỗi: Chiều cao và cân nặng phải lớn hơn 0.")
else:
    bmi = can_nang / (chieu_cao ** 2)
    print(f"Chỉ số BMI của bạn là: {bmi:.1f}")
    if bmi < 18.5:
        print("Phân loại: Thiếu cân -> Bạn nên ăn uống đủ chất và tập luyện để tăng cân.")
    elif bmi < 25:
        print("Phân loại: Bình thường -> Tuyệt vời! Hãy tiếp tục duy trì lối sống lành mạnh.")
    elif bmi < 30:
        print("Phân loại: Thừa cân -> Lưu ý điều chỉnh chế độ ăn và vận động nhiều hơn nhé.")
    else:
        print("Phân loại: Béo phì -> Khuyến nghị gặp bác sĩ để được tư vấn sức khỏe phù hợp.")


# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
print("\n=== TODO 3: Máy bán vé xem phim ===")
loai_ve = input("Nhập loại vé (thuong/vip): ").strip().lower()
ngay = input("Nhập loại ngày (thuong/cuoi_tuan): ").strip().lower()
tuoi = int(input("Nhập tuổi khách hàng: "))

if loai_ve not in ("thuong", "vip"):
    print("Lỗi: Loại vé chỉ chấp nhận 'thuong' hoặc 'vip'.")
elif ngay not in ("thuong", "cuoi_tuan"):
    print("Lỗi: Loại ngày chỉ chấp nhận 'thuong' hoặc 'cuoi_tuan'.")
elif tuoi < 0:
    print("Lỗi: Tuổi không hợp lệ.")
else:
    gia_ve = 80_000 if loai_ve == "thuong" else 120_000

    if ngay == "cuoi_tuan":
        gia_ve *= 1.3

    if tuoi < 12 or tuoi >= 65:
        gia_ve *= 0.5
        uu_dai = "Giảm 50% (Trẻ em / Người cao tuổi)"
    elif 18 <= tuoi <= 25:
        gia_ve *= 0.8
        uu_dai = "Giảm 20% (Sinh viên)"
    else:
        uu_dai = "Không áp dụng giảm giá"

    print(f"Ưu đãi: {uu_dai}")
    print(f"Giá vé cuối cùng: {gia_ve:,.0f} VNĐ")

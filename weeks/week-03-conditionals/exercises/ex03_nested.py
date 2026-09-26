"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp

so_du = int(input("Số dư hiện tại (VND): "))
so_tien_rut = int(input("Số tiền muốn rút (VND): "))

if so_tien_rut <= 0:
    print("❌ Số tiền rút phải lớn hơn 0.")
else:
    if so_tien_rut > so_du:
        print("❌ Số dư không đủ để rút.")
    else:
        if so_tien_rut % 50_000 != 0:
            print("❌ Số tiền rút phải là bội số của 50,000 VND.")
        else:
            so_du -= so_tien_rut
            print(f"✅ Rút tiền thành công! Số dư còn lại: {so_du:,} VND")


# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ

chieu_cao = float(input("Chiều cao (m): "))
can_nang = float(input("Cân nặng (kg): "))

bmi = can_nang / (chieu_cao ** 2)
print(f"BMI của bạn: {bmi:.1f}")

if bmi < 18.5:
    print("📉 Thiếu cân — Bạn nên bổ sung dinh dưỡng và tăng cân.")
elif bmi < 25:
    print("✅ Bình thường — Cân nặng của bạn rất lý tưởng, hãy duy trì!")
elif bmi < 30:
    print("⚠️  Thừa cân — Bạn nên chú ý chế độ ăn uống và tập luyện thêm.")
else:
    print("🚨 Béo phì — Hãy gặp bác sĩ để được tư vấn sức khỏe.")


# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng

loai_ve = input("Loại vé (thuong/vip): ").strip().lower()
ngay = input("Ngày đi (thuong/cuoi_tuan): ").strip().lower()
tuoi_kh = int(input("Tuổi khách hàng: "))

# Giá cơ bản
if loai_ve == "vip":
    gia = 120_000
else:
    gia = 80_000

# Phụ thu cuối tuần
if ngay == "cuoi_tuan":
    gia = gia * 1.3

# Chiết khấu theo tuổi
if tuoi_kh < 12 or tuoi_kh >= 65:
    gia = gia * 0.5
    ghi_chu = "(giảm 50% — trẻ em/người cao tuổi)"
elif 18 <= tuoi_kh <= 25:
    gia = gia * 0.8
    ghi_chu = "(giảm 20% — sinh viên)"
else:
    ghi_chu = ""

print(f"🎬 Giá vé cuối cùng: {gia:,.0f} VND {ghi_chu}")

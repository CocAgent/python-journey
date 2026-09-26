"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# =============================================================
# TODO 1: ATM rút tiền
# Ý tưởng: Mô phỏng máy ATM — kiểm tra 3 tầng lồng nhau:
#   Tầng 1: Số tiền rút có hợp lệ không? (> 0)
#   Tầng 2: Có phải bội số 50,000 không?  (ATM chỉ nhả tờ 50k)
#   Tầng 3: Tài khoản có đủ tiền không?
# Nếu vượt qua cả 3 tầng → rút tiền thành công
# =============================================================

print("--- ATM Rút Tiền ---")
so_du = float(input("Số dư tài khoản (VNĐ): "))
rut   = float(input("Số tiền muốn rút (VNĐ): "))

if rut <= 0:
    # Tầng 1: Kiểm tra số tiền nhập vào có ý nghĩa không
    print("❌ Số tiền rút phải lớn hơn 0!")
else:
    if rut % 50_000 != 0:
        # Tầng 2: % là phép lấy phần dư — nếu dư khác 0 → không chia hết
        # 50_000 → dấu _ chỉ để dễ đọc, Python bỏ qua nó (= 50000)
        print("❌ Số tiền rút phải là bội số của 50,000 VNĐ!")
    else:
        if rut > so_du:
            # Tầng 3: Không được rút nhiều hơn số dư
            # :,.0f → định dạng số: dấu phẩy phân cách nghìn, không thập phân
            print(f"❌ Số dư không đủ! Bạn chỉ có {so_du:,.0f} VNĐ.")
        else:
            so_du -= rut    # -= là viết tắt: so_du = so_du - rut
            print(f"✅ Rút tiền thành công! {rut:,.0f} VNĐ")
            print(f"💰 Số dư còn lại: {so_du:,.0f} VNĐ")


# =============================================================
# TODO 2: Xếp loại BMI
# Ý tưởng: Tính chỉ số BMI từ chiều cao và cân nặng,
#          rồi phân loại sức khỏe theo 4 mức
# Công thức: BMI = cân nặng (kg) ÷ chiều cao² (m²)
#   Ví dụ: 60kg, 1.70m → BMI = 60 / (1.70 × 1.70) ≈ 20.8
# =============================================================

print("\n--- Chỉ số BMI ---")
chieu_cao = float(input("Chiều cao (m, ví dụ 1.70): "))
can_nang  = float(input("Cân nặng (kg): "))

bmi = can_nang / (chieu_cao ** 2)
# ** là toán tử lũy thừa: chieu_cao ** 2 = chieu_cao × chieu_cao
# :.2f → hiển thị 2 chữ số sau dấu phẩy (vd: 20.76)
print(f"BMI của bạn: {bmi:.2f}")

if bmi < 18.5:
    print("⚠️  Thiếu cân — Bạn nên ăn uống đầy đủ và tập thể dục để tăng cân.")
elif bmi < 25:
    # elif = "else if" = nếu điều kiện trước sai, thử điều kiện này
    print("✅ Bình thường — Cơ thể bạn đang ở trạng thái lý tưởng, hãy duy trì nhé!")
elif bmi < 30:
    print("⚠️  Thừa cân — Bạn nên chú ý chế độ ăn và vận động nhiều hơn.")
else:
    # else = "còn lại" = khi tất cả điều kiện trên đều sai (BMI >= 30)
    print("🚨 Béo phì — Bạn nên gặp bác sĩ để được tư vấn sức khỏe!")


# =============================================================
# TODO 3: Máy bán vé xem phim
# Ý tưởng: Tính giá vé theo 3 bước (theo thứ tự):
#   Bước 1: Chọn loại vé (thường 80k / VIP 120k)
#   Bước 2: Có phụ phí cuối tuần không? (+30%)
#   Bước 3: Khách có được giảm giá theo tuổi không?
#            - Trẻ em (<12) và người cao tuổi (>=65): -50%
#            - Sinh viên (18-25): -20%
# =============================================================

print("\n--- Máy Bán Vé Xem Phim ---")
loai_ve  = input("Loại vé (thuong/vip): ").strip().lower()
# .strip() → xóa khoảng trắng thừa ở đầu/cuối nếu người dùng lỡ bấm space
# .lower() → chuyển thành chữ thường (VIP hay vip đều được chấp nhận)
ngay     = input("Ngày chiếu (thuong/cuoi_tuan): ").strip().lower()
tuoi_kh  = int(input("Tuổi khách hàng: "))

# --- Bước 1: Giá cơ bản ---
if loai_ve == "vip":
    gia = 120_000           # VIP: 120,000 VNĐ
else:
    gia = 80_000            # Thường: 80,000 VNĐ (mặc định nếu không phải VIP)

# --- Bước 2: Phụ phí cuối tuần ---
if ngay == "cuoi_tuan":
    gia = gia * 1.3         # Nhân 1.3 = tăng thêm 30%
    # Ví dụ: 80,000 × 1.3 = 104,000

# --- Bước 3: Giảm giá theo tuổi ---
if tuoi_kh < 12 or tuoi_kh >= 65:
    # "or" = HOẶC — một trong hai điều kiện đúng là đủ
    gia  = gia * 0.5        # Nhân 0.5 = giảm còn 50%
    giam = "Trẻ em / Người cao tuổi (-50%)"
elif 18 <= tuoi_kh <= 25:
    # Cú pháp đặc biệt của Python: so sánh chuỗi (18 ≤ tuổi ≤ 25)
    gia  = gia * 0.8        # Nhân 0.8 = giảm còn 80% (tức giảm 20%)
    giam = "Sinh viên (-20%)"
else:
    giam = "Không có"       # Tuổi khác không được giảm

# --- In hóa đơn ---
print(f"\n🎬 Loại vé   : {'VIP' if loai_ve == 'vip' else 'Thường'}")
# Dòng trên dùng "ternary" (điều kiện 1 dòng): giá_trị_nếu_đúng if điều_kiện else giá_trị_nếu_sai
print(f"📅 Ngày chiếu: {'Cuối tuần (+30%)' if ngay == 'cuoi_tuan' else 'Ngày thường'}")
print(f"🎁 Giảm giá  : {giam}")
print(f"💵 Giá vé    : {gia:,.0f} VNĐ")
# :,.0f → hiển thị số có dấu phẩy phân cách nghìn, không có số thập phân

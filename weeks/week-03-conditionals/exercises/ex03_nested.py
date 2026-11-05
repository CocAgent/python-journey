"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
balance = float(input("Nhập số dư hiện tại: "))
amount = float(input("Nhập số tiền muốn rút: "))

if amount <= 0:
    print("Số tiền rút không hợp lệ (phải > 0)")
elif amount > balance:
    print("Không đủ số dư để rút")
elif amount % 50_000 != 0:
    print("Số tiền rút phải là bội số của 50,000")
else:
    balance -= amount
    print(f"Rút tiền thành công! Số dư còn lại: {balance:,.0f} VND")


# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
height = float(input("Nhập chiều cao (m): "))
weight = float(input("Nhập cân nặng (kg): "))

if height <= 0 or weight <= 0:
    print("Chiều cao và cân nặng phải lớn hơn 0")
else:
    bmi = weight / (height ** 2)
    print(f"Chỉ số BMI của bạn là: {bmi:.2f}")
    if bmi < 18.5:
        print("Thiếu cân → Bạn nên ăn uống bồi bổ thêm để tăng cân nhé!")
    elif bmi < 25:
        print("Bình thường → Tuyệt vời, hãy duy trì thể trạng này!")
    elif bmi < 30:
        print("Thừa cân → Cần chú ý chế độ ăn và tập thể dục điều độ!")
    else:
        print("Béo phì → Khuyến nghị nên đi khám bác sĩ hoặc chuyên gia dinh dưỡng!")


# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
ticket_type = input("Loại vé (thuong/vip): ").strip().lower()
day_type = input("Ngày (thuong/cuoi_tuan): ").strip().lower()
age = int(input("Nhập tuổi: "))

# 1. Giá vé cơ bản
if ticket_type == "vip":
    price = 120_000
else:
    price = 80_000

# 2. Phụ thu cuối tuần (+30%)
if day_type == "cuoi_tuan":
    price *= 1.3

# 3. Giảm giá theo đối tượng tuổi
if age < 12 or age >= 65:
    price *= 0.5
elif 18 <= age <= 25:
    price *= 0.8

print(f"Giá vé cuối cùng: {int(price):,} VND")

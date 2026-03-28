"""Lời giải Bài tập 03: Điều kiện lồng nhau"""

# TODO 1
so_du = float(input("Số dư hiện tại: "))
so_tien = float(input("Số tiền muốn rút: "))
if so_tien <= 0:
    print("Số tiền phải lớn hơn 0")
elif so_tien > so_du:
    print("Không đủ số dư")
elif so_tien % 50000 != 0:
    print("Số tiền phải là bội số của 50,000")
else:
    so_du -= so_tien
    print(f"Rút thành công! Số dư còn: {so_du:,.0f} VNĐ")

# TODO 2
h = float(input("Chiều cao (m): "))
w = float(input("Cân nặng (kg): "))
bmi = w / (h ** 2)
print(f"BMI = {bmi:.1f}")
if bmi < 18.5:
    print("Thiếu cân — nên tăng cân hợp lý")
elif bmi < 25:
    print("Bình thường — tuyệt vời!")
elif bmi < 30:
    print("Thừa cân — nên điều chỉnh chế độ ăn")
else:
    print("Béo phì — khuyến nghị gặp bác sĩ")

# TODO 3
loai_ve = input("Loại vé (thuong/vip): ").lower()
ngay = input("Ngày (thuong/cuoi_tuan): ").lower()
tuoi = int(input("Tuổi: "))

gia = 80000 if loai_ve == "thuong" else 120000
if ngay == "cuoi_tuan":
    gia *= 1.3
if tuoi < 12 or tuoi >= 65:
    gia *= 0.5
elif 18 <= tuoi <= 25:
    gia *= 0.8
print(f"Giá vé: {gia:,.0f} VNĐ")

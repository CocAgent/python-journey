"""Lời giải Bài tập 03: Máy tính nhận input"""

# TODO 1
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
print(f"Tổng: {a + b}")
print(f"Hiệu: {a - b}")
print(f"Tích: {a * b}")
if b != 0:
    print(f"Thương: {a / b:.2f}")
else:
    print("Không thể chia cho 0!")

# TODO 2
r = float(input("Nhập bán kính: "))
pi = 3.14159
print(f"Diện tích: {pi * r**2:.2f}")
print(f"Chu vi: {2 * pi * r:.2f}")

# TODO 3
gia_goc = float(input("Giá gốc: "))
giam = float(input("Phần trăm giảm: "))
gia_moi = gia_goc * (1 - giam / 100)
print(f"Giá sau giảm: {gia_moi:,.0f} VNĐ")

# TODO 4
vnd = float(input("Số tiền VNĐ: "))
ty_gia = float(input("Tỷ giá USD/VNĐ: "))
usd = vnd / ty_gia
print(f"{vnd:,.0f} VNĐ = {usd:.2f} USD")

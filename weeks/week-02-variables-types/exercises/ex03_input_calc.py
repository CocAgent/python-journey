"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))
print(f"Tổng: {num1 + num2}")
print(f"Hiệu: {num1 - num2}")
print(f"Tích: {num1 * num2}")
if num2 != 0:
    print(f"Thương: {num1 / num2:.2f}")
else:
    print("Lỗi: Không thể chia cho 0")

# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
r = float(input("\nNhập bán kính hình tròn: "))
pi = 3.14159
dien_tich = pi * r**2
chu_vi = 2 * pi * r
print(f"Diện tích hình tròn: {dien_tich:.2f}")
print(f"Chu vi hình tròn: {chu_vi:.2f}")

# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("\nNhập giá gốc: "))
phan_tram_giam = float(input("Nhập phần trăm giảm giá (%): "))
gia_sau_giam = gia_goc * (1 - phan_tram_giam / 100)
# Sử dụng format :,.0f để hiển thị dấu phẩy ngăn cách hàng nghìn cho đẹp
print(f"Giá sau khi giảm {phan_tram_giam}%: {gia_sau_giam:,.0f} VNĐ")

# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
vnd = float(input("\nNhập số tiền VNĐ muốn đổi: "))
ty_gia = float(input("Nhập tỷ giá USD/VNĐ hiện tại: "))
usd = vnd / ty_gia
print(f"{vnd:,.0f} VNĐ đổi được: {usd:.2f} USD")

print("\n🎉 Tuyệt vời! Bạn đã hoàn thành các bài tập tính toán với input!")

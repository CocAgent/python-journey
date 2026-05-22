"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
so1=float(input("nhap so thu nhat: "))
so2=float(input("nhap so thu hai: "))
print(f"Tổng: {so1} + {so2} = {so1 + so2}")
print(f"Hiệu: {so1} - {so2} = {so1 - so2}")
print(f"Tích: {so1} * {so2} = {so1 * so2}")
if so2 != 0:
    print(f"Thương: {so1} / {so2} = {so1 / so2}")                   

# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
bk = float(input("nhap ban kinh hinh tron:"))
pi = 3.14159
dien_tich = pi * bk ** 2        
chu_vi = 2 * pi * bk
print(f"Dien tich hinh tron: {dien_tich:.2f}")
print(f"Chu vi hinh tron: {chu_vi:.2f}")


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("Nhập giá gốc: "))
giam_gia = float(input("Nhập % giảm giá: "))
gia_sau_giam = gia_goc * (1 - giam_gia / 100)

# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
vnd = float(input("Nhập số tiền VNĐ: "))
ty_gia = float(input("Nhập tỷ giá USD/VNĐ: "))  
usd = vnd / ty_gia
print(f"{vnd:,.0f} VNĐ = {usd:.2f} USD")
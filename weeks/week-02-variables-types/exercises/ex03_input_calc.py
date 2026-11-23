
"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng
# In ra tổng, hiệu, tích, thương
print("TODO 1: May tinh co ban")

a = float(input("Nhap so thu nhat: "))
b = float(input("Nhap so thu hai: "))

print(f"Tong: {a + b}")
print(f"Hieu: {a - b}")
print(f"Tich: {a * b}")

if b != 0:
    print(f"Thuong: {(a / b):.2f}")
else:
    print("Khong the chia cho 0!")
print()


# TODO 2: Tính diện tích và chu vi hình tròn
# Dùng pi = 3.14159
print("TODO 2: Tinh dien tich va chu vi hinh tron")

pi = 3.14159
bankinh = float(input("Nhap ban kinh hinh tron: "))

dientich = pi * bankinh ** 2
chuvi = 2 * pi * bankinh

print(f"Dien tich: {dientich:.2f}")
print(f"Chu vi: {chuvi:.2f}")
print()


# TODO 3: Tính giá sau khi giảm
print("TODO 3: Tinh gia sau khi giam")

giagoc = float(input("Nhap gia goc (VND): "))
phantram = float(input("Nhap phan tram giam gia: "))

sotiengiam = giagoc * phantram / 100
giasaugiam = giagoc - sotiengiam

print(f"So tien duoc giam: {sotiengiam:.2f} VND")
print(f"Gia sau khi giam: {giasaugiam:.2f} VND")
print()


# TODO 4 (Thử thách): Máy đổi tiền
print("TODO 4: Doi tien VND sang USD")

vnd = float(input("Nhap so tien VND: "))
tygia = float(input("Nhap ty gia USD/VND: "))

if tygia > 0:
    usd = vnd / tygia
    print(f"So tien USD: {usd:.2f} USD")
else:
    print("Ty gia phai lon hon 0!")

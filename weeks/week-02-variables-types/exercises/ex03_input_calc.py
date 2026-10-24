"""
Bai tap 03: May tinh nhan input
====================================
Muc tieu: Ket hop input() voi tinh toan
"""

# TODO 1: Nhap 2 so tu nguoi dung, in ra tong, hieu, tich, thuong
a = float(input("Nhap so thu nhat: "))
b = float(input("Nhap so thu hai: "))
print(f"Tong:   {a} + {b} = {a + b}")
print(f"Hieu:   {a} - {b} = {a - b}")
print(f"Tich:   {a} x {b} = {a * b}")
print(f"Thuong: {a} / {b} = {a / b:.2f}")   # chia co the ra so thap phan


# TODO 2: Nhap ban kinh hinh tron, tinh va in:
# - Dien tich = pi x r^2
# - Chu vi    = 2 x pi x r
pi = 3.14159
r = float(input("Nhap ban kinh hinh tron: "))
dien_tich = pi * r ** 2
chu_vi = 2 * pi * r
print(f"Dien tich: {dien_tich:.2f}")
print(f"Chu vi:    {chu_vi:.2f}")


# TODO 3: Nhap gia goc va % giam gia
# Tinh va in gia sau khi giam
# Vi du: Gia goc 500000, giam 20% -> 400000
gia_goc = float(input("Nhap gia goc: "))
phan_tram = float(input("Nhap % giam gia: "))
so_tien_giam = gia_goc * phan_tram / 100
gia_sau_giam = gia_goc - so_tien_giam
print(f"Giam:         {so_tien_giam:,.0f}")
print(f"Gia sau giam: {gia_sau_giam:,.0f}")   # :, de them dau phan cach hang nghin


# TODO 4 (Thu thach): May doi tien
# Nhap so tien VND, ty gia USD/VND
# In ra so USD tuong ung (lam tron 2 chu so)
vnd = float(input("Nhap so tien VND: "))
ty_gia = float(input("Nhap ty gia (1 USD = ? VND): "))
usd = vnd / ty_gia
print(f"{vnd:,.0f} VND = {usd:.2f} USD")

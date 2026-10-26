"""Starter for the Week 03 Decision Ticket."""

name = input("Ten: ")
tuoi = (input("Tuoi: "))
loai_ve = input("Loai ve (thuong/vip): ")
if not name:
    print("Ten khong duoc de trong")
elif not tuoi.isdigit():
    print("Tuoi phai la so nguyen")
else:
    tuoi_int = int(tuoi)
    if tuoi_int < 0 and tuoi_int > 120 and loai_ve not in ["thuong", "vip"]:
        print("Input khong hop le")
    elif tuoi_int < 12:
        print(f"{name}: ve tre em")
    elif loai_ve == "vip":
        print(f"{name}: ve vip")
    else:
        print(f"{name}: ve standard")

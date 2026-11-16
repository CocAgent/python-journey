"""Starter for the Week 03 Decision Ticket."""

name = input("Tên: ").strip()
age_text = input("Tuổi: ").strip()
ticket_type = input("Loại vé (standard/vip): ").strip().lower()

if not name:
    print("Tên không được rỗng")
elif not age_text.isdigit():
    print("Tuổi cần là số nguyên không âm")
else:
    age = int(age_text)
    if age > 120 or ticket_type not in ("standard", "vip"):
        print("Input không hợp lệ")
    elif age < 12:
        print(f"{name}: vé trẻ em")
    elif ticket_type == "vip":
        print(f"{name}: vé VIP")
    else:
        print(f"{name}: vé standard")

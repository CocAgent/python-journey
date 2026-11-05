"""Lời giải 02 — kết hợp and/not, không dùng bool("n")."""

age_text = input("Tuổi: ").strip()
ticket_text = input("Có vé (y/n): ").strip().lower()
closed_text = input("Cửa đóng (y/n): ").strip().lower()

if (
    not age_text.isdigit()
    or ticket_text not in ("y", "n")
    or closed_text not in ("y", "n")
):
    print("Dữ liệu không hợp lệ")
else:
    age = int(age_text)
    if age > 120:
        print("Dữ liệu không hợp lệ")
    else:
        age_ok = age >= 18
        has_ticket = ticket_text == "y"
        is_closed = closed_text == "y"

        if age_ok and has_ticket and not is_closed:
            print("Được vào")
        else:
            print("Không được vào")

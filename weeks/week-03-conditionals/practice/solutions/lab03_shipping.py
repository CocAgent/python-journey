"""Lời giải 03 — bảo vệ dữ liệu và ưu tiên miễn phí trước phí nhanh."""

amount_text = input("Tổng tiền VND: ").strip()
member_text = input("Thành viên (y/n): ").strip().lower()
express_text = input("Giao nhanh (y/n): ").strip().lower()

if (
    not amount_text.isdigit()
    or member_text not in ("y", "n")
    or express_text not in ("y", "n")
):
    print("Dữ liệu không hợp lệ")
else:
    amount = int(amount_text)
    is_member = member_text == "y"
    is_express = express_text == "y"
    free_shipping = (amount >= 200_000) or (is_member and amount >= 100_000)

    if free_shipping:
        fee = 0
    elif is_express:
        fee = 50_000
    else:
        fee = 30_000

    print(f"Phí giao hàng: {fee:,} VND")

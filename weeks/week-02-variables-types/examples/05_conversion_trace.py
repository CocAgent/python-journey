"""Ví dụ 05 — Text -> kiểm -> int -> tính tiền (offline)."""

quantity_text = "3"
unit_price_vnd = 25_000  # số nguyên đồng, không dùng float cho tiền

print(f"Input đang là: {type(quantity_text).__name__}")
print(f"Đầu vào: {quantity_text!r}")
if quantity_text.isdigit():
    quantity = int(quantity_text)
    if quantity > 0:
        total_vnd = quantity * unit_price_vnd
        print(f"Số lượng đã đổi kiểu: {type(quantity).__name__}")
        print(f"Thành tiền: {total_vnd:,} VND")
    else:
        print("Số lượng phải lớn hơn 0")
else:
    print("Số lượng phải gồm các chữ số")

# Hai case sai được kiểm riêng, không gây crash chương trình.
invalid_quantity_text = "ba"
if invalid_quantity_text.isdigit():
    print("Không nên đến đây: số lượng không hợp lệ")
else:
    print("Ví dụ sai 'ba': không chuyển được sang int")

zero_text = "0"
if zero_text.isdigit() and int(zero_text) > 0:
    print("Không nên đến đây: số lượng phải > 0")
else:
    print("Ví dụ sai '0': số lượng phải lớn hơn 0")

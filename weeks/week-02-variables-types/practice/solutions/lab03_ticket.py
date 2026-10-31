"""Lời giải tham khảo 03 — input luôn là text."""

unit_price_vnd = 12_000

name = input("Tên: ").strip()
quantity_text = input("Số vé: ").strip()

# .isdigit() chỉ là kiểm tra đơn giản ở Week02, không thay thế
# validation đầy đủ ở các tuần sau.
if quantity_text.isdigit() and int(quantity_text) > 0:
    quantity = int(quantity_text)
    total_vnd = quantity * unit_price_vnd
    print(f"{name}: {quantity} vé, tổng {total_vnd:,} VND")
else:
    print("Số vé không hợp lệ")

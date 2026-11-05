"""Lời giải tham khảo 02 — dùng int cho đơn giá và số lượng."""

unit_price_text = "25000"
quantity_text = "3"
invalid_text = "ba"

unit_price_vnd = int(unit_price_text)
quantity = int(quantity_text)
total_vnd = unit_price_vnd * quantity

print(f"Thành tiền: {total_vnd:,} VND")

# Không chuyển "ba" ngay sang int: int("ba") sẽ gây ValueError.
if invalid_text.isdigit():
    print("Không nên đến đây vì 'ba' không phải chữ số")
else:
    print(f"Tình huống sai: {invalid_text} không phải số lượng hợp lệ")

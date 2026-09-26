"""Format a small receipt from typed values."""

item = "Notebook"
unit_price = 25_000.0
quantity = 2
total = unit_price * quantity

print(f"Sản phẩm: {item}")
print(f"Đơn giá: {unit_price:,.0f} đ")
print(f"Số lượng: {quantity}")
print(f"Tổng: {total:,.0f} đ")

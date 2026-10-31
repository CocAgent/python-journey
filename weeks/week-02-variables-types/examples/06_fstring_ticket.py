"""Ví dụ 06 — Từ biến -> xử lý -> phiếu giá (không gọi input)."""

name_text = "  An  "
ticket_count_text = "2"
unit_price_vnd = 12_000

# Dữ liệu nhập thô là str. strip() bỏ khoảng trắng hai bên.
name = name_text.strip()
print(f"Tên sau strip: {name}")
print(f"Kiểu số vé trước chuyển: {type(ticket_count_text).__name__}")

# Bước kiểm đơn giản, chỉ dùng các kiến thức đã giới thiệu ở Week02.
if ticket_count_text.isdigit() and int(ticket_count_text) > 0:
    ticket_count = int(ticket_count_text)
    total_vnd = ticket_count * unit_price_vnd
    print(f"Vé của {name}: {ticket_count} × {unit_price_vnd:,} = {total_vnd:,} VND")
else:
    print("Số vé không hợp lệ")

invalid_text = "hai"
if invalid_text.isdigit() and int(invalid_text) > 0:
    print("Không nên đến đây")
else:
    print("Tình huống sai: 'hai' không phải số vé hợp lệ")

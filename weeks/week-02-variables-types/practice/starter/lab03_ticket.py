"""Bài tương tự 03 — nhập tên, số vé và in hóa đơn f-string.

Dữ liệu nhập hợp lệ: Lan + 2 -> Lan: 2 vé, tổng 24,000 VND.
Không hợp lệ: abc / 0 / -1 -> Số vé không hợp lệ (không in hóa đơn).
"""

unit_price_vnd = 12_000

# TODO 1: name = input("Tên: ").strip()
name = input("Tên: ").strip()

# TODO 2: quantity_text = input("Số vé: ").strip()
quantity_text = input("Số vé: ").strip()

# TODO 3: dùng .isdigit() để kiểm, int() để đổi và kiểm > 0.
# TODO 4: hợp lệ thì in "{name}: {quantity} vé, tổng {total:,} VND".
#         Ngược lại in "Số vé không hợp lệ".
# Chưa cần try/except; if được dùng như đoạn xem trước Week03.
if quantity_text.isdigit():
    quantity = int(quantity_text)
    if quantity > 0:
        total = quantity * unit_price_vnd
        print(f"{name}: {quantity} vé, tổng {total:,} VND")
    else:
        print("Số vé không hợp lệ")
else:
    print("Số vé không hợp lệ")

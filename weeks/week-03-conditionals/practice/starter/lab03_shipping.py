"""Lab 03 — Guard và thứ tự ưu tiên: phí giao hàng giả lập.

Input: tổng đơn hàng (VND), thành viên y/n, giao nhanh y/n.
Miễn phí nếu amount >= 200000 HOẶC (member và amount >= 100000).
Nếu không miễn phí: giao nhanh 50000, giao thường 30000.
Dữ liệu sai -> "Dữ liệu không hợp lệ".
"""

amount_text = input("Tổng tiền VND: ").strip()
member_text = input("Thành viên (y/n): ").strip().lower()
express_text = input("Giao nhanh (y/n): ").strip().lower()

# TODO 1: kiểm số nguyên không âm và hai giá trị y/n.
# TODO 2: is_member và is_express là bool, không so sánh bool("n").
# TODO 3: đặt ngoặc cho điều kiện miễn phí.
# TODO 4: ưu tiên miễn phí TRƯỚC khi xét giao nhanh.
# TODO 5: in "Phí giao hàng: 0 VND" hoặc "30,000 VND" / "50,000 VND".
print("TODO Lab 03: cần tính phí giao hàng")

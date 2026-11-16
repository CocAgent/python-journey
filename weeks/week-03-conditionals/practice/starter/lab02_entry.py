"""Lab 02 — Boolean: kiểm tra vào cửa phòng hội thảo (GIẢ LẬP).

Input theo thứ tự: tuổi, có vé y/n, cửa đã đóng y/n.
Cần: >=18 tuổi AND có vé AND NOT cửa đã đóng.
Dữ liệu không hợp lệ: "Dữ liệu không hợp lệ".
"""

age_text = input("Tuổi: ").strip()
ticket_text = input("Có vé (y/n): ").strip().lower()
closed_text = input("Cửa đóng (y/n): ").strip().lower()

# TODO 1: kiểm tuổi là chữ số và 0..120.
# TODO 2: hai câu trả lời chỉ nhận y hoặc n.
# TODO 3: tạo các biến boolean age_ok, has_ticket, is_closed.
# TODO 4: dùng and và not để in một trong:
# "Được vào" / "Không được vào" / "Dữ liệu không hợp lệ".
print("TODO Lab 02: cần kiểm điều kiện vào cửa")

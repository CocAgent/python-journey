"""Ví dụ 04 — Dự đoán: range, continue, break và while.

Chạy từ thư mục gốc repo:
python weeks/week-06-loops/examples/04_predict_range_break_continue.py
Không có input() hoặc vòng lặp vô hạn.
"""

print(f"range(1, 6): {list(range(1, 6))}")  # Có 1..5; không có 6.

selected = []
for number in range(1, 11):
    if number % 3 == 0:
        continue  # Bỏ lượt này, KHÔNG kết thúc cả loop.
    if number > 8:
        break  # Kết thúc toàn bộ vòng for hiện tại.
    selected.append(number)
print(f"Sau continue/break: {selected}")

remaining = 3
while remaining > 0:
    print(f"while: còn {remaining}")
    remaining -= 1  # BẮT BUỘC cập nhật để điều kiện dừng đổi.
print(f"while kết thúc tại: {remaining}")

# Khi bắt đầu từ 0, phần thân while không chạy lần nào.
remaining = 0
while remaining > 0:
    print("Không được in dòng này")
    remaining -= 1
print("while(0): không có lượt nào")

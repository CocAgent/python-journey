"""Ví dụ 04 — Dự đoán KẾT QUẢ trước khi chạy.

Chạy từ repository root:
    python weeks/week-02-variables-types/examples/04_predict_types.py
Không cần input, thư viện hay Internet.
"""

# Dấu ngoặc kép biểu thị CHUỖI (str), không phải số.
number_text = "12"
number = 12

print(f"Chuỗi cộng chuỗi: {number_text + '3'}")  # ghép chuỗi: 123
print(f"Số cộng số: {number + 3}")  # phép cộng: 15
print(f"Kiểu number_text: {type(number_text).__name__}")  # str
print(f"Kiểu number: {type(number).__name__}")  # int

# bool("False") là True vì ĐÂY LÀ CHUỖI CÓ KÝ TỰ.
print(f"bool('False'): {bool('False')}")
print(f"bool(''): {bool('')}")

# / và // không giống nhau.
print(f"5 / 2: {5 / 2}")  # 2.5
print(f"5 // 2: {5 // 2}")  # 2

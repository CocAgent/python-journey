"""Ví dụ 04 — Dự đoán indexing, slicing và find() trước khi chạy.

Chạy từ gốc repo:
    python weeks/week-04-strings/examples/04_predict_slice_and_find.py
"""

word = "Python"
print(f"Ký tự đầu: {word[0]}")
print(f"Ký tự cuối: {word[-1]}")
print(f"Ba ký tự đầu: {word[:3]}")
print(f"Đảo chuỗi: {word[::-1]}")
print(f"Phần tử tại index 3: {word[3]}")

# find() trả về vị trí đầu tiên, hoặc -1 nếu không có.
print(f"find('th'): {word.find('th')}")
print(f"find('Java'): {word.find('Java')}")

# Slicing ngoài ranh giới KHÔNG gây IndexError.
print(f"Slice quá dài: {word[:99]}")

# Index trực tiếp ngoài ranh giới gây IndexError, nên chỉ minh họa an toàn.
print(f"Index 99 có hợp lệ? {99 < len(word)}")

# Chặn trường hợp chuỗi rỗng trước khi đọc ký tự đầu/cuối.
empty = ""
if empty:
    print(empty[0])
else:
    print("Chuỗi rỗng: không đọc được ký tự đầu")

"""Ví dụ 04 — Dự đoán: alias thay đổi cùng list hay không?

Chạy từ gốc repo:
python weeks/week-05-lists-tuples/examples/04_predict_alias_and_copy.py
"""

books = ["Toán", "Văn"]
alias = books  # Hai tên cùng trỏ đến MỘT list.
snapshot = books.copy()  # Một list mới, bản sao nông.

alias.append("Anh")
books[0] = "Tin"

print(f"List gốc: {books}")
print(f"Alias: {alias}")
print(f"Copy: {snapshot}")
print(f"Alias cùng đối tượng: {alias is books}")
print(f"Copy cùng đối tượng: {snapshot is books}")

# Lưu ý nâng cao: shallow copy KHÔNG sao chép sâu các list lồng nhau.
nested = [["A"], ["B"]]
shallow = nested.copy()
nested[0].append("C")
print(f"List lồng nhau sau sửa: {shallow}")  # [['A', 'C'], ['B']]
print(f"Cùng list con thứ nhất: {nested[0] is shallow[0]}")

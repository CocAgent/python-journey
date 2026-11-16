"""Lời giải tham khảo Lab 01: CRUD theo từng bước."""

items = ["Sách", "Bút", "Tẩy"]
items.append("Vở")
items.insert(1, "Thước")
items[0] = "Sách Python"
items.remove("Tẩy")
removed = items.pop()

print(f"Sau CRUD: {items}")
print(f"Đã lấy: {removed}")
print(f"Đầu: {items[0]}")
print(f"Cuối: {items[-1]}")

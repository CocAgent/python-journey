"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]
print("1. Danh sách ban đầu:", subjects)

# Thêm môn vào cuối bằng append(), chèn môn vào vị trí index 1 bằng insert()
subjects.append("Tin học")        # Thêm vào cuối
subjects.insert(1, "Lý")           # Chèn vào vị trí index 1 (sau "Toán")
print("\n2. Sau khi append('Tin học') và insert(1, 'Lý'):", subjects)
print(f"   - Phần tử đầu (index 0): {subjects[0]}")
print(f"   - Phần tử cuối (index -1): {subjects[-1]}")
print(f"   - Phần tử ở giữa (slice 1:-1): {subjects[1:-1]}")

# Cập nhật (update) môn học đầu tiên
subjects[0] = "Toán cao cấp"
print("\n3. Sau khi cập nhật môn đầu tiên subjects[0] = 'Toán cao cấp':", subjects)
print(f"   - Phần tử đầu: {subjects[0]}")
print(f"   - Phần tử cuối: {subjects[-1]}")
print(f"   - Phần tử ở giữa: {subjects[1:-1]}")

# Xóa một môn đã biết bằng remove(), lấy và xóa môn cuối bằng pop()
subjects.remove("Văn")             # Xóa môn "Văn" khỏi danh sách
mon_bi_pop = subjects.pop()        # Lấy ra và xóa phần tử cuối ("Tin học")
print(f"\n4. Sau khi remove('Văn') và pop() [môn bị lấy ra: '{mon_bi_pop}']:", subjects)
print(f"   - Phần tử đầu: {subjects[0]}")
print(f"   - Phần tử cuối: {subjects[-1]}")
print(f"   - Phần tử ở giữa: {subjects[1:-1]}")

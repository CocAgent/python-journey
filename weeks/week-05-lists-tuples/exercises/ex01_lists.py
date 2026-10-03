"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects.append("Tin học")
subjects.insert(1, "Lịch sử")
print("Sau khi append và insert:", subjects)

# TODO: update the first subject.
subjects[0] = "Toán cao cấp"
print("Sau khi update phần tử đầu:", subjects)

# TODO: remove one known subject and pop the last subject.
subjects.remove("Văn")
popped = subjects.pop()
print(f"Đã pop môn: {popped}")
print("Sau khi remove và pop:", subjects)

# TODO: print the first, last and middle slice after each safe operation.
first = subjects[0]
last = subjects[-1]
middle = subjects[1:-1]
print(f"Phần tử đầu (first): {first}")
print(f"Phần tử cuối (last): {last}")
print(f"Khúc giữa (middle slice): {middle}")

print("Danh sách môn học cuối cùng:", subjects)

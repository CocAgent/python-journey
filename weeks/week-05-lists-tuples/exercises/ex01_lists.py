"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects.append("Lý")
subjects.insert(1, "Hóa")

# TODO: update the first subject.
subjects[0] = "Đại số"

# TODO: remove one known subject and pop the last subject.
subjects.remove("Văn")
last_subject = subjects.pop()

# TODO: print the first, last and middle slice after each safe operation.
first_item = subjects[0]
last_item = subjects[-1]
middle_slice = subjects[1:-1]

print(f"Phần tử đầu: {first_item}")
print(f"Phần tử cuối: {last_item}")
print(f"Lát cắt ở giữa: {middle_slice}")
print("Danh sách cuối cùng:", subjects)

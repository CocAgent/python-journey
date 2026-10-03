"""Exercise 01: list create, read, update and delete."""

subjects = ["Toan", "Van", "Anh"]

# 1. append one subject and insert another at index 1.
subjects.append("Lich su")       # Them "Lich su" vao cuoi list
subjects.insert(1, "Ly")         # Chen "Ly" vao vi tri index 1
print("Sau khi them:", subjects)  # ['Toan', 'Ly', 'Van', 'Anh', 'Lich su']

# 2. update the first subject.
subjects[0] = "Tin hoc"          # Cap nhat phan tu dau tien ("Toan" -> "Tin hoc")
print("Sau khi cap nhat:", subjects) # ['Tin hoc', 'Ly', 'Van', 'Anh', 'Lich su']

# 3. remove one known subject and pop the last subject.
subjects.remove("Van")           # Xoa mon "Van" khoi list
last_subject = subjects.pop()    # Lay va xoa phan tu cuoi cung ("Lich su")
print("Sau khi xoa va pop:", subjects) # Con lai: ['Tin hoc', 'Ly', 'Anh']

# 4. print the first, last and middle slice after each safe operation.
print("Phan tu dau (slice):", subjects[:1])   # ['Tin hoc']
print("Phan tu cuoi (slice):", subjects[-1:])  # ['Anh']
print("Phan tu giua (slice):", subjects[1:2])  # ['Ly']

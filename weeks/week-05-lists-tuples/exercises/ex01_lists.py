"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects.append("Lý")
subjects.insert(1, "Hóa")

# TODO: update the first subject.
subjects[0] = "Sinh"

# TODO: remove one known subject and pop the last subject.
subjects.remove("Văn")
subjects.pop()

# TODO: print the first, last and middle slice after each safe operation.
print("First:", subjects[0])
print("Last:", subjects[-1])
print("Middle slice:", subjects[1:-1])

print(subjects)

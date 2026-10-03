"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects.append("Địa")
subjects.insert(1, "Lý")

# TODO: update the first subject.
subjects[0] = "Sử"

# TODO: remove one known subject and pop the last subject.
subjects.remove("Anh")
subjects.pop()

# TODO: print the first, last and middle slice after each safe operation.

print(subjects)
print(subjects[0])
print(subjects[-1])
print(subjects[1:-1])

"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects.append("Tin")
subjects.insert(1, "Lý")

# TODO: update the first subject.
subjects[0] = "Toán cao cấp"

# TODO: remove one known subject and pop the last subject.
subjects.remove("Văn")
subjects.pop()

# TODO: print the first, last and middle slice after each safe operation.
print("first =", subjects[0])
print("last =", subjects[-1])
print("middle slice =", subjects[1:-1])

print("Final subjects:", subjects)

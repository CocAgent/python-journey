"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects.append("Lý")
subjects.insert(1, "Hóa")

# TODO: update the first subject.
subjects[0] = "Sinh"

# TODO: remove one known subject and pop the last subject.
subjects.remove("Anh")
subjects.pop()

# TODO: print the first, last and middle slice after each safe operation.
print("First three subjects:", subjects[0:3])
print("Last three subjects:", subjects[-3:])
print("Middle subjects:", subjects[1:4])

print(subjects)

"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects.append("Tin")
subjects.insert(1, "Lý")
# TODO: update the first subject.
subjects[0] = "hóa"
# TODO: remove one known subject and pop the last subject.
subjects.remove("Văn")
subjects.pop()
# TODO: print the first, last and middle slice after each safe operation.
print(f"Subjects: {subjects}")
print(f"First subject: {subjects[0]}")
print(f"Last subject: {subjects[-1]}")
print(f"Middle subjects: {subjects[1:-1]}")

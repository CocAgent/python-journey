"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects.append("Vật lý")
subjects.insert(1, "Hóa học")

# TODO: update the first subject.
subjects[0] = "Toán học"

# TODO: remove one known subject and pop the last subject.
if "Văn" in subjects:
    subjects.remove("Văn")
if subjects:
    subjects.pop()

# TODO: print the first, last and middle slice after each safe operation.
print(f"first={subjects[0]}")
print(f"last={subjects[-1]}")
print(f"middle={subjects[1:-1]}")

print(subjects)

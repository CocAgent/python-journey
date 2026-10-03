"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects.append("Tin")
subjects.insert(1, "Lý")

# TODO: update the first subject.
subjects[0] = "Đại số"

# TODO: remove one known subject and pop the last subject.
subjects.remove("Văn")
last_subject = subjects.pop()

# TODO: print the first, last and middle slice after each safe operation.
print(f"first={subjects[0]}")
print(f"last={subjects[-1]}")
print(f"middle={subjects[1:-1]}")
print(f"popped={last_subject}")
print(subjects)

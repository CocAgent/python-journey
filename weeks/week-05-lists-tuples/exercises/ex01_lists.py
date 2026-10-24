"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects.append("Tin")
subjects.insert(1, "Sử")
print(f"first={subjects[0]}, last={subjects[-1]}, middle={subjects[1:-1]}")

# TODO: update the first subject.
subjects[0] = "Toán Nâng Cao"
print(f"first={subjects[0]}, last={subjects[-1]}, middle={subjects[1:-1]}")

# TODO: remove one known subject and pop the last subject.
if "Sử" in subjects:
    subjects.remove("Sử")
popped = subjects.pop()
print(f"popped={popped}")

# TODO: print the first, last and middle slice after each safe operation.
print(f"first={subjects[0]}, last={subjects[-1]}, middle={subjects[1:-1]}")

print(subjects)

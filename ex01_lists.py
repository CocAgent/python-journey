"""Exercise 01: list create, read, update and delete."""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects.append("Tin học")
subjects.insert(1, "Vật lý")

# TODO: update the first subject.
subjects[0] = "Toán cao cấp"

# TODO: remove one known subject and pop the last subject.
subjects.remove("Văn")
subjects.pop()

# TODO: print the first, last and middle slice after each safe operation.
print(f"First: {subjects[0]}")
print(f"Last: {subjects[-1]}")
print(f"Middle slice: {subjects[1:-1]}")

print(subjects)

"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects.append("Vật Lý")
subjects.insert(1, "Hóa Học")
print(f"After add: first={subjects[0]}, last={subjects[-1]}, middle={subjects[1:-1]}")

# TODO: update the first subject.
subjects[0] = "Toán Cao Cấp"
print(f"After update: first={subjects[0]}, last={subjects[-1]}, middle={subjects[1:-1]}")

# TODO: remove one known subject and pop the last subject.
subjects.remove("Anh")
subjects.pop()

# TODO: print the first, last and middle slice after each safe operation.
print(f"After remove/pop: first={subjects[0]}, last={subjects[-1]}, middle={subjects[1:-1]}")

print(subjects)

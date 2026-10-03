"""Exercise 01: list create, read, update and delete."""

# Danh sách ban đầu gồm 3 môn học
subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
# 1. append(): Thêm môn "Lý" vào cuối danh sách
subjects.append("Lý")
# 2. insert(1, ...): Chèn môn "Hóa" vào vị trí chỉ số 1
subjects.insert(1, "Hóa")

# TODO: update the first subject.
# Cập nhật môn học đầu tiên (vị trí index 0) thành "Toán nâng cao"
subjects[0] = "Toán nâng cao"

# TODO: remove one known subject and pop the last subject.
# 1. remove("Văn"): Tìm và xóa môn "Văn"
subjects.remove("Văn")
# 2. pop(): Xóa và lấy ra môn học ở cuối danh sách (ở đây là môn "Lý")
removed_subject = subjects.pop()

# TODO: print the first, last and middle slice after each safe operation.
# In ra môn đầu tiên (index 0), môn cuối cùng (index -1), và lát cắt ở giữa (index 1 đến kế cuối)
print("First subject:", subjects[0])
print("Last subject:", subjects[-1])
print("Middle slice:", subjects[1:-1])

print("Final subjects:", subjects)

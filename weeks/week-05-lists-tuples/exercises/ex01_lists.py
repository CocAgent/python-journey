"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.

subjects.append("Tin học")      # Thêm vào cuối
subjects.insert(1, "Vật lý")    # Chèn vào vị trí 1
print("Sau khi thêm:", subjects)
print("Đầu:", subjects[0], "| Cuối:", subjects[-1], "| Giữa:", subjects[1:-1])

# TODO: update the first subject.
subjects[0] = "Hóa học"         # Sửa phần tử đầu
print("Sau khi sửa:", subjects)
print("Đầu:", subjects[0], "| Cuối:", subjects[-1], "| Giữa:", subjects[1:-1])
# TODO: remove one known subject and pop the last subject.
subjects.remove("Văn")         # Xóa theo giá trị
subjects.pop()                 # Xóa phần tử cuối
print("Sau khi xóa:", subjects)
print("Đầu:", subjects[0], "| Cuối:", subjects[-1], "| Giữa:", subjects[1:-1])


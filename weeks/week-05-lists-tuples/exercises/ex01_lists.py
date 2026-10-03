"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]
print("Ban đầu:", subjects)

# TODO: append one subject and insert another at index 1.
subjects.append("Lý")          # thêm vào cuối
subjects.insert(1, "Hóa")      # chèn vào vị trí index 1
print("Sau append + insert:", subjects)

# TODO: update the first subject.
subjects[0] = "Toán Cao Cấp"   # cập nhật phần tử đầu tiên
print("Sau update:", subjects)

# TODO: remove one known subject and pop the last subject.
subjects.remove("Văn")         # xóa theo giá trị
cuoi = subjects.pop()          # xóa và lấy phần tử cuối
print(f"Đã pop: '{cuoi}'")
print("Sau remove + pop:", subjects)

# TODO: print the first, last and middle slice after each safe operation.
if subjects:
    first  = subjects[0]
    last   = subjects[-1]
    mid    = subjects[1:-1]    # slice phần giữa (bỏ đầu và cuối)
    print(f"Đầu: {first!r},  Cuối: {last!r},  Giữa: {mid}")

print(subjects)

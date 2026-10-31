"""Ví dụ 05 — Nhìn rõ từng bước CRUD, slicing và sort.

Tất cả dùng dữ liệu giả lập, không cần input hay vòng lặp.
"""

names = ["An", "Bình", "Chi"]
print(f"Bước 1 — ban đầu: {names}")

names.append("Dũng")  # Thêm cuối.
names.insert(1, "Lan")  # Chèn trước phần tử ở index 1.
print(f"Bước 2 — thêm: {names}")

names[0] = "Mai"  # Sửa phần tử đầu tiên.
names.remove("Chi")  # Xóa theo GIÁ TRỊ.
last = names.pop()  # Xóa/lấy phần tử CUỐI.
print(f"Bước 3 — sửa/xóa: {names}")
print(f"Đã lấy bằng pop(): {last}")

print(f"Hai người đầu: {names[:2]}")
print(f"Thứ tự đảo: {names[::-1]}")
print(f"Slice quá cuối: {names[:99]}")  # Không IndexError.

if "Nam" in names:
    names.remove("Nam")
else:
    print("Không có 'Nam', không gọi remove()")

scores = [7, 4, 9]
ascending = sorted(scores)  # List MỚI, gốc giữ nguyên.
print(f"sorted() trả: {ascending}; gốc: {scores}")
returned = scores.sort()  # SỬA tại chỗ và trả None.
print(f"sort() trả: {returned}; gốc sau sort(): {scores}")

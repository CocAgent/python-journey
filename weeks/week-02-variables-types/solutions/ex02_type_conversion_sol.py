"""Lời giải Bài tập 02: Chuyển đổi kiểu dữ liệu"""

# TODO 1
tuoi_text = "18"

tuoi = int(tuoi_text) + 2

print(f"Sau 2 năm nữa: {tuoi} tuổi")


# TODO 2
diem = 8.99

print(f"Điểm ban đầu: {diem}")
print(f"Sau khi chuyển sang int: {int(diem)}")


# TODO 3
print(f"bool(-1) = {bool(-1)}")            # True
print(f"bool(0.0) = {bool(0.0)}")          # False

print(f'bool(" ") = {bool(" ")}')          # True
print(f'bool("Python") = {bool("Python")}') # True

print(f"bool(()) = {bool(())}")            # False
print(f"bool((1, 2)) = {bool((1, 2))}")    # True


# TODO 4
ban_kinh = float(input("Nhập bán kính hình tròn: "))

dien_tich = 3.14 * (ban_kinh ** 2)

print(f"Diện tích hình tròn = {dien_tich:.2f}")


# TODO 5
tong_tien = int(input("Nhập tổng số tiền: "))

to_500 = tong_tien // 500000
du = tong_tien % 500000

to_200 = du // 200000
du = du % 200000

to_100 = du // 100000

print(f"Số tờ 500k: {to_500}")
print(f"Số tờ 200k: {to_200}")
print(f"Số tờ 100k: {to_100}")

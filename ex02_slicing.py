"""Exercise 02: slicing, mutability, alias and copy."""

numbers = [1, 2, 3, 4, 5, 6]

# TODO: create first_three and last_three using slices.
# - numbers[:3]: Cắt từ đầu đến trước vị trí index 3 (lấy các index 0, 1, 2) -> [1, 2, 3]
first_three: list[int] = numbers[:3]
# - numbers[-3:]: Cắt 3 phần tử cuối cùng (từ index -3 đến hết) -> [4, 5, 6]
last_three: list[int] = numbers[-3:]

# TODO: make alias refer to numbers and copied be a shallow copy.
# - alias = numbers: Cùng trỏ đến đối tượng list trong bộ nhớ (bí danh / tham chiếu)
alias: list[int] = numbers
# - copied = numbers.copy(): Tạo ra một bản sao nông độc lập ở vùng nhớ mới (shallow copy)
copied: list[int] = numbers.copy()

# TODO: append through alias and explain which lists change.
# Thêm số 7 vào list thông qua biến alias:
alias.append(7)

# Giải thích:
# 1. `numbers` BỊ THAY ĐỔI ([1, 2, 3, 4, 5, 6, 7]) vì `alias` và `numbers` thực chất là một list.
# 2. `copied` KHÔNG ĐỔI ([1, 2, 3, 4, 5, 6]) vì là bản sao chép riêng biệt.
# 3. `first_three` và `last_three` KHÔNG ĐỔI vì thao tác slicing đã sinh ra list độc lập.

print("first_three:", first_three)
print("last_three:", last_three)
print("alias:", alias)
print("numbers:", numbers)
print("copied:", copied)
print(first_three, last_three, alias, copied)
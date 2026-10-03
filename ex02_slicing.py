"""Exercise 02: slicing, mutability, alias and copy."""

numbers = [1, 2, 3, 4, 5, 6]

# 1. Dùng slicing để lấy 3 phần tử đầu và 3 phần tử cuối
first_three: list[int] = numbers[:3]    # Lấy từ đầu đến index 3 (không gồm 3): [1, 2, 3]
last_three: list[int] = numbers[-3:]    # Lấy từ index -3 đến hết: [4, 5, 6]

# 2. alias trỏ cùng vào numbers; copied là một bản sao độc lập (shallow copy)
alias: list[int] = numbers              # alias và numbers cùng tham chiếu tới 1 vùng nhớ
copied: list[int] = numbers.copy()      # tạo ra một bản copy độc lập trong vùng nhớ mới

# 3. Thêm một phần tử qua alias (ví dụ thêm số 99)
alias.append(99)

# In kết quả theo yêu cầu
print("first_three :", first_three)
print("last_three  :", last_three)
print("alias       :", alias)
print("copied      :", copied)
print("numbers gốc :", numbers)

# Giải thích:
# - 'numbers' thay đổi theo 'alias' vì cả hai biến cùng trỏ vào 1 list duy nhất (alias là bí danh).
# - 'copied' KHÔNG đổi vì numbers.copy() tạo một list mới tách biệt.
# - 'first_three' và 'last_three' KHÔNG đổi vì slicing tạo ra list mới tại thời điểm cắt.

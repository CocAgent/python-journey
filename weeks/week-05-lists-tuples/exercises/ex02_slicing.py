"""Exercise 02: slicing, mutability, alias and copy."""

numbers = [1, 2, 3, 4, 5, 6]

# TODO: create first_three and last_three using slices.
first_three: list[int] = numbers[:3]
last_three: list[int] = numbers[-3:]

# TODO: make alias refer to numbers and copied be a shallow copy.
alias: list[int] = numbers
copied: list[int] = numbers.copy()

# TODO: append through alias and explain which lists change.
alias.append(7)

# Giải thích:
# - Cả `numbers` và `alias` đều thay đổi (trở thành [1, 2, 3, 4, 5, 6, 7]) vì `alias` trỏ chung một vùng nhớ đối tượng với `numbers`.
# - `copied`, `first_three` và `last_three` KHÔNG thay đổi vì chúng là các bản copy riêng biệt độc lập.

print("first_three:", first_three)
print("last_three: ", last_three)
print("alias:      ", alias)
print("copied:     ", copied)
print("numbers:    ", numbers)
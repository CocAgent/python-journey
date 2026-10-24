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
# Khi append vào alias:
# - 'numbers' thay đổi theo vì 'alias' và 'numbers' cùng tham chiếu tới một list trong bộ nhớ.
# - 'copied' KHÔNG đổi vì được tạo bằng .copy() (shallow copy độc lập).
# - 'first_three' và 'last_three' KHÔNG đổi vì slicing tạo ra list mới độc lập.

print("first_three:", first_three)
print("last_three:", last_three)
print("alias:", alias)
print("numbers:", numbers)
print("copied:", copied)
print("Result tuple:", (first_three, last_three, alias, copied))

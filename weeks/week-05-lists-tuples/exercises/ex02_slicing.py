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
# alias và numbers cùng trỏ tới một list đối tượng trong bộ nhớ,
# nên khi thay đổi qua alias, cả alias và numbers đều thay đổi.
# copied và các lát cắt (first_three, last_three) là các danh sách độc lập nên giữ nguyên.

print(first_three, last_three, alias, copied)
print(f"alias shares changes: {alias == numbers}")
print(f"copied remains independent: {copied != numbers}")

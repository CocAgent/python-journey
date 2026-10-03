"""Exercise 02: slicing, mutability, alias and copy."""

numbers = [1, 2, 3, 4, 5, 6]

# TODO: create first_three and last_three using slices.
first_three: list[int] = numbers[:3]
last_three: list[int] = numbers[-3:]

# TODO: make alias refer to numbers and copied be a shallow copy.
alias: list[int] = numbers
copied: list[int] = numbers.copy()

# TODO: append through alias and explain which lists change.
# alias và numbers cùng trỏ vào một danh sách, nên khi sửa qua alias thì numbers cũng đổi.
# copied là bản shallow copy độc lập nên giữ nguyên.
alias.append(7)

print(first_three, last_three, alias, copied)

"""Exercise 02: slicing, mutability, alias and copy."""

numbers = [1, 2, 3, 4, 5, 6]

# TODO: create first_three and last_three using slices.
first_three: list[int] = numbers[:3]
last_three: list[int] = numbers[-3:]

# TODO: make alias refer to numbers and copied be a shallow copy.
alias: list[int] = numbers
copied: list[int] = numbers.copy()

# TODO: append through alias and explain which lists change.
# alias và numbers cùng trỏ tới một danh sách trong bộ nhớ,
# nên khi thêm phần tử qua alias, cả numbers và alias đều thay đổi.
# copied là bản sao nông (shallow copy) độc lập, nên không bị ảnh hưởng.
alias.append(7)

print(first_three, last_three, alias, copied)

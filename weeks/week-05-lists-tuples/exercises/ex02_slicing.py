"""Exercise 02: slicing, mutability, alias and copy."""

numbers = [1, 2, 3, 4, 5, 6]

# TODO: create first_three and last_three using slices.
first_three: list[int] = numbers[:3]
last_three: list[int] = numbers[-3:]

# TODO: make alias refer to numbers and copied be a shallow copy.
alias: list[int] = numbers
copied: list[int] = numbers.copy()

alias.append(7)

# TODO: append through alias and explain which lists change.
print("Ba số đầu:", first_three)
print("Ba số cuối:", last_three)
print("numbers:", numbers)
print("alias:", alias)
print("copied:", copied)

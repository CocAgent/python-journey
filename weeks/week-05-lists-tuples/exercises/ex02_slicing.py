"""Exercise 02: slicing, mutability, alias and copy."""

numbers = [1, 2, 3, 4, 5, 6]

# TODO: create first_three and last_three using slices.
first_three = numbers[:3]
last_three = numbers[-3:]

# TODO: make alias refer to numbers and copied be a shallow copy.
alias = numbers
copied = numbers.copy()

# TODO: append through alias and explain which lists change.
print(first_three, last_three, alias, copied)
alias.append(7)
print(first_three, last_three, alias, copied)
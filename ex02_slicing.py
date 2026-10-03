"""Exercise 02: slicing, mutability, alias and copy."""

numbers = [1, 2, 3, 4, 5, 6]

# TODO: create first_three and last_three using slices.
first_three = numbers[:3]
last_three = numbers[-3:]

# TODO: make alias refer to numbers and copied be a shallow copy.
alias = numbers
copied = numbers.copy()

# TODO: append through alias and explain which lists change.
alias.append(7)
# Khi append qua alias: cả numbers và alias đều thay đổi vì chúng cùng trỏ tới 1 danh sách trong bộ nhớ (alias is numbers).
# copied (bản sao shallow copy) và các lát cắt (first_three, last_three) là các danh sách độc lập nên không bị thay đổi.
print("first_three:", first_three)
print("last_three :", last_three)
print("alias      :", alias)
print("copied     :", copied)
print("numbers    :", numbers)

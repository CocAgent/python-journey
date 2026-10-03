"""Exercise 02: slicing, mutability, alias and copy."""

numbers = [1, 2, 3, 4, 5, 6]

# TODO: create first_three and last_three using slices.
first_three: list[int] = numbers[:3]   # [1, 2, 3]
last_three:  list[int] = numbers[-3:]  # [4, 5, 6]

# TODO: make alias refer to numbers and copied be a shallow copy.
alias:  list[int] = numbers         # alias trỏ vào CÙNG list với numbers
copied: list[int] = numbers.copy()  # copied là bản sao độc lập

# TODO: append through alias and explain which lists change.
alias.append(99)
# → alias và numbers đều thay đổi (cùng object)
# → copied KHÔNG thay đổi (object riêng biệt)

print("numbers  :", numbers)     # [1, 2, 3, 4, 5, 6, 99]
print("alias    :", alias)       # [1, 2, 3, 4, 5, 6, 99]  — giống numbers
print("copied   :", copied)      # [1, 2, 3, 4, 5, 6]       — không đổi
print("alias is numbers:", alias is numbers)   # True  — cùng object
print("copied is numbers:", copied is numbers) # False — object khác

print(first_three, last_three, alias, copied)

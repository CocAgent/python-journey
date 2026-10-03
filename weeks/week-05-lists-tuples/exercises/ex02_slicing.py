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
# - numbers và alias cùng trỏ tới 1 list object trong bộ nhớ (alias is numbers -> True).
#   Do đó, khi append qua alias thì numbers cũng thay đổi thành [1, 2, 3, 4, 5, 6, 7].
# - copied là bản sao nông (shallow copy) độc lập trong bộ nhớ, nên vẫn giữ nguyên [1, 2, 3, 4, 5, 6].
print(f"first_three: {first_three}")
print(f"last_three: {last_three}")
print(f"numbers (sau alias.append): {numbers}")
print(f"alias: {alias}")
print(f"copied: {copied}")
print(f"numbers is alias: {numbers is alias}")
print(f"numbers is copied: {numbers is copied}")

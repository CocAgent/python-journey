"""Exercise 02: slicing, mutability, alias and copy."""

numbers = [1, 2, 3, 4, 5, 6]

# 1. create first_three and last_three using slices.
first_three: list[int] = numbers[:3]   # 3 phan tu dau: [1, 2, 3]
last_three: list[int] = numbers[-3:]   # 3 phan tu cuoi: [4, 5, 6]

# 2. make alias refer to numbers and copied be a shallow copy.
alias: list[int] = numbers             # alias va numbers cung tro vao mot list
copied: list[int] = numbers.copy()     # copied la ban sao doc lap (shallow copy)

# 3. append through alias and explain which lists change.
alias.append(7)

# Giai thich:
# - `numbers` va `alias` SE THAY DOI (deu co them so 7) vi chung cung quan ly mot vung nho.
# - `copied`, `first_three`, va `last_three` SE KHONG DOI vi chung la cac list doc lap hoan toan.

print("first_three:", first_three)  # [1, 2, 3]
print("last_three:", last_three)    # [4, 5, 6]
print("alias:", alias)              # [1, 2, 3, 4, 5, 6, 7]
print("copied:", copied)            # [1, 2, 3, 4, 5, 6]
print("numbers goc:", numbers)      # [1, 2, 3, 4, 5, 6, 7]

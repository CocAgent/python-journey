"""Lời giải Bài tập 03: In hoa văn"""
n = 5

# TODO 1: Tam giác vuông
for i in range(1, n + 1):
    print("*" * i)

print()

# TODO 2: Tam giác cân
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

print()

# TODO 3: Kim cương
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

print()

# TODO 4: Bàn cờ
n = 4
for r in range(n):
    for c in range(n):
        if (r + c) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()

"""
Bài tập 03: In hoa văn bằng vòng lặp lồng
=========================================
Mục tiêu: Thành thạo nested loops
"""

n = 5

# TODO 1: In tam giác vuông cao n dòng
for row in range(1, n + 1):
    print("*" * row)

# TODO 2: In tam giác cân cao n dòng (căn giữa)
for row in range(1, n + 1):
    spaces = " " * (n - row)
    stars = "*" * (2 * row - 1)
    print(spaces + stars)

# TODO 3: In hình kim cương cao n dòng (n lẻ)
for row in range(1, n + 1):
    print(" " * (n - row) + "*" * (2 * row - 1))
for row in range(n - 1, 0, -1):
    print(" " * (n - row) + "*" * (2 * row - 1))

# TODO 4 (Thử thách): In bàn cờ n x n
board_size = 4
for row in range(board_size):
    for column in range(board_size):
        if (row + column) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()

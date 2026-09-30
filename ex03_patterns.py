"""
Bài tập 03: In hoa văn bằng vòng lặp lồng 🎨
===============================================
Mục tiêu: Thành thạo nested loops
"""

# TODO 1: In tam giác vuông cao n dòng
# n = 5:
# *
# **
# ***
# ****
# *****
n = int(input("Nhập n: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()


# TODO 2: In tam giác cân cao n dòng (căn giữa)
# n = 5:
#     *
#    ***
#   *****
#  *******
# *********
n = int(input("Nhập n: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()


# TODO 3: In hình kim cương cao n dòng (n lẻ)
# n = 5:
#   *
#  ***
# *****
#  ***
#   *
n = int(input("Nhập n (số lẻ): "))
mid = n // 2

for i in range(n):
    if i <= mid:
        spaces = mid - i
        stars = 2 * i + 1
    else:
        spaces = i - mid
        stars = 2 * (n - 1 - i) + 1

    for j in range(spaces):
        print(" ", end="")
    for k in range(stars):
        print("*", end="")
    print()


# TODO 4 (Thử thách): In bàn cờ n x n
# n = 4:
# ■ □ ■ □
# □ ■ □ ■
# ■ □ ■ □
# □ ■ □ ■
n = int(input("Nhập n: "))
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()
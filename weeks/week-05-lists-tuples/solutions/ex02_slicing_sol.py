"""Lời giải Bài tập 02: Slicing & Comprehension"""
numbers = list(range(1, 21))
print(f"5 đầu: {numbers[:5]}")
print(f"5 cuối: {numbers[-5:]}")
print(f"Vị trí chẵn: {numbers[::2]}")

# TODO 2
squares = [i ** 2 for i in range(1, 11)]
evens = [x for x in range(0, 21) if x % 2 == 0]
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(squares, evens, upper)

# TODO 3
scores = [45, 78, 92, 56, 33, 88, 71, 95, 62, 50]
passed = [s for s in scores if s >= 60]
failed = [s for s in scores if s < 50]
labels = ["Đạt" if s >= 60 else "Rớt" for s in scores]
print(f"Đạt: {passed}\nRớt: {failed}\nLabels: {labels}")

# TODO 4
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)

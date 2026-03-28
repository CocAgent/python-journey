"""Lời giải Bài tập 03: Tuple & Unpacking"""
# TODO 1
coords = (3, 7)
x, y = coords
print(f"x={x}, y={y}")
# coords[0] = 5  # TypeError: tuple không thay đổi được!

# TODO 2
def tinh_thong_ke(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

nho, lon, tb = tinh_thong_ke([7, 9, 5, 8, 10])
print(f"Min: {nho}, Max: {lon}, TB: {tb:.1f}")

# TODO 3
students = [("An", 8.5), ("Bình", 7.0), ("Châu", 9.2), ("Dũng", 6.5)]
for ten, diem in students:
    print(f"{ten}: {diem}")
best = max(students, key=lambda s: s[1])
print(f"Cao nhất: {best[0]} ({best[1]})")
students.sort(key=lambda s: s[1], reverse=True)
print(f"Giảm dần: {students}")

# TODO 4
names = ["A", "B", "C"]
scores = [8, 9, 7]
for i, (name, score) in enumerate(zip(names, scores), 1):
    print(f"{i}. {name} — {score} điểm")

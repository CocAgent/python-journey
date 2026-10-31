"""Lời giải Lab 01: ghép đúng cặp, đánh số và tính tổng."""

names = ["An", "Bình", "Chi"]
scores = [8, 9, 7]

for position, (name, score) in enumerate(
    zip(names, scores, strict=True), start=1
):
    print(f"{position}. {name}: {score}")

total = 0
for score in scores:
    total += score
print(f"Tổng điểm: {total}")

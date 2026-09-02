"""Pair positions and related collections."""

names = ["An", "Bình", "Châu"]
scores = [8, 9, 7]

for position, (name, score) in enumerate(
    zip(names, scores, strict=True), start=1
):
    print(f"{position}. {name}: {score}")

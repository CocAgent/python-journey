"""Starter for the Week 06 Iteration Report."""

topics = ["loops", "enumerate", "zip", "comprehensions"]
scores = [8, 9, 8, 7]

# 1. Dùng zip(..., strict=True) ghép hai list và enumerate(..., start=1) để đánh số
for position, (topic, score) in enumerate(
    zip(topics, scores, strict=True), start=1
):
    print(f"{position}. {topic}: {score}")

# 2. Dùng comprehension đơn giản để lấy các điểm đạt từ 8 trở lên
strong_scores = [score for score in scores if score >= 8]
print(f"strong_scores={strong_scores}")

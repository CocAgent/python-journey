"""Exercise 01: for, range, enumerate and zip."""

topics = ["loops", "enumerate", "zip"]
scores = [7, 8, 9]

# TODO 1: print numbers 1 through 5 with range.
for i in range(1, 6):
    print(i)

# TODO 2: print each topic with a one-based position using enumerate.
for position, topic in enumerate(topics, start=1):
    print(position, topic)

# TODO 3: pair topics and scores with zip(..., strict=True).
for topic, score in zip(topics, scores, strict=True):
    print(topic, score)

print(topics, scores)

"""Exercise 01: for, range, enumerate and zip."""

topics = ["loops", "enumerate", "zip"]
scores = [7, 8, 9]

# TODO: print numbers 1 through 5 with range.
for i in range (5):
    print (i)
# TODO: print each topic with a one-based position using enumerate.
for index, topic in enumerate (topics,start=1):
    print(f"{index}.{topic}")

# TODO: pair topics and scores with zip(..., strict=True).
for topic, score in zip(topics, scores, strict=True):
    print(f"{topic}: {score}")
print(topics, scores)

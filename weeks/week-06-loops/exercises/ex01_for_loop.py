"""Exercise 01: for, range, enumerate and zip."""

topics = ["loops", "enumerate", "zip"]
scores = [7, 8, 9]

# In các số từ 1 đến 5 bằng range
print("Các số từ 1 đến 5:")
for num in range(1, 6):
    print(num)

# In từng topic với vị trí bắt đầu từ 1 bằng enumerate
print("\nDanh sách topic:")
for pos, topic in enumerate(topics, start=1):
    print(f"{pos}. {topic}")

# Ghép cặp topics và scores bằng zip(..., strict=True)
print("\nGhép cặp topic và score:")
for topic, score in zip(topics, scores, strict=True):
    print(f"{topic}: {score}")

print("\nDanh sách ban đầu:", topics, scores)

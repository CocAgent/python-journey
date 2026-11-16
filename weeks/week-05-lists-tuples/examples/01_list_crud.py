"""Create, read, update and remove list items."""

topics = ["strings", "lists", "tuples"]
topics.append("mutability")
topics.insert(1, "slicing")
topics[0] = "text processing"
topics.remove("tuples")

print(topics)
print(f"first={topics[0]}")
print(f"last={topics[-1]}")

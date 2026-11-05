"""Pack and unpack small fixed groups of values."""

coordinate = (3, 7)
x, y = coordinate
print(f"x={x}, y={y}")

profile = "An", 20, "Python"
name, age, topic = profile
print(f"{name} is {age} and studies {topic}")

left = "A"
right = "B"
left, right = right, left
print(left, right)

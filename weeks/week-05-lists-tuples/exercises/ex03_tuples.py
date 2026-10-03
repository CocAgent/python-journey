"""Exercise 03: tuple, packing and unpacking."""

coordinate = (3, 7)

# TODO: unpack coordinate into x and y.
x, y = coordinate      # x = 3, y = 7

# TODO: pack name, age and topic into one profile tuple, then unpack it.
profile: tuple[str, int, str] = ("An", 20, "Python")
name, age, topic = profile  # giải nén lại

# TODO: swap left and right using unpacking.
left  = "A"
right = "B"
left, right = right, left   # swap không cần biến tạm

print(x, y, profile, left, right)

# --- Bonus: kiểm tra kết quả ---
print(f"\nx={x}, y={y}")
print(f"name={name!r}, age={age}, topic={topic!r}")
print(f"left={left!r}, right={right!r}  (đã hoán đổi)")

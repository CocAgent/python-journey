"""Use for and while with visible boundaries."""

for number in range(1, 4):
    print(f"for={number}")

remaining = 3
while remaining > 0:
    print(f"remaining={remaining}")
    remaining -= 1

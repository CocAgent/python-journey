"""Exercise 02: while, break and continue."""

remaining = 5

# TODO 1: count down to 1 and update remaining on every pass.
while remaining >= 1:
    print(remaining)
    remaining -= 1

# TODO 2: loop through 1..10, skip multiples of 3 and stop after 8.
for i in range(1, 11):
    if i % 3 == 0:
        continue

    if i > 8:
        break

    print(i)

print(remaining)

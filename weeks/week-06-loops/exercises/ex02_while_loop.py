"""Exercise 02: while, break and continue."""

remaining = 5

# TODO: count down to 1 and update remaining on every pass.
while remaining > 0:
    print(remaining)
    remaining -= 1


# TODO: loop through 1..10, skip multiples of 3 and stop after 8.
i = 1
while i <= 10:
    if i > 8:
        break
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1

print(remaining)

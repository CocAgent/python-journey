"""Exercise 02: while, break and continue."""

remaining = 5

# TODO: count down to 1 and update remaining on every pass.
while remaining >= 1:
    print(remaining)
    remaining -= 1
# TODO: loop through 1..10, skip multiples of 3 and stop after 8.
for numbers in range(1, 11):
    if numbers % 3 == 0:
        continue
    if numbers > 8:
        break
    print(numbers)

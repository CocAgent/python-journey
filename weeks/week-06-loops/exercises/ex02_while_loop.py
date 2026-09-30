"""Exercise 02: while, break and continue."""

remaining = 5

# TODO: count down to 1 and update remaining on every pass.
while remaining > 0:
    print(remaining)
    remaining -= 1

# TODO: loop through 1..10, skip multiples of 3 and stop after 8.
number = 1
while number <= 10:
    if number > 8:
        break
    if number % 3 == 0:
        number += 1
        continue
    print(number)
    number += 1

print(remaining)
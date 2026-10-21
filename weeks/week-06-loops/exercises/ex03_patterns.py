"""Exercise 03: readable list comprehensions."""

numbers = range(1, 11)

# TODO: build squares for all numbers.
squares: list[int] = [x**2 for x in numbers]
# TODO: build even_numbers with one filter.
even_numbers: list[int] = [x for x in numbers if x % 2 == 0]
# TODO: rewrite one comprehension as a normal loop and compare readability.
odd_numbers: list[int] = []
for x in numbers:
    if x % 2 == 1:
        odd_numbers.append(x)

print(squares, even_numbers, odd_numbers)

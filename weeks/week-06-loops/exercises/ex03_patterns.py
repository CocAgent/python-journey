"""Exercise 03: readable list comprehensions."""

numbers = range(1, 11)

# TODO: build squares for all numbers.
squares: list[int] = [x**2 for x in numbers]

# TODO: build even_numbers with one filter.
even_numbers: list[int] = [x for x in numbers if x % 2 == 0]

# TODO: rewrite one comprehension as a normal loop and compare readability.
# Viết lại even_numbers dạng vòng lặp thường (for loop):
even_numbers_loop: list[int] = []
for x in numbers:
    if x % 2 == 0:
        even_numbers_loop.append(x)

print(squares, even_numbers)
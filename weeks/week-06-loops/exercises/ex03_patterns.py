"""Exercise 03: readable list comprehensions."""

numbers = range(1, 11)

# TODO: build squares for all numbers.
squares: list[int] = [number ** 2 for number in numbers]
# TODO: build even_numbers with one filter.
even_numbers: list[int] = [number for number in numbers if number % 2 == 0]
# TODO: rewrite one comprehension as a normal loop and compare readability.
squares_loop: list[int] = []
for number in numbers:
    squares_loop.append(number ** 2)
print(squares, even_numbers)

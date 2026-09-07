"""Keep comprehensions small and readable."""

numbers = range(1, 7)
squares = [number**2 for number in numbers]
even_squares = [number**2 for number in numbers if number % 2 == 0]

print(squares)
print(even_squares)

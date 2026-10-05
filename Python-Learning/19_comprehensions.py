"""Lesson 19 — Comprehensions: build collections in one line. Author: Adarsh."""
numbers = range(1, 11)

# List comprehension: [expression for item in iterable]
squares = [n * n for n in numbers]
print(squares)

# With a filter condition
evens = [n for n in numbers if n % 2 == 0]
print(evens)

# Transform + filter together
even_squares = [n * n for n in numbers if n % 2 == 0]
print(even_squares)

# Apply a function
words = ["  hi ", "bye ", " nice"]
cleaned = [w.strip().upper() for w in words]
print(cleaned)

# Dict comprehension: {key_expr: value_expr for item in iterable}
lengths = {w: len(w) for w in ["python", "git", "ai"]}
print(lengths)

# Set comprehension
unique_first_letters = {city[0] for city in ["Delhi", "Mumbai", "Daman"]}
print(unique_first_letters)

# Generator expression — lazy, memory-friendly ( ) not [ ]
total = sum(n * n for n in numbers)
print(total)     # 385

# Nested comprehension: flatten a grid
grid = [[1, 2, 3], [4, 5, 6]]
flat = [cell for row in grid for cell in row]
print(flat)      # [1, 2, 3, 4, 5, 6]

# Conditional expression inside (value_if_true if cond else value_if_false)
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(labels[:5])

# Readability rule: if it spans many conditions, use a normal loop instead.

# Practice: from "python", make a dict {letter: ord(letter)} via comprehension.

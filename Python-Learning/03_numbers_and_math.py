"""Lesson 03 — Numbers and math operators. Author: Adarsh."""
x = 7
y = 3

print(x + y)    # 10   addition
print(x - y)    # 4    subtraction
print(x * y)    # 21   multiplication
print(x / y)    # 2.33... true division (always float)
print(x // y)   # 2    floor division (rounds down)
print(x % y)    # 1    modulo (remainder)
print(x ** y)   # 343  exponent (power)

# Augmented assignment
count = 10
count += 5      # count = count + 5 -> 15
count *= 2      # -> 30
print(count)

# Useful built-ins and the math module
print(abs(-8), round(3.567, 2), min(4, 2, 9), max(4, 2, 9))

import math
print(math.sqrt(16))       # 4.0
print(math.pi)             # 3.14159...
print(math.ceil(2.1))      # 3
print(math.floor(2.9))     # 2

# Floats are approximate — never compare with ==
print(0.1 + 0.2)                     # 0.30000000000000004
print(math.isclose(0.1 + 0.2, 0.3)) # True — the right way

# Practice: compute the area of a circle with radius 5 using math.pi.

"""Lesson 02 — Variables and core data types. Author: Adarsh."""
# A variable is a name bound to a value. No type declaration needed.
age = 25                # int      (whole number)
height = 5.9            # float    (decimal)
name = "Adarsh"         # str      (text)
is_learning = True      # bool     (True / False)
nothing = None          # NoneType ("no value yet")

# type() tells you what a value is
print(type(age), type(height), type(name), type(is_learning), type(nothing))

# Dynamic typing: a name can be rebound to a different type
x = 10
x = "ten"
print(x, type(x))

# Casting between types
n = "42"
print(int(n) + 1)       # str -> int, arithmetic works: 43
print(float(n))         # 42.0
print(str(3.14))        # '3.14'
# int("abc") would raise ValueError — lesson 25 covers errors.

# Multiple assignment and swapping
a, b = 1, 2
a, b = b, a             # classic Python swap, no temp variable
print(a, b)             # 2 1

# Practice: make variables for your name, age, and pi; print them with types.

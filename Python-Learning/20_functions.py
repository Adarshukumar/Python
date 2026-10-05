"""Lesson 20 — Functions. Author: Adarsh."""
# def name(parameters): body — package logic for reuse and clarity
def greet(name):
    """Return a greeting string. (This is a docstring.)"""
    return f"Hello, {name}!"

print(greet("Adarsh"))

# Return value vs printing: return lets the CALLER decide what to do
def add(a, b):
    return a + b

result = add(2, 3) * 10       # can keep calculating with it
print(result)

# Default arguments
def power(base, exponent=2):
    return base ** exponent
print(power(5), power(5, 3))  # 25 125

# Keyword arguments — order doesn't matter, code reads clearly
def make_profile(name, age, city="Delhi"):
    return f"{name}, {age}, {city}"
print(make_profile("Adarsh", 21))
print(make_profile(age=22, name="Riya", city="Mumbai"))

# A function without return returns None
def say_hi():
    print("hi")
value = say_hi()
print(value)                  # None

# Multiple returns = tuple
def divmod_(a, b):
    return a // b, a % b
q, r = divmod_(17, 5)
print(q, r)

# Early return pattern
def is_even(n):
    if n % 2 == 0:
        return True
    return False

# Docstrings are visible via help()
help(greet)

# Practice: write is_leap_year(year) returning True/False (look up the rule).

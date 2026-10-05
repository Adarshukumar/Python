"""Lesson 07 — Booleans, comparisons, truthiness. Author: Adarsh."""
a, b = 10, 3

print(a > b, a < b, a >= 10, a <= 9)   # True False True False
print(a == 10, a != 5)                 # equality / inequality
print(1 < a < 20)                      # chained comparison: True

# Logic operators: and, or, not
age, has_id = 20, True
print(age >= 18 and has_id)    # True — both must hold
print(age < 18 or has_id)      # True — at least one holds
print(not has_id)              # False

# Truthiness: these are all "falsy"
falsy = [0, 0.0, "", [], {}, set(), None]
for value in falsy:
    print(bool(value), repr(value))    # all False

# Everything else is truthy — very useful in conditions
items = []
if not items:
    print("The list is empty")

# Short-circuit evaluation
def check():
    print("check() ran")
    return True
False and check()     # check() never runs — Python skips it
True or check()       # check() never runs here either

# is vs ==
x = [1, 2]; y = [1, 2]
print(x == y)   # True  — same VALUES
print(x is y)    # False — different OBJECTS in memory
print(x is x)    # True
# Use `is` only for None / singletons: `if value is None:`

# Practice: write a condition true only when score is between 60 and 100.

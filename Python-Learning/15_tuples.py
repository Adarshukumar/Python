"""Lesson 15 — Tuples: immutable sequences. Author: Adarsh."""
point = (3, 7)
rgb = 255, 200, 100        # parentheses optional
single = (42,)             # one-element tuple NEEDS the comma

print(point[0], rgb[2])    # index like lists
print(len(rgb))            # 3

# Tuples cannot be changed
# point[0] = 9             # TypeError!

# Tuple unpacking — assign many variables at once
x, y = point
r, g, b = rgb
print(f"x={x} y={y} r={r}")

# Swap variables (tuple packing behind the scenes)
a, b = 1, 2
a, b = b, a

# Star-unpacking: collect the rest
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)     # 1 [2, 3, 4] 5

# Returning multiple values from a function
def min_max(values):
    return min(values), max(values)   # returns a tuple
lo, hi = min_max([4, 9, 1])
print(lo, hi)

# Tuples are hashable -> usable as dict keys and set members
locations = {(28.6, 77.2): "Delhi", (19.1, 72.9): "Mumbai"}
print(locations[(28.6, 77.2)])

# tuple() constructor and list<->tuple conversion
print(tuple([1, 2, 3]), list((4, 5)))

# Practice: unpack (name, age, city) from a tuple and print a sentence.

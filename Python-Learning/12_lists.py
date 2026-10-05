"""Lesson 12 — Lists: ordered, mutable collections. Author: Adarsh."""
numbers = [10, 20, 30, 40]
mixed = [1, "two", 3.0, True, [5, 6]]    # any types, even nested lists
empty = []

print(len(numbers))      # 4
print(numbers[0])        # 10 (first)
print(numbers[-1])       # 40 (last)
print(mixed[4][1])       # 6  (index into nested list)

# Lists are mutable — change in place
numbers[1] = 99
print(numbers)           # [10, 99, 30, 40]

# Slicing returns a NEW list (copies elements)
print(numbers[1:3])      # [99, 30]
print(numbers[:2])       # [10, 99]
print(numbers[::2])      # [10, 30] every 2nd element
copy_of = numbers[:]     # full shallow copy

# Concatenation and repetition
print([1, 2] + [3, 4])   # [1, 2, 3, 4]
print([0] * 3)           # [0, 0, 0]

# Membership and iteration
print(30 in numbers)     # True
for n in numbers:
    print(n, end=" ")
print()

# Beware the shared-reference trap
a = [1, 2, 3]
b = a            # same object, NOT a copy
b.append(4)
print(a)         # [1, 2, 3, 4] — a changed too!
print(a is b)    # True

# Practice: build a list of the first 10 square numbers with a loop.

"""Lesson 23 — lambda, map, filter. Author: Adarsh."""
# lambda: tiny anonymous one-expression function
square = lambda x: x * x            # same as def square(x): return x*x
print(square(6))

add = lambda a, b: a + b
print(add(3, 4))

# Lambdas shine as arguments to other functions
pairs = [(1, 9), (2, 3), (3, 5)]
pairs.sort(key=lambda p: p[1])       # sort by second element
print(pairs)

people = [("Adarsh", 21), ("Riya", 19), ("Kiran", 25)]
oldest = max(people, key=lambda p: p[1])
print(oldest)

# map: apply a function to every item -> lazy iterable
numbers = [1, 2, 3, 4]
print(list(map(lambda x: x * 10, numbers)))    # [10, 20, 30, 40]
print(list(map(str.upper, ["a", "b"])))        # ['A', 'B']

# filter: keep items where the function returns True
print(list(filter(lambda x: x % 2 == 0, numbers)))   # [2, 4]

# Comprehensions usually read better than map/filter — prefer them
print([x * 10 for x in numbers])
print([x for x in numbers if x % 2 == 0])

words = ["pear", "fig", "watermelon", "kiwi"]
print(sorted(words, key=lambda w: len(w), reverse=True))

# Practice: use max(key=...) to find the longest word in a sentence.

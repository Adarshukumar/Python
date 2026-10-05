"""Lesson 10 — for loops and range(). Author: Adarsh."""
# for iterates over any sequence — the most common Python loop
for letter in "abc":
    print(letter, end=" ")
print()

for item in [10, 20, 30]:
    print(item, end=" ")
print()

# range(start, stop, step) — stop is excluded
for i in range(5):            print(i, end=" ")   # 0 1 2 3 4
print()
for i in range(2, 6):         print(i, end=" ")   # 2 3 4 5
print()
for i in range(10, 0, -2):    print(i, end=" ")   # 10 8 6 4 2
print()

# enumerate() — index AND value together
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# zip() — walk two lists in parallel
names = ["Adarsh", "Riya"]
scores = [91, 88]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Nested loops — multiplication table
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row*col:3}", end=" ")
    print()

# Practice: print all even numbers from 1 to 20 using range with a step.

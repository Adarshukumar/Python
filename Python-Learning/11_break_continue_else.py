"""Lesson 11 — break, continue, and loop else. Author: Adarsh."""
# break exits the loop entirely
for n in [3, 7, 12, 5, 8]:
    if n > 10:
        print("Found a big number:", n)
        break
    print("small:", n)

# continue skips to the next iteration
for n in range(1, 11):
    if n % 2 == 0:
        continue          # skip even numbers
    print(n, end=" ")     # 1 3 5 7 9
print()

# The rarely-seen but neat loop `else`:
# it runs only if the loop finished WITHOUT break.
target = 6
for n in [2, 4, 8]:
    if n == target:
        print("found", n)
        break
else:
    print(f"{target} was not in the list")   # this runs

# Searching with a flag variable (alternative style)
found = False
for n in [2, 4, 8]:
    if n == target:
        found = True
        break
print("found via flag:", found)

# While + break: retry pattern
attempts = 0
while True:
    attempts += 1
    if attempts >= 3:
        print("giving up after", attempts, "attempts")
        break

# Practice: loop 1..50, skip multiples of 3, stop at 40 (print the rest).

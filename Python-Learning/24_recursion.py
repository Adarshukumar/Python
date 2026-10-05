"""Lesson 24 — Recursion. Author: Adarsh."""
# A function that calls itself. Every recursion needs:
#   1. a BASE CASE that stops the chain
#   2. a step that moves toward the base case

def countdown(n):
    if n == 0:                 # base case
        print("Lift off!")
        return
    print(n, end=" ")
    countdown(n - 1)           # recursive step
countdown(5); print()

def factorial(n):
    if n <= 1:                 # base case
        return 1
    return n * factorial(n - 1)
print(factorial(6))            # 720

# Fibonacci (naive — slow for big n, but clear)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
print([fib(i) for i in range(10)])

# Recursive sum of a nested list — recursion shines on nested data
def deep_sum(item):
    total = 0
    for element in item:
        if isinstance(element, list):
            total += deep_sum(element)   # recurse into sublist
        else:
            total += element
    return total
print(deep_sum([1, [2, [3, 4]], 5]))     # 15

import sys
print("recursion limit:", sys.getrecursionlimit())

# Iterative factorial — same result, no stack risk
def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Practice: write recursive sum_digits(1234) -> 1+2+3+4 = 10.

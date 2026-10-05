"""Lesson 44 — Generators, iterators, and context managers. Author: Adarsh."""

# A generator uses yield to produce values one at a time — lazily.
def countdown(n):
    print("starting countdown")
    while n > 0:
        yield n              # pause here, hand back a value
        n -= 1

for x in countdown(3):
    print(x, end=" ")        # 3 2 1
print()

gen = countdown(2)
print(next(gen))             # starts function, runs to first yield -> 2
print(next(gen))             # resumes -> 1
# next(gen) again -> StopIteration (exhausted)

# Memory win: range-like object vs a giant list
import sys
big_list = [i * i for i in range(100_000)]
big_gen  = (i * i for i in range(100_000))    # generator expression
print(f"list: {sys.getsizeof(big_list):,} bytes | generator: {sys.getsizeof(big_gen)} bytes")

# Generator pipeline — process data in stages without holding everything
def read_numbers(text):
    for token in text.split():
        yield int(token)

def only_even(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

def squared(nums):
    for n in nums:
        yield n * n

data = "1 2 3 4 5 6 7 8"
print(list(squared(only_even(read_numbers(data)))))   # [4, 16, 36, 64]

# yield from — delegate to a sub-generator
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
print(list(flatten([1, [2, [3, 4]], 5])))            # [1, 2, 3, 4, 5]

# Context manager: the `with` statement — setup + guaranteed teardown
from contextlib import contextmanager

@contextmanager
def timer(label):
    import time
    start = time.perf_counter()
    try:
        yield                                   # body of the with block runs here
    finally:
        print(f"[{label}] {time.perf_counter() - start:.4f}s")

with timer("sleep"):
    total = sum(range(500_000))
print("total:", total)

# Class-based context manager: __enter__ / __exit__
class Tag:
    def __init__(self, name): self.name = name
    def __enter__(self):
        print(f"<{self.name}>", end=" ")
        return self                     # the `as` variable
    def __exit__(self, exc_type, exc_val, tb):
        print(f"</{self.name}>")
        return False                    # don't swallow exceptions

with Tag("greeting"):
    print("hello from Adarsh", end=" ")
print()

# Practice: generator fibonacci(n) then sum the first 20 fibonacci numbers.

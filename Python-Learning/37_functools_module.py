"""Lesson 37 — functools: function tools. Author: Adarsh."""
from functools import reduce, partial, lru_cache, wraps, cache
import time

# reduce — fold a list into ONE value
nums = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a * b, nums))       # 120 (factorial-ish)
print(reduce(lambda a, b: a if a > b else b, nums))   # max manually
print(reduce(lambda a, b: a + b, nums, 100))  # 115 (initial value 100)

# partial — pre-fill some arguments
def power(base, exponent):
    return base ** exponent
square = partial(power, exponent=2)
cube = partial(power, exponent=3)
print(square(7), cube(3))

int_base2 = partial(int, base=2)
print(int_base2("1011"))                      # 11

# lru_cache / cache — memoization: never recompute a pure function
@lru_cache(maxsize=None)                      # @cache does the same (3.9+)
def slow_fib(n):
    return n if n < 2 else slow_fib(n - 1) + slow_fib(n - 2)

t0 = time.perf_counter()
print("fib(180) =", slow_fib(180))
print(f"cached fib took {time.perf_counter() - t0:.4f}s")   # instant
print(slow_fib.cache_info())

# Only cache PURE functions — same input must give same output,
# and arguments must be hashable.

# wraps — preserve a function's name/docstring when writing decorators
def my_decorator(func):
    @wraps(func)                              # <- without this, identity is lost
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner

@my_decorator
def greet(name):
    """Greet someone."""
    return f"hi {name}"

print(greet("Adarsh"), "| name:", greet.__name__, "| doc kept:", bool(greet.__doc__))

# total_ordering — fill in all comparisons from __eq__ + one other (advanced)
from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, n): self.n = n
    def __eq__(self, other): return self.n == other.n
    def __lt__(self, other): return self.n < other.n

print(Version(2) < Version(3), Version(3) >= Version(3))

# Practice: time fib(30) with and without caching — see the difference.

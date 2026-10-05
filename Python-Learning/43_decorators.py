"""Lesson 43 — Decorators. Author: Adarsh."""
import functools
import time

# A decorator is a function that takes a function and returns an enhanced one.
def shout(func):
    @functools.wraps(func)                 # keep name/docstring of the original
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() + "!!!"
    return wrapper

@shout                                      # same as: greet = shout(greet)
def greet(name):
    """Say hello politely."""
    return f"hello {name}"

print(greet("Adarsh"))                     # HELLO ADARSH!!!
print(greet.__name__)                      # greet (thanks to @wraps)

# Practical decorator #1: timing
def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        ms = (time.perf_counter() - start) * 1000
        print(f"[timed] {func.__name__} took {ms:.2f} ms")
        return result
    return wrapper

@timed
def slow_sum():
    return sum(range(1_000_000))
print("sum:", slow_sum())

# Practical decorator #2: call counting
def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"  call #{wrapper.calls} to {func.__name__}")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def step(): return "done"
step(); step(); step()

# Decorator WITH arguments = three levels of nesting
def repeat(n):                              # takes the argument...
    def decorator(func):                    # ...takes the function...
        @functools.wraps(func)
        def wrapper(*args, **kwargs):       # ...takes the call's args
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(n=3)
def ping():
    print("  ping", end=" | ")
print(); print(ping())

# Stacking: applied bottom-up (bold runs inside shout's wrapper)
def bold(func):
    @functools.wraps(func)
    def wrapper(*a, **kw): return "**" + func(*a, **kw) + "**"
    return wrapper

@shout
@bold
def cheer(): return "go adarsh"
print(cheer())                              # **GO ADARSH**!!!

# Practice: write a decorator that retries a function up to 3 times on failure.

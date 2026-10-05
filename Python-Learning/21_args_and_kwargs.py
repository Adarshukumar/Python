"""Lesson 21 — *args and **kwargs. Author: Adarsh."""
# *args collects EXTRA positional args into a tuple
def add_all(*args):
    print(type(args))          # <class 'tuple'>
    return sum(args)
print(add_all(1, 2, 3, 4))     # 10

# **kwargs collects extra keyword args into a dict
def show_profile(**kwargs):
    print(type(kwargs))        # <class 'dict'>
    for key, value in kwargs.items():
        print(f"  {key} = {value}")
show_profile(name="Adarsh", age=21, city="Delhi")

# Combined — standard order: positional, keyword, *args, **kwargs
def report(title, *args, unit="cm", **kwargs):
    print("TITLE:", title)
    print("values:", args)
    print("unit:", unit)
    print("extra:", kwargs)
report("Sizes", 10, 20, 30, unit="m", owner="Adarsh", urgent=True)

# Unpacking at the CALL site — the mirror image
def area(width, height):
    return width * height
dims = [4, 5]
print(area(*dims))             # same as area(4, 5)

settings = {"width": 3, "height": 6}
print(area(**settings))        # keyword unpacking

# Real-world use: forwarding arguments to another function
def logged_call(func, *args, **kwargs):
    print("calling with", args, kwargs)
    return func(*args, **kwargs)
print(logged_call(area, 2, 8))

# Practice: write describe(name, **facts) that prints each fact as 'key: value'.

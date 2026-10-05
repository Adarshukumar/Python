"""Lesson 22 — Scope: LEGB rule. Author: Adarsh."""
# Python looks names up in: Local -> Enclosing -> Global -> Built-in

message = "I am global"

def outer():
    message = "I am enclosing"          # enclosing scope

    def inner():
        message = "I am local"          # local scope
        print("inner sees:", message)
    inner()
    print("outer sees:", message)

outer()
print("module sees:", message)

# Reading a global from a function works fine
count = 0
def show():
    print("count is", count)   # reading is OK
show()

# MODIFYING a global needs the global keyword
def bump():
    global count
    count += 1
bump(); bump()
print("after bumps:", count)   # 2

# Prefer passing values as parameters over globals — clearer and testable
counter = {"n": 0}             # mutable workaround people use
def bump_dict():
    counter["n"] += 1

# nonlocal: modify the ENCLOSING function's variable (closures)
def make_counter():
    n = 0
    def increment():
        nonlocal n
        n += 1
        return n
    return increment

tick = make_counter()
print(tick(), tick(), tick())  # 1 2 3 — closure keeps its own n

# Practice: predict the output of outer()/inner() above before running. Then run.

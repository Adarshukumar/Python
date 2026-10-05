"""Lesson 25 — Errors and exception handling. Author: Adarsh."""
# Exceptions crash your program — unless you catch them.
# try: risky code  except: recovery code

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None

print(divide(10, 2))    # 5.0
print(divide(10, 0))    # message + None

# Catching multiple exception types
def to_int(text):
    try:
        return int(text)
    except ValueError:              # bad text
        return 0
    except TypeError as e:          # wrong type entirely
        print("Type problem:", e)
        return 0
print(to_int("42"), to_int("abc"))

# finally and else
def process(filename):
    try:
        f = open(filename)
    except FileNotFoundError:
        print("missing:", filename)
        return
    else:                 # runs only if NO exception happened
        print("opened OK")
        f.close()
    finally:              # ALWAYS runs — cleanup spot
        print("done with", filename)
process("does_not_exist.txt")

# Common exceptions you will meet
for risky, exc in [
    (lambda: 1 / 0,               ZeroDivisionError),
    (lambda: [1][5],              IndexError),
    (lambda: {}["k"],             KeyError),
    (lambda: int("x"),            ValueError),
    (lambda: "a" + 1,             TypeError),
    (lambda: undefined_var,       NameError),
]:
    try:
        risky()
    except exc as e:
        print(f"{exc.__name__:>20}: {e}")

# Raising your own exceptions
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age

# Practice: wrap input("number: ") in try/except until the user types an int.

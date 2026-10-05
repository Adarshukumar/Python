"""Lesson 26 — Custom exception classes. Author: Adarsh."""
# Subclass Exception to describe YOUR program's failure modes precisely.

class AppError(Exception):
    """Base class for all errors in this app."""
    pass

class InvalidPasswordError(AppError):
    def __init__(self, password, reason):
        super().__init__(f"weak password: {reason}")
        self.password_len = len(password)
        self.reason = reason

class OutOfStockError(AppError):
    def __init__(self, item):
        super().__init__(f"'{item}' is out of stock")
        self.item = item

def register(password):
    if len(password) < 8:
        raise InvalidPasswordError(password, "needs 8+ characters")

def order(item, stock):
    if item not in stock:
        raise OutOfStockError(item)
    return f"ordered {item}"

# Catch the specific class, or the shared base class
try:
    register("short")
except InvalidPasswordError as e:
    print("Registration failed:", e, "| reason:", e.reason)

stock = ["apple", "banana"]
for want in ["apple", "mango"]:
    try:
        print(order(want, stock))
    except OutOfStockError as e:
        print("Order failed:", e)

# One handler for the whole family
try:
    order("mango", stock)
except AppError as e:
    print("Some app error occurred:", type(e).__name__)

# Exception hierarchy reminder:
# BaseException -> Exception -> ValueError, KeyError, ... -> YOUR classes
# Rule: catch narrowly, raise specifically, never write bare `except:`.

# Practice: create UnderAgeError and raise it from check_age(int(input())).

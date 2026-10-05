"""Lesson 42 — property, classmethod, staticmethod. Author: Adarsh."""
class Temperature:
    def __init__(self, celsius=0.0):
        self._celsius = celsius            # underscore = "internal" convention

    @property
    def celsius(self):                     # read t.celsius
        return self._celsius

    @celsius.setter
    def celsius(self, value):              # write t.celsius = 25
        if value < -273.15:
            raise ValueError("below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):                  # computed attribute — no storage
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9

    @classmethod
    def from_fahrenheit(cls, value):       # alternative constructor
        t = cls()
        t.fahrenheit = value
        return t

    @staticmethod
    def is_freezing(c):                    # utility — no self, no cls
        return c <= 0

t = Temperature(25)
print(t.celsius, t.fahrenheit)             # 25 77.0
t.fahrenheit = 100
print(t.celsius)                           # 37.77...

try:
    t.celsius = -300
except ValueError as e:
    print("blocked:", e)

t2 = Temperature.from_fahrenheit(212)
print("boiling point:", t2.celsius)          # 100.0
print(Temperature.is_freezing(-1), Temperature.is_freezing(10))

# Summary:
# @property      -> attribute-style access to computed/validated values
# @x.setter      -> run code on assignment (validation!)
# @classmethod   -> factory methods; cls is the CLASS (subclass-friendly)
# @staticmethod  -> plain function living inside the class namespace

# Realistic example: read-only property
class Disk:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        import math
        return math.pi * self.radius ** 2

d = Disk(2)
print(f"area: {d.area:.2f}")      # 12.57 — no () needed, it's a property
# d.area = 5                      # AttributeError — read-only

# Practice: Wallet with balance property that blocks negative values.

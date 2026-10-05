"""Lesson 39 — Inheritance and polymorphism. Author: Adarsh."""
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def intro(self):
        return f"I am {self.name} and I say {self.speak()}"

class Dog(Animal):                     # Dog IS-A Animal
    def speak(self):                   # override the parent method
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Puppy(Dog):
    def speak(self):                   # extend instead of replace
        return super().speak() + " (tiny woof)"

# Same call, different behavior = polymorphism
for pet in [Dog("Rocky"), Cat("Simba"), Puppy("Bruno")]:
    print(pet.intro())

# super() calls the parent — used for __init__ chaining too
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

class Car(Vehicle):
    def __init__(self, brand, seats):
        super().__init__(brand, wheels=4)   # let parent set brand/wheels
        self.seats = seats

c = Car("Tata", 5)
print(c.brand, c.wheels, c.seats)

# isinstance works through the whole chain
print(isinstance(c, Vehicle), isinstance(c, Car))

# Multiple inheritance & MRO
class Flyer:
    def move(self): return "flies"
class Swimmer:
    def move(self): return "swims"
class Duck(Flyer, Swimmer):           # left parent wins conflicts
    pass
print(Duck().move())                  # 'flies'
print([k.__name__ for k in Duck.__mro__])

# Abstract base classes — force subclasses to implement methods
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): ...

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2

# Shape() would raise TypeError — can't instantiate abstract class
print(Square(4).area())

# Practice: make Employee -> Manager with a raise_salary() override.

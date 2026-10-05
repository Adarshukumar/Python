"""Lesson 38 — Classes and objects. Author: Adarsh."""
# A class is a blueprint; an object is one thing built from it.
class Student:
    school = "ZCode Academy"          # class attribute — shared by ALL objects

    def __init__(self, name, marks):  # runs when the object is created
        self.name = name              # instance attributes — per object
        self.marks = marks

    def describe(self):               # method — self is the object itself
        return f"{self.name} ({self.school}) scored {self.average():.1f}"

    def average(self):
        return sum(self.marks) / len(self.marks)

    def __repr__(self):               # how the object prints
        return f"Student({self.name!r})"

adarsh = Student("Adarsh", [88, 91, 79])      # __init__ runs here
riya = Student("Riya", [95, 90, 99])

print(adarsh.name, riya.name)         # each object keeps its own data
print(adarsh.describe())
print(riya.describe())
print(adarsh)                         # uses __repr__

# Class vs instance attributes
print(Student.school)                 # via the class
adarsh.school = "Night School"        # shadows only for THIS object
print(adarsh.school, "|", riya.school, "|", Student.school)

# Objects are mutable; methods can change them
riya.marks.append(100)
print(riya.describe())

# isinstance and type
print(isinstance(adarsh, Student), type(adarsh) is Student)

# Everything in Python is an object
print((3).bit_length(), "hi".upper, isinstance(print, object))

# Practice: create a Book class with title/author/pages + a describe() method.

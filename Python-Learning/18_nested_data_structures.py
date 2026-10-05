"""Lesson 18 — Nested data structures. Author: Adarsh."""
# Real programs combine lists + dicts. This looks like JSON/API data.
contacts = [
    {"name": "Adarsh", "phone": "98xxx", "skills": ["python", "git"]},
    {"name": "Riya",   "phone": "97xxx", "skills": ["python", "sql"]},
    {"name": "Kiran",  "phone": "96xxx", "skills": ["java"]},
]

# Chain indexing to reach deep values
print(contacts[0]["name"])            # Adarsh
print(contacts[1]["skills"][1])       # sql

# Loop over structured data
for person in contacts:
    print(f"{person['name']:<6} {person['phone']} knows: {', '.join(person['skills'])}")

# Search the structure
def find_person(people, name):
    for person in people:
        if person["name"].lower() == name.lower():
            return person
    return None

print(find_person(contacts, "riya"))
print(find_person(contacts, "nobody"))    # None

# Safely reaching into possibly-missing data
maybe = find_person(contacts, "nobody")
print(maybe.get("phone", "no phone") if maybe else "not found")

# Building nested structures
report = {}
for person in contacts:
    report[person["name"]] = len(person["skills"])
print(report)     # {'Adarsh': 2, 'Riya': 2, 'Kiran': 1}

# Grid = list of lists
grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
for row in grid:
    for cell in row:
        print(cell, end=" ")
print()
print(grid[1][2])    # 6 — row 1, column 2

# Practice: add a new contact dict to contacts, then print all names.

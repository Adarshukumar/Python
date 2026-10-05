"""Lesson 17 — Dictionaries: key -> value maps. Author: Adarsh."""
student = {"name": "Adarsh", "age": 21, "course": "Python"}

print(student["name"])            # 'Adarsh'
print(student.get("age"))         # 21
print(student.get("grade"))       # None (no crash!)
print(student.get("grade", "N/A"))# 'N/A' — default value

student["age"] = 22               # update existing
student["city"] = "Delhi"         # add new key
del student["course"]             # remove key
print(student)

print("name" in student)          # True — checks KEYS
print(len(student))

# Iterating
for key in student:
    print(key, "->", student[key])

for key, value in student.items():
    print(f"{key:>5}: {value}")

print(list(student.keys()))
print(list(student.values()))

# Counting pattern — extremely common
word = "mississippi"
counts = {}
for ch in word:
    counts[ch] = counts.get(ch, 0) + 1
print(counts)                     # {'m':1,'i':4,'s':4,'p':2}

# Merging (Python 3.5+ / 3.9+)
defaults = {"theme": "light", "font": 12}
user = {"theme": "dark"}
print({**defaults, **user})       # {'theme':'dark','font':12}
print(defaults | user)            # same, 3.9+ syntax

# Values can be anything — nested dicts, lists...
school = {"class": {"strength": 30, "topper": "Riya"}}

# Keys must be hashable (str, int, tuple OK; list NOT ok)
# {"[1,2]": "x"}   # fine — that's a string key
# {[1, 2]: "x"}    # TypeError — list is unhashable

# Practice: count word frequencies in "the cat and the dog and the bird".

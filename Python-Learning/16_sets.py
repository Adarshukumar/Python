"""Lesson 16 — Sets: unique, unordered items. Author: Adarsh."""
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
empty = set()            # {} would create an EMPTY DICT, not a set!

# Duplicates vanish automatically
print({1, 1, 2, 2, 3})   # {1, 2, 3}
letters = set("banana")
print(letters)           # {'a', 'b', 'n'} — unordered!

# Fast membership test (O(1) — much faster than lists for big data)
print(3 in a)            # True

# Set algebra
print(a | b)             # union:           {1,2,3,4,5,6}
print(a & b)             # intersection:    {3, 4}
print(a - b)             # difference:      {1, 2}
print(a ^ b)             # symmetric diff:  {1, 2, 5, 6}

print(a.issubset(b), a.issuperset({1, 2}))

# Mutating sets
a.add(10)
a.discard(99)            # no error if missing
a.remove(1)              # KeyError if missing
frozen = frozenset([1, 2, 3])   # immutable set — hashable

# Classic use: deduplicate a list (order not preserved)
names = ["adarsh", "riya", "adarsh", "kiran"]
unique = set(names)
print(len(unique))       # 3

# Practice: find which letters two words share using one set operation.

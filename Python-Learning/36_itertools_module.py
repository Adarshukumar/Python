"""Lesson 36 — itertools: iteration power tools. Author: Adarsh."""
from itertools import count, cycle, repeat, chain, product, permutations, combinations, groupby, islice, accumulate, zip_longest

# Infinite iterators (always slice/limit them!)
print(list(islice(count(10, 3), 5)))           # [10, 13, 16, 19, 22]
print(list(islice(cycle("AB"), 5)))            # ['A','B','A','B','A']
print(list(repeat("hi", 3)))                   # ['hi','hi','hi']

# chain — glue iterables together
print(list(chain([1, 2], "ab", range(3, 5))))  # [1, 2, 'a', 'b', 3, 4]

# product / permutations / combinations — the combinatorics trio
print(list(product("AB", "12")))               # all pairs: A1 A2 B1 B2
print(list(permutations("ABC", 2)))            # ordered, no repeats
print(list(combinations("ABC", 2)))            # unordered pairs

# accumulate — running totals (and other folds)
print(list(accumulate([1, 2, 3, 4])))          # [1, 3, 6, 10]
print(list(accumulate([2, 5, 3], max)))        # [2, 5, 5]

# zip_longest — zip that pads the shorter list
ids = [1, 2, 3]
names = ["adarsh", "riya"]
print(list(zip_longest(ids, names, fillvalue="?")))

# groupby — group SORTED data by a key
people = [
    {"name": "Adarsh", "team": "dev"},
    {"name": "Riya", "team": "dev"},
    {"name": "Kiran", "team": "ops"},
]
people.sort(key=lambda p: p["team"])           # sort BEFORE grouping!
for team, members in groupby(people, key=lambda p: p["team"]):
    print(team, "->", [m["name"] for m in members])

# starmap / takewhile / dropwhile quick look
from itertools import starmap, takewhile, dropwhile
print(list(starmap(pow, [(2, 3), (3, 2)])))        # [8, 9]
print(list(takewhile(lambda x: x < 3, [1, 2, 5, 1])))  # [1, 2]
print(list(dropwhile(lambda x: x < 3, [1, 2, 5, 1])))  # [5, 1]

# Practice: list every 2-letter arrangement of "abc" (permutations).

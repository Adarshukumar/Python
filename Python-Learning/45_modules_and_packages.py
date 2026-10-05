"""Lesson 45 — Modules and packages. Author: Adarsh."""
# A module is any .py file. A package is a folder of modules with __init__.py.

# The standard library ships with Python — import and go
import math, random, json
from datetime import date                  # import ONE name directly
from os import path as osp                 # rename on import

print(math.sqrt(144), date.today(), osp.join("a", "b"))
random.seed(42)                            # reproducible randomness
print(random.randint(1, 6), random.choice(["a", "b", "c"]))
print(random.sample(range(1, 50), 6))      # lottery picks, no repeats

# import statistics as stats               # common short aliases
import statistics as stats
print(stats.mean([90, 80, 85]), stats.median([1, 9, 5]))

# sys — interpreter internals
import sys
print("python:", sys.version.split()[0], "| script:", sys.argv[0])
print("platform:", sys.platform)

# __name__ == "__main__" — run code only when executed directly,
# NOT when imported. This is the standard script layout:
if __name__ == "__main__":
    print("this file was run directly (not imported)")

# Your own modules: if you had utils.py next to this file:
#   import utils            -> utils.helper()
#   from utils import helper-> helper()
# Packages:
#   mypkg/__init__.py
#   mypkg/core.py          -> from mypkg import core / from mypkg.core import fn

# Third-party packages come from PyPI:  pip install requests
# then: import requests

# Practice: use random to simulate rolling 2 dice 10 times; print each total.

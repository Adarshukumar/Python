"""Lesson 05 — Common string methods. Author: Adarsh."""
s = "  Adarsh Learns Python  "

print(s.strip())                 # remove surrounding whitespace
print(s.lstrip(), "|", s.rstrip())# left-only / right-only strip
print(s.strip().lower())         # 'adarsh learns python'
print(s.strip().upper())         # 'ADARSH LEARNS PYTHON'
print(s.strip().title())         # 'Adarsh Learns Python'

text = "python is fun"
print(text.replace("fun", "powerful"))
print(text.split())              # ['python', 'is', 'fun']  (whitespace split)
print("a,b,c".split(","))        # ['a', 'b', 'c']
print("-".join(["2026", "10", "05"]))   # '2026-10-05'

csv_line = "adarsh,python,42"
name, topic, num = csv_line.split(",")
print(name, topic, num)

print("python".startswith("py")) # True
print("python".endswith("on"))   # True
print("python".find("th"))       # 2 (index; -1 if not found)
print("python".count("t"))       # 1
print("42".isdigit())            # True
print("abc".isalpha())           # True
print("Adarsh123".isalnum())     # True
print("   ".isspace())           # True

# center / ljust / rjust for simple text tables
print("Adarsh".center(20, "="))
print("Python".ljust(10, ".") + "done")

# Practice: ask for a sentence, print it with words reversed and title-cased.

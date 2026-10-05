"""Lesson 08 — if / elif / else. Author: Adarsh."""
temperature = 31

if temperature > 35:
    print("Very hot")
elif temperature > 25:
    print("Warm")           # this branch runs
elif temperature > 10:
    print("Cool")
else:
    print("Cold")

# Conditional expression (ternary) — assign one of two values
score = 74
status = "pass" if score >= 50 else "fail"
print(status)

# Nested conditionals — prefer flattening with and/or
age, member = 16, False
if age >= 18:
    if member:
        print("Welcome back")
    else:
        print("Please sign up")
else:
    print("Adults only")

# match statement (Python 3.10+) — structural pattern matching
command = "start"
match command:
    case "start":
        print("Engine starting")
    case "stop":
        print("Engine stopping")
    case "start" | "restart":        # multiple patterns
        print("Restarting")
    case _:                           # default
        print("Unknown command")

# Practice: convert a numeric grade (0-100) to a letter grade A/B/C/D/F.

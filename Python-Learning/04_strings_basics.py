"""Lesson 04 — String basics. Author: Adarsh."""
s = "Python"

print(len(s))          # 6 — number of characters
print(s[0])            # 'P' — indexing starts at 0
print(s[-1])           # 'n' — negative index counts from the end
print(s[0:3])          # 'Pyt' — substring (stop index excluded)

# Strings are immutable — they cannot be changed in place
# s[0] = "J"  # TypeError!
s = "J" + s[1:]        # build a NEW string instead
print(s)               # 'Jython'

# Concatenation and repetition
greeting = "Hello" + ", " + "Adarsh"
line = "-" * 20
print(greeting)
print(line)

# Iterating characters
for ch in "abc":
    print(ch)

# Membership test
print("yth" in "Python")    # True
print("xyz" not in "Python")# True

# Escape characters
print("Line1\nLine2")       # \n new line
print("Tab:\there")         # \t tab
print("She said \"hi\"")    # \" quote inside string
print(r"C:\new\folder")     # raw string: backslashes kept

# Practice: count how many times 'a' appears in "banana" using a loop.

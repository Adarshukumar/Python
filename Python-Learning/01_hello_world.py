"""Lesson 01 — Hello World, comments, and input(). Author: Adarsh."""
# This is a comment. Python ignores everything after the # symbol.

print("Hello, World!")            # print() writes text to the screen
print("Hello", "Adarsh")          # commas add a space automatically
print("Adarsh", end="!\n")        # end= replaces the default newline

# input() pauses and waits for the user to type something (returns a string)
name = input("What is your name? ")
print("Nice to meet you,", name)

# Multi-line strings use triple quotes
print("""
This is a
multi-line string.
""")

# Practice: print your own banner box around your name using * characters.

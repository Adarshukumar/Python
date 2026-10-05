"""Lesson 28 — Writing and appending to files. Author: Adarsh."""
# Modes: "r" read (default) | "w" write (ERASES existing!) | "a" append | "x" exclusive-new

# "w" — creates the file, or OVERWRITES it completely
with open("notes_28.txt", "w", encoding="utf-8") as f:
    f.write("Shopping list\n")
    f.write("milk\n")

# "a" — appends to the end, keeps existing content
with open("notes_28.txt", "a", encoding="utf-8") as f:
    f.write("bread\n")
    f.writelines(["eggs\n", "chai\n"])    # writes each item, no added \n

with open("notes_28.txt", encoding="utf-8") as f:
    print(f.read())

# Appending to the SAME open file needs seek; simpler to reopen in "a" mode.
# print() can write to files too (file= keyword)
with open("notes_28.txt", "a", encoding="utf-8") as f:
    print("sugar (via print)", file=f)

# "x" mode fails if file exists — protects you from accidental overwrites
try:
    with open("notes_28.txt", "x") as f:
        f.write("never happens")
except FileExistsError:
    print("notes_28.txt already exists — x mode refused to overwrite")

# Binary mode "wb"/"rb" for images and any non-text data
with open("mini_28.bin", "wb") as f:
    f.write(bytes([0, 1, 2, 255]))
with open("mini_28.bin", "rb") as f:
    print("binary read:", list(f.read()))

import os
os.remove("notes_28.txt"); os.remove("mini_28.bin")   # cleanup

# Practice: write a diary app loop — each run appends "date: text" lines.

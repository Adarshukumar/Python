"""Lesson 27 — Reading files. Author: Adarsh."""
# Files are closed automatically when the `with` block exits — always use with!
# Create a demo file first (lesson 28 covers writing in detail)
with open("demo_27.txt", "w", encoding="utf-8") as f:
    f.write("line one: hello Adarsh\nline two: python\nline three: files\n")

# 1) read() — the whole file as ONE string
with open("demo_27.txt", encoding="utf-8") as f:
    content = f.read()
print(content)

# 2) readlines() — list of lines (keeps \n)
with open("demo_27.txt", encoding="utf-8") as f:
    lines = f.readlines()
print("second line:", lines[1].strip())

# 3) BEST: iterate the file object directly — memory-friendly for big files
with open("demo_27.txt", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"  {i}: {line.strip()}")

# read(n) reads only n characters
with open("demo_27.txt", encoding="utf-8") as f:
    print("first 4 chars:", f.read(4))

# File cursor: seek(0) rewinds to the start
with open("demo_27.txt", encoding="utf-8") as f:
    f.read(4)
    f.seek(0)
    print("after seek:", f.readline().strip())

# File existence check
from pathlib import Path
print("exists:", Path("demo_27.txt").exists())

import os
os.remove("demo_27.txt")    # clean up the demo file

# Practice: print only the lines of any file that contain the word 'python'.

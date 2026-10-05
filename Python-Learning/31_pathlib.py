"""Lesson 31 — pathlib: modern path handling. Author: Adarsh."""
from pathlib import Path

# Path objects replace messy string concatenation
p = Path("C:/Users/Adarsh") / "projects" / "demo.txt"
print(p)                    # C:/Users/Adarsh/projects/demo.txt
print(p.name)               # demo.txt
print(p.stem)               # demo
print(p.suffix)             # .txt
print(p.parent)             # C:/Users/Adarsh/projects
print(p.parent.parent)      # C:/Users/Adarsh

home = Path.home()          # user home directory
cwd = Path.cwd()            # current working directory
print("home:", home)
print("cwd :", cwd)

# Building and changing names
csv_path = p.with_suffix(".csv")
print(csv_path)             # .../demo.csv
print(p.with_name("other.txt"))

# Checks
print("cwd exists:", cwd.exists(), "| is dir:", cwd.is_dir())

# Make dirs (parents=True creates missing folders, exist_ok=True no error)
demo = Path("demo_dir_31/sub")
demo.mkdir(parents=True, exist_ok=True)
(demo / "note.txt").write_text("hello from Adarsh", encoding="utf-8")

# Reading/writing whole files in one call
print((demo / "note.txt").read_text(encoding="utf-8"))

# Globbing — find files by pattern (recursively with **)
for txt in demo.glob("*.txt"):
    print("found:", txt)
print(sorted(Path(".").glob("*.py"))[:3])   # lesson files in this folder!

# Cleanup
import shutil; shutil.rmtree("demo_dir_31")

# Practice: count all .py files under the current directory with rglob.

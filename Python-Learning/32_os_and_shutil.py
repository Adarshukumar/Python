"""Lesson 32 — os and shutil: files, folders, processes. Author: Adarsh."""
import os
import shutil

# Environment variables — secrets/config often arrive this way
print("user:", os.environ.get("USERNAME"))
print("path starts:", os.environ.get("PATH", "")[:40])

# Current dir and listing
print("cwd:", os.getcwd())
print("entries here:", len(os.listdir(".")))

# Creating and removing (clear leftovers so re-runs always work)
shutil.rmtree("demo_32", ignore_errors=True)
os.makedirs("demo_32/a/b", exist_ok=True)
open("demo_32/a/b/file.txt", "w").write("data")

# Renaming / moving / copying
os.rename("demo_32/a/b/file.txt", "demo_32/a/b/renamed.txt")
shutil.copy("demo_32/a/b/renamed.txt", "demo_32/copy.txt")
shutil.move("demo_32/copy.txt", "demo_32/a/moved.txt")

# Walking a tree
for dirpath, dirnames, filenames in os.walk("demo_32"):
    print("dir:", dirpath, "| files:", filenames)

# Removing: file vs empty dir vs whole tree
os.remove("demo_32/a/moved.txt")
os.remove("demo_32/a/b/renamed.txt")
os.rmdir("demo_32/a/b")   # only works if EMPTY           # only works if EMPTY
shutil.rmtree("demo_32")          # removes everything — careful!

# Splitting paths (string style — pathlib is nicer)
print(os.path.join("x", "y", "z.txt"))
print(os.path.split("/tmp/report.csv"))     # ('/tmp', 'report.csv')
print(os.path.splitext("photo.png"))        # ('photo', '.png')
print(os.path.getsize("."), "bytes-ish")    # size of cwd entry

# Running other programs
# os.system("echo hello from the shell")   # simple but blind to output
result = os.popen("echo captured output").read()
print("captured:", result.strip())

# Practice: build dir tree demo2/x/y, create 3 files inside, then delete it all.

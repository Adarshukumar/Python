"""Lesson 29 — CSV files with the csv module. Author: Adarsh."""
import csv

rows = [
    ["name", "score", "city"],
    ["Adarsh", "91", "Delhi"],
    ["Riya", "88", "Mumbai"],
    ["Kiran", "79", "Pune"],
]
with open("scores_29.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)                 # write all rows at once

# csv.writer — newline="" is REQUIRED on Windows to avoid blank lines
with open("scores_29.csv", "a", newline="", encoding="utf-8") as f:
    csv.writer(f).writerow(["Meera", "95", "Goa"])

# Reading with csv.reader
with open("scores_29.csv", encoding="utf-8") as f:
    data = list(csv.reader(f))
header, body = data[0], data[1:]
print("header:", header)
for row in body:
    print(row)

# DictReader / DictWriter — work with dicts, forget column indexes
with open("scores_29.csv", encoding="utf-8") as f:
    for record in csv.DictReader(f):
        print(f"{record['name']:<6} {record['city']:<7} {record['score']}")

with open("more_29.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score", "city"])
    writer.writeheader()
    writer.writerow({"name": "Dev", "score": "70", "city": "Jaipur"})

import os
os.remove("scores_29.csv"); os.remove("more_29.csv")

# Practice: write then read back a 2-column CSV of your weekly study hours.

"""Lesson 30 — JSON with the json module. Author: Adarsh."""
import json

# JSON is THE data format of APIs. Python types map onto it:
# dict<->object, list<->array, str<->string, int/float<->number,
# True/False<->true/false, None<->null

profile = {
    "name": "Adarsh",
    "age": 21,
    "skills": ["python", "git", "sql"],
    "active": True,
    "mentor": None,
}

# dumps = dump-string: Python object -> JSON text
text = json.dumps(profile, indent=2)       # indent makes it readable
print(text)

# loads = load-from-string: JSON text -> Python object
back = json.loads(text)
print(back["skills"][0], back["active"], back["mentor"])

# Saving / loading files: dump() and load()
with open("profile_30.json", "w", encoding="utf-8") as f:
    json.dump(profile, f, indent=2)

with open("profile_30.json", encoding="utf-8") as f:
    loaded = json.load(f)
print("from file:", loaded["name"], loaded["age"])

# sort_keys keeps output deterministic
print(json.dumps({"z": 1, "a": 2}, sort_keys=True))

# JSON errors
try:
    json.loads("{not valid json]")
except json.JSONDecodeError as e:
    print("bad JSON:", e.msg, "at char", e.pos)

import os; os.remove("profile_30.json")

# Practice: save a dict of 3 book titles->authors to books.json and read it back.

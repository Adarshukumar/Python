"""Lesson 34 — Regular expressions with re. Author: Adarsh."""
import re

text = "Adarsh paid $49.99 on 2026-10-05, email: adarsh@example.com"

# Core functions ---------------------------------------------------------
print(re.search(r"\d{4}-\d{2}-\d{2}", text).group())   # first match
print(re.findall(r"\d+", text))                        # ['49','99','2026',...]
print(re.sub(r"\$\d+\.\d{2}", "$XX.XX", text))         # replace

# Pattern -> parts
m = re.search(r"(\w+)@(\w+)\.com", text)
if m:
    print("user:", m.group(1), "| domain:", m.group(2))

# Character classes: \d digit  \w word char  \s space   (uppercase = NOT)
# Quantifiers:   * 0+   + 1+   ? 0 or 1   {2,4} between 2 and 4
# Anchors:       ^ start   $ end   \b word boundary

print(re.findall(r"\b\w{5}\b", "power python is truly great fun"))  # 5-letter words

# Matching at start/end
line = "ERROR: disk full"
print(bool(re.match(r"ERROR", line)))      # match anchors at START
print(bool(re.fullmatch(r"ERROR.*", line)))# fullmatch must cover ALL

# Compile once when reusing a pattern (tiny speed win, cleaner code)
hexcode = re.compile(r"#[0-9a-fA-F]{6}")
print(hexcode.findall("colors: #ff0000 and #00FF42"))

# Case-insensitive flag
print(re.findall(r"python", "Python PYTHON python", re.IGNORECASE))

# finditer: match objects with positions
for m in re.finditer(r"\d+", "a1 bb22 ccc333"):
    print(m.group(), "at", m.span())

# Practical: a weak email validator
def looks_like_email(s):
    return bool(re.fullmatch(r"[\w.+-]+@[\w-]+\.[\w.]+", s))
print(looks_like_email("adarsh@example.com"), looks_like_email("nope@@"))

# Practice: extract all capitalized names from "Adarsh and Riya met Kiran".

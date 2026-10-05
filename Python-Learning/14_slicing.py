"""Lesson 14 — Slicing sequences. Author: Adarsh."""
# sequence[start:stop:step] — start included, stop EXCLUDED
s = "PythonLearning"
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(s[0:6])        # 'Python'
print(s[6:])         # 'Learning'
print(s[:6])         # 'Python'
print(s[-7:])        # 'Learning' — negative start counts from end
print(s[:-7])        # 'Python'
print(s[::2])        # every 2nd char: 'Pto enin' style stride
print(s[::-1])       # reversed string: 'gninraeLnohtyP'

print(n[2:5])        # [2, 3, 4]
print(n[-3:])        # [7, 8, 9]   — last three
print(n[::2])        # [0, 2, 4, 6, 8] — even indices
print(n[1::2])       # [1, 3, 5, 7, 9] — odd indices
print(n[::-1])       # full reverse
print(n[5:2:-1])     # [5, 4, 3]  — backwards slice

# Slices never raise IndexError — they clamp gracefully
print(n[100:200])    # []      — out of range is fine
print(s[100:])       # ''      — same for strings

# slice objects (used internally — nice to know)
every_other = slice(0, None, 2)
print(n[every_other])

# Practice: extract the middle third of a 9-element list in one slice.

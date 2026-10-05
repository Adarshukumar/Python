"""Lesson 40 — Dunder (magic) methods: operator overloading. Author: Adarsh."""
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):                    # debug/developer display
        return f"Vector({self.x}, {self.y})"

    def __str__(self):                     # print() / str() display
        return f"({self.x}, {self.y})"

    def __add__(self, other):              # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):              # v1 - v2
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):             # v * 3
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):               # v1 == v2
        return self.x == other.x and self.y == other.y

    def __len__(self):                     # len(v)
        return 2

    def __getitem__(self, i):              # v[0], v[1]
        return (self.x, self.y)[i]

    def __bool__(self):                    # if v: ...
        return bool(self.x or self.y)

    def __call__(self, scale):             # v(10) — object as function
        return self * scale

v1, v2 = Vector(1, 2), Vector(3, 4)
print(repr(v1), str(v2))
print(v1 + v2)                 # (4, 6)
print(v2 - v1)                 # (2, 2)
print(v1 * 3)                  # (3, 6)
print(v1 == Vector(1, 2))      # True
print(len(v1), v1[0], v1[1])   # 2 1 2
print(bool(Vector(0, 0)))      # False — zero vector is falsy
print(v2(2))                   # (6, 8) via __call__

# container dunders behind the scenes
class Playlist:
    def __init__(self, *songs): self.songs = list(songs)
    def __contains__(self, song):   return song in self.songs       # in
    def __iter__(self):             return iter(self.songs)         # for
    def __len__(self):              return len(self.songs)          # len()

pl = Playlist("tum hi ho", "believer")
print("believer" in pl, len(pl))
for song in pl:
    print(" -", song)

# Practice: add __lt__ to Vector so sorted([v2, v1]) works by x value.

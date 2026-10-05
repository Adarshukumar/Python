"""Lesson 41 — dataclasses and enums. Author: Adarsh."""
from dataclasses import dataclass, field
from enum import Enum, auto

# dataclass auto-writes __init__, __repr__, __eq__ for data-holder classes
@dataclass
class Product:
    name: str
    price: float
    tags: list[str] = field(default_factory=list)   # mutable default done right
    in_stock: bool = True

    def total_with_tax(self, rate=0.18):
        return round(self.price * (1 + rate), 2)

p1 = Product("Keyboard", 999.0, ["gaming"])
p2 = Product("Keyboard", 999.0, ["gaming"])
print(p1)                          # nice __repr__ for free
print(p1 == p2)                    # True — value equality for free
print(p1.total_with_tax())         # 1178.82

# frozen=True makes it immutable and hashable (usable in sets/dict keys)
@dataclass(frozen=True)
class Point:
    x: int
    y: int
print({Point(1, 2), Point(1, 2)})   # deduped to one item

# asdict for serialization (pairs nicely with JSON)
from dataclasses import asdict
import json
print(json.dumps(asdict(p1), indent=1))

# Enum — fixed set of named constants
class Status(Enum):
    DRAFT = auto()          # auto() assigns 1, 2, 3...
    PUBLISHED = auto()
    ARCHIVED = auto()

class Level(Enum):
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3

print(Status.DRAFT, Status.DRAFT.name, Status.DRAFT.value)
print(Level(2))                     # lookup by value -> Level.INTERMEDIATE
print(Level["ADVANCED"])            # lookup by name

post = {"status": Status.PUBLISHED}
if post["status"] is Status.PUBLISHED:
    print("post is live")

for s in Status:                    # enums iterate
    print("-", s.name)

# Enum members are singletons — compare with `is`, never create new ones
print(Status.DRAFT is Status.DRAFT)

# Practice: dataclass Task(title, done=False) + a method to toggle done.

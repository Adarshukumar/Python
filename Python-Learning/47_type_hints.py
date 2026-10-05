"""Lesson 47 — Type hints. Author: Adarsh."""
# Hints document intent; they don't enforce anything at runtime,
# but tools (mypy, IDEs) catch bugs before running.

def add(a: int, b: int) -> int:
    return a + b

def greet(name: str, excited: bool = False) -> str:
    return f"hi {name}{'!' if excited else '.'}"

print(add(1, 2), greet("Adarsh", excited=True))
print(add(1.5, 2))          # runs fine — hints are NOT enforced at runtime

# Variables
count: int = 0
names: list[str] = []                # 3.9+ built-in generics
scores: dict[str, float] = {}        # keys str, values float
point: tuple[int, int] = (3, 7)
maybe: str | None = None             # 3.10+ union syntax

# Typing module extras
from typing import Optional, Union, Any, Callable

def find_first(items: list[str], prefix: str) -> Optional[str]:   # str | None
    for item in items:
        if item.startswith(prefix):
            return item
    return None

def process(data: Union[int, str]) -> str:   # same as int | str
    return str(data)

def anything(value: Any) -> None:            # Any = no check
    print(value)

Callback = Callable[[int, int], int]         # takes (int,int), returns int

# Iterable / Sequence for flexible inputs
from collections.abc import Iterable, Sequence

def total(nums: Iterable[float]) -> float:
    return sum(nums)

def first(seq: Sequence[str]) -> str:
    return seq[0]

print(total([1, 2, 3]), total((4, 5)), total(x for x in range(3)))
print(first(["a", "b"]), find_first(["apple", "pear"], "ap"))

# Type hints on classes
class Account:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.balance += amount

acc = Account("Adarsh", 100.0)
acc.deposit(50)
print(acc.owner, acc.balance)

# Practice: annotate a function repeat(text: str, times: int) -> list[str].

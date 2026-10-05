# Python Cheatsheet — by Adarsh

## Data types
| Type | Example | Mutable? |
|---|---|---|
| int / float | `42`, `3.14` | — |
| str | `"hi"` | no |
| list | `[1, 2]` | yes |
| tuple | `(1, 2)` | no |
| set | `{1, 2}` | yes |
| dict | `{"a": 1}` | yes |
| bool / None | `True`, `None` | — |

## Strings
```python
s.strip()  s.lower()  s.upper()  s.title()
s.split(",")  "-".join(parts)  s.replace("a","b")
s.startswith("x")  s.endswith("y")  s.find("q")  s.count("a")
f"{name} scored {score:.1f}"      # f-string
```

## Slicing `s[start:stop:step]`
```python
s[:3]  s[3:]  s[-3:]  s[::2]  s[::-1]   # reverse
```

## Comprehensions
```python
[x*x for x in nums if x % 2 == 0]
{k: len(v) for k, v in data.items()}
(x*x for x in nums)                 # generator
```

## Loops
```python
for i, v in enumerate(items, 1): ...
for a, b in zip(xs, ys): ...
for/while ... else: ...             # else runs if no break
```

## Functions
```python
def f(a, b=2, *args, **kwargs): ...
f(*list_args, **dict_kwargs)        # unpack at call site
lambda x: x * 2                     # tiny anonymous fn
```

## Dict tricks
```python
d.get("k", default)  d.setdefault("k", [])
counts[k] = counts.get(k, 0) + 1
merged = {**defaults, **overrides}  # or defaults | overrides
```

## Files
```python
with open("f.txt", encoding="utf-8") as f:   # r / w / a / x
    text = f.read()          # or: for line in f:
from pathlib import Path
p = Path("dir") / "file.txt"
p.read_text()  p.write_text(s)  p.exists()  p.glob("*.py")
```

## Exceptions
```python
try: risky()
except (ValueError, KeyError) as e: print(e)
else: pass          # no exception happened
finally: cleanup()  # always
raise ValueError("msg")
```

## OOP
```python
class Dog(Animal):
    def __init__(self, name): super().__init__(); self.name = name
    def __repr__(self): return f"Dog({self.name})"
    @property
    def label(self): return self.name.title()
    @classmethod
    def create(cls): return cls("rex")
    @staticmethod
    def is_good(): return True
```

## stdlib gems
```python
collections.Counter(seq).most_common(3)
collections.defaultdict(list)
itertools.chain(a, b)  product()  permutations()  combinations()
functools.lru_cache   functools.partial
datetime.now().strftime("%Y-%m-%d %H:%M")
re.findall(r"\d+", text)   json.load(f)   json.dumps(obj, indent=2)
random.choice(seq)  random.sample(seq, k)  random.shuffle(lst)
```

## venv + pip
```bash
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt && pip freeze > requirements.txt
```

— Adarsh

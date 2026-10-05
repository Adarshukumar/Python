"""Lesson 35 — collections: smart containers. Author: Adarsh."""
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# Counter — counting made trivial
words = "the cat and the dog chased the cat".split()
c = Counter(words)
print(c)                          # Counter({'the': 3, 'cat': 2, ...})
print(c.most_common(2))           # [('the', 3), ('cat', 2)]
print(Counter("mississippi").most_common(3))

# defaultdict — no more KeyError on first access
scores = defaultdict(list)        # missing key -> empty list
scores["Adarsh"].append(91)       # key created automatically
scores["Adarsh"].append(85)
scores["Riya"].append(88)
print(dict(scores))

groups = defaultdict(int)         # missing key -> 0
for ch in "hello":
    groups[ch] += 1
print(dict(groups))

# deque — fast appends/pops at BOTH ends (list is only fast at the right)
dq = deque([2, 3])
dq.appendleft(1); dq.append(4)    # deque([1, 2, 3, 4])
dq.popleft()                      # 1
print(dq)
recent = deque(maxlen=3)          # rolling window — old items drop off
for i in range(6):
    recent.append(i)
print("last 3 seen:", list(recent))   # [3, 4, 5]

# namedtuple — tuples with named fields, tiny memory footprint
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 7)
print(p.x, p.y, p[0])             # name or index both work
total = sum(p)                    # still a tuple underneath
Person = namedtuple("Person", "name age city", defaults=["Delhi"])
print(Person("Adarsh", 21))

# OrderedDict — plain dict is ordered since 3.7; still used for move_to_end
od = OrderedDict(a=1, b=2)
od.move_to_end("a")
print(od)

# Practice: find the 3 most common words in any sentence with Counter.

"""Lesson 06 — f-strings and formatting. Author: Adarsh."""
name = "Adarsh"
score = 91.5678
items = 7

# f-strings: put expressions inside {} — the modern way (Python 3.6+)
print(f"Hello, {name}!")
print(f"Next year you'll have {items + 1} items.")
print(f"Score: {score}")          # 91.5678
print(f"Score: {score:.1f}")      # 91.6  (1 decimal place)
print(f"Score: {score:.2f}")      # 91.57
print(f"Score: {10:.2f}")         # 10.00

# Width and alignment — great for tables
print(f"|{name:<10}|")            # left,   width 10: '|Adarsh    |'
print(f"|{name:>10}|")            # right,  width 10: '|    Adarsh|'
print(f"|{name:^10}|")            # center, width 10: '|  Adarsh  |'
print(f"{1234567:,}")             # 1,234,567 (thousands separator)
print(f"{0.854:.1%}")             # 85.4%  (percentage)

# Debug trick (Python 3.8+): {var=} prints name AND value
x = 3 * 4
print(f"{x=}")                    # x=12

# Older styles you will still see in real code
print("Hello %s, score %.1f" % (name, score))   # %-formatting (legacy)
print("Hello {}, score {:.1f}".format(name, score))  # str.format

# Practice: print a receipt-style table of 3 products with aligned prices.

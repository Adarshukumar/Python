"""Lesson 50 — sqlite3: a real database, zero setup. Author: Adarsh."""
# Every Python ships with SQLite — perfect for learning SQL and small apps.
import sqlite3

conn = sqlite3.connect("demo_50.db")     # file created if missing (":memory:" = RAM)
cur = conn.cursor()

# CREATE
cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        name   TEXT NOT NULL,
        score  REAL,
        city   TEXT DEFAULT 'Delhi'
    )
""")

# INSERT — ALWAYS use ? placeholders (never f-strings: SQL injection risk!)
students = [("Adarsh", 91.0, "Delhi"), ("Riya", 88.5, "Mumbai"), ("Kiran", 79.0, "Pune")]
cur.executemany("INSERT INTO students (name, score, city) VALUES (?, ?, ?)", students)
conn.commit()                            # persist changes

# SELECT
cur.execute("SELECT id, name, score FROM students WHERE score >= ? ORDER BY score DESC", (85,))
for row in cur.fetchall():
    print(row)

# Row factory: access columns by NAME
conn.row_factory = sqlite3.Row
r = conn.execute("SELECT * FROM students WHERE name = ?", ("Riya",)).fetchone()
print(dict(r))                           # {'id': 2, 'name': 'Riya', ...}

# UPDATE and DELETE
cur.execute("UPDATE students SET score = score + ? WHERE name = ?", (2.0, "Kiran"))
cur.execute("DELETE FROM students WHERE score < ?", (50,))
conn.commit()

# Aggregate queries
cur = conn.cursor()
print(cur.execute("SELECT city, COUNT(*), ROUND(AVG(score),1) FROM students GROUP BY city").fetchall())

# Cleanup
conn.close()
import os; os.remove("demo_50.db")

# Patterns to remember:
# 1. conn = sqlite3.connect(...)  2. cur = conn.cursor()
# 2. cur.execute("... ? ...", (values,))   <- placeholders!
# 3. conn.commit() after writes; conn.close() when done
# 4. with sqlite3.connect(...) as conn:  auto-commits (but still close())

# Practice: make a books table, insert 3 rows, query books cheaper than a price.

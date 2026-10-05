"""Lesson 33 — dates and times. Author: Adarsh."""
from datetime import date, time, datetime, timedelta

# date / time / datetime objects
today = date.today()                       # 2026-10-05 style
print(today, today.year, today.month, today.day, today.weekday())  # Mon=0
print(today.isoformat())                   # '2026-10-05'

now = datetime.now()
print(now)                                 # date AND time with microseconds
print(now.hour, now.minute, now.strftime("%H:%M:%S"))

# Creating specific moments
birthday = date(2004, 7, 15)
meeting = datetime(2026, 12, 1, 10, 30)
print(birthday, meeting)

# Formatting: strftime = object -> string
print(now.strftime("%d-%b-%Y"))            # 05-Oct-2026
print(now.strftime("%A %d %B %Y"))         # Monday 05 October 2026
print(now.strftime("%I:%M %p"))            # 03:45 PM

# Parsing: strptime = string -> object
dt = datetime.strptime("2026-10-05 14:30", "%Y-%m-%d %H:%M")
print(dt, "| parsed OK")

# Arithmetic with timedelta
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)
print(tomorrow, last_week)

age_days = (date.today() - birthday).days
print("days alive:", age_days)

# Differences between datetimes
delta = datetime(2026, 12, 31) - datetime.now()
print("to new year:", delta.days, "days", delta.seconds // 3600, "hours")

# Timestamps (Unix epoch seconds) — common in APIs
import time
ts = time.time()                           # float seconds since 1970
print("timestamp:", int(ts))
print(datetime.fromtimestamp(ts))

# Careful: naive vs aware datetimes. Store/compare UTC in backends:
from datetime import timezone
utc_now = datetime.now(timezone.utc)
print("utc:", utc_now)

# Practice: print your exact age in days AND in weeks.

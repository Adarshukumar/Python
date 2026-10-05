"""Lesson 48 — The logging module. Author: Adarsh."""
# print() is for users; logging is for diagnosing. Levels:
# DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL (default threshold: WARNING)
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)

log = logging.getLogger("adarsh.app")       # named loggers per module

log.debug("fine details: variable x = %s", 42)   # lazy %-formatting
log.info("app started")
log.warning("disk usage at 85%")
log.error("failed to save file")
try:
    1 / 0
except ZeroDivisionError:
    log.exception("math went wrong")        # exception() logs the traceback too

# Log to a file instead of the console
import logging.handlers
handler = logging.FileHandler("app_48.log", encoding="utf-8")
handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
file_log = logging.getLogger("adarsh.file")
file_log.addHandler(handler)
file_log.setLevel(logging.INFO)
file_log.info("this line goes to app_48.log only")

# Silence noisy libraries
logging.getLogger("urllib3").setLevel(logging.WARNING)

for h in file_log.handlers[:]:      # Windows: close the file first
    h.close()
    file_log.removeHandler(h)
import os; os.remove("app_48.log")

# Guidance:
# - default root logger prints WARNING+ to stderr — often enough for scripts
# - libraries should log, not configure; apps configure logging once at startup
# - log.exception() inside except blocks — saves hours of debugging

# Practice: log the steps of reading a file at DEBUG and failures at ERROR.

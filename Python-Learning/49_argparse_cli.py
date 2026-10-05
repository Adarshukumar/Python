"""Lesson 49 — Command-line apps with argparse. Author: Adarsh."""
import argparse

# Run this file like:
#   python 49_argparse_cli.py Adarsh --count 3 --shout
#   python 49_argparse_cli.py --help

parser = argparse.ArgumentParser(
    prog="greet",
    description="Friendly greeter by Adarsh",
    epilog="Thanks for using greet!",
)

# positional argument (required by default)
parser.add_argument("name", help="who to greet")

# option with a typed value and default
parser.add_argument("--count", type=int, default=1, help="how many times")

# flag (True/False)
parser.add_argument("--shout", action="store_true", help="UPPERCASE output")

# option with limited choices, and a shortcut
parser.add_argument("-l", "--lang", choices=["en", "hi"], default="en")

args = parser.parse_args()          # parses sys.argv automatically
print(args)                         # Namespace(name=..., count=..., ...)

for _ in range(args.count):
    message = f"Hello {args.name}!" if args.lang == "en" else f"Namaste {args.name}!"
    if args.shout:
        message = message.upper()
    print(message)

# Also handy:
#   nargs="+"                  -> list values: --tags py git sql
#   type=int / type=float      -> auto conversion
#   required=True              -> force an option
#   action="append"            -> repeatable flags: -v -v -v
#   default=...                -> fallback value
# sys.argv holds the raw strings: ["script.py", "Adarsh", "--count", "3"]

# Practice: build a todo CLI: add/list/done as a positional 'command'.

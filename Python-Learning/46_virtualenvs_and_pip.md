# Virtual Environments & pip — Notes by Adarsh

## Why virtual environments?
Each project gets its own isolated set of packages. Project A can use
`requests 2.28` while Project B uses `2.31` — no conflicts, no "it works
on my machine".

## Creating and using (built-in `venv`)

```bash
# create a folder named .venv holding the isolated interpreter
python -m venv .venv

# activate it
.venv\Scripts\activate        # Windows (cmd / PowerShell)
source .venv/bin/activate     # macOS / Linux

# once active, prompt shows (.venv) — python and pip are now the isolated ones
python -m pip install requests pandas
python -m pip list
python -m pip show requests

# leave the environment
deactivate
```

## pip cheat sheet

```bash
pip install requests              # latest version
pip install "requests==2.31.0"    # exact pin
pip install "pandas>=2.0,<3"     # range
pip install -r requirements.txt  # everything a project needs
pip install package --upgrade    # bump to newest
pip uninstall package            # remove
pip freeze > requirements.txt    # snapshot current env
pip list --outdated              # what can be updated
pip cache purge                  # free disk space
```

## requirements.txt — the project's shopping list
One package per line, committed to git. Teammates recreate your env with:
`python -m venv .venv && pip install -r requirements.txt`

## Modern alternative: uv
`uv` is a fast Rust-based replacement: `uv venv`, `uv pip install ...`,
or `uv add` with a lockfile (pyproject.toml based projects).

## Rules of thumb
1. Never install project dependencies into the global Python.
2. One `.venv` per project, usually gitignored (add `.venv/`).
3. Commit `requirements.txt` (or `pyproject.toml`), NOT the venv folder.
4. `python -m pip` is safer than bare `pip` (guarantees the right env).

— Adarsh

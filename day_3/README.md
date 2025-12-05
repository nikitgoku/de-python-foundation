# Day 3 — Modular Programming and OOP Introduction

This folder demonstrates a small package-style layout, relative imports, and a couple of example modules:
- src/main — small CLI entry point demonstrating relative imports
- src/greeting — greeting utility used by main
- src/pizza_order_system — small domain model (Pizza) with pricing and logging

Purpose
- Teach how to organize simple Python code for reusability and maintainability.
- Show relative imports and how to run a module from the project root
- Provide a small example class (Pizza) that includes docstrings, simple validation hints, and logger usage

Repository layout
```
day_3/
├─ src/
│  ├─ greeting/
│  │  ├─ greeting.py
│  │  └─ __init__.py
│  ├─ main/
│  │  ├─ main.py
│  │  └─ __init__.py
│  └─ pizza_order_system/
│     ├─ pizza_order.py
│     └─ __init__.py
└─ README.md
```

Quick notes about imports and "module not found"
- Python finds modules using the import machinery and the contents of sys.path.
- Recommended: make each directory a package by adding empty `__init__.py` files (shown above). These can be empty; their presence signals Python to treat the directory as a package.
- Use relative imports inside package modules. Example (already used in this project):
  from ..greeting.greeting import say_hello
- To execute a module that uses relative imports, run it as a module from the project root:
  ```
  python -m day_3.src.main.main
  ```
  Running `python day_3/src/main/main.py` directly will fail when relative imports are used.

Create __init__.py (if missing)
- On macOS / Linux:
  ```
  touch day_3/src/greeting/__init__.py day_3/src/main/__init__.py day_3/src/pizza_order_system/__init__.py
  ```
- They can be empty; optionally include package-level metadata if desired.

How to run examples
- From repository root (project root that contains `day_3`):
  - Run the main example:
    ```
    python -m day_3.src.main.main
    ```
  - Run the pizza example interactively (recommended via module):
    ```
    python -c "from day_3.src.pizza_order_system.pizza_order import Pizza; \
    from loguru import logger; \
    p=Pizza(1,'small','extra_cheese','neapolitan'); logger.info(p.calculate_price())"
    ```

Dependencies
- Examples use only the standard library except for `loguru` used for logging. Install with:
  ```
  pip install loguru
  ```

Best practices / troubleshooting
- Always run modules as packages (python -m ...) when code uses relative imports.
- If you prefer running scripts directly, convert relative imports to absolute imports or modify PYTHONPATH (not recommended for long-term projects).
- For development, use a virtual environment:
  ```
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt  # if present
  ```
- Add simple unit tests under a tests/ directory and run with pytest.

Pizza example notes
- pizza_order.py contains:
  - class Pizza: class-level price maps and instance attributes
  - describe_order(): logs a readable order summary
  - calculate_price(): computes total price; currently uses dict.get() — consider validating keys and raising a clear error or providing defaults if a key is missing.
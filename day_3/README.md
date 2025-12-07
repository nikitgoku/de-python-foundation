# Day 3 — Modular Programming and OOP Introduction

This folder demonstrates a small package-style layout, relative imports, and a couple of example modules:
- src/main — small CLI entry point demonstrating relative imports
- src/greeting — greeting utility used by main
- src/pizza_order_system — small domain model (Pizza) with pricing and logging
This folder added comprehensive OOP examples using a pizza-order analogy.

Purpose
- Teach how to organize Python code into packages for reusability and maintainability.
- Demonstrate relative imports and how to run modules from the project root.
- Introduce the four pillars of Object-Oriented Programming with simple, beginner-friendly examples.
- Show best practices for encapsulation, abstraction, inheritance, and polymorphism.

Repository layout
```
day_3/
├─ src/
│  ├─ pizza_order_system/
│  │  ├─ pizza_base.py          # Base Pizza class
│  │  ├─ encapsulation.py       # Encapsulation example
│  │  ├─ inheritance.py         # Inheritance example
│  │  ├─ polymorphism.py        # Polymorphism example
│  │  ├─ abstraction.py         # Abstraction example
│  │  └─ __init__.py
│  ├─ main/
│  │  ├─ main.py            # Demo script tying all examples together
│  │  └─ __init__.py
│  └─ greeting/
│     ├─ greeting.py
│     └─ __init__.py
├─ data/
│  └─ sample_orders.json        # Sample pizza orders for demo
├─ test/
└─ README.md
```

## The Four Pillars of OOP

### 1. Encapsulation
**File:** `src/pizza_order_system/encapsulation.py`

Encapsulation hides internal state and provides controlled access through getter/setter methods.

- Protects internal attributes from direct modification.
- Validates input through setter methods.
- Example: `EncapsulatedPizza` uses private attributes (`__count`, `__size`) with `get_count()` and `set_count()` methods.

```python
ep = EncapsulatedPizza(2, "medium")
ep.set_count(3)  # Controlled access with validation
print(ep.get_count())  # 3
```

### 2. Abstraction
**File:** `src/pizza_order_system/abstraction.py`

Abstraction simplifies complexity by defining an interface and hiding implementation details.

- Base class defines the contract (interface).
- Subclasses provide concrete implementations.
- Example: `BaseOrder` defines `total_price()` as a contract; `SimpleOrder` implements it by delegating to a Pizza object.

```python
pizza = Pizza(1, "small", "extra_cheese", "neapolitan")
order = SimpleOrder(pizza)
print(order.total_price())  # Abstracts price calculation
```

### 3. Inheritance
**File:** `src/pizza_order_system/inheritance.py`

Inheritance allows subclasses to reuse and customize behavior from a parent class.

- Child classes extend parent functionality.
- Methods can be overridden to provide specialized behavior.
- Example: `VegPizza` and `ChickenPizza` inherit from `Pizza` but override `calculate_price()` to apply discounts or surcharges.

```python
veg = VegPizza(2, "large", "veg", "thin_crust")
print(veg.calculate_price())  # Veg discount applied

chicken = ChickenPizza(1, "medium", "chicken", "neapolitan")
print(chicken.calculate_price())  # Chicken surcharge applied
```

### 4. Polymorphism
**File:** `src/pizza_order_system/polymorphism.py`

Polymorphism allows different objects to be treated the same way if they share a common interface.

- Multiple classes provide the same method name.
- A single function can work with objects of different types.
- Example: `VeganPizza` and `MeatPizza` both have a `prepare()` method; `process_preparations()` works with both without knowing their type.

```python
pizzas = [VeganPizza(1, "small"), MeatPizza(2, "large")]
steps = process_preparations(pizzas)
for step in steps:
    print(step)
```

## Core Classes and Modules

### pizza_base.py
The foundational `Pizza` class with:
- Class attributes: `base_price`, `toppings_price`, `crust_price` (shared across all instances)
- Instance attributes: `count`, `size`, `toppings`, `crust_type` (specific to each order)
- Methods: `describe_order()`, `calculate_price()`, `__repr__()`
- Input validation with clear error messages

### encapsulation.py
`EncapsulatedPizza` demonstrates:
- Private attributes with name-mangling (`__count`, `__size`)
- Getter and setter methods with validation
- Controlled access to internal state

### inheritance.py
Subclasses extend `Pizza`:
- `VegPizza`: applies a 10% discount on total price
- `ChickenPizza`: adds a fixed surcharge per pizza

### polymorphism.py
Classes with a common interface:
- `VeganPizza.prepare()`
- `MeatPizza.prepare()`
- `process_preparations(pizza_list)`: works with any object that has a `prepare()` method

### abstraction.py
Abstract-like interface pattern:
- `BaseOrder`: defines the contract with `total_price()` (raises `NotImplementedError` if not overridden)
- `SimpleOrder`: concrete implementation that wraps a Pizza object

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
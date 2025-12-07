from ..greeting.greeting import say_hello
"""
Simple runnable demo that ties the small OOP examples together.

Run from the project root to ensure package imports work:
    python -m day_3.src.main.oop_demo
"""
from pathlib import Path
from loguru import logger
import json

# Relative imports between sibling packages under src
from ..pizza_order_system.pizza_base import Pizza
from ..pizza_order_system.inheritance import VegPizza, ChickenPizza
from ..pizza_order_system.polymorphism import VeganPizza, MeatPizza, process_preparations
from ..pizza_order_system.abstraction import SimpleOrder

def load_sample_orders():
    # Resolve data path relative to this file: ../.. => day_3, then data/sample_orders.json
    data_file = Path(__file__).resolve().parents[2] / "data" / "sample_orders.json"
    with open(data_file, encoding="utf-8") as fh:
        return json.load(fh)

def demo_basic_and_inheritance(orders):
    logger.info(f"="*20 + f" Basic Pizza and Inheritance demo " + f"="*20)
    for o in orders:
        # choose subclass based on kind
        if o.get("kind") == "veg":
            p = VegPizza(o["count"], o["size"], o["toppings"], o["crust_type"])
        else:
            p = ChickenPizza(o["count"], o["size"], o["toppings"], o["crust_type"])
        logger.info(f"{p}")  # __repr__ from base class
        try:
            logger.info(f"Total price: {p.calculate_price()}\n")
        except ValueError as e:
            logger.error(f"Invalid order: {e}\n")


def demo_encapsulation_and_abstraction():
    logger.info(f"="*20 + f" Encapsulation and Abstraction demo " + f"="*20)
    from ..pizza_order_system.encapsulation import EncapsulatedPizza
    from ..pizza_order_system.pizza_base import Pizza as BasePizza

    ep = EncapsulatedPizza(2, "medium")
    logger.info(f"{ep.summary()}")
    ep.set_count(3)
    logger.info(f"After set_count: {ep.get_count()}")

    # Use SimpleOrder (abstraction) to wrap a Pizza and compute total
    pizza = BasePizza(1, "small", "extra_cheese", "neapolitan")
    so = SimpleOrder(pizza)
    logger.info(f"SimpleOrder total: {so.total_price()}")

def demo_polymorphism():
    logger.info(f"="*20 + f" Polymorphism demo " + f"="*20)
    v = VeganPizza(1, "small")
    m = MeatPizza(2, "large")
    steps = process_preparations([v, m])
    for s in steps:
        logger.info(f"{s}")

def main():
    orders = load_sample_orders()
    demo_basic_and_inheritance(orders)
    demo_encapsulation_and_abstraction()
    demo_polymorphism()

if __name__ == "__main__":
    main()
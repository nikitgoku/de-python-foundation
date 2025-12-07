"""
Abstraction example:
- Shows a simple abstract-like base class (no decorators used).
- Base class defines an interface by raising NotImplementedError.
"""
class BaseOrder:
    def total_price(self):
        """
        Intended to be overridden by subclasses. Raises an explicit error
        if a concrete implementation is not provided.
        """
        raise NotImplementedError("Subclasses must implement total_price()")

class SimpleOrder(BaseOrder):
    def __init__(self, pizza):
        # pizza is an instance that exposes calculate_price()
        self.pizza = pizza

    def total_price(self):
        # Delegate to the pizza object to compute the cost
        return self.pizza.calculate_price()
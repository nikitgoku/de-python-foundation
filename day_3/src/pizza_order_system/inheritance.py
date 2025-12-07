"""
Inheritance example:
- Subclasses extend and customize behaviour from a base class (Pizza).
- Shows overriding of methods to change or extend calculation logic.
"""
from .pizza_base import Pizza

class VegPizza(Pizza):
    """
    VegPizza inherits everything from Pizza but applies a small veg discount
    per pizza to demonstrate overriding behaviour.
    """
    def calculate_price(self):
        base_total = super().calculate_price()
        # Veg discount: 10% off per pizza
        discount = int(0.10 * (self.base_price[self.size] + self.toppings_price[self.toppings] + self.crust_price[self.crust_type]) ) * self.count
        return base_total - discount

class ChickenPizza(Pizza):
    """
    ChickenPizza inherits from Pizza but adds a fixed surcharge for premium topping.
    """
    def calculate_price(self):
        base_total = super().calculate_price()
        surcharge = 20 * self.count  # small surcharge per pizza
        return base_total + surcharge
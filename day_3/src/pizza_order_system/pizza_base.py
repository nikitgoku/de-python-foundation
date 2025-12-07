"""
Simple Pizza class demonstrating basic object-oriented principles:
- constructor / instance attributes
- class attributes (shared price maps)
- instance methods
- a readable representation (__repr__)
"""
from loguru import logger


class Pizza():
    """
    Pizza represents a customer's pizza order.

    Attributes:
        base_price (dict): price mapping for pizza sizes.
        toppings_price (dict): price mapping for toppings.
        crust_price (dict): price mapping for crust types.
    """
    # Class Attributes: price lookups shared across all instances
    base_price = {'small': 300, 'medium': 400, 'large': 600}
    toppings_price = {'chicken': 50, 'extra_cheese': 100, 'veg': 30}
    crust_price = {'thin_crust': 50, 'deep_dish': 200, 'neapolitan': 150}

    def __init__(self, count, size, toppings, crust_type):
        """
        Initialize a Pizza order.

        Args:
            count (int): number of pizzas in the order.
            size (str): size key matching base_price (e.g., 'small').
            toppings (str): topping key matching toppings_price.
            crust_type (str): crust key matching crust_price.
        """
        # Instance attributes: specific to each order
        self.count      = int(count)
        self.size       = size
        self.toppings   = toppings
        self.crust_type = crust_type

    def describe_order(self):
        """
        Log a human-readable description of the order.
        """
        # Use logger.info to print order details
        return f"{self.count}x {self.size} pizza(s) with {self.toppings} on {self.crust_type}"

    def calculate_price(self):
        """
        Compute total price for the order using class price maps.
        If a key is missing from a map, a ValueError is raised to signal
        the caller to provide valid keys.
        """
        # Validate keys explicitly so errors are clear
        if self.size not in self.base_price:
            raise ValueError(f"Unknown size: {self.size}")
        if self.toppings not in self.toppings_price:
            raise ValueError(f"Unknown toppings: {self.toppings}")
        if self.crust_type not in self.crust_price:
            raise ValueError(f"Unknown crust_type: {self.crust_type}")

        per_pizza = (self.base_price[self.size] +
                     self.toppings_price[self.toppings] +
                     self.crust_price[self.crust_type])
        total = self.count * per_pizza
        logger.info(f"[Pizza] {self.describe_order()} => per pizza {per_pizza}, total {total}")
        return total
    
    def __repr__(self):
        return f"Pizza(count={self.count}, size='{self.size}', toppings='{self.toppings}', crust_type='{self.crust_type}')"
    

# # Example usage:
# # Create a Pizza instance and log the calculated total price.
# # In production, this instantiation would be guarded by `if __name__ == "__main__":`
# # or handled by higher-level application code.
# order = Pizza(1, 'small', 'extra_cheese' , 'neapolitan')
# order_2 = Pizza(2, 'large', 'chicken', 'thin_crust')
# logger.info(f"Total price for the order is: {order.calculate_price()}")
# logger.info(f"Total price for the order is: {order_2.calculate_price()}")

# logger.info(f"{order.__dict__}")
# logger.info(f"{dir(order)}")
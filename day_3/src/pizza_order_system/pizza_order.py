from loguru import logger

# Module-level docstring / summary:
# Simple pizza order model used to demonstrate a small class with pricing logic.
# Uses loguru for informational logging.

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
        self.count      = count
        self.size       = size
        self.toppings   = toppings
        self.crust_type = crust_type

    def describe_order(self):
        """
        Log a human-readable description of the order.
        """
        # Use logger.info to print order details
        logger.info(f"You order is {self.count} {self.size} {self.toppings} {self.crust_type} pizza.")

    def calculate_price(self):
        """
        Calculate and return the total price for the order.

        The calculation multiplies the per-pizza price (base + toppings + crust)
        by the number of pizzas in the order.

        Returns:
            int: total price in the same currency units as the class price maps.
        """
        # Log the order before computing total
        self.describe_order()

        # Safely retrieve prices from the lookup dictionaries using .get()
        # If a key is missing, .get() will return None — in production code you
        # might want to provide defaults or raise a clear error.
        total_price = self.count * (self.base_price.get(self.size) + 
                                    self.toppings_price.get(self.toppings) + 
                                    self.crust_price.get(self.crust_type))

        return total_price
    

# Example usage:
# Create a Pizza instance and log the calculated total price.
# In production, this instantiation would be guarded by `if __name__ == "__main__":`
# or handled by higher-level application code.
order = Pizza(1, 'small', 'extra_cheese' , 'neapolitan')
order_2 = Pizza(2, 'large', 'chicken', 'thin_crust')
logger.info(f"Total price for the order is: {order.calculate_price()}")
logger.info(f"Total price for the order is: {order_2.calculate_price()}")
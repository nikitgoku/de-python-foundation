"""
Polymorphism example:
- Different classes provide the same method name and can be used interchangeably.
- A single function works with any object that implements the expected method.
"""
class VeganPizza:
    def __init__(self, count, size):
        self.count = int(count)
        self.size = size

    def prepare(self):
        return f"Preparing {self.count} vegan {self.size} pizza(s)"

class MeatPizza:
    def __init__(self, count, size):
        self.count = int(count)
        self.size = size

    def prepare(self):
        return f"Preparing {self.count} meat {self.size} pizza(s)"

def process_preparations(pizza_list):
    """
    Accepts a list of objects and calls .prepare() on each.
    This works because both VeganPizza and MeatPizza implement prepare().
    """
    results = []
    for p in pizza_list:
        # we rely on the presence of .prepare(); this is duck-typing-based polymorphism
        results.append(p.prepare())
    return results
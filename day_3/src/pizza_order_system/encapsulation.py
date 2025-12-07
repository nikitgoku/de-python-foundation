"""
Encapsulation example:
- Demonstrates hiding internal state and using getter/setter style methods.
- Avoids exposing internal attributes directly to encourage validation.
"""
class EncapsulatedPizza:
    def __init__(self, count, size):
        # "Private" attribute by name-mangling (convention in Python)
        self.__count = int(count)
        self.__size = size

    # Getter: controlled read access
    def get_count(self):
        return self.__count

    # Setter: controlled write access with validation
    def set_count(self, new_count):
        new_count = int(new_count)
        if new_count < 0:
            raise ValueError("count cannot be negative")
        self.__count = new_count

    # Public method that uses the hidden state
    def summary(self):
        return f"Encapsulated order: {self.__count} x {self.__size}"
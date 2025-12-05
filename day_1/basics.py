# 1. Variables
"""
Variables are anything that can hold a value. 
In Python, you can create a variable by simply assigning a value to a name.
"""
x = 100
y = 10.5
"""
These are all variables holding different types of values.
These values are stored in the RAM (Random Access Memory) of your computer.
An address is assigned to each variable in memory, and when the variable is called,
the value stored at that address is retrieved.
"""
print(f"x: {x}, y: {y}")    # Prints the value of x and y
# If you want to check at what address a variabled is stored, you can use the following code
print(f"Address of x: {id(x)} and address of y: {id(y)}")

# 2. Data Types
"""
Python has several built-in data types. 
Some of the most common ones:
1. Integer (int): Whole numbers, e.g., 1, -5, 100
2. Float (float): Decimal numbers, e.g., 3.14, -0.001, 2.0
3. String (str): Text, e.g., "Hello World!", 'Python is fun'
4. Boolean (bool): True or False values

Note: In Python, you don't need to declare the data types of the variables explicitly.
Since this is an interpreted and dynamically typed language, Python automatically assigns the 
data type based on the value assigned to the variable.
"""
company = "Amazon"          # String
employees = 500             # Integer
rating = 4.5                # Float
is_hiring = True            # Boolean
clearing_interview = False  # Boolean

# 2.1 Type Casting and Checking
"""
There are two types of type casting in Python:
1. Implicit Type Casting: Python automatically does the data type change
2. Explicit Type Casting: We manually convert one data type to another using built-in functions
"""
# Implicit Type Casting
a = 10        # Integer
b = 2.5      # Float
c = a + b    # Implicitly converts 'a' to float and adds
print(f"Value of c: {c}, Type of c: {type(c)}")

# Explicit Type Casting
d = 10.7
e = int(d)   # Explicitly converts float to integer
print(f"Value of e: {e}, Type of e: {type(e)}")

# 3. Print Statement and Logging
"""
Why do we use print statements?
Main use case is to print values to the console and displaying values.
Other beneficial operation includes debugginga and logging.
Majority of the time, when we are debugging the code, we print the values to
see if what we are expecting is the same as what we are getting.
"""
print("Company:", company)
print("""This is the first line.
      This is the second line.""")
# We can also makje use of escape sequences to format the output. For example:
print("This is the first line.\nThis is the sencond line.")
# backslash (\) is used as an escape character in Python. Can also be used to skip characters.
print("He said, \"Hello!\"")  # Output: He said, "Hello

# 3.1 String Formatting
"""
1. f-Strings (Python 3.6+) is mainly used in production code.
The main syntax is to prefix the string with 'f' and use curly braces {} to 
print expressions using string literals.
"""
print(f"{company} has {employees} employees with a rating of {rating}")

"""
2. Format Method is another way to format strings in Python.
The main syntax is to use curly braces {} as placeholders in the string
and call the format() method on the string to replace the placeholders with values.
"""
print("{} has {} employees with a rating of {}".format(company, employees, rating))

# 3.2 Logging
"""
Logging is a way to track events that happen when some software runs.
The logging module in Python provides a way to configure different log handlers
and a way to route log messages to these handlers.
Apart from this, a library like 'loguru' can also be used for logging in Python.
Here is a simple example of logging using the logging module:
"""
import logging
FORMAT = "%(asctime)s %(clientip)-15s %(user)-8s %(message)s"
logging.basicConfig(format=FORMAT)
logging.info(f"{company} is hiring: {is_hiring}")
# For logging, we have to manually set the logging level. 
# logger module provides an easier way.
# from loguru import logger

# logger.info(f"Clearing interview: {clearing_interview} for {company}")

# 4. Operators
"""
Operators are special symbols that perform operations on variables and their values.
Some common types of operators in Python:
1. Arithmetic Operators: +, -, *, /, %, //, **
2. Comparison Operators: ==, !=, >, <, >=, <=
3. Logical Operators: and, or, not, ^ (XOR)
4. Assignment Operators: =, +=, -=, *=, /=, %=, //=, **=
5. String Operators: + (concatenation), * (repetition)
"""
import math
a = 5
b = 10.5
c = 21
print(f"Addition: {a + b}") # Output: 15.5
print(f"Modulo (Remainder Operations): {c % a}")   # Output: 1
print(f"Floor Division: {c // a}")  # Output: 4
print(f"Ceiling division: {math.ceil(c / a)}")  # Output: 5

# 5. Control Flow: if, elif, else
"""
Control flow statements are used to control the flow of execution of the program.
Most common control flow statements in Python:
1. if statement
2. elif statement
3. else statement
"""
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'D'
print(f"Score: {score}, Grade: {grade}")

# 6. Loops: for, while
"""
Loops are used to execute a block of code repeatedly until a certain condition is met.
Most common loops in Python:
1. for loop
2. while loop
"""
# For Loop
print("For Loop Example:")
for i in range(5):
    print(f"Iteration {i}")

# While Loop
print("While Loop Example:")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1


# 6. Strings
"""
Strings are sequences of characters enclosed in single quotes (' '), double quotes (" "),
or triple quotes (''' ''' or """ """).
Strings are immutable, meaning once they are created, they cannot be changed.
"""
greeting = "Hello, World!"
print(f"Greeting: {greeting}")  # Output: Hello, World!
print(f"Length of greeting: {len(greeting)}")  # Output: 13
print(f"First character: {greeting[0]}")  # Output: H
print(f"Last character: {greeting[-1]}")  # Output: !
new_greeting = greeting.replace("World", "Python")
print(f"New Greeting: {new_greeting}")  # Output: Hello, Python!

# Split and Join
"""
The split() method splits a string into a list where each word is a list item.
The join() method joins the elements of a list into a single string.
"""
api_endpoint = "https://api.example.com/v1/users"
# Splitting the string into a list
endpoint_parts = api_endpoint.split("/")
print(f"Endpoint Parts: {endpoint_parts}")
# Joining the list back into a string
reconstructed_endpoint = "/".join(endpoint_parts)
print(f"Reconstructed Endpoint: {reconstructed_endpoint}")


# 7. Python Collections: List, Dictionary, Set, Tuple
# LIST
"""
A list is a collection of same or different data types that is ordered and mutable.
Lists are defined using square brackets [].
"""
target_companies = ['Google', 'Microsoft','Atlassian', 'Barclays', 'JPMC']
# These elements are stored in contiguous memory locations, 
# and each element can be accessed using its index. Where list name has the base address
# Accessing elements
print(f"First company: {target_companies[0]}")  # Output: Google
print(f"Last company: {target_companies[-1]}")  # Output: JPMC
# Modifying elements
target_companies[1] = 'Amazon'
print(f"Modified List: {target_companies}")  # Output: ['Google', 'Amazon', 'Atlassian', 'Barclays', 'JPMC']
# Adding elements
target_companies.append('Facebook')
print(f"List after appending: {target_companies}")  # Output: ['Google', 'Amazon', 'Atlassian', 'Barclays', 'JPMC', 'Facebook']
# Removing elements
target_companies.remove('Amazon')
print(f"List after removing: {target_companies}")  # Output: ['Google', 'Atlassian', 'Barclays', 'JPMC', 'Facebook']
"""
Now as this is a mutable collection, we can modify, add or remove elements from the list.
However, there are costs associated with these operations in terms of time complexity.
1. Access: list[i]: O(1)
2. Appending: list.append(item): O(1) average case, but amortized since occasionally a resize may be required which can be an O(n) operation. 
3. Insert: list.insert(i, item): O(n) because it might need to shift all subsequent items.
4. Extend: list.extend(iterable): O(k) where k is the length of the iterable being added.
5. Pop: list.pop(): O(1) for the end, but list.pop(i): O(n) for arbitrary positions due to required shifts.
6. Remove: list.remove(item): O(n) as it needs to find the item and then remove it, which might require a shift of items.
7. Iteration: for item in list: O(n)
8. Get slice: list[a:b]: O(b-a) since it creates a new list of size b-a.
9. Del slice: del list[a:b]: O(n)
10. Search: item in/not in list: O(n) in the average case since it may have to scan the entire list.
11. Sort: list.sort(): O(n log n) - Python uses Timsort for this.
"""

# List Slicing
"""
List slicing allows you to access a subset of elements from a list.
The syntax for list slicing is list[start:stop:step], where:
- start: The index to start the slice (inclusive).
- stop: The index to end the slice (exclusive).
- step: The step size or interval between elements in the slice.
"""
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original List: {numbers}")  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Sliced List (2 to 7): {numbers[2:8]}") # Output: [2, 3, 4, 5, 6, 7]
print(f"Sliced List (0 to 9 with step 2): {numbers[0:10:2]}") # Output: [0, 2, 4, 6, 8]
print(f"Negative Sliced List (from the end): {numbers[-1::-1]}") # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# DICTIONARY
"""
A dictionary is a collection of key-value pairs that is unordered, mutable, and indexed.
Dictionaries are defined using curly braces {}.
"""
experience = {'company': 'Alstom', 'years': 3, 'role': 'Software Engineer'}
# Accessing elements
print(experience.keys())  # Output: dict_keys(['company', 'years', 'role'])
print(experience.values())  # Output: dict_values(['Alstom', 3, 'Software Engineer'])
print(experience.items())  # Output: dict_items([('company', 'Alstom'), ('years', 3), ('role', 'Software Engineer')])

# If for some reason, the key is not present in the dictionary, we can use the get() method to avoid KeyError
# This is a useful method in production environments where the key may or may not be present.
print(f"Location: {experience.get('location', 'Not specified')}")  # Output: Not specified

# Modifying values
experience['years'] = 4
print(f"Modified Experience: {experience}")  # Output: {'company': 'Alstom', 'years': 4, 'role': 'Software Engineer'}

# Adding key-value pairs
experience['location'] = 'Glasgow'
print(f"Experience after adding location: {experience}")  # Output: {'company': 'Alstom', 'years': 4, 'role': 'Software Engineer', 'location': 'Glasgow'}

# Removing key-value pairs
del experience['location']
print(f"Experience after removing location: {experience}")  # Output: {'company': 'Alstom', 'years': 4, 'role': 'Software Engineer'}

# Dictionary Comprehensions
"""
Dictionary comprehensions provide a concise way to create dictionaries.
Syntax: {key_expression: value_expression for item in iterable if condition}
Syntax (with if and else condition): {key_expression: (value_if_true if condition else value_if_false) for item in iterable}
"""
# Creating an example dictionary
network_with_cost = {'Jio': 999, 'Airtel': 899, 'Vi': 1200, 'BSNL': 499}
print(f"Original Network with costs: {network_with_cost}")  
network_with_cost = {key:network_with_cost[key] - 200 if key=='Vi'
                     else network_with_cost[key] for key in network_with_cost}
print(f"Network with updated costs: {network_with_cost}")   # Output: {'Jio': 999, 'Airtel': 899, 'Vi': 1000, 'BSNL': 499}

# When searching for a key in a dictionary, the average time complexity is O(1) 
# due to the underlying hash table implementation.
# However, in the worst case (e.g., many hash collisions), it can degrade to O(n).
# As opposed to lists where searching for an element has a time complexity of O(n).

# SET
"""
A set is a collection of unique elements that is unordered and mutable.
Sets are defined using curly braces {} or the set() function. When you want to create an empty set,
you must use the set() function, as using {} will create an empty dictionary.
"""
unique_numbers = {1, 2, 2, 3, 4, 5}
print(f"Original Set: {unique_numbers}")  # Output: {1, 2, 3, 4, 5}
# Adding elements
unique_numbers.add(6)
print(f"Set after adding an element: {unique_numbers}")  # Output: {1, 2, 3, 4, 5, 6}
# Removing elements
unique_numbers.remove(3)
print(f"Set after removing an element: {unique_numbers}")  # Output: {1, 2, 4, 5, 6}
# Note: If you try to remove an element that is not present, it will raise a KeyError.
# To avoid this, you can use the discard() method which does not raise an error if the element is not found.
unique_numbers.discard(10)  # No error raised
print(f"Set after discarding a non-existing element: {unique_numbers}")  # Output: {1, 2, 4, 5, 6}

# Set union, intersection, difference
unique_numbers_2 = {5, 6, 7, 8, 9}
print(f"Union: {unique_numbers.union(unique_numbers_2)}")  # Output: {1, 2, 4, 5, 6, 7, 8, 9}
print(f"Intersection: {unique_numbers.intersection(unique_numbers_2)}")  # Output: {5, 6}
print(f"Difference: {unique_numbers.difference(unique_numbers_2)}")  # Output: {1, 2, 4}


# TUPLE
"""
A tuple is a collection of ordered elements that is immutable.
Tuples are defined using parentheses ().
"""
numbers_tuple = (1, 2, 3, 4, 5)
print(f"Original Tuple: {numbers_tuple}")  # Output: (1, 2, 3, 4, 5)
# Accessing elements
print(f"First element of tuple: {numbers_tuple[0]}")  # Output: 1
print(f"Last element of tuple: {numbers_tuple[-1]}")  # Output: 5
# Tuples are immutable, so we cannot modify, add or remove elements from the tuple.
# However, we can concatenate two tuples to create a new tuple.
new_tuple = numbers_tuple + (6, 7, 8)
print(f"New Tuple after concatenation: {new_tuple}")  # Output: (1, 2, 3, 4, 5, 6, 7, 8)


# 8. List Comprehensions
"""
List comprehensions provide a concise way to create lists.
Syntax: [expression for item in iterable if condition]
Syntax (with if and else condition): [expression_if_true if condition else expression_if_false for item in iterable]
"""
# Example 1: Creating a list of squares of even numbers from 0 to 9
squares_of_even = [x**2 for x in range(10) if x % 2 == 0]
print(f"Squares of even numbers: {squares_of_even}")  # Output: [0, 4, 16, 36, 64]

# Example 2: Creating a list of 'Even' or 'Odd' based on the number
even_odd = ['Even' if x % 2 == 0 else 'Odd' for x in range(5)]
print(f"Even or Odd: {even_odd}")   # Output: ['Even', 'Odd', 'Even', 'Odd', 'Even']

# 9. Functions
"""
Functions are blocks of reusable code that perform a specific task.
They are defined using the "def" keyword.
"""
def greet(name):
    """
    This function takes a name as input and returns a greeting message.
    """
    return f"Hello, {name}!"

print(greet("Nikit"))  # Output: Hello, Nikit!

print(f"{math.ceil(25/3)}")
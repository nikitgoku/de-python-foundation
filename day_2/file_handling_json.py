"""
JSON (JavaScript Object Notation) is a type of text format which is used to store data.
JSON Syntax is very similar to Python Dictionary. The data is stored in key:value format.
Where in keys represents attributes and values can be any information associated with the keys.
Note: A dictionary key can only be string in JSON. Numbers are also converted into strings,
Example of JSON file:
[
    {
        "username": "userA",
        "Platform": "Windows",
        "email": "userA@company.com",
        "device": "Laptop"
    },
    {
        "username": "userB",
        "Platform": "macOS",
        "email": "userB@company.com",
        "device": "Desktop"
    }
]
"""

# Just like the CSV module, Python has a JSON module
import json

# Reading
# There are two main methods to read JSON.
# 1. json.load()
# 2. json.loads()
# The difference is that .loads() is used when JSON data is already loaded as a string,
# for example, when data is straigtaway loaded from an API or raw text, and we use .load() when
# reading data directly from a file. For out case we'll use .load()
__jsonFilePath__ = "/Users/nikit/Documents/dbt/code-space/de-python-foundation/day_2/json_files/example_data.json"

with open(__jsonFilePath__, 'r') as file:
    json_data = json.load(file)

print(f"{json_data}")

# From a string (like an API response)
json_string = '{"name": "John", "age": 30}'
json_data = json.loads(json_string)  # .loads() for strings

# Unpacking usernames from the JSON data
usernames = [data['username'] for data in json_data]
print(f"{usernames}")

# Writing
# There are again two main method to write in a JSON data file.
# 1. json.dump()
# 2. json.dumps()
# The difference is the .dump() method converts a Python object into JSON and writes it into the file
# whereas .dumps() encodes a Python object into a JSON and returns a string (best to use when you are passing data directly to an API).
__jsonFileWritePath__ = "/Users/nikit/Documents/dbt/code-space/de-python-foundation/day_2/json_files/example_data_write.json"

json_write_data = [
    {
        "username": "userA",
        "Platform": "Windows",
        "email": "userA@company.com",
        "device": "Laptop"
    },
    {
        "username": "userB",
        "Platform": "macOS",
        "email": "userB@company.com",
        "device": "Desktop"
    }
]

with open(__jsonFileWritePath__, 'w') as file:
    file.write(json.dumps(json_write_data, indent=2))

"""
When writing data from Python Objects to JSON, data conversion takes place, which means that some
attributes will be converted to a different data type to suit JSON data types.
For example, where you write a tuple to JSON it becomes an array.
An important thing to note is that there are certain limitations to data type conversion from
Python to JSON, for example it is not possible to write dictionary in JSON format if it has tuple
as key.
Here additional parameters to .dump() method becomes useful.
"""

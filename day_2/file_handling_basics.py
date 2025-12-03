# File Handling Basics
# This script demonstrates basic file handling operations in Python,
# including reading from and writing to text files.

# Reading a normal text file using open() method
with open('/Users/nikit/Documents/dbt/code-space/de-python-foundation/day_2/configs/normal.txt', 'r') as file:
   file_content = file.read()
# Display the file contect on the terminal
print(f"File Content: \n{file_content}\n")

# Writing to the same text file using open() method
with open('/Users/nikit/Documents/dbt/code-space/de-python-foundation/day_2/configs/normal.txt', 'w') as file:
   for i in range(1, 6):
      file.write(f"Hello {i}\n")

# Reading Line by Line
with open('/Users/nikit/Documents/dbt/code-space/de-python-foundation/day_2/configs/normal.txt', 'r') as file:
   for line in file:
      print(f"{line}")

# CONFIG FILE
# To use the configurations from a config file, we'll make use of the configparser module.
from loguru import logger
import configparser

# 1. Create a ConfigParser object
config = configparser.ConfigParser()

# 2. Read from a configuration file
try:
   config.read("/Users/nikit/Documents/dbt/code-space/de-python-foundation/day_2/configs/config_file.ini")
except configparser.Error as e:
   logger.error(f"Configuration file not found. Error: {e}")
   exit(1)

# 3. Accessing data from the config file
"""
Accessing the configurations values is similar to accessing values in a dictionary (nested-dictionary).
For example, to access the database name from the 'database' section:
database_name = config['DATABASE']['NAME']
In many scenarios, you might want to use the get method to retrieve values:
API_KEY = config.get('API_KEYS', 'API_KEY')
Just remember that the section names and keys are case-sensitive and the default data-type
for every value read from the config file is a string.
"""

# Accessing the value from the 'database' section
database_name = config['DATABASE']['NAME']
logger.info(f"Database Name from the config file: {database_name}")
# Output: Database Name from the config file: my_miniexervise_db.db

# Accessing the value from the API Keys section
API_KEY = config.get('API_KEYS', 'API_KEY')
logger.info(f"API Key from the config file: {API_KEY}")
# Output: API Key from the config file: YOUR_SECRET_API_KEY_HERE
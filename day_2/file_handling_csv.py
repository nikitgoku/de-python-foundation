"""
CSV (comma separated value), is a type of file which saves data in tabular format (rows and columns).
It may contain data either from a manually created CSV file or from a database table.
EAch value is seperated using a , symbol and each line represents a single row of a table.
Alternative to this is a TSV (tab seperated value) file, which as the name suggests the values 
are seperated using a tab-space in the middle.
Example of a CSV data:

username, platform, email, device
abc123, X, abc@email.com, HP
xyZ**, Facebook, z@rmail.com, Apple
lmn444, Reddit, l44@email.com, Apple
qrs5%5, Facebook, qrs@rmail.com, Dell
"""

# Python has a seperate CSV module which can be imported if you want to work with CSV files
import csv

# Reading a CSV file
__csvFilePath__ = '/Users/nikit/Documents/dbt/code-space/de-python-foundation/day_2/csv_files/example_data.csv'
with open(__csvFilePath__, 'r') as file:
    csv_file = csv.reader(file)
    # Headers can be also be seperated
    headers = next(csv_file)
    for row in csv_file:
        print(f"{row}")
    print(f"Headers: {headers}")    # Print headers seperately

# The csv.reader is an iterator itself. It can also be converted into a list for convinience
with open(__csvFilePath__, 'r') as file:
    csv_file = csv.reader(file)
    print(f"Printed as list: {list(csv_file)}")

# Write a CSV file
# Example Data
data = [
    ['username', 'platform', 'email', 'device'],
    ['alice123', 'Notion', 'alice@email.com', 'Lenovo, Processor'],
    ['dave456', 'Orkut', 'dave@email.com', 'Apple, MacMini'],
    ['john678', 'Facebook', 'johncena@email.com', 'Dell, Laptop']
]

# The data contains a comma inside the quotation for example, "Apple, MacMini"
# Now this won't be considered as separate data, instead the value is in quotation.
# Even if the value contains a comma and is enclosed under a quotation, it is considered as single value
__csvFileWritePath__ = "/Users/nikit/Documents/dbt/code-space/de-python-foundation/day_2/csv_files/example_data_write.csv"
with open(__csvFileWritePath__, 'w') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    # Write the data row by row
    for row in data:
        writer.writerow(row)

# More importantly, for many purposes, this CSV file is imported as dictionary.
# Using the 'DictReader()' method
# Because it is more convinient to get dictionaries, in which column names are the keys
# and column values are dictionary values
with open(__csvFileWritePath__, 'r') as file:
    csv_file = csv.DictReader(file)
    print(f"CSV File in Dictionary format: \n")
    for row in csv_file:
        print(f"{row}")

# Similarly, we can also write Dictionary data as CSV file,
# using the 'DictWriter()' method 
dictionary_data = [
    {
        'username': 'userA',
        'Platform': 'Windows',
        'email': 'userA@company.com',
        'device': 'Laptop'
    },
    {
        'username': 'userB',
        'Platform': 'macOS',
        'email': 'userB@company.com',
        'device': 'Desktop'
    },
    {
        'username': 'userC',
        'Platform': 'Linux',
        'email': 'userC@company.com',
        'device': 'Tablet'
    },
    {
        'username': 'userD',
        'Platform': 'iOS',
        'email': 'userD@company.com',
        'device': 'Smartphone'
    }
]

__csvFileWritePathDict__ = "/Users/nikit/Documents/dbt/code-space/de-python-foundation/day_2/csv_files/example_dict_data_write.csv"
with open(__csvFileWritePathDict__, 'w') as file:
    write_csv = csv.DictWriter(
        file, fieldnames=list(dictionary_data[0].keys()), quoting=csv.QUOTE_NONNUMERIC
    )   # This is important as field names (column) are necessary for the CSV files
    write_csv.writeheader() # To write the header first
    for data in dictionary_data:
        write_csv.writerow(data)
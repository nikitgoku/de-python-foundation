"""
Mini Exercise. The task is to convert the "example_data.json" file into "example_data.csv" file
using what we have learned
"""
import csv
import json

# Store the file path
__jsonFilePath__ = "/Users/nikit/Documents/dbt/code-space/de-python-foundation/day_2/json_files/example_data.json"
__csvFilePath__ = "/Users/nikit/Documents/dbt/code-space/de-python-foundation/day_2/csv_files/example_data_converted.csv"

# Read the json file and store the JSON as Python Object
with open(__jsonFilePath__, "r") as file:
    json_data = json.load(file)

# Display the json_data and the type of data that we have.
print(f"JSON data: {json_data}")
print(f"Type of Data: {type(json_data)}")

# Write the data into a CSV file
with open(__csvFilePath__, 'w') as file:
    write_csv = csv.DictWriter(
        file, fieldnames=list(json_data[0].keys()), quoting=csv.QUOTE_NONNUMERIC
    )
    # Write the header first in the CSV file
    write_csv.writeheader()
    for data in json_data:
        write_csv.writerow(data)

# Verify that the data written is correct
with open(__csvFilePath__, 'r')as file:
    print(file.read())
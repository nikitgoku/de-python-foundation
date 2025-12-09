"""
Pandas Basics: Creating and Loading DataFrames

This module demonstrates various ways to create and load pandas DataFrames:
- Creating DataFrames from dictionaries
- Creating DataFrames from lists
- Loading DataFrames from CSV, JSON, and Excel files
- Using custom indices (list comprehension, NumPy arrays)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================================
# 1. LOAD DATA
# ============================================================================
# Dictionary with column names as keys and lists of values
# This is a common way to create a DataFrame with labeled columns
data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 55000, 65000, 52000]
    # 'JoiningDate': pd.to_datetime(['2020-01-15', '2019-03-10', '2021-07-23', '2018-11-01', '2020-06-30'])
}

# Define file paths relative to this script's location
# This ensures the script works regardless of the current working directory
csvFilePath = Path(__file__).resolve().parent / "data" / "employee_data.csv"
jsonFilePath = Path(__file__).resolve().parent / "data" / "employee_data.json"
excelFilePath = Path(__file__).resolve().parent / "data" / "employee_data.xlsx"

# Raw data as a list of lists (rows)
# Each inner list represents a record with [EmployeeID, Name, Department, Salary]
# Note: 'David' has a leading space that may need cleaning
data_list = [[1, 'Alice' , 'HR', 50000],
             [2, 'Bob', 'IT', 60000],
             [3, 'Charlie', 'Finance', 55000],
             [4, ' David', 'IT', 65000]]

# Creates a DataFrame with default index (0, 1, 2, 3, 4)
df = pd.DataFrame(data)

# Creates a DataFrame with custom index starting from 1 instead of 0
# Uses list comprehension to generate index: [1, 2, 3, 4, 5]
df_lstcomp = pd.DataFrame(data=data, index=[x for x in range(1, 6)])

# Creates a DataFrame with custom index using NumPy array
# More efficient for large indices compared to list comprehension
df_nparr = pd.DataFrame(data=data, index=np.array([x for x in range(1, 6)], int))

# Creates a DataFrame from raw list data
# Column names must be explicitly provided via 'columns' parameter
# Note: This data has only 4 rows (vs 5 in the dictionary data)
df_lst = pd.DataFrame(data=data_list, columns=['EmployeeID', 'Name', 'Department', 'Salary'])

# Reads a CSV file into a DataFrame
# CSV files are comma-separated plain text files, widely used for data exchange
# pandas.read_csv() automatically infers column names from the first row (header)
df_csv = pd.read_csv(csvFilePath)

# Reads a JSON file into a DataFrame
# JSON format stores structured data and is commonly used in APIs and web services
# pandas.read_json() parses JSON and converts it to tabular format
df_json = pd.read_json(jsonFilePath)

# Reads an Excel file (.xlsx) into a DataFrame
# Excel is widely used for business data; pandas requires openpyxl library for .xlsx files
# You may need to install: pip install openpyxl
df_excel = pd.read_excel(excelFilePath)

# ============================================================================
# 2. EXPLORING DATA
# ============================================================================
# Preview rows
# Print the first 2 rows from the dataframe (column labels are inclusive)
# print(f"{df.head(2)}")
# Print the last 2 rows from the dataframe
print(f"{df.tail(2)}")

# Viewing and Exploring data
print(f"{df.info()}")

# Display summary statistics (mean, std, min, max, etc.) for numeric columns
print(f"{df.describe()}")

# Display the shape of the DataFrame as a tuple (rows, columns)
print(f"{df.shape}")

# Display the column names as an Index object
print(f"{df.columns}")

# Access a row by label using .loc[] (row index 10 from df_csv)
print(f"{df_csv.loc[10]}")

# Access a row by integer position using .iloc[] (7th row, 0-indexed)
print(f"{df_csv.iloc[7]}")

# Access a specific cell by row label and column name using .loc[]
print(f"{df_csv.loc[10, 'Department']}")

# Access a slice of rows and columns using .iloc[] with start:stop:step notation (rows 0-8, every 2nd row, column 4)
print(f"{df_csv.iloc[0:9:2, 4]}")

# Access a specific cell by row label and column name using .at[] (faster for single values)
print(f"{df_csv.at[9, 'Name']}")

# Access a specific cell by integer row and column position using .iat[] (faster for single values)
print(f"{df_csv.iat[0, 1]}")

# ============================================================================
# 3. CLEANING DATA
# ============================================================================
print(f"{df_json}")                                  # print the DataFrame built from JSON for quick inspection
df_dropna = df_json.dropna()                        # drop any rows that contain at least one NA value
print(f"{df_dropna}")                               # show resulting DataFrame after dropping missing rows

df_fillna = df_json.fillna(value=0)                 # replace all NA values with 0 (useful for numeric columns)
print(f"{df_fillna}")                               # display DataFrame after filling missing values with 0

# Replace missing values using the mean salary from the 'df' DataFrame as a sensible default
df_fill_mean = df_json.fillna(df['Salary'].mean()) 
print(f"{df_fill_mean}")                            # show DataFrame after filling NA with mean salary

# ============================================================================
# 4. DATA TRANSFORMATION
# ============================================================================
df_csv['Annual_Bonus'] = df_csv['Salary'] * 0.10    # create a new column 'Annual_Bonus' = 10% of Salary
print(f"{df_csv}")                                  # display df_csv to verify the new column

# Create a categorical tier column from numeric Salary using a simple threshold
df_csv['Salary_Tier'] = df_csv['Salary'].apply(lambda x: 'Senior' if x > 55000 else 'Junior')
print(f"{df_csv}")                                  # show DataFrame after adding 'Salary_Tier'

# Map department names to numeric codes using a lookup dictionary
dept_map = {'HR': 1, 'IT': 2, 'Finance': 3, 'Marketing': 4, 'Sales': 5, 'Engineering': 6, 'Operations': 7}
df_csv['Dept_Code'] = df_csv['Department'].map(dept_map)  # add a mapped integer code column
print(f"{df_csv}")                                  # display df_csv to confirm Dept_Code values

# ============================================================================
# 5. GROUPING AND AGGREGATIONS
# ============================================================================
print(f"{df_csv.describe()}")                       # show numeric summaries for df_csv
print(f"{df_csv['Salary'].mean()}")                 # print overall average Salary
print(f"{df_csv['Annual_Bonus'].sum()}")            # total of the Annual_Bonus column
print(f"{df_csv['Salary'].agg(['sum', 'count', 'max'])}")  # multiple aggregations for Salary

# Compute mean salary per department using groupby and aggregation
average_salary = df_csv.groupby('Department')['Salary'].mean()
print(f"{average_salary}")                          # display mean salary per Department
print(f"{average_salary.info()}")                   # print meta info about the resulting Series

# Compute mean salary grouped by Department and Salary_Tier (multi-index result)
average_salary_by_tier = df_csv.groupby(['Department', 'Salary_Tier'])['Salary'].mean()
print(f"{average_salary_by_tier}")                  # display grouped means with multi-index

# ============================================================================
# 6. MERGING AND JOINING
# ============================================================================
# Build a small DataFrame with department manager info to demonstrate joins
dept_info = pd.DataFrame({
    'Department': ['HR', 'IT', 'Finance', 'Sales', 'Operations', 'Engineering', 'Marketing'],
    'Manager': ['Dart', 'Piet', 'Lisp', 'Julia', 'Kotlin', 'Haskell', 'Erlang']
})

merged_df = pd.merge(df_csv, dept_info, on='Department')  # inner join on the Department column
print(f"{merged_df}")

# Create two example yearly DataFrames to demonstrate concatenation and deduplication
data_2022 = {
    'EmployeeID': [101, 102, 103, 104, 105, 107],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'George'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'IT'],
    'Salary': [50000, 60000, 55000, 65000, 52000, 70000],
    'JoiningDate': ['2022-01-15', '2022-03-10', '2022-07-23', '2022-11-01', '2022-06-30', '2022-05-20']
}

df_2022 = pd.DataFrame(data_2022)                    # DataFrame representing hires/records for 2022

data_2024 = {
    'EmployeeID': [109, 112, 115, 118],
    'Name': ['Ian', 'Laura', 'Oscar', 'Riley'],
    'Department': ['Operations', 'HR', 'Sales', 'IT'],
    'Salary': [51000, 53000, 61000, 69000],
    'JoiningDate': ['2024-01-20', '2024-07-11', '2024-04-18', '2024-10-29']
}

df_2024 = pd.DataFrame(data_2024)                    # DataFrame representing hires/records for 2024

# Concatenate row-wise to build a combined dataset from multiple sources/years
df_combined = pd.concat([df_2022, df_2024])
print(f"{df_combined}")                              # display the combined DataFrame

# Create a Bonus Series to demonstrate column-wise concatenation and alignment by index
bonus = pd.Series([2000.0, 3500.0, 1500.0, 1000.0], name="Bonus")
# Concatenate along columns; Series aligns by index and will introduce NaN where indexes don't match
df_combined_with_bonus = pd.concat([df_2024, bonus], axis=1)
print(f"{df_combined_with_bonus}")                   # show DataFrame with Bonus column (NaN where missing)

# ============================================================================
# 7. BASIC VISUALISATION
# ============================================================================
# Create a simple bar plot of average salary per department (Series.plot returns an Axes)
average_salary.plot(kind='bar')                      # plot bars for each department's average salary
plt.title("Average Salary by Department")            # add a descriptive title
plt.xlabel("Department")                             # label x-axis for clarity
plt.ylabel("Average Salary")                         # label y-axis for clarity
plt.tight_layout()                                   # adjust layout to avoid clipping labels/titles
plt.show()  

# ============================================================================
# 8. EXPORTING DATA
# ============================================================================
# Build an export path next to the original CSV file
export_path = Path(__file__).resolve().parent / "data" / "employee_data_export.csv"  # export filename in data/ folder

# Export df_csv to CSV with UTF-8 encoding and without the DataFrame index
df_csv.to_csv(export_path, index=False, encoding='utf-8')

# Inform the user where the file was written
print(f"Exported df_csv to {export_path}")
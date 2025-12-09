from pathlib import Path
import pandas as pd
# Question: For every 'Salary_Tier' of 'Senior', increase the salary by 1000

# Define file paths relative to this script's location
csvFilePath = Path(__file__).resolve().parent / "data" / "employee_data_export.csv"

df_csv = pd.read_csv(csvFilePath)

# Approach 1: Using vectorised operation, to locate rows which has 'Senior' as their salary tier
# Define the condition
is_senior = df_csv['Salary_Tier'] == 'Senior'

# Use .loc[] to select only Senior' rows and increase their salary by 1000.00
df_csv.loc[is_senior, 'Salary'] = df_csv.loc[is_senior, 'Salary'] + 1000.00
print(f"{df_csv}")

# Approach 2: Using .apply() with a lambda function
# Note: To apply row-wise logic, we always select axis=1
"""
axis : {0 or 'index', 1 or 'columns'}, default 0
Axis along which the function is applied:

0 or 'index': apply function to each column.
1 or 'columns': apply function to each row.
"""
# df_csv['Salary'] = df_csv.apply(lambda row: row['Salary'] + 1000.00 if row['Salary_Tier'] == 'Senior' else row['Salary'],
#                                 axis=1)
# print(f"{df_csv}")

"""
Always prefer Vectorized Operations (.loc[] or numpy.where()) over .apply(lambda, axis=1) 
for simple conditional transformations, as they offer significant performance advantages on large datasets.
"""
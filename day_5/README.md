# Day 5 — Pandas Basics

📚 Overview

On Day 5, we focus on Pandas — a core library for data engineering workflows. You will learn how to load, explore, clean, transform, aggregate, join, visualize, and export structured datasets (CSV, JSON, Excel) using Pandas DataFrames.

🧠 Key Concepts

1. Creating DataFrames  
   ✅ A DataFrame is an in-memory table (like SQL or Excel). Each column is a Series.

2. Reading Data from Files  
   - `pd.read_csv(path)` — CSV  
   - `pd.read_json(path)` — JSON  
   - `pd.read_excel(path)` — Excel (requires openpyxl for .xlsx)

3. Exploring and Selecting Data  
   - `df.head()` — first rows  
   - `df.info()` — dtypes and non-null counts  
   - `df.shape` — (rows, cols)  
   - `df.columns` — column names  
   - Select columns: `df[["month", "revenue"]]`  
   - Filter rows: `df[df["revenue"] > 6000]`  
   - Sort: `df.sort_values(by="revenue", ascending=False)`

4. Cleaning and Transforming Data
   - Handling missing values: `dropna()`, `fillna()`  
   - Converting types: `df["col"] = df["col"].astype(int)`  
   - Renaming: `df.rename(columns={"old":"new"}, inplace=True)` (safe for full-DF ops)
   - Inplace best practice:
     - df.rename(..., inplace=True) — OK for whole DF
     - df["col"] = df["col"].fillna(x) — preferred for a single column (avoid chained assignment)

   Quick rules:
   - Use assignment for single-column changes: `df["col"] = ...`
   - Prefer vectorized operations (`.loc`, `np.where`) over `apply(axis=1)` for performance

5. Aggregations and Grouping
   - `df.groupby("key")["metric"].agg(["sum","mean","count"])`
   - Useful for GROUP BY style summaries and pivot-like results

6. Joining and Merging
   - `pd.merge(left, right, on="key", how="inner")` — SQL-like joins  
   - `pd.concat([df1, df2], ignore_index=True)` — stack vertically or horizontally

7. Basic Visualization
   - Use `Series.plot(kind="bar")` or `df.plot()` for simple charts (matplotlib backend)
   - Add titles/axis labels and `plt.tight_layout()` before `plt.show()`

⚙️ Common Pitfalls & Best Practices
- Always specify `encoding='utf-8'` when reading/writing external files unless needed otherwise.  
- For CSV writing use `df.to_csv(path, index=False, encoding='utf-8')`.  
- Avoid chained assignment that can trigger SettingWithCopyWarning. Assign back to the column.  
- Prefer vectorized `.loc` operations for conditional updates:
  - Good: `df.loc[df['Salary_Tier']=='Senior', 'Salary'] += 1000`
  - Avoid slow: `df.apply(lambda r: ..., axis=1)`

# 📑 Pandas Cheat Sheet

A quick reference for common Pandas commands and their purposes.

| Command                   | Purpose                                                                 |
|---------------------------|-------------------------------------------------------------------------|
| `pd.read_csv()`           | Load data from a CSV file into a DataFrame                              |
| `pd.read_json()`          | Load data from a JSON file                                              |
| `pd.read_excel()`         | Load data from an Excel file                                            |
| `.head()` / `.tail()`     | Preview the first/last rows of a DataFrame                              |
| `.info()`                 | Get column names, data types, and non‑null counts                       |
| `.describe()`             | Summary statistics (mean, std, min, max, quartiles)                     |
| `.shape` / `.columns`     | Get dimensions and column names                                         |
| `.loc[]` / `.iloc[]`      | Select rows/columns by label or position                                |
| `.dropna()` / `.fillna()` | Handle missing values (drop or fill)                                    |
| `.drop_duplicates()`      | Remove duplicate rows                                                   |
| `.rename()`               | Rename columns or index                                                 |
| `.apply()` / `.map()`     | Apply functions to columns or elements                                  |
| `.groupby()`              | Group data and apply aggregation functions (mean, sum, count, etc.)     |
| `pd.merge()`              | Join two DataFrames on a key                                            |
| `pd.concat()`             | Concatenate DataFrames along rows or columns                            |
| `.pivot_table()`          | Create pivot tables for summarization                                   |
| `.plot()`                 | Quick visualization (integrates with Matplotlib)                        |
| `.to_csv()` / `.to_json()`| Save DataFrame to CSV or JSON                                           |
| `.to_excel()`             | Save DataFrame to Excel                                                 |

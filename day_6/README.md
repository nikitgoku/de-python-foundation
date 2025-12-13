# Day 6 — Database Integration & ETL with Pandas

## Overview

On Day 6, we focus on building a closely resembling **ETL (Extract, Transform, Load) pipeline** that connect to real databases. We learned how to read data from PostgreSQL, clean and transform it using Pandas, and write results back to the database using SQLAlchemy.

## Key Concepts

1. **Database Connections with SQLAlchemy**
   - `create_engine()` — factory for DB connections
   - Context managers (`engine.begin()`, `engine.connect()`) — safe resource handling
   - Always call `engine.dispose()` when done

2. **Reading Data from Databases**
   - `pd.read_sql(sql, con=engine)` — execute SQL query and get a DataFrame
   - Example: `df = pd.read_sql("SELECT * FROM pizza_orders;", con=engine)`

3. **Extracting Data (Step 1)**
   - Query raw data from source tables
   - Use functions like `fetch_orders(engine)` to encapsulate DB reads

4. **Transforming Data (Step 2)**
   - Clean missing values: `df["col"].fillna(df["col"].mean())`
   - Convert types: `df["col"] = pd.to_numeric(df["col"], errors="coerce")`
   - Round decimals: `df["price"] = df["price"].round(2)`
   - Normalize text: `df["size"] = df["size"].str.strip().str.upper()`
   - Compute derived columns: `df["total_price"] = (df["price"] * df["quantity"]).round(2)`

5. **Loading Data (Step 3)**
   - Write DataFrames back to DB: `df.to_sql(name="table", con=engine, if_exists="replace")`
   - Control behavior: `if_exists="replace"` (drop & recreate), `"append"` (add rows), `"fail"` (error if exists)

6. Configuration Management
   - Store credentials in `.ini` files
   - Example `.ini`:
     ```
     POSTGRES_USER=postgres
     POSTGRES_PASSWORD=secret
     POSTGRES_HOST=localhost
     POSTGRES_PORT=5432
     POSTGRES_DB=pizza_shop
     ```

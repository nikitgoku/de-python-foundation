# Day 7 - Production‑Style ETL Pipeline

## Overview
On Day 7, we are focusing on builsing and designing a modular, reusable, production‑style pipeline that:
- Extracts data from a public REST API 
- Loads it into a Pandas DataFrame 
- Cleans, normalises, and reshapes the data 
- Saves the transformed data into PostgreSQL incrementally 
- Uses a modular folder structure similar to modern ETL frameworks.

## Folder Structure
```
day_7/
├── src/
│  ├── extract.py          # Extracts remote API data into DataFrame
│  ├── transform.py        # Pure transformation functions
│  ├── load.py             # Incremental loader to PostgreSQL
│  ├── config.py           # Config loader (.env and defaults)
│  ├── main.py             # Thin orchestrator: extract -> transform -> load
│  └── __init__.py
├── compose.yaml           # Python dependencies
└── README.md              # This file
```

## What each file does

- `extract.py`
  - Uses requests to call a REST API.
  - Builds a DataFrame from returned JSON; logs and returns an empty DataFrame on error.

- `transform.py`
  - Implements transform_posts() and other pure functions.
  - Validation, enforcing data types, parsing datetimes, flatenning, filling missing values.

- `load.py`
  - Implements Loader which:
    - Loads existing unique key values from destination table,
    - Filters new rows from the incoming DataFrame,
    - Appends new rows to the table using pandas.to_sql (append),
    - Logs behavior and handles missing tables gracefully.

- `config.py`
  - Loads configuration variables via config parser.
  - Exposes API_URL and a helper to construct the DB connection URL.

- `main.py`
  - Thin orchestrator: instantiate components and run ETL:
    - raw <- Extractor.extract_posts_data()
    - df <- transform_posts_data(raw)
    - Loader.load_incremental(df)

## Key Concepts

1. **Separation of Concerns**
   - Each module has one responsibility: extract, transform, or load.
   - Keeps code testable and easier to maintain.

2. **Idempotent / Incremental Loads**
   - The Loader inspects existing keys and only appends rows whose unique_key is not already present.
   - This prevents duplicates and supports re-runs of the pipeline.

3. **Robust Extraction**
   - Use timeouts and HTTP status checks during requests.
   - Return an empty DataFrame on extractor errors to avoid crashing the pipeline.

4. **Pure Transformations**
   - Transformation functions are pure: accept and return DataFrames.
   - This makes testing straightforward (no DB or network side-effects).

5. **Safe Database Writes**
   - Use SQLAlchemy engine and context managers for safe writes (transactions).
   - Use to_sql with append/replace semantics depending on behavior needed.

6. **Configuration & Secrets**
   - Use .env to store secrets and environment settings (do not commit .env).
   - Use python-dotenv to load environment values for local development.

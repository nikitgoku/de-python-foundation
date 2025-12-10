import pandas as pd
from loguru import logger
from .db import write_data

# Function to fetch the data using a sample query.
# The data is transformed into a pandas DataFrame, and returned to the main.
def fetch_orders(db_connection):
    sample_query = """SELECT * FROM pizza_orders;"""
    return pd.read_sql(sample_query, db_connection)

# ============================================================================
# DATA CLEANING
# ============================================================================
# Function to perform transformations, by cleaning the data, 
# adding additional column for total price, 
# Normalising the size column
# This function returns a cleaned dataframe
def clean_data(df):
    # Filter the orders with "status" marked as pending.
    df = df[df['status'] != 'Pending']

    # Fill the missing prices with mean value and assign back
    df['price'] = df['price'].fillna(df['price'].mean())

    # Ensure price is rounded to 2 decimal places and numeric
    df['price'] = pd.to_numeric(df['price']).round(2)

    # Normalise the text in the "size" column
    df['size'] = df['size'].str.upper()

    # Add the "total_price" column
    df['total_price'] = (df['price'] * df['quantity']).round(2)

    # Return the cleaned df
    return df

# ============================================================================
# ANALYSIS USING AGGREGATIONS
# ============================================================================
# Function to get average price by pizza type and size
def average_pizza_price(df):
    return df.groupby(['pizza_type', 'size'])['price'].mean()

# Function to get busiest order hour
def busiest_order_hour(df):
    # Extract 'hour' from the timestamp
    df['hour'] = df['order_time'].dt.hour

    # Get the count of orders grouped by every hour
    return df.groupby('hour')['order_id'].count()

# ============================================================================
# LOAD DATA
# ============================================================================
def persist_results(engine, cleaned_df):
    # Write cleaned dataframe (creates or replaces table 'cleaned_orders')
    write_data(engine, cleaned_df, "cleaned_orders", if_exists="replace")
    # Write average price by pizza_type & size
    write_data(engine, average_pizza_price(cleaned_df), "avg_pizza_price", if_exists="replace")
    # Write busiest order hour
    write_data(engine, busiest_order_hour(cleaned_df), "busiest_order_hour", if_exists="replace")

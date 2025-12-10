from loguru import logger
from pathlib import Path
from .config import get_connection_url
from .db import create_db_engine
from .data_transactions import fetch_orders, clean_data, busiest_order_hour, average_pizza_price, persist_results

def main():
    # Define the config file path
    config_file_path = Path(__file__).resolve().parents[1] / "configs" /"config.ini"
    logger.info(f"{config_file_path}")

    # Get the connection URL to the PostgreSQL database
    connection_url = get_connection_url(config_file_path)

    # Get engine instance
    engine = create_db_engine(connection_url)

    # Create a connection to the database using the  engine instance
    db_connection = engine.connect()

    try:
        df = fetch_orders(db_connection)
        cleaned_df = clean_data(df)
        # avg_pizza_price_df = average_pizza_price(cleaned_df)
        # busiest_order_hour_df = busiest_order_hour(cleaned_df)
        persist_results(engine, cleaned_df)
    finally:
        db_connection.close()
        engine.dispose()
        logger.info("Connection Closed. Engine Disposed")


if __name__ == "__main__":
    main()
from sqlalchemy import create_engine
from loguru import logger

def create_db_engine(connection_url):
    """Create SQLAlchemy engine."""
    try:
        # Create the DB Engine instance for the database
        db_engine_instance = create_engine(connection_url)
        logger.info(f"Engine for database 'pizza_shop' created successfully.")
    except Exception as e:
        logger.warning(f"Failed to connect to database 'pizza_shop': {e}")

    return db_engine_instance

def write_data(engine, df, table_name, if_exists):
    """Write DataFrame to DB inside a transaction."""
    try:
        df.to_sql(
            name=table_name, 
            con=engine, 
            if_exists=if_exists, 
            index=False
        )
        logger.info(f"Wrote table: {table_name}")
    except Exception as e:
        logger.error(f"Failed writing {table_name}: {e}")
        raise
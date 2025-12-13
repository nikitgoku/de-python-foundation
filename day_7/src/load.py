import pandas as pd
from sqlalchemy import create_engine, text
from loguru import logger

"""
Small incremental loader for writing new rows from a DataFrame
into a target SQL table using SQLAlchemy. The loader ensures only
rows with new values for a configured unique_key are appended.
"""

class Loader:
    """
    Loader encapsulates the logic to insert only new rows into a DB table.

    Args:
        connection_uri (str): SQLAlchemy-compatible connection URI for DB.
        table (str): Destination table to insert into.
        unique_key (str): Column name used to detect duplicates / existing rows.
    """
    def __init__(self, connection_uri: str, table: str, unique_key: str):
        self.engine = create_engine(connection_uri)
        self.table = table
        self.unique_key = unique_key

    def _get_existing_ids(self) -> set:
        """
        Query the destination table and return a set of existing unique key values.

        Returns:
            set: set of values currently present in self.table under self.unique_key.
                 Returns empty set if table does not exist or on query error.
        """
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(f"SELECT {self.unique_key} FROM {self.table};"))
                # Extract values from result rows into a set for fast membership checks
                return {row[0] for row in result}
        except Exception:
            # Either Table missing or first instance of the batch is being loaded
            # warn and return empty set
            logger.warning(f"Table {self.table} does not exist yet.")
            return set()
        
    def load_incremental(self, df: pd.DataFrame):
        """
        Insert new rows from df into the configured table.

        Steps:
         - If df empty: warn and return.
         - Read existing unique keys from DB.
         - Filter df for rows whose unique_key value is not present in DB.
         - If there are new rows: append them using pandas.to_sql.

        Args:
            df (pd.DataFrame): DataFrame containing rows to insert. Must contain self.unique_key column.
        """
        if df.empty:
            logger.warning("Loader received an empty DataFrame")
            return pd.DataFrame()

        # Collect IDs already in the table to avoid duplicates
        existing_ids = self._get_existing_ids()

        # Filter out rows that already exist. This uses pandas boolean indexing.
        new_rows = df[~df[self.unique_key].isin(existing_ids)]

        # If no new rows, log and return
        if new_rows.empty:
            logger.info("No new rows to insert.")
            return

        logger.info(f"{len(new_rows)} of new rows to be inserted.")

        # Use pandas.to_sql to append rows into the SQL table
        # Default arguments: if_exists='append' and index=False are important here
        new_rows.to_sql(
            name=self.table, 
            con=self.engine, 
            if_exists="append", 
            index=False
        )

        logger.info(f"Inserted {len(new_rows)} new rows in {self.table}.")
import requests
import pandas as pd
from loguru import logger
from .config import API_URL

class Extractor:
    """
        Extract data from the public REST API and return as a Pandas DataFrame.
    """
    def __init__(self, url: str):
        self.url = url

    def extract_posts_data(self) -> pd.DataFrame:
        """
        Extract data from the public REST API and return as a Pandas DataFrame.

        Steps:
        - Request the URL and parse JSON
        - Validate returned payload shape
        - Convert nested posts list into pandas DataFrame
        - Return an empty DataFrame on any failure for safe pipeline semantics
        """
        logger.info("Starting the Extraction Process.")
        try:
            # Log the start of the data extraction process
            logger.info(f"Requesting data from {API_URL}")
            
            # Send GET request to the API
            response = requests.get(self.url, timeout=10)    # 10 sec timeout

            # Rase an exception
            response.raise_for_status()

            # Parse the extracted JSON data into Python dict
            data = response.json()

            # Check if the API returned any data
            if not data:
                logger.warning("No data returned from the API!")
                # Return an empty DataFrame to avoid breaking the pipeline
                return pd.DataFrame()
            
            # Convert the dictionary data into pandas DataFrame
            # The data we want is the value associated with the 'posts' key
            df = pd.DataFrame(data['posts'])

            # Log summary information of the data\
            logger.info(F"Extraced {len(df)} rows and {len(df.columns)} columns from the API.")

            # Return the DataFrame
            return df

        except Exception as e:
            # Return an empty dataframe when failed
            logger.error(f"Error while extracting data from API: {e}")
            return pd.DataFrame()
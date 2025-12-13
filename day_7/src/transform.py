import pandas as pd
from datetime import datetime, timezone
from loguru import logger

class Transformer:
    def transform_posts(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Transform posts DataFrame into a normalized structure ready for loading.

        Key steps:
        - Validate input DataFrame and return empty DF if no rows
        - Enforce dataType
        - Flatten the nested dictionary
        - Parse timestamp columns into pandas datetime dtype
        - Select final columns and return

        Args:
            df (pd.DataFrame): Raw DataFrame from the API.

        Returns:
            pd.DataFrame: Cleaned and enriched DataFrame ready for loading.
        """
        # Log the start of the transformation process
        logger.info("Starting the Transformation Process.")

        # Check if the DataFrame passed is correct
        if df is None or df.empty:
            logger.warning("Empty DataFrame passed to transform_post() method.")
            return df
        
        # Create a new object, so that modification is done on a new df, and not
        # the original data, so that original data is maintained
        df = df.copy()
        
        # Enforce data types
        df['id']     = df['id'].astype('int64')
        df['views']  = df['views'].astype('int64')
        df['userId'] = df['userId'].astype('int64')
        df['title']  = df['title'].astype('string')
        df['body']   = df['body'].astype('string')

        # Flatten the "reactions" column, as it contains dictionary
        # This creates a new DataFrame: reactions_df
        reactions_df = pd.json_normalize(df['reactions'])

        # Rename columns to avoid conflicts
        reactions_df.columns = ["reactions_" + col for col in reactions_df.columns]

        # Drop the nested column
        df_to_merge = df.drop(columns=["reactions"])

        # Concatenate the DataFrame horizontally (on axis=1)
        df_flattened = pd.concat([df_to_merge, reactions_df], axis=1)

        # Fill the missing values wiht a placeholder: "N/A"
        # This avoids any missing values related issues
        df_flattened.fillna("N/A", inplace=True)

        # Add metadata
        df['ingestion_timestamp'] = datetime.now(timezone.utc)

        # Log the completion of the transformation process, summarising the 
        # transformed DataFrame
        logger.info(f"Transformation complete. The data now contains {len(df_flattened)} rows and {len(df_flattened.columns)} columns.")

        # Return the transformed DataFrame
        return df_flattened

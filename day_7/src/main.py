from loguru import logger
from .config import API_URL, CONNECTION_URI, TARGET_TABLE_NAME, UNIQUE_KEY
from .extract import Extractor
from .transform import Transformer
from .load import Loader

class ETLPipeline:
    def __init__(self, extractor, transformer, loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self):
        # Log the start of the Pipeline
        logger.info("Starting ETL Pipeline...")

        df_raw = self.extractor.extract_posts_data()
        df_clean = self.transformer.transform_posts(df_raw)
        self.loader.load_incremental(df_clean)

        logger.info("ETL Pipeline complete successfully.")



if __name__ == "__main__":
    # Instantiate, Extractor, Transformer and Loader classobjects
    # 1. Extractor
    extractor = Extractor(API_URL)
    # 2. Transformer
    transformer = Transformer()
    # 3. Loader
    loader = Loader(CONNECTION_URI, TARGET_TABLE_NAME, UNIQUE_KEY)
    
    # Instantiate ETLPipeline class object, with extractor, transformer, and loader
    pipeline = ETLPipeline(extractor, transformer, loader)
    pipeline.run()

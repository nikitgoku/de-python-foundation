import configparser
from loguru import logger
from pathlib import Path

config_file_path = Path(__file__).resolve().parents[1] / "configs" / "config.ini"

config = configparser.ConfigParser()

# Read from the configuration file
try:
    config.read(config_file_path)
except configparser.Error as e:
    logger.error(f"Configuration file not found. Error: {e}")
    exit(1)

# Public REST API
API_URL = config.get("API", "API_BASE_URL")

# Database Credentials
POSTGRES_USER     = config.get('DATABASE', 'POSTGRES_USER')
POSTGRES_PASSWORD = config.get("DATABASE", "POSTGRES_PASSWORD")
POSTGRES_DB       = config.get("DATABASE", "POSTGRES_DB")
POSTGRES_HOST     = config.get("DATABASE", "POSTGRES_HOST")
POSTGRES_PORT     = config.get("DATABASE", "POSTGRES_PORT")

CONNECTION_URI = url = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Target table name
TARGET_TABLE_NAME = "user_posts_data"
UNIQUE_KEY = "id"
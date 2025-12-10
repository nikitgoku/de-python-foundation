import configparser
from loguru import logger

def get_connection_url(config_file_path):
    # Create a config parser object
    config = configparser.ConfigParser()
    # Read from the configuration file
    try:
        config.read(config_file_path)
    except configparser.Error as e:
        logger.error(f"Configuration file not found. Error: {e}")
        exit(1)

    # Prepare the URL to connect with the database
    url = f"postgresql+psycopg2://{config.get('DATABASE', 'POSTGRES_USER')}:{config.get('DATABASE', 'POSTGRES_PASSWORD')}@{config.get('DATABASE', 'POSTGRES_HOST')}:{config.get('DATABASE', 'POSTGRES_PORT')}/{config.get('DATABASE', 'POSTGRES_DB')}"

    # Return the URL
    return url
from loguru import logger


def say_hello(name):
    logger.info(f"Saying Hello to {name}")
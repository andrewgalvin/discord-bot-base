import logging

from bot.config import DISCORD_BOT_NAME


def setup_logger(name, level=logging.INFO):
    """
    Sets up a logger with the specified name and logging level.
    Args:
        name (str): The name of the logger.
        level (int, optional): The logging level. Defaults to logging.INFO.
    Returns:
        logging.Logger: Configured logger instance.
    """
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(stream_handler)

    return logger


# Update name of logger based on your project
logger = setup_logger(DISCORD_BOT_NAME, logging.DEBUG)

import logging
import sys


def setup_logger():

    logger = logging.getLogger("binance_bot")
    logger.setLevel(logging.INFO)

    logging_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler = logging.FileHandler("trading_bot.log")
    console_handler = logging.StreamHandler(sys.stdout)

    file_handler.setFormatter(logging_format)
    console_handler.setFormatter(logging_format)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger

logger = setup_logger()

#logger_config.py

import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

def setup_logging():
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)

    current_date = datetime.now().strftime('%Y-%m-%d')
    log_file = os.path.join(log_dir, f'{current_date}.log')

    file_handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, encoding='utf-8')
    file_handler.suffix = "%Y-%m-%d.log"
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

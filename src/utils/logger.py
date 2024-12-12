import logging
from datetime import datetime

class Logger:
    def __init__(self):
        logging.basicConfig(
            filename='logs/file_operations.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger()

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)

# utility/log_generator.py
import os
import logging

class LogGenerator:
    @staticmethod
    def get_logger():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Logs', 'automation.log')
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

"""
Purpose: This file includes all the Utilities needed for project

    FileAndStreamLogger is a called for Log management
"""

import logging
from configparser import ConfigParser
from logging.handlers import RotatingFileHandler

parser = ConfigParser()
parser.read("config.ini")


class FileAndStreamLogger:
    def __init__(self, name, log_file):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Create a ROTATING file handler
        # file_handler = logging.FileHandler(log_file)
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=parser.getfloat("Logger", "LOG_FILE_SIZE_maxBytes") or 10_00_000,
            backupCount=parser.getint("Logger", "LOG_FILE_backupCount") or 2,
        )
        file_handler.setLevel(logging.DEBUG)

        # Create a stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        # Create a formatter and add it to the handlers
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)8s %(name)s %(message)s",
            datefmt="%d-%b-%Y %I:%M:%S %p",
        )
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

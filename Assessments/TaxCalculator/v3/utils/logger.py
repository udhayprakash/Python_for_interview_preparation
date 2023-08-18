"""
Logger utility
"""

import logging


class Logger:
    def __init__(self):
        self.logger = logging.getLogger("tax_calculator")
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)

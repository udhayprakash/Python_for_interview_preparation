import logging
from unittest.mock import MagicMock

import pytest
from your_file_name import FileAndStreamLogger


@pytest.fixture
def mock_config_parser(monkeypatch):
    mock_parser = MagicMock()
    monkeypatch.setattr("your_file_name.parser", mock_parser)
    return mock_parser


def test_file_and_stream_logger_init(mock_config_parser):
    logger_name = "test_logger"
    log_file = "test_log.txt"

    logger = FileAndStreamLogger(logger_name, log_file)

    assert logger.logger.name == logger_name
    assert isinstance(logger.logger.handlers[0], logging.handlers.RotatingFileHandler)
    assert isinstance(logger.logger.handlers[1], logging.StreamHandler)


def test_file_and_stream_logger_debug(mock_config_parser):
    logger_name = "test_logger"
    log_file = "test_log.txt"
    message = "Test debug message"

    logger = FileAndStreamLogger(logger_name, log_file)
    logger.debug(message)

    logger.logger.debug.assert_called_once_with(message)


# Similarly, write test cases for other methods: info, warning, error, critical

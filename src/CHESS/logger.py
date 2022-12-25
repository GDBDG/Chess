"""Logging configuration"""
import json
import logging
import os
import re
from datetime import datetime

import coloredlogs
import json_log_formatter

from src.CHESS.constants import SOURCE_DIR

APP_LOG_LEVEL = "DEBUG"
LOG_DIR = SOURCE_DIR / "logs/"
LOG_FILE = LOG_DIR / "logfile.json"


def escape_ansi(line: str):
    """Remove formatting characters in the log message."""
    ansi_escape = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]")
    return ansi_escape.sub("", line)


class LogFormatter(json_log_formatter.JSONFormatter):
    """Custom json formatter for logs"""

    def json(self, message, extra, record):
        """
        Store the logs in json
        @param message:
        @param extra:
        @param record:
        @return: dict with logs
        """
        dict_check = extra.copy()
        for key, value in dict_check.items():
            try:
                json.dumps(value)
            except TypeError:
                del extra[key]
        # Include builtin
        log_response = {"app": "chess"}
        if "time" not in extra:
            log_response["date"] = datetime.utcnow()
        log_response["type"] = record.levelname
        log_response["function"] = record.name + ":" + record.funcName
        log_response["info"] = escape_ansi(message)

        if record.exc_info:
            log_response["exc_info"] = self.formatException(record.exc_info)

        return {**log_response, **extra}


def create_logger():
    """
    Instantiate the logger
    @return: instance of logger
    """
    logger = logging.getLogger("log_app")
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)
        coloredlogs.install(level="DEBUG")
        os.makedirs(LOG_DIR, exist_ok=True)
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setLevel(APP_LOG_LEVEL)
        file_handler.setFormatter(LogFormatter())
        logger.addHandler(file_handler)
    return logger


LOGGER = create_logger()

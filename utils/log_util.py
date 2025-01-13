import datetime
import logging
import os
from pathlib import Path


class LoggingUtility:

    def __init__(self):
        self.logger = logging.getLogger('pytest_logger')
        self.logger.setLevel(logging.DEBUG)
        get_log_file_path = self.initialize_log_file()

        # Check if the logger has handlers already
        if not self.logger.handlers:
            # Create handlers
            file_handler = logging.FileHandler(get_log_file_path)
            file_handler.setLevel(logging.DEBUG)

            # Create formatters and add it to handlers
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)

            # Add handlers to the logger
            self.logger.addHandler(file_handler)

    def initialize_log_file(self):
        log_file_path = None
        if log_file_path is None:
            log_directory = Path(os.getcwd()) / 'logs'
            log_directory.mkdir(parents=True, exist_ok=True)

            # Get current date
            current_date = datetime.datetime.now()
            formatted_date = current_date.strftime("%Y%m%d")

            # Generate logs file path using only the date
            log_file_path = log_directory / f"{formatted_date}_logs.txt"
            return log_file_path

    def get_log_formatted_message(self, message_template, log_level, **kwargs):

        formatted_message = message_template.format(**kwargs)

        match log_level:
            case "debug":
                self.logger.debug(formatted_message)
            case "info":
                self.logger.info(formatted_message)
            case "warning":
                self.logger.warning(formatted_message)
            case "error":
                self.logger.error(formatted_message)
            case "critical":
                self.logger.critical(formatted_message)
        return formatted_message


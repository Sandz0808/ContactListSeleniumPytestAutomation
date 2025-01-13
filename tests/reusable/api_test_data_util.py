import json
import os
from pathlib import Path
from utils.log_util import LoggingUtility
from utils.config_util import ConfigReader
from utils.exception_message_util import *
from utils.log_message_util import *


class ApiTestDataUtil:
    def __init__(self):
        self.config_reader = ConfigReader()
        self.test_data_path = Path(os.getcwd()) / self.config_reader.get_value('paths', 'test_data_path')
        self.data = None
        self.check_path_exist = False
        self.log = LoggingUtility()

    def check_testdata_path(self):
        """Check if the test data exists."""
        if not self.check_path_exist:
            if not os.path.exists(self.test_data_path):
                self.log.get_log_formatted_message(DATA_DOES_NOT_EXIST, "error")
                return False
            self.check_path_exist = True
        return True

    def load_data(self):
        """Load test data from the JSON file."""
        if self.data is None:
            if not self.check_testdata_path():
                return None  # Return None if the path doesn't exist

            try:
                with open(self.test_data_path, 'r') as file:
                    self.data = json.load(file)
                    self.log.get_log_formatted_message(TEST_DATA_LOADED, "info")
            except Exception as e:
                self.log.get_log_formatted_message(FAILED_TO_LOAD_DATA, "error")
                return None

        return self.data

    def get_api_testdata(self, test_key):
        """Retrieve test data specifically for API tests."""
        json_data = self.load_data()
        if json_data is None:
            self.log.get_log_formatted_message(FAILED_TO_LOAD_DATA, "error")
            return None

        if test_key not in json_data:
            raise KeyError(self.log.get_log_formatted_message(TEST_KEY_NOT_FOUND, "error"))

        return json_data[test_key]

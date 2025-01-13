import json
import os
from pathlib import Path
from utils.config_util import ConfigReader
from utils.reporter_util import ReporterUtil
from utils.log_message_util import *
from utils.exception_message_util import *

config_reader = ConfigReader()
TESTDATA_PATH = Path(os.getcwd()) / config_reader.get_value('paths', 'test_data_path')


class JsonDataUtil:
    DATA = None
    CHECK_PATH_EXIST = False

    def __init__(self, driver):
        self.driver = driver
        self.reporter = ReporterUtil(driver)

    def check_testdata_path(self):
        """Check if the test data exists."""
        if not self.CHECK_PATH_EXIST:
            if not os.path.exists(TESTDATA_PATH):
                self.reporter.results_reporter(NO_TESTDATA_FILE_EXIST_MESSAGE, "debug", testdata_path=TESTDATA_PATH)
                return False

            self.CHECK_PATH_EXIST = True
        return True

    def load_data(self):
        """Load test data from the JSON file."""
        if self.DATA is None:
            ""
            if not self.check_testdata_path():
                return None  # Return None if the path doesn't exist

            try:
                with open(TESTDATA_PATH, 'r') as file:
                    self.DATA = json.load(file)
                    self.reporter.results_reporter(TESTDATA_FILE_EXIST_MESSAGE, testdata_path=TESTDATA_PATH)
            except Exception as e:
                self.reporter.results_reporter(NO_TESTDATA_FILE_EXCEPTION_MESSAGE, "error", testdata_path=TESTDATA_PATH,
                                               error=e)
                return None

        return self.DATA

    def get_testdata(self, test_key):
        """Retrieve data from the loaded test data."""
        json_data = self.load_data()
        if test_key not in json_data:
            raise KeyError(self.reporter.results_reporter(TEST_KEY_NOT_FOUND, "error"))

        result = json_data[test_key]  # This returns the entire dictionary for 'valid_login'

        if result:
            self.reporter.results_reporter(VALUE_RETRIEVED_MESSAGE, result=result)
        return result

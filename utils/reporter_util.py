import pytest
from datetime import datetime
from conftest import get_current_test_info
from utils.config_util import ConfigReader
from utils.log_util import LoggingUtility
from utils.screenshot_util import ScreenshotUtility

log = LoggingUtility()
config_reader = ConfigReader()
screenshot = ScreenshotUtility()


class ReporterUtil:

    def __init__(self, driver):
        self.driver = driver

    def results_reporter(self, log_message, log_level="info", **kwargs):
        current_test = get_current_test_info()
        test_file = current_test.get('test_file')
        test_function = current_test.get('test_function')
        test_scenario_name = test_file.replace("tests", "").replace(".py", " ").replace("_", " ").strip().title()
        test_case_name = test_function.replace("test", "").replace("_", " ").strip().title()
        capture_screenshot = config_reader.get_value("screenshot_settings", "capture_screenshot")
        screenshot_name = self.get_screenshot_datetime()
        # Passed if log_level = info
        if log_level == "info":

            log.get_log_formatted_message(log_message, log_level, **kwargs)
            if capture_screenshot == "Yes":
                screenshot.save_screenshot(self.driver,test_scenario_name, test_case_name, screenshot_name)
        else:
            # Failed if log_level = warning, error, debug or critical
            screenshot.save_screenshot(self.driver,test_scenario_name, test_case_name, screenshot_name)
            if capture_screenshot == "Yes":
                screenshot.save_screenshot(self.driver,test_scenario_name, test_case_name, screenshot_name)
            pytest.fail(log.get_log_formatted_message(log_message, log_level, **kwargs))

    def get_screenshot_datetime(self):
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%m%d%Y")
        formatted_time = current_datetime.strftime("%H%M%S%f")[:9]
        screenshot_name = f"screenshot_{formatted_date}_{formatted_time}"
        return screenshot_name

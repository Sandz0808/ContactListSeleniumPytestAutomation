import datetime
import os
from pathlib import Path
from utils.config_util import ConfigReader
from utils.exception_message_util import *
from utils.log_message_util import *
from utils.log_util import LoggingUtility

config_reader = ConfigReader()
log = LoggingUtility()


class ScreenshotUtility:
    RUN_FOLDER = None

    def __init__(self):
        self.screenshot_base_path = Path(os.getcwd()) / config_reader.get_value('paths', 'screenshot_folder')

    def setup_folder(self):
        """Sets up the base folder for storing screenshots for the current test run."""
        if self.RUN_FOLDER is None:
            current_datetime = datetime.datetime.now()
            formatted_date = current_datetime.strftime("%Y%m%d")
            formatted_time = current_datetime.strftime("%H%M%S")
            self.RUN_FOLDER = self.screenshot_base_path / f"{formatted_date}_{formatted_time}_Screenshots"
            self.RUN_FOLDER.mkdir(parents=True, exist_ok=True)

    def create_scenario_folder(self, scenario: str) -> Path:
        """Creates a folder for the specified scenario."""
        scenario_folder = self.RUN_FOLDER / scenario
        scenario_folder.mkdir(parents=True, exist_ok=True)
        return scenario_folder

    def create_testcase_folder(self, scenario: str, test_case: str, iteration: int = 0) -> Path:
        """Creates a folder for the specified test case under the given scenario."""
        scenario_folder = self.create_scenario_folder(scenario)
        tc_folder = scenario_folder / test_case
        tc_folder.mkdir(parents=True, exist_ok=True)

        # If there is an iteration, create a subfolder for it
        if iteration > 0:
            iteration_folder = tc_folder / f"Iteration_{iteration}"
            iteration_folder.mkdir(parents=True, exist_ok=True)
            return iteration_folder
        else:
            return tc_folder

    def save_screenshot(self, driver, scenario: str, test_case: str, filename: str, iteration: int = 0):
        self.setup_folder()
        """Saves a screenshot to the appropriate folder based on scenario, test case, and iteration."""
        # Determine the folder structure for saving the screenshot
        if iteration > 0:
            iteration_folder = self.create_testcase_folder(scenario, test_case, iteration)
            screenshot_file = iteration_folder / f"{filename}.png"
        else:
            tc_folder = self.create_testcase_folder(scenario, test_case)
            screenshot_file = tc_folder / f"{filename}.png"

        # Save screenshot with try-except block
        try:
            driver.save_screenshot(str(screenshot_file))
            log.get_log_formatted_message(SCREENSHOT_MESSAGE, "info")
        except Exception as e:
            log.get_log_formatted_message(SCREENSHOT_SAVING_EXCEPTION_MESSAGE, "error", error=e)

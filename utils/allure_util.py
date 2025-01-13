import allure
import json
import os
from utils.config_util import ConfigReader
from selenium.common.exceptions import WebDriverException

class AllureStepWithAttachment:
    def __init__(self, driver, step_description):
        self.driver = driver
        self.step_description = step_description

    def __enter__(self):
        self.step = allure.step(self.step_description)  # Start the allure step
        self.step.__enter__()  # Explicitly enter the step context
        return self

    @staticmethod
    def attach_response(data=None):
        config_reader = ConfigReader()
        response_file_path = config_reader.get_value('paths', 'response_file_path')

        if data is None:
            try:
                if not os.path.exists(response_file_path):
                    return

                # If no data is provided, try to load it from the response file
                with open(response_file_path, 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                return
            except json.JSONDecodeError:
                return

        if data:
            json_data = json.dumps(data, indent=4)  # Pretty-print JSON response
            allure.attach(json_data, name="API Response", attachment_type=allure.attachment_type.JSON)


    def __exit__(self, exc_type, exc_val, exc_tb):
        # Always take a screenshot if driver is not None
        if self.driver is not None:  # This explicitly checks if driver is not None
            try:
                screenshot = self.driver.get_screenshot_as_png()
                attachment_name = "image_on_failure" if exc_type else "image"
                allure.attach(screenshot, name=attachment_name, attachment_type=allure.attachment_type.PNG)
            except WebDriverException as e:
                # Handle specific WebDriverException when taking a screenshot
                error_message = f"Error while capturing screenshot: {str(e)}"
                allure.attach(error_message, name="screenshot_error", attachment_type=allure.attachment_type.TEXT)
            except IOError as e:
                # Handle specific IOErrors for file handling issues
                error_message = f"IO Error during screenshot: {str(e)}"
                allure.attach(error_message, name="screenshot_io_error", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                # General fallback in case of unforeseen errors
                error_message = f"Unexpected error during screenshot: {str(e)}"
                allure.attach(error_message, name="screenshot_unknown_error",
                              attachment_type=allure.attachment_type.TEXT)

        # Exit the allure step context
        self.step.__exit__(exc_type, exc_val, exc_tb)

        # If an exception occurred, re-raise it
        if exc_type is not None:
            raise exc_val


'''UPDATE: Fix Warning on Broad exception'''
''' PREVIOUS VERSION'''
'''
def __exit__(self, exc_type, exc_val, exc_tb):
        # Always take a screenshot if driver is not None
        if self.driver is not None:  # This explicitly checks if driver is not None
            try:
                screenshot = self.driver.get_screenshot_as_png()
                attachment_name = "image_on_failure" if exc_type else "image"
                allure.attach(screenshot, name=attachment_name, attachment_type=allure.attachment_type.PNG)
            except Exception:
                # If there's an error while taking the screenshot, attach error screenshot
                allure.attach(screenshot, name="screenshot_error", attachment_type=allure.attachment_type.PNG)

        # Exit the allure step context
        self.step.__exit__(exc_type, exc_val, exc_tb)

        # If an exception occurred, re-raise it
        if exc_type is not None:
            raise exc_val
'''
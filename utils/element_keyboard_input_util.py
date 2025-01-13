from utils.element_wait_util import ElementWaitUtil
from utils.reporter_util import ReporterUtil
from utils.log_message_util import *
from utils.exception_message_util import *


class ElementKeyboardInputUtil:

    def __init__(self, driver):
        """Initialize with the WebDriver instance."""
        self.driver = driver
        self.reporter = ReporterUtil(driver)
        self.wait_util = ElementWaitUtil(driver)

    def input_element(self, locator, input_value):
        """Input value into an element specified by the locator after waiting for it to be visible."""
        element = self.wait_util.wait_element_to_be_visible(locator)
        try:
            element.send_keys(input_value)
            self.reporter .results_reporter(INPUT_TEXT_MESSAGE, input_value=input_value, locator=locator)
        except Exception as e:
            self.reporter.results_reporter(INPUT_EXCEPTION_ERROR_MESSAGE, "error", error=e)

    def clear_element(self, locator):
        """Input value into an element specified by the locator after waiting for it to be visible."""
        element = self.wait_util.wait_element_to_be_visible(locator)
        try:
            element.clear()
            self.reporter .results_reporter(CLEAR_MESSAGE, locator=locator)
        except Exception as e:
            self.reporter.results_reporter(CLEAR_ERROR_MESSAGE, "error", error=e)




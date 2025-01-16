from utils.config_util import ConfigReader
from utils.reporter_util import ReporterUtil
from utils.log_message_util import *
from utils.exception_message_util import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



config_reader = ConfigReader()


class ElementWaitUtil:
    def __init__(self, driver):
        self.driver = driver
        self.reporter = ReporterUtil(driver)

    def wait_element_to_be_visible(self, locator):
        """Wait for the element to be visible."""
        try:
            element = WebDriverWait(self.driver, config_reader.get_value
            ('settings', 'element_visibility_timeout')).until(
                EC.visibility_of_element_located(locator)
            )
            self.reporter.results_reporter(VISIBLE_ELEMENT_MESSAGE, locator=locator)
            return element
        except TimeoutException as e:
            self.reporter.results_reporter(TIMEOUT_EXCEPTION_ERROR_MESSAGE, "error", locator=locator)

    def wait_element_to_be_present(self, locator):
        """Wait for the element to be present."""
        try:
            element = WebDriverWait(self.driver, config_reader.get_value
            ('settings', 'element_visibility_timeout')).until(
                EC.presence_of_element_located(locator)
            )
            self.reporter.results_reporter(VISIBLE_ELEMENT_MESSAGE, locator=locator)
            return element
        except TimeoutException as e:
            self.reporter.results_reporter(TIMEOUT_EXCEPTION_ERROR_MESSAGE, "error", locator=locator)

    def wait_for_element(self, locator, condition_type='visible'):
        """Wait for the element based on the specified condition."""
        try:
            if condition_type == 'visible':
                condition = EC.visibility_of_element_located(locator)
            elif condition_type == 'present':
                condition = EC.presence_of_element_located(locator)
            else:
                raise ValueError("Invalid condition type. Use 'visible' or 'present'.")

            element = WebDriverWait(self.driver,
                                    config_reader.get_value('settings', 'element_visibility_timeout')).until(condition)
            self.reporter.results_reporter(
                VISIBLE_ELEMENT_MESSAGE if condition_type == 'visible' else "Element Present", locator=locator)
            return element
        except TimeoutException as e:
            self.reporter.results_reporter(TIMEOUT_EXCEPTION_ERROR_MESSAGE, "error", locator=locator)


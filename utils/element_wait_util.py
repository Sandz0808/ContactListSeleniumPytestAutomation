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





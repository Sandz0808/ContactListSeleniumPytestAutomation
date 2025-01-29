from utils.element_wait_util import ElementWaitUtil
from utils.reporter_util import ReporterUtil
from utils.log_message_util import *
from utils.exception_message_util import *
from selenium.common.exceptions import WebDriverException


class ElementMouseActionsUtil:

    def __init__(self, driver):
        self.driver = driver
        self.reporter = ReporterUtil(driver)
        self.wait_util = ElementWaitUtil(driver)

    def click_element(self, locator):
        element = self.wait_util.wait_element_to_be_visible(locator)
        try:
            element.click()
            self.reporter.results_reporter(CLICKING_MESSAGE, locator=locator)
        except WebDriverException as e:
            self.reporter.results_reporter(CLICKING_EXCEPTION_ERROR_MESSAGE, "error", error=e)

    # to be move to reusable
    def click_delete_and_accept_alert(self, locator):
        element = self.wait_util.wait_element_to_be_visible(locator)
        try:
            element.click()
            alert = self.driver.switch_to.alert
            alert.accept()
            self.reporter.results_reporter(ALERT_ACCEPTED,"info")
        except Exception as e:
            self.reporter.results_reporter(ALERT_ERROR, "error", error=e)


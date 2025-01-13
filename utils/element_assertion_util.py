from utils.element_wait_util import ElementWaitUtil
from utils.reporter_util import ReporterUtil
from utils.log_message_util import *
from utils.exception_message_util import *



class ElementAssertionUtil:

    def __init__(self, driver):
        self.driver = driver
        self.reporter = ReporterUtil(driver)
        self.wait_util = ElementWaitUtil(driver)

    def assert_element_attribute(self, locator, attribute, expected_attribute_value):
        """Verify element attribute value"""
        self.wait_util.wait_element_to_be_visible(locator)
        actual_attribute_value = self.get_element_attribute(locator, attribute)
        try:
            assert actual_attribute_value == expected_attribute_value
            self.reporter.results_reporter(ELEMENT_ASSERTION_MESSAGE, actual_attribute_value=actual_attribute_value,
                                           expected_attribute_value=expected_attribute_value)
        except AssertionError as e:
            self.reporter.results_reporter(ASSERTION_EXCEPTION_ERROR_MESSAGE, "error",
                                           actual_attribute_value=actual_attribute_value,
                                           expected_attribute_value=expected_attribute_value,
                                           error=e)

    def get_element_attribute(self, locator, attribute):
        """Get element attribute then return"""
        element = self.wait_util.wait_element_to_be_visible(locator)
        actual_attribute_value = element.get_attribute(attribute)
        try:
            self.reporter.results_reporter(ELEMENT_ATTRIBUTE_MESSAGE, actual_attribute_value=actual_attribute_value)
            return actual_attribute_value
        except AssertionError as e:
            self.reporter.results_reporter(ELEMENT_ATTRIBUTE_EXCEPTION_MESSAGE, "error", error=e)

    def assert_url(self, expected_url):
        """Verify the current URL matches the expected URL"""
        actual_url = self.driver.current_url
        try:
            assert actual_url == expected_url
            self.reporter.results_reporter(f"URL Assertion Passed: {actual_url}")
        except AssertionError as e:
            self.reporter.results_reporter(f"URL Assertion Failed: Expected {expected_url}, but got {actual_url}",
                                           "error", error=e)







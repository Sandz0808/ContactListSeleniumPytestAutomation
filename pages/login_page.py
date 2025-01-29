from selenium.webdriver.common.by import By
from utils.element_assertion_util import ElementAssertionUtil
from utils.element_mouse_action_util import ElementMouseActionsUtil
from utils.element_keyboard_input_util import ElementKeyboardInputUtil


class LoginPage:

    SUBMIT_BTN = (By.ID, "submit")
    PASSWORD_TXT = (By.ID, "password")
    ERROR_MESSAGE_TXT = (By.ID, "error")
    EMAIL_TXT = (By.CSS_SELECTOR, "#email")

    def __init__(self, driver):
        self.driver = driver
        self.element_assertion_util = ElementAssertionUtil(driver)
        self.element_mouse_actions_util = ElementMouseActionsUtil(driver)
        self.element_keyboard_input_util = ElementKeyboardInputUtil(driver)


    def enter_email(self, email):
        self.element_keyboard_input_util.input_element(self.EMAIL_TXT, email)

    def enter_password(self, password):
        self.element_keyboard_input_util.input_element(self.PASSWORD_TXT, password)

    def click_login(self):
        self.element_mouse_actions_util.click_element(self.SUBMIT_BTN)

    def verify_failed_login(self, attribute, expected_attribute_value):
        self.element_assertion_util.assert_element_attribute_visible(self.ERROR_MESSAGE_TXT, attribute, expected_attribute_value)



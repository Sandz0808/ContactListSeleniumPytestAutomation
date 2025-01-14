from selenium.webdriver.common.by import By
from utils.element_assertion_util import ElementAssertionUtil
from utils.element_mouse_action_util import ElementMouseActionsUtil
from utils.element_keyboard_input_util import ElementKeyboardInputUtil


class LoginPage(ElementKeyboardInputUtil, ElementMouseActionsUtil, ElementAssertionUtil):

    EMAIL_TXT = (By.CSS_SELECTOR, "#email")
    PASSWORD_TXT = (By.ID, "password")
    SUBMIT_BTN = (By.ID, "submit")
    ERROR_MSG = (By.ID, "error")


    def enter_email(self, email):
        self.input_element(self.EMAIL_TXT, email)

    def enter_password(self, password):
        self.input_element(self.PASSWORD_TXT, password)

    def click_login(self):
        self.click_element(self.SUBMIT_BTN)

    def verify_failed_login(self, attribute, expected_attribute_value):
        self.assert_element_attribute(self.ERROR_MSG, attribute, expected_attribute_value)



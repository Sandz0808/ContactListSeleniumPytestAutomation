from selenium.webdriver.common.by import By
from utils.element_assertion_util import ElementAssertionUtil
from utils.element_mouse_action_util import ElementMouseActionsUtil
from utils.element_keyboard_input_util import ElementKeyboardInputUtil


class SignUpPage(ElementKeyboardInputUtil, ElementMouseActionsUtil,
                 ElementAssertionUtil):

    SIGNUP_BUTTON = (By.ID, "signup")
    FIRST_NAME_TXT = (By.ID, "firstName")
    LAST_NAME_TXT = (By.CSS_SELECTOR, "#lastName")
    EMAIL_TXT = (By.ID, "email")
    PASSWORD_TEXT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MSG = (By.ID, "error")
    LOG_OUT_BTN = (By.ID, "logout")



    def click_signup_button(self):
        self.click_element(self.SIGNUP_BUTTON)

    def enter_first_name(self, firstname):
        self.input_element(self.FIRST_NAME_TXT, firstname)

    def enter_last_name(self, lastname):
        self.input_element(self.LAST_NAME_TXT, lastname)

    def enter_email_address(self, email):
        self.input_element(self.EMAIL_TXT, email)

    def enter_password(self, password):
        self.input_element(self.PASSWORD_TEXT, password)

    def click_submit_button(self):
        self.click_element(self.SUBMIT_BUTTON)

    def click_cancel_button(self):
        self.click_element(self.CANCEL_BUTTON)

    def verify_failed_signup(self, attribute, expected_attribute_value):
        self.assert_element_attribute(self.ERROR_MSG, attribute, expected_attribute_value)





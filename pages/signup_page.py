from selenium.webdriver.common.by import By
from utils.element_assertion_util import ElementAssertionUtil
from utils.element_mouse_action_util import ElementMouseActionsUtil
from utils.element_keyboard_input_util import ElementKeyboardInputUtil


class SignUpPage:

    SIGNUP_BTN = (By.ID, "signup")
    FIRST_NAME_TXT = (By.ID, "firstName")
    LAST_NAME_TXT = (By.ID, "lastName")
    EMAIL_TXT = (By.ID, "email")
    PASSWORD_TXT = (By.ID, "password")
    SUBMIT_BTN = (By.ID, "submit")
    CANCEL_BTN = (By.ID, "cancel")
    ERROR_MESSAGE_TXT = (By.ID, "error")
    LOGOUT_BTN = (By.ID, "logout")

    def __init__(self, driver):
        self.driver = driver
        self.element_assertion_util = ElementAssertionUtil(driver)
        self.element_mouse_actions_util = ElementMouseActionsUtil(driver)
        self.element_keyboard_input_util = ElementKeyboardInputUtil(driver)

    def click_signup_button(self):
        self.element_mouse_actions_util.click_element(self.SIGNUP_BTN)

    def enter_first_name(self, firstname):
        self.element_keyboard_input_util.input_element(self.FIRST_NAME_TXT, firstname)

    def enter_last_name(self, lastname):
        self.element_keyboard_input_util.input_element(self.LAST_NAME_TXT, lastname)

    def enter_email_address(self, email):
        self.element_keyboard_input_util.input_element(self.EMAIL_TXT, email)

    def enter_password(self, password):
        self.element_keyboard_input_util.input_element(self.PASSWORD_TXT, password)

    def click_submit_button(self):
        self.element_mouse_actions_util.click_element(self.SUBMIT_BTN)

    def click_cancel_button(self):
        self.element_mouse_actions_util.click_element(self.CANCEL_BTN)

    def verify_failed_signup(self, attribute, expected_attribute_value):
        self.element_assertion_util.assert_element_attribute_visible(self.ERROR_MESSAGE_TXT, attribute, expected_attribute_value)





from selenium.webdriver.common.by import By
from utils.element_assertion_util import ElementAssertionUtil
from utils.element_mouse_action_util import ElementMouseActionsUtil


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.element_assertion_util = ElementAssertionUtil(driver)
        self.element_mouse_actions_util = ElementMouseActionsUtil(driver)

    LOGOUT_BTN = (By.ID, "logout")

    def click_logout_button(self):
        self.element_mouse_actions_util.click_element(self.LOGOUT_BTN)




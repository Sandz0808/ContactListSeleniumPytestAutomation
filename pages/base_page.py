from selenium.webdriver.common.by import By
from utils.element_assertion_util import ElementAssertionUtil
from utils.element_mouse_action_util import ElementMouseActionsUtil


class BasePage(ElementAssertionUtil, ElementMouseActionsUtil):

    LOG_OUT_BTN = (By.ID, "logout")


    def click_logout_button(self):
        self.click_element(self.LOG_OUT_BTN)




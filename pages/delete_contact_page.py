from selenium.webdriver.common.by import By
from utils.element_assertion_util import ElementAssertionUtil
from utils.element_keyboard_input_util import ElementKeyboardInputUtil
from utils.element_mouse_action_util import ElementMouseActionsUtil
from utils.element_wait_util import ElementWaitUtil


class DeletePage:


    CONTACT_BTN = (By.CSS_SELECTOR, "table tr:nth-child(3) td:nth-child(2)")
    DELETE_BTN = (By.ID, "delete")

    def __init__(self, driver):
        self.driver = driver
        self.element_mouse_actions_util = ElementMouseActionsUtil(driver)
        self.element_keyboard_input_util = ElementKeyboardInputUtil(driver)
        self.element_assertion_util = ElementAssertionUtil(driver)
        self.element_wait_util = ElementWaitUtil(driver)


    def click_contact(self):
        self.element_mouse_actions_util.click_element(self.CONTACT_BTN)

    def click_delete_button(self, action=True):
        self.element_mouse_actions_util.click_delete_and_accept_alert(self.DELETE_BTN)





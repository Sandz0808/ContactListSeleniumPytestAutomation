from selenium.webdriver.common.by import By
from tests.reusable.reusable_scripts import ReusableScripts
from utils.element_wait_util import ElementWaitUtil
from utils.element_assertion_util import ElementAssertionUtil
from utils.element_mouse_action_util import ElementMouseActionsUtil
from utils.element_keyboard_input_util import ElementKeyboardInputUtil


class DeleteContactPage:

    DELETE_BTN = (By.ID, "delete")
    CONTACT_ROW = (By.CSS_SELECTOR, "td:nth-child(2)")


    def __init__(self, driver):

        self.driver = driver
        self.reusable_Script = ReusableScripts(self.driver)
        self.element_mouse_actions_util = ElementMouseActionsUtil(driver)
        self.element_keyboard_input_util = ElementKeyboardInputUtil(driver)
        self.element_assertion_util = ElementAssertionUtil(driver)
        self.element_wait_util = ElementWaitUtil(driver)

    def click_contact(self):
        self.element_mouse_actions_util.click_element(self.CONTACT_ROW)

    def click_delete_button(self):
        self.reusable_Script.click_delete_and_accept_alert(self.DELETE_BTN)





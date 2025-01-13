from selenium.webdriver.common.by import By
from utils.element_assertion_util import ElementAssertionUtil
from utils.element_keyboard_input_util import ElementKeyboardInputUtil
from utils.element_mouse_action_util import ElementMouseActionsUtil
from utils.element_wait_util import ElementWaitUtil


class DeletePage(ElementAssertionUtil, ElementKeyboardInputUtil,
                 ElementMouseActionsUtil, ElementWaitUtil):

    CONTACT_BTN = (By.CSS_SELECTOR, "table tr:nth-child(3) td:nth-child(2)")
    DELETE_BTN = (By.ID, "delete")

    def click_contact(self):
        self.click_element(self.CONTACT_BTN)

    def click_delete_button(self, action=True):
        self.click_delete_and_accept_alert(self.DELETE_BTN)





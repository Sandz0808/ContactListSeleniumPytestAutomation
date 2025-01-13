from selenium.webdriver.common.by import By
from utils.element_assertion_util import ElementAssertionUtil
from utils.element_mouse_action_util import ElementMouseActionsUtil


class HomePage(ElementAssertionUtil, ElementMouseActionsUtil):

    CONTACT_LIST_LBL = (By.XPATH, "//h1[text()='Contact List']")
    ADD_A_NEW_CONTACT_BTN = (By.ID, "add-contact")

    def assert_contact_list(self, attribute, expected_attribute_value):
        self.assert_element_attribute(self.CONTACT_LIST_LBL,
                                                             attribute, expected_attribute_value)

    def click_add_new_contact_button(self):
        self.click_element(self.ADD_A_NEW_CONTACT_BTN)
from selenium.webdriver.common.by import By
from utils.element_assertion_util import ElementAssertionUtil
from utils.element_mouse_action_util import ElementMouseActionsUtil
from utils.element_keyboard_input_util import ElementKeyboardInputUtil
from utils.element_wait_util import ElementWaitUtil


class EditPage:

    def __init__(self, driver):
        self.driver = driver
        self.element_keyboard_input_util = ElementKeyboardInputUtil(driver)
        self.element_mouse_actions_util = ElementMouseActionsUtil(driver)
        self.element_assertion_util = ElementAssertionUtil(driver)
        self.element_wait_util = ElementWaitUtil(driver)


    """ Field mapping as a class-level constant """
    LOCATORS = {
        "firstName": (By.CSS_SELECTOR, "#firstName"),
        "lastName": (By.ID, "lastName"),
        "birthdate": (By.ID, "birthdate"),
        "email": (By.ID, "email"),
        "phone": (By.ID, "phone"),
        "street1": (By.ID, "street1"),
        "street2": (By.ID, "street2"),
        "city": (By.ID, "city"),
        "stateProvince": (By.ID, "stateProvince"),
        "postalCode": (By.ID, "postalCode"),
        "country": (By.ID, "country"),
    }

    """ Locators for non-mapped elements """
    CONTACT_ROW = (By.CSS_SELECTOR, "table tr:nth-child(3) td:nth-child(2)")
    EDIT_BTN = (By.ID, "edit-contact")
    SUBMIT_BTN = (By.ID, "submit")
    CONTACT_DETAILS_LBL = (By.XPATH, "//h1[contains(text(),'Contact Details')]")
    EDIT_CONTACT_LBL = (By.XPATH, "//h1[normalize-space()='Edit Contact']")
    ERROR_MESSAGE_TXT = (By.CSS_SELECTOR, "#error")
    UPDATED_DETAILS = (By.CSS_SELECTOR, "#firstName")

    """ Helper method to fetch locator from FIELD_MAPPING """

    def _get_locator(self, field_name):
        return self.LOCATORS.get(field_name)

    def clear_field(self, field_name):
        self.element_keyboard_input_util.clear_element(self._get_locator(field_name))

    def enter_field(self, field_name, value):
        self.element_keyboard_input_util.input_element(self._get_locator(field_name), value)

    def assert_updated_details(self, attribute, expected_attribute_value):
        self.element_assertion_util.assert_element_attribute_visible(self.UPDATED_DETAILS, attribute, expected_attribute_value)

    def assert_error_message(self, attribute, expected_attribute_value):
        self.element_assertion_util.assert_element_attribute_visible(self.ERROR_MESSAGE_TXT, attribute, expected_attribute_value)

    def assert_contact_details(self, attribute, expected_attribute_value):
        self.element_assertion_util.assert_element_attribute_visible(self.CONTACT_DETAILS_LBL, attribute, expected_attribute_value)

    def assert_edit_contact(self, attribute, expected_attribute_value):
        self.element_assertion_util.assert_element_attribute_visible(self.EDIT_CONTACT_LBL, attribute, expected_attribute_value)

    def click_contact(self):
        self.element_mouse_actions_util.click_element(self.CONTACT_ROW)

    def click_edit_button(self):
        self.element_mouse_actions_util.click_element(self.EDIT_BTN)

    def click_submit(self):
        self.element_mouse_actions_util.click_element(self.SUBMIT_BTN)






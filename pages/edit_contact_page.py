from selenium.webdriver.common.by import By
from utils.element_assertion_util import ElementAssertionUtil
from utils.element_mouse_action_util import ElementMouseActionsUtil
from utils.element_keyboard_input_util import ElementKeyboardInputUtil
from utils.element_wait_util import ElementWaitUtil


class EditPage(ElementAssertionUtil, ElementMouseActionsUtil, ElementKeyboardInputUtil, ElementWaitUtil):

    """ Field mapping as a class-level constant """
    ELEMENT_MAPPING = {
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

    """ Helper method to fetch locator from FIELD_MAPPING """
    def _get_locator(self, field_name):
        locator = self.ELEMENT_MAPPING.get(field_name)
        if not locator:
            raise ValueError(f"Invalid field name: {field_name}")
        return locator

    def assert_error_message(self, attribute, expected_attribute_value):
        self.assert_element_attribute(self.ERROR_MESSAGE_TXT, attribute, expected_attribute_value)

    def assert_contact_details(self, attribute, expected_attribute_value):
        self.assert_element_attribute(self.CONTACT_DETAILS_LBL, attribute, expected_attribute_value)

    def assert_edit_contact(self, attribute, expected_attribute_value):
        self.assert_element_attribute(self.EDIT_CONTACT_LBL, attribute, expected_attribute_value)

    def click_contact(self):
        self.click_element(self.CONTACT_ROW)

    def click_edit_button(self):
        self.click_element(self.EDIT_BTN)

    def click_submit(self):
        self.click_element(self.SUBMIT_BTN)

    def clear_field(self, field_name):
        locator = self._get_locator(field_name)
        self.clear_element(locator)

    def enter_field(self, field_name, value):
        locator = self._get_locator(field_name)
        self.input_element(locator, value)

    def assert_field(self, field_name, attribute, expected_attribute_value):
        locator = self._get_locator(field_name)
        actual_value = self.get_element_attribute(locator, attribute)

        """ Strip and clean the values before assertion """
        actual_value = str(actual_value).strip().rstrip('.')
        expected_attribute_value = str(expected_attribute_value).strip().rstrip('.')

        assert actual_value == expected_attribute_value, (
            f"Failed: An error occurred during Assertion. "
            f"Actual value is: '{actual_value}' while Expected value is: '{expected_attribute_value}'.")




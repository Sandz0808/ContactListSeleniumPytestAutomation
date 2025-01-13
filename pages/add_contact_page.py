from selenium.webdriver.common.by import By
from utils.element_assertion_util import ElementAssertionUtil
from utils.element_mouse_action_util import ElementMouseActionsUtil
from utils.element_keyboard_input_util import ElementKeyboardInputUtil


class AddPage(ElementAssertionUtil, ElementMouseActionsUtil, ElementKeyboardInputUtil):

    LOCATORS = {
        "add_contact_btn": (By.ID, "add-contact"),
        "contact_row": (By.CSS_SELECTOR, "td:nth-child(2)"),
        "firstName": (By.ID, "firstName"),
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
        "submit_btn": (By.ID, "submit"),
        "error_message": (By.ID, "error"),
    }

    # Dynamic field input method
    def enter_field(self, field_name, value):
        locator = self.LOCATORS.get(field_name)
        if locator:
            self.input_element(locator, value)
        else:
            raise ValueError(f"Invalid field name: {field_name}")

    # Dynamic field assertion method
    def assert_field(self, field_name, attribute, expected_attribute_value):
        locator = self.LOCATORS.get(field_name)
        if locator:
            actual_value = self.get_element_attribute(locator, attribute).strip()
            expected_value = str(expected_attribute_value).strip()
            print(f"Comparing field: {field_name} -> Expected: {expected_value}, Actual: {actual_value}")
            assert actual_value == expected_value, f"Assertion failed for {field_name}. Expected: {expected_value}, Actual: {actual_value}"
        else:
            raise ValueError(f"Invalid field name: {field_name}")

    # Specific actions
    def click_submit_contact(self):
        self.click_element(self.LOCATORS["submit_btn"])

    def click_added_contact(self):
        self.click_element(self.LOCATORS["contact_row"])

    def failed_error_message(self,attribute, expected_attribute_value):
        self.assert_element_attribute(self.LOCATORS['error_message'], attribute, expected_attribute_value)
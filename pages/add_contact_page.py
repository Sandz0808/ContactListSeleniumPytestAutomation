from selenium.webdriver.common.by import By
from utils.element_assertion_util import ElementAssertionUtil
from utils.element_mouse_action_util import ElementMouseActionsUtil
from utils.element_keyboard_input_util import ElementKeyboardInputUtil


class AddNewContactPage:

    def __init__(self, driver):
        self.driver = driver
        self.element_assertion_util = ElementAssertionUtil(driver)
        self.element_mouse_actions_util = ElementMouseActionsUtil(driver)
        self.element_keyboard_input_util = ElementKeyboardInputUtil(driver)

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
        self.element_keyboard_input_util.input_element(self.LOCATORS.get(field_name), value)

    # Dynamic field assertion method
    def assert_field(self, field_name, attribute, expected_attribute_value):
        return self.element_assertion_util.get_element_attribute(self.LOCATORS.get(field_name), attribute).strip() == str(expected_attribute_value).strip()

    # Specific actions
    def click_submit_contact(self):
        self.element_mouse_actions_util.click_element(self.LOCATORS["submit_btn"])

    def click_added_contact(self):
        self.element_mouse_actions_util.click_element(self.LOCATORS["contact_row"])

    def failed_error_message(self,attribute, expected_attribute_value):
        self.element_assertion_util.assert_element_attribute_visible(self.LOCATORS['error_message'], attribute, expected_attribute_value)
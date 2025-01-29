import pytest
from utils.allure_util import AllureStepWithAttachment
from tests.reusable.reusable_scripts import ReusableScripts
from utils.element_assertion_util import ElementAssertionUtil
from utils.json_data_util import JsonDataUtil
from utils.exception_message_util import *
from tests.reusable.decorator_utils import EditContact
from pages.edit_contact_page import EditContactPage
from pages.home_page import HomePage
from test_data.data_generator import DataGenerator


@EditContact.class_edit_contact_decorators_ui
class TestContactManagementFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        self.driver = self.driver
        self.homepage = HomePage(self.driver)
        self.reusable = ReusableScripts(self.driver)
        self.edit_contact = EditContactPage(self.driver)
        self.element_assertion_util = ElementAssertionUtil(self.driver)
        self.json_data_util = JsonDataUtil(self.driver)
        self.url = ElementAssertionUtil(self.driver)


    def edit_contact_process(self, valid_data):

        with AllureStepWithAttachment(self.driver, "Step 1: Login to Contact List App"):
            self.reusable.login_with_valid_data()

        with AllureStepWithAttachment(self.driver, "Step 2: Click Contact"):
            self.edit_contact.click_contact()

        with AllureStepWithAttachment(self.driver, "Step 3: Click Edit Contact Button"):
            self.edit_contact.click_edit_button()

        with AllureStepWithAttachment(self.driver, "Step 4: Clear and edit the field"):
            self.reusable.edit_contact_process(valid_data)

        with AllureStepWithAttachment(self.driver, "Step 5: Click Submit Button"):
            self.edit_contact.click_submit()


    @EditContact.edit_contact_decorators_tc7_001_ui
    def test_edit_contact_with_valid_data_via_ui(self):
        valid_data = self.json_data_util.get_testdata("updated_contact_data")
        self.edit_contact_process(valid_data)
        with AllureStepWithAttachment(self.driver, "Step 6: Verify success edit"):
            self.edit_contact.assert_contact_details('innerText', 'Contact Details')
            self.edit_contact.assert_updated_details('innerText', 'Updated')


    @EditContact.edit_contact_decorators_tc7_002_ui
    def test_edit_contact_with_empty_required_field_ui(self):
        invalid_data = DataGenerator().generate_invalid_add_contact_data()
        self.edit_contact_process(invalid_data)
        with AllureStepWithAttachment(self.driver, "Step 6: Verify failed edit"):
            self.edit_contact.assert_error_message('innerText', EDIT_CONTACT_EMPTY_FIELD_ERROR)












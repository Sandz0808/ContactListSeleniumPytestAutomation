import pytest
from utils.allure_util import AllureStepWithAttachment
from tests.reusable.reusable_scripts import ReusableScripts
from utils.exception_message_util import *
from tests.reusable.decorator_utils import AddContact
from pages.add_contact_page import AddNewContactPage
from pages.home_page import HomePage
from test_data.data_generator import DataGenerator


@AddContact.class_add_contact_decorators_ui
class TestContactManagementFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        self.driver = self.driver
        self.homepage = HomePage(self.driver)
        self.add_contact = AddNewContactPage(self.driver)
        self.signup = ReusableScripts(self.driver)
        self.verify = ReusableScripts(self.driver)
        self.add_contact_process = ReusableScripts(self.driver)


    @AddContact.add_contact_decorators_tc4_001_ui
    def test_add_contact_with_valid_data_via_ui(self):
        data = DataGenerator().generate_valid_add_contact_data()
        with AllureStepWithAttachment(self.driver, "Step 1: Login to Contact List App"):
            self.signup.login_with_valid_data()
        with AllureStepWithAttachment(self.driver, "Step 2: Click Add a New Contact button"):
            self.homepage.click_add_new_contact_button()
        with AllureStepWithAttachment(self.driver, "Step 3: Fill out the contact form"):
            self.add_contact_process.add_contact_process(data)
        with AllureStepWithAttachment(self.driver, "Step 4: Click Submit button"):
            self.add_contact.click_submit_contact()
        with AllureStepWithAttachment(self.driver, "Step 5: Verify Added Contact"):
            self.add_contact.click_added_contact()
            self.verify.add_contact_verifying_process(data)


    @AddContact.add_contact_decorators_tc4_002_ui
    def test_add_contact_with_empty_required_field_via_ui(self):
        data = DataGenerator().generate_invalid_add_contact_data()
        with AllureStepWithAttachment(self.driver, "Step 1: Login to Contact List App"):
            self.signup.login_with_valid_data()
        with AllureStepWithAttachment(self.driver, "Step 2: Click Add a New Contact button"):
            self.homepage.click_add_new_contact_button()
        with AllureStepWithAttachment(self.driver, "Step 3: Fill out the contact form"):
            self.add_contact_process.add_contact_process(data)
        with AllureStepWithAttachment(self.driver, "Step 4: Click Submit button"):
            self.add_contact.click_submit_contact()
        with AllureStepWithAttachment(self.driver, "Step 5: Verify Error Message"):
            self.add_contact.failed_error_message("innerText", ADD_CONTACT_ERROR_EMPTY_FIRSTNAME)



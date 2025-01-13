from utils.imports_util import *

@AddContact.class_add_contact_decorators_ui
class TestContactManagementFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        self.driver = self.driver
        self.homepage = HomePage(self.driver)
        self.add_contact = AddPage(self.driver)
        self.signup = ReusableScripts(self.driver)

    def fill_contact_form(self, data):
        self.homepage.click_add_new_contact_button()
        for field, value in data.items():
            if value:
                self.add_contact.enter_field(field, value)


    def verify_contact_details(self, data):
        self.add_contact.click_added_contact()
        for field, value in data.items():
            self.add_contact.assert_field(field, "innerText", value)

    @AddContact.add_contact_decorators_tc4_001_ui
    def test_add_contact_with_valid_data_via_ui(self):
        data = DataGenerator().generate_valid_add_contact_data()
        with AllureStepWithAttachment(self.driver, "Step 1: Login to Contact List App"):
            self.signup.signup_with_valid_data()
        with AllureStepWithAttachment(self.driver, "Step 2: Add a New Contact"):
            self.fill_contact_form(data)
            self.add_contact.click_submit_contact()
        with AllureStepWithAttachment(self.driver, "Step 3: Verify Added Contact"):
            self.verify_contact_details(data)

    @AddContact.add_contact_decorators_tc4_002_ui
    def test_add_contact_with_empty_required_field_via_ui(self):
        data = DataGenerator().generate_invalid_add_contact_data()
        with AllureStepWithAttachment(self.driver, "Step 1: Login to Contact List App"):
            self.signup.signup_with_valid_data()
        with AllureStepWithAttachment(self.driver, "Step 2: Add Contact with invalid data"):
            self.fill_contact_form(data)
            self.add_contact.click_submit_contact()
        with AllureStepWithAttachment(self.driver, "Step 3: Verify Error Message"):
            self.add_contact.failed_error_message("innerText", ADD_CONTACT_ERROR_EMPTY_LASTNAME)

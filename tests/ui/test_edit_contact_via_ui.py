from utils.imports_util import *


@EditContact.class_edit_contact_decorators_ui
class TestContactManagementFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        self.driver = self.driver
        self.homepage = HomePage(self.driver)
        self.login = ReusableScripts(self.driver)
        self.edit_contact = EditPage(self.driver)
        self.element_assertion_util = ElementAssertionUtil(self.driver)
        self.json_data_util = JsonDataUtil(self.driver)

    def edit_contact_details(self, user_data, verify_error=False):
        with AllureStepWithAttachment(self.driver, "Step 1: Login to Contact List App and Click Existing Contact"):
            self.login.login_with_valid_data()
            self.edit_contact.click_contact()

        with AllureStepWithAttachment(self.driver, "Step 2: Click Contact for Edit"):
            self.edit_contact.click_edit_button()

        with AllureStepWithAttachment(self.driver, "Step 3: Clearing the field for Edit"):
            self.edit_contact.assert_edit_contact("innerText", "Edit Contact")

            fields_to_clear = [
                "firstName", "lastName", "birthdate", "email", "phone",
                "street1", "street2", "city", "stateProvince", "postalCode", "country"
            ]
            for field in fields_to_clear:
                self.edit_contact.clear_field(field)

        with AllureStepWithAttachment(self.driver, "Step 4: Enter new details to the cleared field"):
            for key, value in user_data.items():
                self.edit_contact.enter_field(key, value)

        with AllureStepWithAttachment(self.driver, "Step 5: Click Submit"):
            self.edit_contact.click_submit()
            time.sleep(5)

        if verify_error:
            with AllureStepWithAttachment(self.driver, "Step 6: Verify edit failed due to empty required field"):
                self.edit_contact.assert_error_message('innerText', EDIT_CONTACT_EMPTY_FIELD_ERROR)
        else:
            with AllureStepWithAttachment(self.driver, "Step 6: Verify that edited details match the generated data"):
                for key, value in user_data.items():
                    stripped_value = value.strip() if isinstance(value, str) else value
                    self.edit_contact.assert_field(key, "innerText", stripped_value)


    @EditContact.edit_contact_decorators_tc7_001_ui
    def test_edit_contact_with_valid_data_via_ui(self):
        valid_data = DataGenerator().generate_valid_add_contact_data()
        self.edit_contact_details(valid_data)

    @EditContact.edit_contact_decorators_tc7_002_ui
    @pytest.mark.parametrize("user", user_update_data())
    def test_edit_contact_with_invalid_data_via_ui(self, user):
        self.edit_contact_details(user, verify_error=True)

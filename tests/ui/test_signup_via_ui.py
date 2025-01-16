import pytest
from pages.home_page import HomePage
from pages.signup_page import SignUpPage
from test_data.data_generator import DataGenerator
from utils.allure_util import AllureStepWithAttachment
from utils.decorator_utils import SignUp
from utils.element_assertion_util import ElementAssertionUtil


@SignUp.class_signup_decorators_ui
class TestUserSignupFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        self.driver = self.driver
        self.signup = SignUpPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.assertion = ElementAssertionUtil(self.driver)


    def signup_steps(self, user, is_valid):
        with AllureStepWithAttachment(self.driver, "Step 1: Click Signup Button"):
            self.signup.click_signup_button()

        with AllureStepWithAttachment(self.driver, "Step 2: Enter user information"):
            self.signup.enter_first_name(user['firstName'])
            self.signup.enter_last_name(user['lastName'])
            self.signup.enter_email_address(user['email'])
            self.signup.enter_password(user['password'])

        with AllureStepWithAttachment(self.driver, "Step 3: Click Signup Button"):
            self.signup.click_submit_button()

        if is_valid:
            with AllureStepWithAttachment(self.driver, "Step 4: Verify Success Signup"):
                self.home_page.assert_contact_list("innerText", "Contact List")

        else:
            with AllureStepWithAttachment(self.driver, "Step 4: Verify Failed Signup"):
                self.signup.verify_failed_signup("innerText", user['result'])


    @SignUp.signup_decorators_tc1_001_ui
    def test_signup_with_valid_data_via_ui(self):
        user = DataGenerator().generate_valid_signup_data()
        self.signup_steps(user, is_valid=True)

    @SignUp.signup_decorators_tc1_002_004_ui
    def test_signup_with_invalid_data_via_ui(self):
        user = DataGenerator().generate_invalid_signup_data()
        self.signup_steps(user, is_valid=False)













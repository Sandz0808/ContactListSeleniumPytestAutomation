from utils.imports_util import *


@SignUp.class_signup_decorators_ui
class TestUserSignupFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        self.driver = self.driver
        self.signup = SignUpPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.assertion = ElementAssertionUtil(self.driver)

    def perform_signup(self, user):
        self.signup.click_signup_button()
        self.signup.enter_first_name(user['firstName'])
        self.signup.enter_last_name(user['lastName'])
        self.signup.enter_email_address(user['email'])
        self.signup.enter_password(user['password'])
        self.signup.click_submit_button()


    @SignUp.signup_decorators_tc1_001_ui
    def test_signup_with_valid_data_via_ui(self):
        with AllureStepWithAttachment(self.driver, "Step 1: Signup to Contact List App with valid Data"):
            user = DataGenerator().generate_valid_signup_data()
            self.perform_signup(user)

        with AllureStepWithAttachment(self.driver, "Step 2: Verify Success Signup"):
            self.home_page.assert_contact_list("innerText", "Contact List")


    @SignUp.signup_decorators_tc1_002_004_ui
    @pytest.mark.parametrize("user", user_sign_up_data()[:-1])
    def test_signup_with_invalid_data_via_ui(self, user): # 7 negative test run
        with AllureStepWithAttachment(self.driver, "Step 1: Signup to Contact List App with invalid Data"):
            self.perform_signup(user)

        with AllureStepWithAttachment(self.driver, "Step 2: Verify Failed Signup"):
            if user['result'] in {SHORT_PASSWORD, USED_EMAIL, EMPTY_FIRST_NAME, EMPTY_LAST_NAME, EMPTY_EMAIL,
                                  EMPTY_PASSWORD, LONG_PASSWORD}:
                self.signup.verify_failed_signup("innerText", user['result'])

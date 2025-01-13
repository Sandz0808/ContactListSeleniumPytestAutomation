from utils.imports_util import *

@Login.class_login_decorators_ui
class TestUserLoginFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        self.driver = self.driver
        self.login = LoginPage(self.driver)
        self.homepage = HomePage(self.driver)

    def perform_login(self, email, password, result_message, is_valid):

        with AllureStepWithAttachment(self.driver, "Step 1: Enter valid login data"):
            self.login.enter_email(email)
            self.login.enter_password(password)

        with AllureStepWithAttachment(self.driver, "Step 2: Click Login Button"):
            self.login.click_login()

        if is_valid:
            with AllureStepWithAttachment(self.driver, "Step 3: Verifying Successful Login"):
                self.homepage.assert_contact_list("innerText", result_message)
        else:
            with AllureStepWithAttachment(self.driver, "Step 3: Verifying Failed Login"):
                self.login.verify_invalid_login_web("innerText", result_message)

    @Login.login_decorators_tc3_001_ui
    def test_login_with_valid_credential_via_ui(self):
        user = user_login_data()[-1]  # Fetch the last entry (valid data)
        self.perform_login(user['email'], user['password'], user['Result'], is_valid=True)

    @Login.login_decorators_tc3_002_ui
    @pytest.mark.parametrize("user", user_login_data()[:-1])
    def test_login_with_invalid_credential_via_ui(self, user):
        self.perform_login(user['email'], user['password'], user['Result'], is_valid=False)

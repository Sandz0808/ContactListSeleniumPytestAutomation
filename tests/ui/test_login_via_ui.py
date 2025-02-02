import pytest
from utils.allure_util import AllureStepWithAttachment
from utils.json_data_util import JsonDataUtil
from tests.reusable.decorator_utils import Login
from pages.home_page import HomePage
from pages.login_page import LoginPage


@Login.class_login_decorators_ui
class TestUserLoginFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        self.driver = self.driver
        self.login = LoginPage(self.driver)
        self.homepage = HomePage(self.driver)
        self.json_data_util = JsonDataUtil(self.driver)


    def login_steps(self, email, password, is_valid):
        with AllureStepWithAttachment(self.driver, "Step 1: Enter login data"):
            self.login.enter_email(email)
            self.login.enter_password(password)

        with AllureStepWithAttachment(self.driver, "Step 2: Click Login Button"):
            self.login.click_login()

    @Login.login_decorators_tc3_001_ui
    def test_login_with_valid_credential_via_ui(self):
        user = self.json_data_util.get_testdata("valid_login")
        self.login_steps(user['email'], user['password'], is_valid=True)
        with AllureStepWithAttachment(self.driver, "Step 3: Verifying Success Login"):
            self.homepage.assert_contact_list("innerText", "Contact List")

    @Login.login_decorators_tc3_002_ui
    def test_login_with_invalid_credential_via_ui(self):
        user = self.json_data_util.get_testdata("invalid_login")
        self.login_steps(user['email'], user['password'], is_valid=False)
        with AllureStepWithAttachment(self.driver, "Step 3: Verifying Failed Login"):
            self.login.verify_failed_login("innerText", "Incorrect username or password")


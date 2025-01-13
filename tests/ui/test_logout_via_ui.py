from conftest import CONFIG_READER
from utils.imports_util import *


@Logout.class_logout_decorators_ui
class TestLogoutFunctionalityUI:
    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        self.driver = self.driver
        self.logout = BasePage(self.driver)
        self.url = ElementAssertionUtil(self.driver)
        self.log_in = ReusableScripts(self.driver)
        self.json_data_util = JsonDataUtil(self.driver)

    @Logout.logout_decorators_tc6_001_ui
    def test_verify_contact_deletion_via_ui(self, config):
        with AllureStepWithAttachment(self.driver, "Step 1: Login to Contact List App"):
            self.log_in.login_with_valid_data()

        with AllureStepWithAttachment(self.driver, "Step 2: Click Logout"):
            self.logout.click_logout_button()

        with AllureStepWithAttachment(self.driver, "Step 3: Verify Logout"):
            normalized_env = config.lower()
            url = CONFIG_READER.get_value(f'{normalized_env}', 'url')
            self.url.assert_url(url + "/logout")


import pytest
from pages.delete_contact_page import DeletePage
from pages.home_page import HomePage
from utils.decorator_utils import Delete
from tests.reusable.reusable_scripts import ReusableScripts
from utils.allure_util import AllureStepWithAttachment


@Delete.class_delete_decorators_UI
class TestContactDeletionFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        self.driver = self.driver
        self.homepage = HomePage(self.driver)
        self.delete_page = DeletePage(self.driver)
        self.log_in = ReusableScripts(self.driver)


    @Delete.delete_decorators_tc8_001_ui
    def test_verify_contact_deletion_via_ui(self):
        with AllureStepWithAttachment(self.driver, "Step 1: Login to Contact List App"):
            self.log_in.login_with_valid_data()

        with AllureStepWithAttachment(self.driver, "Step 2: Click selected Contact on table "):
            self.delete_page.click_contact()

        with AllureStepWithAttachment(self.driver, "Step 3: Click Delete button"):
            self.delete_page.click_delete_button()

        with AllureStepWithAttachment(self.driver, "Step 4: Verify Deletion"):
            self.homepage.assert_contact_list("innerText", "Contact List")


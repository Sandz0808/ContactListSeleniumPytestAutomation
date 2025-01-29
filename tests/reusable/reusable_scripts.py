from contextlib import contextmanager
from utils.allure_util import AllureStepWithAttachment
from utils.element_wait_util import ElementWaitUtil
from utils.exception_message_util import ALERT_ERROR
from utils.json_data_util import JsonDataUtil
from utils.log_message_util import ALERT_ACCEPTED
from utils.reporter_util import ReporterUtil
from pages.add_contact_page import AddNewContactPage
from pages.edit_contact_page import EditContactPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.signup_page import SignUpPage


class ReusableScripts:


    def __init__(self, driver):


        self.driver = driver
        self.reporter = ReporterUtil(self.driver)
        self.wait_util = ElementWaitUtil(self.driver)
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.json_data_util = JsonDataUtil(self.driver)
        self.signup = SignUpPage(self.driver)
        self.edit_contact = EditContactPage(self.driver)
        self.add_contact = AddNewContactPage(self.driver)


    def login_with_valid_data(self):
        login_data = self.json_data_util.get_testdata("valid_login")

        login_email = login_data.get("email")
        login_password = login_data.get("password")

        self.login_page.enter_email(login_email)
        self.login_page.enter_password(login_password)
        self.login_page.click_login()
        self.home_page.assert_contact_list("innerText", "Contact List")


    def add_contact_verifying_process(self, user_data):
        element = AddNewContactPage.LOCATORS
        fields = list(element.keys())
        for field in fields:
            if field in user_data:
                self.add_contact.assert_field(field, "innerText", user_data[field])

    def add_contact_process(self, user_data):
        element = EditContactPage.LOCATORS
        fields = list(element.keys())
        for field in fields:
            if field in user_data:
                self.add_contact.enter_field(field, user_data[field])

    def edit_contact_process(self, user_data):
        element = EditContactPage.LOCATORS
        fields = list(element.keys())
        for field in fields:
            if field in user_data:
                self.edit_contact.clear_field(field)
                self.edit_contact.enter_field(field, user_data[field])


    def click_delete_and_accept_alert(self, locator):
        element = self.wait_util.wait_element_to_be_visible(locator)
        try:
            element.click()
            alert = self.driver.switch_to.alert
            alert.accept()
            self.reporter.results_reporter(ALERT_ACCEPTED,"info")
        except Exception as e:
            self.reporter.results_reporter(ALERT_ERROR, "error", error=e)


    @contextmanager
    def allure_step_definition(self, steps):
        with AllureStepWithAttachment(self.driver, steps):
            yield  # Allows wrapped code execution

















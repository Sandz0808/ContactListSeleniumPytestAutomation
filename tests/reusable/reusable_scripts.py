from pages.edit_contact_page import EditPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.signup_page import SignUpPage
from test_data.data_generator import DataGenerator
from utils.json_data_util import JsonDataUtil

class ReusableScripts:


    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.json_data_util = JsonDataUtil(self.driver)
        self.signup = SignUpPage(self.driver)
        self.edit_contact = EditPage(self.driver)


    def login_with_valid_data(self):
        login_data = self.json_data_util.get_testdata("valid_login")

        login_email = login_data.get("email")
        login_password = login_data.get("password")

        self.login_page.enter_email(login_email)
        self.login_page.enter_password(login_password)
        self.login_page.click_login()
        self.home_page.assert_contact_list("innerText", "Contact List")


    def edit_update_process(self, user_data):

        element = EditPage.LOCATORS
        fields = list(element.keys())
        for field in fields:
            if field in user_data:
                self.edit_contact.clear_field(field)
                self.edit_contact.enter_field(field, user_data[field])



















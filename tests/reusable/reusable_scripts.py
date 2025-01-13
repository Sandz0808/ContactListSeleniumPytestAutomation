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


    def login_with_valid_data(self):
        login_data = self.json_data_util.get_testdata("valid_login")

        login_email = login_data.get("email")
        login_password = login_data.get("password")

        self.login_page.enter_email(login_email)
        self.login_page.enter_password(login_password)
        self.login_page.click_login()
        self.home_page.assert_contact_list("innerText", "Contact List")


    def signup_with_valid_data(self):
        user = DataGenerator().generate_valid_signup_data()

        self.signup.click_signup_button()
        self.signup.enter_first_name(user['firstName'])
        self.signup.enter_last_name(user['lastName'])
        self.signup.enter_email_address(user['email'])
        self.signup.enter_password(user['password'])
        self.signup.click_submit_button()
        self.home_page.assert_contact_list("innerText", "Contact List")


    def login_with_valid_data2(self, data):
        pass


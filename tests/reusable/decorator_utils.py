import allure
import pytest

class Delete:
    @staticmethod
    def class_delete_decorators_UI(func):
        func = allure.parent_suite("Regression")(func)
        func = allure.suite("Contact Deletion Functionality")(func)
        func = allure.feature("Contact Deletion Functionality")(func)
        func = pytest.mark.tags("ui_delete_functionality")(func)
        func = allure.severity(allure.severity_level.NORMAL)(func)
        return func

    @staticmethod
    def class_delete_decorators_API(func):
        func = allure.parent_suite("Regression")(func)
        func = allure.suite("Contact Deletion Functionality")(func)
        func = allure.feature("Contact Deletion Functionality")(func)
        func = pytest.mark.tags("api_delete_functionality")(func)
        func = allure.severity(allure.severity_level.NORMAL)(func)
        return func

    @staticmethod
    def delete_decorators_tc8_001_ui(func):
        func = allure.sub_suite("TC8_001: Deleted Contact via UI")(func)
        func = allure.title("TC8_001: Deleted Contact via UI")(func)
        func = pytest.mark.tags("ui_delete_functionality")(func)
        return func

    @staticmethod
    def delete_decorators_tc8_002_api(func):
        func = allure.sub_suite("TC8_002: Deleted Contact via API")(func)
        func = allure.title("TC8_002: Deleted Contact via API")(func)
        func = pytest.mark.tags("api_delete_functionality")(func)
        return func

    @staticmethod
    def delete_decorators_tc8_003_api(func):
        func = allure.sub_suite("TC8_003: Delete Non-Existent Contact via API")(func)
        func = allure.title("TC8_003: Delete Non-Existent Contact via API")(func)
        func = pytest.mark.tags("api_delete_functionality")(func)
        return func


class AddContact:

    @staticmethod
    def class_add_contact_decorators_ui(func):
        func = allure.parent_suite("Regression")(func)
        func = allure.suite("Contact Management Functionality")(func)
        func = allure.feature("Contact Management Functionality")(func)
        func = pytest.mark.tags("ui_management_functionality")(func)
        func = allure.severity(allure.severity_level.NORMAL)(func)
        return func

    @staticmethod
    def class_add_contact_decorators_api(func):
        func = allure.parent_suite("Regression")(func)
        func = allure.suite("Contact Management Functionality")(func)
        func = allure.feature("Contact Management Functionality")(func)
        func = pytest.mark.tags("api_management_functionality")(func)
        func = allure.severity(allure.severity_level.NORMAL)(func)
        return func

    @staticmethod
    def add_contact_decorators_tc4_001_ui(func):
        func = allure.sub_suite("TC4_001: Add Contact with valid Data via UI")(func)
        func = allure.title("TC4_001: Add Contact with valid Data via UI")(func)
        func = pytest.mark.tags("ui_management_functionality")(func)
        return func

    @staticmethod
    def add_contact_decorators_tc4_002_ui(func):
        func= allure.sub_suite("TC4_002: Add Contact with invalid Data via UI")(func)
        func= allure.title("TC4_002: Add Contact with invalid Data via UI")(func)
        func= pytest.mark.tags("ui_management_functionality")(func)
        return func

    @staticmethod
    def add_contact_decorators_tc4_003_api(func):
        func = allure.sub_suite("TC4_003: Add Contact with valid Data via API")(func)
        func = allure.title("TC4_003: Add Contact with valid Data via API")(func)
        func = pytest.mark.tags("api_management_functionality")(func)
        return func

    @staticmethod
    def add_contact_decorators_tc4_004_api(func):
        func = allure.sub_suite("TC4_004: Add Contact with invalid Data via API")(func)
        func = allure.title("TC4_004: Add Contact with invalid Data via API")(func)
        func = pytest.mark.tags("api_management_functionality")(func)
        return func

class EditContact:

    @staticmethod
    def class_edit_contact_decorators_ui(func):
        func = allure.parent_suite("Regression")(func)
        func = allure.suite("Contact Edit Functionality")(func)
        func = allure.feature("Contact Edit Functionality")(func)
        func = pytest.mark.tags("ui_edit_functionality")(func)
        func = allure.severity(allure.severity_level.NORMAL)(func)
        return func

    @staticmethod
    def class_edit_contact_decorators_api(func):
        func= allure.parent_suite("Regression")(func)
        func= allure.suite("Contact Edit Functionality")(func)
        func= allure.feature("Contact Edit Functionality")(func)
        func= pytest.mark.tags("api_edit_functionality")(func)
        func= allure.severity(allure.severity_level.NORMAL)(func)
        return func

    @staticmethod
    def edit_contact_decorators_tc7_001_ui(func):
        func= allure.sub_suite("TC7_001: Edit Contact with valid Data via UI")(func)
        func= allure.title("TC7_001: Edit Contact with valid Data via UI")(func)
        func= pytest.mark.tags("ui_edit_functionality")(func)
        return func

    @staticmethod
    def edit_contact_decorators_tc7_002_ui(func):
        func= allure.sub_suite("TC7_002: Edit Contact with empty required field via UI")(func)
        func= allure.title("TC7_002: Edit Contact with empty required field via UI")(func)
        func= pytest.mark.tags("ui_edit_functionality")(func)
        return func

    @staticmethod
    def edit_contact_decorators_tc7_003_api(func):
        func = allure.sub_suite("TC7_003: Edit Contact with valid data via API")(func)
        func = allure.title("TC7_003:  Edit Contact with valid data via API")(func)
        func = pytest.mark.tags("api_edit_functionality")(func)
        return func

    @staticmethod
    def edit_contact_decorators_tc7_004_api(func):
        func = allure.sub_suite("TC7_004: Edit Contact with empty required field via API")(func)
        func = allure.title("TC7_004: Edit Contact with empty required field via API")(func)
        func = pytest.mark.tags("api_edit_functionality")(func)
        return func

class Login:

    @staticmethod
    def class_login_decorators_ui(func):
        func= allure.parent_suite("Regression")(func)
        func= allure.suite("User Login Functionality")(func)
        func= allure.feature("User Login Functionality")(func)
        func= pytest.mark.tags("ui_login_functionality")(func)
        func= allure.severity(allure.severity_level.NORMAL)(func)
        return func

    @staticmethod
    def class_login_decorators_api(func):
        func = allure.parent_suite("Regression")(func)
        func = allure.suite("User Login Functionality")(func)
        func = allure.feature("User Login Functionality")(func)
        func = pytest.mark.tags("api_login_functionality")(func)
        func = allure.severity(allure.severity_level.NORMAL)(func)
        return func

    @staticmethod
    def login_decorators_tc3_001_ui(func):
        func= allure.sub_suite("TC3_001: Log In with valid credentials via UI")(func)
        func= allure.title("TC3_001:  Log In with valid credentials via UI")(func)
        func= pytest.mark.tags("ui_login_functionality")(func)
        return func

    @staticmethod
    def login_decorators_tc3_002_ui(func):
        func= allure.sub_suite("TC3_002: Log In with invalid credentials via UI")(func)
        func= allure.title("TC3_002: Log In with invalid credentials via UI")(func)
        func= pytest.mark.tags("ui_login_functionality")(func)
        return func

    @staticmethod
    def login_decorators_tc3_003_api(func):
        func= allure.sub_suite("TC3_003: Log In with valid credentials via API")(func)
        func= allure.title("TC3_003: Log In with valid credentials via API")(func)
        func= pytest.mark.tags("api_login_functionality")(func)
        return func

    @staticmethod
    def login_decorators_tc3_004_api(func):
        func = allure.sub_suite("TC3_004: Log In with invalid credentials via API")(func)
        func = allure.title("TC3_004: Log In with invalid credentials via API")(func)
        func = pytest.mark.tags("api_login_functionality")(func)

        return func


class SignUp:

    @staticmethod
    def class_signup_decorators_ui(func):
        func= allure.parent_suite("Regression")(func)
        func= allure.suite("User SignUp Functionality")(func)
        func= allure.feature("User SignUp Functionality")(func)
        func= pytest.mark.tags("ui_signup_functionality")(func)
        func= allure.severity(allure.severity_level.NORMAL)(func)
        return func

    @staticmethod
    def class_signup_decorators_api(func):
        func = allure.parent_suite("Regression")(func)
        func = allure.suite("User SignUp Functionality")(func)
        func = allure.feature("User SignUp Functionality")(func)
        func = pytest.mark.tags("api_signup_functionality")(func)
        func = allure.severity(allure.severity_level.NORMAL)(func)
        return func

    @staticmethod
    def signup_decorators_tc1_001_ui(func):
        func= allure.sub_suite("TC1_001: Signup_with_valid_data via UI")(func)
        func= allure.title("TC1_001: Signup_with_valid_data via UI")(func)
        func= pytest.mark.tags("ui_signup_functionality")(func)
        return func

    @staticmethod
    def signup_decorators_tc1_002_004_ui(func):
        func= allure.sub_suite("TC1_002: Signup_with_invalid_data via UI")(func)
        func= allure.title("TC1_002: Signup_with_invalid_data via UI")(func)
        func= pytest.mark.tags("ui_signup_functionality")(func)
        return func

    @staticmethod
    def signup_decorators_tc1_005_api(func):
        func = allure.sub_suite("TC1_003: Signup_with_valid_data via API")(func)
        func = allure.title("TC1_003: Signup_with_valid_data via API")(func)
        func = pytest.mark.tags("api_signup_functionality")(func)
        return func

    @staticmethod
    def signup_decorators_tc1_006_008_api(func):
        func = allure.sub_suite("TC1_004: Signup_with_invalid_data via API")(func)
        func = allure.title("TC1_004: Signup_with_invalid_data via API")(func)
        func = pytest.mark.tags("api_signup_functionality")(func)
        return func


class Logout:

    @staticmethod
    def class_logout_decorators_ui(func):
        func= allure.parent_suite("Regression")(func)
        func= allure.suite("User Logout Functionality")(func)
        func= allure.feature("User Logout Functionality")(func)
        func= pytest.mark.tags("ui_logout_functionality")(func)
        func= allure.severity(allure.severity_level.NORMAL)(func)
        return func

    @staticmethod
    def class_logout_decorators_api(func):
        func = allure.parent_suite("Regression")(func)
        func = allure.suite("User Logout Functionality")(func)
        func = allure.feature("User Logout Functionality")(func)
        func = pytest.mark.tags("api_logout_functionality")(func)
        func = allure.severity(allure.severity_level.NORMAL)(func)
        return func

    @staticmethod
    def logout_decorators_tc6_001_ui(func):
        func= allure.sub_suite("TC6_001: Logout via UI")(func)
        func= allure.title("TC6_001: Logout via UI")(func)
        func= pytest.mark.tags("ui_logout_functionality")(func)
        return func

    @staticmethod
    def logout_decorators_tc6_002_api(func):
        func = allure.sub_suite("TC6_002: Logout via API")(func)
        func = allure.title("TC6_002: Logout via API")(func)
        func = pytest.mark.tags("api_logout_functionality")(func)
        return func

    @staticmethod
    def logout_decorators_t6_003_api(func):
        func= allure.sub_suite("TC6_003: Logout with Invalid or Expired Token via API")(func)
        func= allure.title("TC6_003: Logout with Invalid or Expired Token via API")(func)
        func= pytest.mark.tags("api_logout_functionality")(func)
        return func




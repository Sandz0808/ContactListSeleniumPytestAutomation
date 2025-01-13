from utils.imports_util import *

@Login.class_login_decorators_api
class TestUserLoginFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.http_util = HttpUtil()
        self.api_test_data_util = ApiTestDataUtil()

    def process_login(self, test_data_type):
        login_data = self.api_test_data_util.get_api_testdata(test_data_type)
        with AllureStepWithAttachment(None, f"Step 1: Send a POST request to /users/login"):
            response_data = self.http_util.post_request("/users/login", login_data)
            AllureStepWithAttachment.attach_response(response_data)
            return response_data

    @Login.login_decorators_tc3_003_api
    def test_successful_login_via_api(self):
        self.process_login("valid_login")

    @Login.login_decorators_tc3_004_api
    def test_failed_login_via_api(self):
        self.process_login("invalid_login")




from utils.imports_util import *


@Logout.class_logout_decorators_api
class TestLogoutFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.http_util = HttpUtil()
        self.api_test_data_util = ApiTestDataUtil()
        self.valid_login_data = self.api_test_data_util.get_api_testdata("valid_login")
        self.token = self.http_util.post_request("/users/login", self.valid_login_data)['token']

    @Logout.logout_decorators_tc6_002_api
    def test_verify_successful_user_logout(self):
        with AllureStepWithAttachment(None, "Step 1: Verify if a User can be Successfully Logged out via the API"):
            headers = self.http_util.build_auth_headers(self.token)
            response_data = self.http_util.post_request("/users/logout", headers=headers)
            AllureStepWithAttachment.attach_response(response_data)

    @Logout.logout_decorators_t6_003_api
    def test_verify_logout_with_invalid_or_expired_token(self):
        with AllureStepWithAttachment(None, "Step 1: Verify API Handles Logout with Invalid or Expired Token"):
            headers = self.http_util.build_auth_headers('invalidToken')
            response_data = self.http_util.post_request("/users/logout", headers=headers)
            AllureStepWithAttachment.attach_response(response_data)


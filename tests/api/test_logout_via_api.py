import pytest
from tests.reusable.api_test_data_util import ApiTestDataUtil
from utils.allure_util import AllureStepWithAttachment
from utils.decorator_utils import Logout
from utils.http_util import HttpUtil


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
        with AllureStepWithAttachment(None, "Step 1: Submit POST request with valid data"):
            headers = self.http_util.build_auth_headers(self.token)
            response_data = self.http_util.post_request("/users/logout", headers=headers)
        with AllureStepWithAttachment(None, "Step 2: Verified Success Logout"):
            AllureStepWithAttachment.attach_response(response_data)

    @Logout.logout_decorators_t6_003_api
    def test_verify_logout_with_invalid_or_expired_token(self):
        with AllureStepWithAttachment(None, "Step 1: Submit POST request with invalid Token"):
            headers = self.http_util.build_auth_headers('invalidToken')
            response_data = self.http_util.post_request("/users/logout", headers=headers)
        with AllureStepWithAttachment(None, "Step 2: Verified failed Logout"):
            AllureStepWithAttachment.attach_response(response_data)


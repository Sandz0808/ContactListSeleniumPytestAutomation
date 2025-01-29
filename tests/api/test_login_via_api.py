import pytest
from utils.allure_util import AllureStepWithAttachment
from tests.reusable.api_test_data_util import ApiTestDataUtil
from tests.reusable.decorator_utils import Login
from tests.reusable.http_util import HttpUtil


@Login.class_login_decorators_api
class TestUserLoginFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.http_util = HttpUtil()
        self.api_test_data_util = ApiTestDataUtil()

    def process_login(self, test_data_type):
        login_data = self.api_test_data_util.get_api_testdata(test_data_type)
        response_data = self.http_util.post_request("/users/login", json_data=login_data)
        AllureStepWithAttachment.attach_response(response_data)
        return response_data


    @Login.login_decorators_tc3_003_api
    def test_successful_login_via_api(self):
        with AllureStepWithAttachment(None, "Step 1: Send POST request with valid data "):
            with AllureStepWithAttachment(None, "Step 2: Verify success Login."):
                    self.process_login("valid_login")

    @Login.login_decorators_tc3_004_api
    def test_failed_login_via_api(self):
        with AllureStepWithAttachment(None, "Step 1: Send POST request with invalid data "):
            with AllureStepWithAttachment(None, "Step 2: Verify failed Login."):
                self.process_login("invalid_login")






import pytest
from utils.allure_util import AllureStepWithAttachment
from tests.reusable.decorator_utils import SignUp
from tests.reusable.http_util import HttpUtil
from test_data.data_generator import DataGenerator


@SignUp.class_signup_decorators_api
class TestUserSignupFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.http_util = HttpUtil()
        self.signup_endpoint = "/users"
        self.data_generator = DataGenerator()

    def signup_process(self, user_data):
        response_data = self.http_util.post_request(self.signup_endpoint, json_data=user_data)
        AllureStepWithAttachment.attach_response(response_data)


    @SignUp.signup_decorators_tc1_005_api
    def test_successful_signup_via_api(self):
        with AllureStepWithAttachment(None, "Step 1: Submit POST request with valid data."):
            valid_signup = self.data_generator.generate_valid_signup_data()
        with AllureStepWithAttachment(None, "Step 2: Verify success Signup."):
            self.signup_process(valid_signup)


    @SignUp.signup_decorators_tc1_006_008_api
    def test_failed_signup_using_invalid_data(self):
        with AllureStepWithAttachment(None, "Step 1: Submit POST request with invalid data."):
            invalid_signup = self.data_generator.generate_invalid_signup_data()
        with AllureStepWithAttachment(None, "Step 2: Verify failed Signup."):
            self.signup_process(invalid_signup)




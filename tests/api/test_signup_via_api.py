from utils.imports_util import *


@SignUp.class_signup_decorators_api
class TestUserSignupFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.http_util = HttpUtil()
        self.signup_endpoint = "/users"
        self.data_generator = DataGenerator()

    def process_signup(self, user_data):
        response_data = self.http_util.post_request(self.signup_endpoint, json_data=user_data)
        AllureStepWithAttachment.attach_response(response_data)

    @SignUp.signup_decorators_tc1_005_api
    def test_successful_signup_via_api(self):
        with AllureStepWithAttachment(None, "Step 1: Send a POST request to the registration endpoint with valid data."):
            valid_signup = self.data_generator.generate_valid_signup_data()
            self.process_signup(valid_signup)

    @SignUp.signup_decorators_tc1_006_008_api
    def test_failed_signup_using_invalid_data(self):
        with AllureStepWithAttachment(None, "Step 1: Send a POST request to the registration endpoint with invalid data."):
            invalid_signup = self.data_generator.generate_invalid_signup_data()
            self.process_signup(invalid_signup)




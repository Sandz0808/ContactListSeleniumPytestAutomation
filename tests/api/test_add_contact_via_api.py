import pytest
from utils.allure_util import AllureStepWithAttachment
from tests.reusable.http_util import HttpUtil
from tests.reusable.decorator_utils import AddContact
from tests.reusable.api_test_data_util import ApiTestDataUtil


@AddContact.class_add_contact_decorators_api
class TestAddContactFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.http_util = HttpUtil()
        self.api_test_data_util = ApiTestDataUtil()
        self.valid_login_data = self.api_test_data_util.get_api_testdata("valid_login")
        self.token = self.http_util.post_request("/users/login", self.valid_login_data)['token']

    def post_request(self, contact_data, method="POST"):
        headers = self.http_util.build_auth_headers(self.token)
        return self.http_util.post_request("/contacts", json_data=contact_data, headers=headers)\
            if method == "POST" else self.http_util.get_request(f"/contacts/{contact_data['_id']}", headers=headers)

    @AddContact.add_contact_decorators_tc4_003_api
    def test_add_contact_with_valid_data_via_the_api(self):
        valid_add_contact_data = self.api_test_data_util.get_api_testdata("add_contact")
        with AllureStepWithAttachment(None, "Step 1: Submit POST request with valid data"):
            api_response_data = self.post_request(valid_add_contact_data, "POST")
        with AllureStepWithAttachment(None, "Step 2: Verify success Add Contact"):
            AllureStepWithAttachment.attach_response(api_response_data)


    @AddContact.add_contact_decorators_tc4_004_api
    def test_verify_if_the_api_handles_invalid_contact_data(self):
        invalid_add_contact_data = self.api_test_data_util.get_api_testdata("invalid_contact_data")
        with AllureStepWithAttachment(None, "Step 1: Submit POST request with invalid data"):
            api_response_data = self.post_request(invalid_add_contact_data, "POST")
        with AllureStepWithAttachment(None, "Step 2: Verify failed  Add Contact"):
            AllureStepWithAttachment.attach_response(api_response_data)




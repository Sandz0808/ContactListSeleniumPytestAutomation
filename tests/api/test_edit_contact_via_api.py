import pytest
from tests.reusable.api_test_data_util import ApiTestDataUtil
from utils.allure_util import AllureStepWithAttachment
from utils.decorator_utils import EditContact
from utils.http_util import HttpUtil


@EditContact.class_edit_contact_decorators_api
class TestContactEditFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.http_util = HttpUtil()
        self.api_test_data_util = ApiTestDataUtil()
        self.token = self.http_util.post_request("/users/login", self.api_test_data_util.get_api_testdata("valid_login"))['token']

    def add_contact(self, contact_data):
        headers = self.http_util.build_auth_headers(self.token)
        return self.http_util.post_request("/contacts", json_data=contact_data, headers=headers)

    def edit_contact(self, contact_id, updated_data):
        headers = self.http_util.build_auth_headers(self.token)
        return self.http_util.put_request(f"/contacts/{contact_id}", json_data=updated_data, headers=headers)

    @EditContact.edit_contact_decorators_tc7_003_api
    def test_verify_if_a_contact_can_be_successfully_edited_via_the_api(self):
        contact_data = self.api_test_data_util.get_api_testdata("add_contact")
        with AllureStepWithAttachment(None, "Step 1: Send PUT request with valid data "):
            added_contact = self.add_contact(contact_data)
            AllureStepWithAttachment.attach_response(added_contact)
            contact_id = added_contact['_id']
            updated_contact_data = self.api_test_data_util.get_api_testdata("updated_contact_data")
        with AllureStepWithAttachment(None, "Step 2: Verify success Edit status"):
            response_data = self.edit_contact(contact_id, updated_contact_data)
            AllureStepWithAttachment.attach_response(response_data)


    @EditContact.edit_contact_decorators_tc7_004_api
    def test_verify_if_the_api_fails_when_editing_a_contact_with_invalid_data(self):
        contact_data = self.api_test_data_util.get_api_testdata("add_contact")
        with AllureStepWithAttachment(None, "Step 1: Send PUT request with invalid data "):
            added_contact = self.add_contact(contact_data)
            AllureStepWithAttachment.attach_response(added_contact)
            contact_id = added_contact['_id']
            invalid_contact_data = self.api_test_data_util.get_api_testdata("invalid_contact_data")
        with AllureStepWithAttachment(None, "Step 2: Verify failed Edit status"):
            response_data = self.edit_contact(contact_id, invalid_contact_data)
            AllureStepWithAttachment.attach_response(response_data)

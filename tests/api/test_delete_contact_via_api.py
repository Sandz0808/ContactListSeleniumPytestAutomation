from utils.imports_util import *

@Delete.class_delete_decorators_api
class TestContactDeletionFunctionality:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.http_util = HttpUtil()
        self.api_test_data_util = ApiTestDataUtil()
        self.token = self.http_util.post_request("/users/login", self.api_test_data_util.get_api_testdata("valid_login"))['token']

    def add_contact(self):
        contact_data = self.api_test_data_util.get_api_testdata("add_contact")
        headers = self.http_util.build_auth_headers(self.token)
        return self.http_util.post_request("/contacts", json_data=contact_data, headers=headers)

    def delete_contact(self, contact_id):
        headers = self.http_util.build_auth_headers(self.token)
        return self.http_util.delete_request(f"/contacts/{contact_id}", headers=headers)

    @Delete.delete_decorators_tc8_002_api
    def test_successful_delete_contact_via_api(self):
        added_contact = self.add_contact()
        AllureStepWithAttachment.attach_response(added_contact)

        contact_id = added_contact['_id']
        response_data = self.delete_contact(contact_id)
        AllureStepWithAttachment.attach_response(response_data)

        self.http_util.get_request(f"/contacts/{contact_id}", headers=self.http_util.build_auth_headers(self.token))

    @Delete.delete_decorators_tc8_003_api
    def test_delete_nonexistent_contact_via_api(self):
        non_existent_contact_id = self.api_test_data_util.get_api_testdata("non_existent_contact")["non_existent_contact_id"]
        response_data = self.delete_contact(non_existent_contact_id)
        AllureStepWithAttachment.attach_response(response_data)

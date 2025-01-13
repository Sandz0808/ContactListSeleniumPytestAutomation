import requests
import json
from utils.log_util import LoggingUtility
from utils.config_util import ConfigReader
from utils.log_message_util import *
from utils.exception_message_util import *

class HttpUtil:
    def __init__(self):
        self.log = LoggingUtility()
        self.config_reader = ConfigReader()
        self.base_url = self.config_reader.get_value('staging', 'url')
        self.response_file_path = self.config_reader.get_value('paths', 'response_file_path')

    def get_auth_token(self, valid_login_data):
        try:
            response_data = self.post_request("/users/login", json_data=valid_login_data)
            token = response_data.get("token")

            if token is None:
                raise ValueError(TOKEN_ERROR)

            self.log.get_log_formatted_message(TOKEN_RETRIEVAL_SUCCESS, "info")
            return token

        except requests.exceptions.RequestException:
            self.log.get_log_formatted_message(HTTP_REQUEST_ERROR, "error")
            raise
        except ValueError:
            self.log.get_log_formatted_message(VALUE_ERROR, "error")
            raise
        except Exception:
            self.log.get_log_formatted_message(UNEXPECTED_ERROR, "error")
            raise

    def post_request(self, endpoint, json_data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, json=json_data, headers=headers)
            response.raise_for_status()
            self.log.get_log_formatted_message(REQUEST_SUCCESS, "info")

            data = response.json() if response.content else {}
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': response.status_code, 'response': data}, file, indent=4)

            return data

        except requests.exceptions.RequestException:
            self.log.get_log_formatted_message(POST_REQUEST_ERROR, "error")
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 400, 'response': 'Invalid Data'}, file, indent=4)
            return None
        except json.JSONDecodeError:
            self.log.get_log_formatted_message(JSON_DECODE_ERROR, "error")
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': response.status_code, 'response': 'JSON decode error'}, file, indent=4)
            return None
        except Exception:
            self.log.get_log_formatted_message(UNEXPECTED_ERROR, "error")
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 500, 'response': 'Unexpected error'}, file, indent=4)
            return None

    def get_request(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            self.log.get_log_formatted_message(GET_REQUEST_SUCCESS, "info")

            data = response.json() if response.content else {}
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': response.status_code, 'response': data}, file, indent=4)

            return data

        except requests.exceptions.RequestException:
            self.log.get_log_formatted_message(GET_REQUEST_ERROR, "error")
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 400, 'response': 'Nonexistent Contact'}, file, indent=4)
            return None
        except json.JSONDecodeError:
            self.log.get_log_formatted_message(JSON_DECODE_ERROR, "error")
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': response.status_code, 'response': 'JSON decode error'}, file, indent=4)
            return None
        except Exception:
            self.log.get_log_formatted_message(UNEXPECTED_ERROR, "error")
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 500, 'response': 'Unexpected error'}, file, indent=4)
            return None

    def put_request(self, endpoint, json_data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.put(url, json=json_data, headers=headers)
            response.raise_for_status()
            self.log.get_log_formatted_message(PUT_REQUEST_SUCCESS, "info")

            data = response.json() if response.content else {}
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': response.status_code, 'response': data}, file, indent=4)

            return data

        except requests.exceptions.RequestException:
            self.log.get_log_formatted_message(PUT_REQUEST_ERROR, "error")
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 400, 'response': 'Invalid Data'}, file, indent=4)
            return None
        except json.JSONDecodeError:
            self.log.get_log_formatted_message(JSON_DECODE_ERROR, "error")
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': response.status_code, 'response': 'JSON decode error'}, file, indent=4)
            return None
        except Exception:
            self.log.get_log_formatted_message(UNEXPECTED_ERROR, "error")
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 500, 'response': 'Unexpected error'}, file, indent=4)
            return None

    def delete_request(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.delete(url, headers=headers)

            if response.status_code in [204, 200]:
                self.log.get_log_formatted_message(DELETE_REQUEST_SUCCESS, "info")
                with open(self.response_file_path, 'w') as file:
                    json.dump({'status_code': response.status_code, 'response': 'Deleted successfully'}, file, indent=4)
                return None
            else:
                response.raise_for_status()

        except requests.exceptions.RequestException:
            self.log.get_log_formatted_message(DELETE_REQUEST_ERROR, "error")
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 400, 'response': 'Nonexistent Contact'}, file, indent=4)
            return None
        except Exception:
            self.log.get_log_formatted_message(UNEXPECTED_ERROR, "error")
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 500, 'response': 'Unexpected error'}, file, indent=4)
            return None

    def build_auth_headers(self, token):
        return {'Authorization': f'Bearer {token}'}

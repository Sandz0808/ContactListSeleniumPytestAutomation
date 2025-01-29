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

    """ Usage:
    post_status = self.success_response("POST", REQUEST_SUCCESS)
    delete_status = self.success_response("DELETE", DELETE_REQUEST_SUCCESS)
    put_status = self.success_response("PUT", PUT_REQUEST_SUCCESS)
    get_status = self.success_response("PUT", GET_REQUEST_SUCCESS)
    """
    def actual_response(self, operation_type, success_message):
        response = requests.get(self.base_url)

        if 200 <= response.status_code < 300:
            # Success condition
            status_code = f"Success Code: {response.status_code} {self.log.get_log_formatted_message(success_message, None)}"
            return status_code

        else:
            # Failure condition
            error_message = f"{operation_type} Failed with Status Code: {response.status_code}, Content: {response.text}"
            self.log.get_log_formatted_message(error_message, "error")
            return error_message


    def log_error_response(self, response):
        """Logs detailed error information from the response."""
        try:
            response_content = response.json() if response.content else {}
        except json.JSONDecodeError:
            response_content = response.text
        self.log.get_log_formatted_message(
            f"Error Response: Status Code {response.status_code}, Content: {response_content}", "error")

        return response_content

    def post_request(self, endpoint, json_data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, json=json_data, headers=headers)
            response.raise_for_status()

            # Get user data and full response data
            user_data = response.json().get('user')
            full_response_data = response.json()

            pretty1 = json.dumps(user_data, indent=4)
            pretty2 = json.dumps(full_response_data, indent=4)

            # Log success response
            success_response = self.actual_response("POST", REQUEST_SUCCESS)
            self.log.get_log_formatted_message(success_response, "info")

            # Log user data and full response
            if user_data:
                self.log.get_log_formatted_message(
                    "User POST request: {user_data}",
                    "info",
                    user_data=user_data
                )
            self.log.get_log_formatted_message(
                "Response Body: {full_response}",
                "debug",
                full_response=full_response_data
            )


            # Save response to file
            data = response.json() if response.content else {}
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': response.status_code, 'response': data}, file, indent=4)

            return data

        except requests.exceptions.RequestException as e:
            response_content = self.log_error_response(e.response) if e.response else str(e)
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 400, 'response': response_content}, file, indent=4)
            return None
        except Exception as e:
            self.log.get_log_formatted_message(f"Unexpected error: {e}", "error")
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 500, 'response': str(e)}, file, indent=4)
            return None


        except Exception as e:
            error_message = str(e)
            self.log.get_log_formatted_message(
                f"\n--- Unexpected Error ---\n"
                f"Error: {error_message}\n",
                "error"
            )
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 500, 'response': error_message}, file, indent=4)
            return None

    def get_request(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            success_response = self.actual_response("GET", GET_REQUEST_SUCCESS)
            self.log.get_log_formatted_message(success_response, "info")

            # Get user data and full response data
            user_data = response.json().get('user')
            full_response_data = response.json()

            pretty1 = json.dumps(user_data, indent=4)
            pretty2 = json.dumps(full_response_data, indent=4)

            print(pretty1)
            print(pretty2)

            # Log user data and full response
            if user_data:
                self.log.get_log_formatted_message("User GET request: {user_data}", "info", user_data=user_data)
                self.log.get_log_formatted_message("Response Body: {full_response}", "debug",full_response=full_response_data)

            data = response.json() if response.content else {}
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': response.status_code, 'response': data}, file, indent=4)

            return data

        except requests.exceptions.RequestException as e:
            response_content = self.log_error_response(e.response) if e.response else str(e)
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 400, 'response': response_content}, file, indent=4)
            return None
        except Exception as e:
            self.log.get_log_formatted_message(f"Unexpected error: {e}", "error")
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 500, 'response': str(e)}, file, indent=4)
            return None

    def put_request(self, endpoint, json_data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.put(url, json=json_data, headers=headers)
            response.raise_for_status()
            success_response = self.actual_response("PUT", PUT_REQUEST_SUCCESS)
            self.log.get_log_formatted_message(success_response, "info")

            # Get user data and full response data
            user_data = response.json().get('user')
            full_response_data = response.json()

            # Log user data and full response
            if user_data:
                self.log.get_log_formatted_message(
                    "User PUT request: {user_data}",
                    "info",
                    user_data=user_data
                )
            self.log.get_log_formatted_message(
                "Response Body: {full_response}",
                "debug",
                full_response=full_response_data
            )


            data = response.json() if response.content else {}
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': response.status_code, 'response': data}, file, indent=4)

            return data

        except requests.exceptions.RequestException as e:
            response_content = self.log_error_response(e.response) if e.response else str(e)
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 400, 'response': response_content}, file, indent=4)
            return None
        except Exception as e:
            self.log.get_log_formatted_message(f"Unexpected error: {e}", "error")
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 500, 'response': str(e)}, file, indent=4)
            return None

    def delete_request(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.delete(url, headers=headers)

            if response.status_code in [204, 200]:
                success_response = self.actual_response("DELETE", DELETE_REQUEST_SUCCESS)
                self.log.get_log_formatted_message(success_response, "info")

                # Get user data and full response data
                user_data = response.json().get('user')
                full_response_data = response.json()

                # Log user data and full response
                if user_data:
                    self.log.get_log_formatted_message(
                        "User DELETE request: {user_data}",
                        "info",
                        user_data=user_data
                    )
                self.log.get_log_formatted_message(
                    "Response Body: {full_response}",
                    "debug",
                    full_response=full_response_data
                )

                with open(self.response_file_path, 'w') as file:
                    json.dump({'status_code': response.status_code, 'response': 'Deleted successfully'}, file, indent=4)
                return None
            else:
                response.raise_for_status()

        except requests.exceptions.RequestException as e:
            response_content = self.log_error_response(e.response) if e.response else str(e)
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 400, 'response': response_content}, file, indent=4)
            return None
        except Exception as e:
            self.log.get_log_formatted_message(f"Unexpected error: {e}", "error")
            with open(self.response_file_path, 'w') as file:
                json.dump({'status_code': 500, 'response': str(e)}, file, indent=4)
            return None



    def build_auth_headers(self, token):
        return {'Authorization': f'Bearer {token}'}



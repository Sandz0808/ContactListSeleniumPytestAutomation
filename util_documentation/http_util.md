# HTTP Utility Class Documentation

## Overview
The `HttpUtil` class is a utility for making HTTP requests (GET, POST, PUT, DELETE) to interact with web services. It includes functionalities for retrieving authentication tokens, building authorization headers, and handling API responses.

## Requirements
- Python 3.7+
- `requests` library

Install the `requests` library if not already installed:
```bash
pip install requests
```

## Dependencies
- `requests`
- `json`
- `utils.log_util.LoggingUtility`
- `utils.config_util.ConfigReader`
- `utils.log_message_util`
- `utils.exception_message_util`

---

## Class: `HttpUtil`
The `HttpUtil` class provides methods to perform HTTP operations such as GET, POST, PUT, and DELETE.

### Constructor: `__init__(self)`
Initializes the class with the following attributes:
- `self.log`: Instance of `LoggingUtility` for logging messages.
- `self.config_reader`: Instance of `ConfigReader` for reading configuration values.
- `self.base_url`: Base URL fetched from the `config.toml` file.
- `self.response_file_path`: File path to save API responses.

---

### Method: `get_auth_token(self, valid_login_data)`
Retrieves an authentication token by making a POST request to the `/users/login` endpoint.

**Parameters:**
- `valid_login_data` (dict): JSON payload containing login credentials.

**Returns:**
- `token` (str): The authentication token.

**Exceptions Handled:**
- `requests.exceptions.RequestException`: Handles HTTP request errors.
- `ValueError`: Raised when the token is not found in the response.
- `Exception`: Handles unexpected errors.

---

### Method: `post_request(self, endpoint, json_data=None, headers=None)`
Sends a POST request to the specified endpoint.

**Parameters:**
- `endpoint` (str): The API endpoint to send the request to.
- `json_data` (dict): JSON payload to be sent with the request.
- `headers` (dict): Optional headers to be included in the request.

**Returns:**
- `data` (dict): Parsed JSON response.

**Exceptions Handled:**
- `requests.exceptions.RequestException`: Handles request errors.
- `json.JSONDecodeError`: Handles errors while decoding the JSON response.
- `Exception`: Handles unexpected errors.

---

### Method: `get_request(self, endpoint, headers=None)`
Sends a GET request to the specified endpoint.

**Parameters:**
- `endpoint` (str): The API endpoint to send the request to.
- `headers` (dict): Optional headers to be included in the request.

**Returns:**
- `data` (dict): Parsed JSON response.

**Exceptions Handled:**
- `requests.exceptions.RequestException`
- `json.JSONDecodeError`
- `Exception`

---

### Method: `put_request(self, endpoint, json_data=None, headers=None)`
Sends a PUT request to the specified endpoint.

**Parameters:**
- `endpoint` (str): The API endpoint to send the request to.
- `json_data` (dict): JSON payload to be sent with the request.
- `headers` (dict): Optional headers to be included in the request.

**Returns:**
- `data` (dict): Parsed JSON response.

**Exceptions Handled:**
- `requests.exceptions.RequestException`
- `json.JSONDecodeError`
- `Exception`

---

### Method: `delete_request(self, endpoint, headers=None)`
Sends a DELETE request to the specified endpoint and handles alerts.

**Parameters:**
- `endpoint` (str): The API endpoint to send the request to.
- `headers` (dict): Optional headers to be included in the request.

**Returns:**
- `None`

**Exceptions Handled:**
- `requests.exceptions.RequestException`
- `Exception`

---

### Method: `build_auth_headers(self, token)`
Builds authorization headers using the provided token.

**Parameters:**
- `token` (str): The authentication token.

**Returns:**
- `headers` (dict): Authorization headers in the format `{'Authorization': 'Bearer <token>'}`.

---

## Logging Messages
- `TOKEN_RETRIEVAL_SUCCESS`
- `HTTP_REQUEST_ERROR`
- `VALUE_ERROR`
- `UNEXPECTED_ERROR`
- `REQUEST_SUCCESS`
- `POST_REQUEST_ERROR`
- `JSON_DECODE_ERROR`
- `GET_REQUEST_SUCCESS`
- `GET_REQUEST_ERROR`
- `PUT_REQUEST_SUCCESS`
- `PUT_REQUEST_ERROR`
- `DELETE_REQUEST_SUCCESS`
- `DELETE_REQUEST_ERROR`

---

## Error Handling
The class includes comprehensive error handling for different types of exceptions, ensuring that any issues during the API interaction are logged and handled appropriately.

## Usage Example
```python
from http_util import HttpUtil

# Initialize the HTTP utility
http_util = HttpUtil()

# Retrieve authentication token
login_data = {"username": "test_user", "password": "test_pass"}
token = http_util.get_auth_token(login_data)

# Perform a POST request
endpoint = "/api/resource"
response = http_util.post_request(endpoint, json_data={"key": "value"}, headers=http_util.build_auth_headers(token))
print(response)
```


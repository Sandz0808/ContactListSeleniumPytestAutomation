import logging

class APIAssertions:
    @staticmethod
    def assert_status_code(response, expected_code):
        """
        Asserts that the response status code matches the expected status code.
        """
        actual_code = response.status_code
        assert actual_code == expected_code, (
            f"Expected status code {expected_code}, but got {actual_code}. "
            f"Response: {response.json()}"
        )
        logging.info(f"Status code {actual_code} is as expected.")

    @staticmethod
    def assert_success(response):
        """
        Asserts that the response status code is a success (200 or 201).
        """
        assert response.status_code in [200, 201], (
            f"Expected success status code (200 or 201), but got {response.status_code}. "
            f"Response: {response.json()}"
        )
        logging.info(f"Success! Status code {response.status_code}.")

    @staticmethod
    def assert_bad_request(response):
        """
        Asserts that the response status code is 400 (Bad Request).
        """
        assert response.status_code == 400, (
            f"Expected 400 Bad Request, but got {response.status_code}. "
            f"Response: {response.json()}"
        )
        logging.info("Bad Request status code 400 validated.")

    @staticmethod
    def assert_unauthorized(response):
        """
        Asserts that the response status code is 401 (Unauthorized).
        """
        assert response.status_code == 401, (
            f"Expected 401 Unauthorized, but got {response.status_code}. "
            f"Response: {response.json()}"
        )
        logging.info("Unauthorized status code 401 validated.")

    @staticmethod
    def assert_forbidden(response):
        """
        Asserts that the response status code is 403 (Forbidden).
        """
        assert response.status_code == 403, (
            f"Expected 403 Forbidden, but got {response.status_code}. "
            f"Response: {response.json()}"
        )
        logging.info("Forbidden status code 403 validated.")

    @staticmethod
    def assert_not_found(response):
        """
        Asserts that the response status code is 404 (Not Found).
        """
        assert response.status_code == 404, (
            f"Expected 404 Not Found, but got {response.status_code}. "
            f"Response: {response.json()}"
        )
        logging.info("Not Found status code 404 validated.")

    @staticmethod
    def assert_server_error(response):
        """
        Asserts that the response status code is 500 (Internal Server Error).
        """
        assert response.status_code == 500, (
            f"Expected 500 Internal Server Error, but got {response.status_code}. "
            f"Response: {response.json()}"
        )
        logging.info("Server Error status code 500 validated.")

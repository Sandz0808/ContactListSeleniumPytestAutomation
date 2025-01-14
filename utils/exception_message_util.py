# HelperUtils Exception messages:
CLICKING_EXCEPTION_ERROR_MESSAGE = "An error occurred while attempting to click the element: {error}"
INPUT_EXCEPTION_ERROR_MESSAGE = "An error occurred while attempting to input text into the element: {error}"
ASSERTION_EXCEPTION_ERROR_MESSAGE = ("An error occurred during Assertion. Actual value is: {actual_attribute_value} "
                                     "while Expected value is: {expected_attribute_value}. {error}")
CLEAR_ERROR_MESSAGE = "An error occurred while attempting to clear the text field: {error}"
POSITION_ASSERTION_EXCEPTION_ERROR_MESSAGE = "An error occurred during element position assertion: {error}"
HEX_ASSERTION_EXCEPTION_ERROR_MESSAGE = "Assertion Error in HEX value: {error}"
NO_SUCH_ELEMENT_EXCEPTION_ERROR_MESSAGE = "Element with locator {locator} was not found."
TIMEOUT_EXCEPTION_ERROR_MESSAGE = ("Element with locator {locator} is not visible "
                                   "within the timeout period")
URL_WEBDRIVER_EXCEPTION_ERROR_MESSAGE = "An error occurred while navigating to {url}: {error}"
URL_VALUE_ERROR_MESSAGE = "Invalid URL: {url}"
SCROLL_INTO_VIEW = "Element with locator {locator} not found: {error}"
ERROR_OCCURRED_EXCEPTION = "An error occurred: {error}"
INITIAL_SRC_NONE_EXCEPTION_MESSAGE = "Initial src attribute should not be None"
ELEMENT_ATTRIBUTE_EXCEPTION_MESSAGE = "An error occurred getting the attribute: {error}"
ELEMENT_LOCATION_EXCEPTION_MESSAGE = "An error occurred getting the location: {error}"
ELEMENT_REGEX_EXCEPTION_MESSAGE = "An error occurred getting the location: {error}"
NOT_IN_LINE_EXCEPTION_MESSAGE = "Location of {element_description1} and {element_description2} is not in line"
EXPECTED_TEXT_NOT_EQUAL_EXCEPTION_MESSAGE = "Expected text to be '{expected_text}' but got '{actual_text}'"
NAVIGATE_URL_EXCEPTION_MESSAGE = "An error occurred while navigating to {url}: {error}"
SWITCHING_TAB_EXCEPTION_MESSAGE = "Error switching to the newest tab: {error}"
NOT_ENOUGH_TAB_EXCEPTION_MESSAGE = "There are not enough tabs open to switch."
HEX_VALUE_ASSERTION_MESSAGE = "Assertion Error in HEX value, not equal: {error}"
EXPECTED_FILE_NOT_FOUND = "Expected file '{downloaded_file}' not found in {download_dir1}"
REGEX_PATTERN_EXCEPTION_MESSAGE = "The {element_description} that has element text '{actual_text}' does not match pattern"
NEW_EMAIL_EXCEPTION_MESSAGE = "There is a new email"
TAB_DETECTED_EXCEPTION_MESSAGE = "Timeout while waiting for a new tab to open: {error}"
SWITCHING_IFRAME_EXCEPTION_MESSAGE = "Error switching to the newest frame"
DOWNLOADED_FILE_EXCEPTION_MESSAGE = "Downloaded file did not exist: {error}"
UPLOADED_FILE_EXCEPTION_MESSAGE = "Error in uploading file: {error}"
RENAMED_FILE_EXCEPTION_MESSAGE = "Renamed file did not exist: {error}"
SCREENSHOT_SAVING_EXCEPTION_MESSAGE = "Error in saving screenshot: {error}"

# WebDriver Manager exception messages:
SAFARI_ENVIRONMENT_ERROR_MESSAGE = "Safari WebDriver can only be run on macOS."
UNSUPPORTED_BROWSER_TYPE_EXCEPTION_ERROR_MESSAGE = "Unsupported browser type: {browser_type}"

# config.ini exception messages:
CONFIGURATION_SECTION_ERROR_MESSAGE = "Section '{section}' not found in the configuration file."
CONFIGURATION_KEY_ERROR_MESSAGE = "Key '{key}' not found in section '{section}'."

# JsonUtil exception messages:
NO_TESTDATA_KEY_EXCEPTION_ERROR_MESSAGE = "Key '{value_key}' not found in group '{test_key}'"
NO_TESTDATA_GROUP_EXCEPTION_ERROR_MESSAGE = "Group '{test_key}' not found in the JSON object"
NO_TESTDATA_SUBKEY_EXCEPTION_ERROR_MESSAGE = "Sub-key '{sub_key}' not found in '{value_key}' group"
NO_TESTDATA_FILE_EXCEPTION_MESSAGE = "File '{testdata_path}' did not exists. {error}"

# Conftest exception message:
NO_OPTION_EXCEPTION_ERROR_MESSAGE = "No option '{config}' in section 'URLs'. Please check your configuration."

# Allure util exception message:
STEP_FAIL_ERROR_MESSAGE = "Step '{step_name}' failed with error: {error}"

# General HTTP request errors
HTTP_REQUEST_ERROR = "An error occurred while making an HTTP request."
POST_REQUEST_ERROR = "An error occurred during the POST request."
GET_REQUEST_ERROR = "An error occurred during the GET request."
PUT_REQUEST_ERROR = "An error occurred during the PUT request."
DELETE_REQUEST_ERROR = "An error occurred during the DELETE request."

# Specific error handling for JSON decoding
JSON_DECODE_ERROR = "Error occurred while decoding the JSON response."

# Token and Login Errors
TOKEN_RETRIEVAL_ERROR = "Error occurred while retrieving the authentication token."
VALUE_ERROR = "Value error during the process, possibly related to missing data or incorrect format."

# General errors
UNEXPECTED_ERROR = "An unexpected error occurred. Please check the logs for more details."

# Token error
TOKEN_ERROR = "No token found in the login response."

# Section and Key Error Messages
SECTION_NOT_FOUND_ERROR = "Section '{section}' not found."
KEY_NOT_FOUND_ERROR = "Key '{key}' not found in section '{section}'."

# Driver Error
VALUE_DRIVER_ERROR = "Unsupported browser type provided."

# Setup Error
SETUP_ERROR = "Failed to retrieve the URL from the configuration file."

# Test Key
TEST_KEY_NOT_FOUND = "Test key not found."

# Test data errors
FAILED_TO_LOAD_DATA = "Failed to load test data."
DATA_DOES_NOT_EXIST = "Test data file does not exist"

# Environment Error
ENVIRONMENT_ERROR = "This browser only works on MacOS"

# Alert
ALERT_ERROR = "Error handling delete action or accepting alert. {error}"


# UI Error Message
ADD_CONTACT_ERROR_EMPTY_LASTNAME = "Contact validation failed: lastName: Path `lastName` is required."
ADD_CONTACT_ERROR_EMPTY_FIRSTNAME = "Contact validation failed: firstName: Path `firstName` is required."
INVALID_USERNAME_PASSWORD_ERROR = "Incorrect username or password"



# SignUp Error
USED_EMAIL = "Email address is already in use"
EMPTY_FIRST_NAME = "User validation failed: firstName: Path `firstName` is required."
EMPTY_LAST_NAME = "User validation failed: lastName: Path `lastName` is required."
EMPTY_PASSWORD = "User validation failed: password: Path `password` is required."
SHORT_PASSWORD = "User validation failed: password: Path `password` (`123456`) is shorter than the minimum allowed length (7)."
LONG_PASSWORD = "User validation failed: password: Path `password` (`iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii`) is longer than the maximum allowed length (100)."
EMPTY_EMAIL = "User validation failed: email: Email is invalid"
INVALID_EMAIL = "User validation failed: email: Email is invalid"
# Edit Contact Error
EDIT_CONTACT_EMPTY_FIELD_ERROR = "Validation failed: firstName: Path `firstName` is required."




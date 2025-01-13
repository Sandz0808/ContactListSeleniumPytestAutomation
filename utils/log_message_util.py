# Wait Element
VISIBLE_ELEMENT_MESSAGE = "Element with locator: {locator} is visible within the timeout period"

# Element Interaction - Click and Input
CLICKING_MESSAGE = "Clicking the element {locator}"
INPUT_TEXT_MESSAGE = "Input text value: '{input_value} into element with locator: {locator}"
NOT_CLICKABLE_ELEMENT_VERIFICATION_MESSAGE = ("The element: {element_description} with "
                                              "locator: {locator} is not clickable")
CLICKABLE_ELEMENT_VERIFICATION_MESSAGE = ("The element: {element_description} with "
                                          "locator: {locator} is clickable")
DISABLED_ELEMENT_VERIFICATION_MESSAGE = ("The element {element_description} with "
                                         "locator: {locator} is disabled")
# Alert Visible
ALERT_VISIBLE = "Alert is visible"
# Element Clear
CLEAR_MESSAGE = "Text field cleared"

# Element Display & Scroll Assertions
ELEMENT_TO_SCROLL_IN_DISPLAY = "Element {locator} is displayed after scrolling into view."
ELEMENT_DISPLAY_ASSERTION_MESSAGE = ("The element {element_description} with locator: "
                                     "{locator} is displayed")

# Text Assertion
ELEMENT_ASSERTION_MESSAGE = "Actual value is: {actual_attribute_value} while Expected value is: {expected_attribute_value}"

# Element Attribute
ELEMENT_ATTRIBUTE_MESSAGE = "Actual value of attribute is: {actual_attribute_value}"

# Element Location
ELEMENT_LOCATION_MESSAGE = "Actual location is: {actual_location}"

# Compare Element Location
COMPARE_LOCATION_MESSAGE = "Actual value is: {actual_locator} while Expected value is: {expected_location}"

# Font & Bold Assertions
BOLD_TEXT_ASSERTION_MESSAGE = "The element {locator} font-family is '{font_family}' and in bold"


# Image Src Assertions
SRC_ASSERTION_MESSAGE = "Actual src is: {actual_text} with Expected src is: {source}"


# Positioning Assertions
RIGHT_POSITION_ASSERTION_MESSAGE = ("Target {element_description1} element: {locator2} is on the right side"
                                    " of the initial {element_description2} element: {locator1}")

BELOW_POSITION_ASSERTION_MESSAGE = ("Target {element_description2} element located by {locator2} is below"
                                    " the initial {element_description1} element located by {locator1}.")

ABOVE_POSITION_ASSERTION_MESSAGE = ("Target element located by {locator2} is above the initial element "
                                    "located by {locator1}.")

# Expansion Assertions
EXPANDED_ELEMENT_ASSERTION_MESSAGE = ("{element_description} element is expanded. Initial height is: "
                                      "{str(initial_height)}, New height is: {str(new_height)}")

# Color Assertions
HIGHLIGHTED_COLOR_ASSERTION_MESSAGE = ("Actual HEX color is {actual_hex_color} and "
                                       "Expected HEX value is: {expected_hex_color}")

# Time Assertions
TIME_ASSERTION_MESSAGE = "There are no new emails at the moment."

# File Download and Upload
DOWNLOADED_MESSAGE = "File {set_new_filename} downloaded and exists"
UPLOADED_MESSAGE = "File uploaded successfully"
RENAMED_FILE_MESSAGE = "Renamed file exists"

# Screenshot
SCREENSHOT_MESSAGE = "Screenshot saved successfully"

# Regex Validation
REGEX_PATTERN_VALIDATION_MESSAGE = ("The {element_description} that has element "
                                    "text '{actual_text}' does not match pattern '{regex_pattern}'")

REGEX_ASSERTION_MESSAGE = "Actual value is: {actual_attribute_value} while Expected value is: {expected_pattern}"

# Length Assertions
EQUAL_LENGTH_ASSERTION_MESSAGE = ("The expected length is "
                                  "{elem_length} and the actual is {elements_count}")

MORE_THAN_LENGTH_ASSERTION_MESSAGE = (
    "The expected length is {elem_length} less than or equal to {elements_count}"
)

LESS_THAN_LENGTH_ASSERTION_MESSAGE = (
    "The expected length is {elem_length} and it is less than to {elements_count}"
)

# Link Assertions
LINK_ASSERTION = "Element {element} is a link"

# Sorting Validation
ASCENDING_SORT_MESSAGE_VALIDATION = "Messages are in ascending order"

DESCENDING_SORT_MESSAGE_VALIDATION = "Messages are in descending order"

# General Assertion Failure
FALSE_ASSERTION_MESSAGE = "{element_description}"

# Configuration Assertion Messages
CONFIGURATION_FILE_EXIST_MESSAGE = "Configuration file found at: {config_file_path}"
CONFIG_RETRIEVED_MESSAGE = "Retrieve value for '{key}' in section '{section}': {value}"

# Allure Util logs messages
STEP_PASSED_MESSAGE = "Step '{step_name}' executed successfully."

# JsonUtil Log Messages
NO_TESTDATA_FILE_EXIST_MESSAGE = "File '{testdata_path}' not found"
TESTDATA_FILE_EXIST_MESSAGE = "File '{testdata_path}' exists, proceeding to read data."
VALUE_RETRIEVED_MESSAGE = "Retrieved value: {result}"

# Conftest Log Message
DRIVER_QUIT_MESSAGE = "Driver quit successfully"

# URL Log Message
URL_WEBDRIVER_MESSAGE = "Successfully navigated to {url}"

# Tab Switching
SWITCHING_TAB_MESSAGE = "Successfully switched to the newest tab"

# Iframe Switching
SWITCHING_IFRAME_MESSAGE = "Element with locator: {locator} Successfully switched to the newest frame"

# Time out Message
TAB_DETECTED = "New tab detected"

# Success messages
REQUEST_SUCCESS = "The HTTP request was successful."
GET_REQUEST_SUCCESS = "The GET request was successful."
PUT_REQUEST_SUCCESS = "The PUT request was successful."
DELETE_REQUEST_SUCCESS = "The DELETE request was successful."
TOKEN_RETRIEVAL_SUCCESS = "Authentication token retrieved successfully."

# Test Data loaded
TEST_DATA_LOADED = "Test data file found and loaded"

# Alert
ALERT_ACCEPTED = "Delete button clicked and alert accepted."
ALERT_DISMISSED = "Dismissed alert"




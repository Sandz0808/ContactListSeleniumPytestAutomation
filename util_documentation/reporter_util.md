# ReporterUtil Class Documentation

## Overview
The `ReporterUtil` class is a utility for managing reporting and logging of test results during automated testing. It integrates with logging and screenshot utilities to capture logs and screenshots for both passed and failed test cases. The class also interacts with configuration files to dynamically adjust its behavior based on the test settings.

---

## Key Features
- Logs test results based on their status.
- Captures and saves screenshots for both passed and failed test cases.
- Dynamically generates test scenario and test case names from test function names.
- Reads settings from a configuration file to control screenshot capturing behavior.

---

## Dependencies
- `pytest`
- `datetime`
- `conftest.get_current_test_info`
- `utils.config_util.ConfigReader`
- `utils.log_util.LoggingUtility`
- `utils.screenshot_util.ScreenshotUtility`

---

## Initialization
### Constructor
```python
ReporterUtil(driver)
```
**Parameters:**
- `driver` (WebDriver): An instance of Selenium WebDriver passed to the class to capture screenshots during test execution.

---

## Methods
### 1. `results_reporter(log_message, log_level="info", **kwargs)`
**Description:**
Logs the test result message and captures a screenshot based on the test outcome.

**Parameters:**
- `log_message` (str): The message to be logged.
- `log_level` (str): The log level for the message. Default is "info".
- `**kwargs`: Additional keyword arguments to format the log message.

**Behavior:**
- If the log level is `info`, the test is considered passed.
- If the log level is `warning`, `error`, `debug`, or `critical`, the test is considered failed.
- Takes screenshots for both passed and failed tests if the `capture_screenshot` setting is enabled in the configuration file.

**Example Usage:**
```python
reporter = ReporterUtil(driver)
reporter.results_reporter("Test passed successfully.")
reporter.results_reporter("Element not found.", log_level="error")
```

---

### 2. `get_screenshot_datetime()`
**Description:**
Generates a unique name for the screenshot based on the current date and time.

**Returns:**
- `screenshot_name` (str): The formatted screenshot name in the format `screenshot_MMDDYYYY_HHMMSSFFF`.

**Example Usage:**
```python
screenshot_name = reporter.get_screenshot_datetime()
print(screenshot_name)  # Output: screenshot_01052025_101530123
```

---

## Configuration Settings
The `ReporterUtil` class uses the `ConfigReader` utility to read settings from a configuration file. Specifically, it looks for the `screenshot_settings` section to determine if screenshots should be captured.

**Example Configuration:**
```ini
[screenshot_settings]
capture_screenshot = Yes
```

- **`capture_screenshot`**: Set to `Yes` to enable automatic screenshot capture for all test cases.

---

## Error Handling
- Uses the `pytest.fail()` method to fail the test if the log level indicates an error.
- Logs detailed messages with timestamps using the `LoggingUtility` class.

---

## Example Usage in a Test Case
```python
from utils.reporter_util import ReporterUtil

# Initialize WebDriver (example)
driver = webdriver.Chrome()

# Create an instance of ReporterUtil
reporter = ReporterUtil(driver)

# Report a passing test case
reporter.results_reporter("Test passed successfully.")

# Report a failing test case
try:
    element = driver.find_element_by_id("non_existent_id")
except Exception as e:
    reporter.results_reporter(f"Element not found: {e}", log_level="error")
```

---

## Logs and Screenshots
- Logs are generated using the `LoggingUtility` class.
- Screenshots are captured using the `ScreenshotUtility` class and saved with a unique name based on the date and time.

---

## Notes
- Ensure the `ConfigReader`, `LoggingUtility`, and `ScreenshotUtility` utilities are correctly implemented and imported.
- Update your configuration file to match the required settings for the `ReporterUtil` class.
- Handle exceptions during test execution to ensure all errors are logged and reported appropriately.

---

## Author
This utility class is designed to streamline reporting and logging for automation frameworks using Python and Selenium.


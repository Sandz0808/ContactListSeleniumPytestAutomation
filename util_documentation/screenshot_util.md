# ScreenshotUtility Class Documentation

## Overview
The `ScreenshotUtility` class is a utility for managing and organizing screenshot captures during test execution. It automatically creates structured folders for scenarios, test cases, and iterations, making it easy to manage screenshots for reporting and debugging purposes. It also integrates with a logging utility to track screenshot-saving activities.

---

## Key Features
- **Setup of screenshot directories based on test scenarios and test cases.**
- **Automatic folder creation for each test run.**
- **Supports storing screenshots by iteration for data-driven tests.**
- **Logs success and failure messages when saving screenshots.**

---

## Dependencies
- `datetime`
- `os`
- `pathlib`
- `utils.config_util.ConfigReader`
- `utils.exception_message_util`
- `utils.log_message_util`
- `utils.log_util.LoggingUtility`

---

## Initialization
### Constructor
```python
ScreenshotUtility()
```
Upon initialization, the `ScreenshotUtility` class sets the base path for storing screenshots as specified in the configuration file.

---

## Methods

### 1. `setup_folder()`
**Description:**
Sets up the base folder for storing screenshots for the current test run. The folder name includes the current date and time.

**Usage:**
```python
screenshot_util.setup_folder()
```
---

### 2. `create_scenario_folder(scenario: str) -> Path`
**Description:**
Creates a folder for the specified test scenario under the base screenshot folder.

**Parameters:**
- `scenario` (str): The name of the test scenario.

**Returns:**
- A `Path` object pointing to the created scenario folder.

**Usage:**
```python
scenario_folder = screenshot_util.create_scenario_folder("LoginTests")
```
---

### 3. `create_testcase_folder(scenario: str, test_case: str, iteration: int = 0) -> Path`
**Description:**
Creates a folder for the specified test case under the given scenario folder. Supports creating subfolders for iterations if specified.

**Parameters:**
- `scenario` (str): The name of the test scenario.
- `test_case` (str): The name of the test case.
- `iteration` (int): The iteration number for data-driven tests (optional).

**Returns:**
- A `Path` object pointing to the created test case folder.

**Usage:**
```python
test_case_folder = screenshot_util.create_testcase_folder("LoginTests", "ValidLogin", 1)
```
---

### 4. `save_screenshot(driver, scenario: str, test_case: str, filename: str, iteration: int = 0)`
**Description:**
Saves a screenshot to the appropriate folder based on the scenario, test case, and iteration. It uses Selenium's `save_screenshot` method.

**Parameters:**
- `driver`: The Selenium WebDriver instance used to capture the screenshot.
- `scenario` (str): The name of the test scenario.
- `test_case` (str): The name of the test case.
- `filename` (str): The filename for the screenshot.
- `iteration` (int): The iteration number for data-driven tests (optional).

**Usage:**
```python
screenshot_util.save_screenshot(driver, "LoginTests", "ValidLogin", "screenshot_12345", 1)
```

**Exception Handling:**
If the screenshot cannot be saved, an error message is logged using the `LoggingUtility` class.

---

## Folder Structure Example
```
logs/
  └── 20250114_Screenshots/
      └── LoginTests/
          └── ValidLogin/
              └── Iteration_1/
                  └── screenshot_01142025_123456789.png
```
---

## Configuration
Ensure that the `screenshot_folder` path is defined in your configuration file under the `paths` section. Example:
```ini
[paths]
screenshot_folder = screenshots
```

---

## Logs and Messages
The class logs success and failure messages when saving screenshots using the `LoggingUtility` class. The following log messages are used:
- **`SCREENSHOT_MESSAGE`**: Logged when a screenshot is successfully saved.
- **`SCREENSHOT_SAVING_EXCEPTION_MESSAGE`**: Logged when an error occurs while saving a screenshot.

---

## Example Usage
```python
from selenium import webdriver
from utils.screenshot_util import ScreenshotUtility

# Initialize WebDriver and ScreenshotUtility
driver = webdriver.Chrome()
screenshot_util = ScreenshotUtility()

# Save a screenshot
screenshot_util.save_screenshot(driver, "LoginTests", "ValidLogin", "screenshot_12345")
```


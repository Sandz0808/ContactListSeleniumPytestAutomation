# ElementWaitUtil

## Overview
The `ElementWaitUtil` class provides utility methods to wait for web elements to become visible during Selenium test execution. It helps in handling dynamic web content by ensuring that elements are loaded and visible before interacting with them.

## Requirements
- Python 3.x
- Selenium WebDriver
- `utils` package containing:
  - `ConfigReader`
  - `ReporterUtil`
  - `log_message_util`
  - `exception_message_util`

Ensure that `config.toml` is properly configured to include the `element_visibility_timeout` setting.

## Methods

### 1. `__init__(self, driver)`
**Description:**
Initializes the `ElementWaitUtil` class with the WebDriver instance.

**Parameters:**
- `driver`: Selenium WebDriver instance.

---

### 2. `wait_element_to_be_visible(self, locator)`
**Description:**
Waits for a web element to become visible on the page within the timeout specified in the configuration.

**Parameters:**
- `locator`: A tuple specifying the strategy to locate the element (e.g., `(By.ID, 'element_id')`).

**Returns:**
- The web element if it becomes visible within the timeout period.

**Error Handling:**
- If the element is not visible within the timeout period, a `TimeoutException` is raised, and an error message is logged using `ReporterUtil`.

---

## Example Usage
```python
from selenium import webdriver
from utils.element_wait_util import ElementWaitUtil
from selenium.webdriver.common.by import By

# Initialize the WebDriver and ElementWaitUtil
driver = webdriver.Chrome()
element_wait_util = ElementWaitUtil(driver)

# Open a web page
driver.get("https://example.com")

# Wait for an element to be visible
locator = (By.ID, "submit_button")
submit_button = element_wait_util.wait_element_to_be_visible(locator)

# Perform an action after the element is visible
if submit_button:
    submit_button.click()

# Close the browser
driver.quit()
```

## Error Reporting
The class utilizes `ReporterUtil` to log messages and errors:
- **Success:** Logs a message when the element is successfully found and visible.
- **TimeoutException:** Logs an error message if the element is not visible within the specified timeout period.

## Configuration
The visibility timeout value is read from the `config.toml` file using the `ConfigReader` utility.

Example `config.toml`:
```toml
[settings]
element_visibility_timeout = 10
```

## Dependencies
- `ConfigReader`: Utility to read values from a configuration file.
- `ReporterUtil`: Utility to log test execution reports.
- `log_message_util`: Contains message templates for logging.
- `exception_message_util`: Contains error message templates.


# ElementAssertionUtil

The `ElementAssertionUtil` is a utility class designed to help automate the process of asserting web elements during Selenium tests. It provides methods to verify element attributes, retrieve element attributes, and validate the current URL. This utility integrates with existing logging and reporting modules to provide comprehensive feedback on test execution.

---

## Table of Contents
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Class Structure](#class-structure)
- [Methods](#methods)
- [Example Usage](#example-usage)
- [Error Handling](#error-handling)

---

## Dependencies
The `ElementAssertionUtil` relies on the following utility modules:
- `ElementWaitUtil`: Handles element wait conditions.
- `ReporterUtil`: Logs test results.
- `log_message_util`: Contains log messages used in reporting.
- `exception_message_util`: Contains exception-related messages.

Make sure these modules are available in your project.

---

## Installation
1. Clone the repository.
2. Ensure the `utils` directory contains the required utility modules.
3. Install Selenium if not already installed:
   ```bash
   pip install selenium
   ```

---

## Class Structure
The `ElementAssertionUtil` class is initialized with a Selenium `WebDriver` instance and provides the following methods:

### **Initialization**
```python
class ElementAssertionUtil:
    def __init__(self, driver):
        self.driver = driver
        self.reporter = ReporterUtil(driver)
        self.wait_util = ElementWaitUtil(driver)
```
- **driver**: The Selenium WebDriver instance.
- **reporter**: An instance of `ReporterUtil` to log results.
- **wait_util**: An instance of `ElementWaitUtil` to handle element waits.

---

## Methods
### 1. `assert_element_attribute(locator, attribute, expected_attribute_value)`
**Description:** Verifies that a web element's attribute matches the expected value.

**Parameters:**
- `locator` (tuple): Locator of the web element (e.g., `(By.ID, 'username')`).
- `attribute` (str): The attribute to verify (e.g., `"value"`).
- `expected_attribute_value` (str): The expected value of the attribute.

**Example:**
```python
element_assertion.assert_element_attribute((By.ID, 'username'), 'placeholder', 'Enter your username')
```

### 2. `get_element_attribute(locator, attribute)`
**Description:** Retrieves the value of a web element's attribute.

**Parameters:**
- `locator` (tuple): Locator of the web element.
- `attribute` (str): The attribute to retrieve.

**Returns:**
- The value of the specified attribute.

**Example:**
```python
placeholder_text = element_assertion.get_element_attribute((By.ID, 'username'), 'placeholder')
```

### 3. `assert_url(expected_url)`
**Description:** Asserts that the current URL matches the expected URL.

**Parameters:**
- `expected_url` (str): The expected URL.

**Example:**
```python
element_assertion.assert_url('https://example.com/dashboard')
```

---

## Example Usage
Below is an example of how to use the `ElementAssertionUtil` in a test:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.element_assertion_util import ElementAssertionUtil

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get('https://example.com/login')

# Initialize the ElementAssertionUtil
element_assertion = ElementAssertionUtil(driver)

# Assert the placeholder attribute of a username field
element_assertion.assert_element_attribute((By.ID, 'username'), 'placeholder', 'Enter your username')

# Get and print the placeholder text
placeholder_text = element_assertion.get_element_attribute((By.ID, 'username'), 'placeholder')
print(f"Placeholder text: {placeholder_text}")

# Assert the current URL
element_assertion.assert_url('https://example.com/login')

# Close the WebDriver
driver.quit()
```

---

## Error Handling
The `ElementAssertionUtil` handles assertion errors and logs the results using `ReporterUtil`. The following messages are used:
- `ELEMENT_ASSERTION_MESSAGE`: For successful element attribute assertions.
- `ASSERTION_EXCEPTION_ERROR_MESSAGE`: For failed assertions.
- `ELEMENT_ATTRIBUTE_MESSAGE`: For successful retrieval of an element's attribute.
- `ELEMENT_ATTRIBUTE_EXCEPTION_MESSAGE`: For errors encountered while retrieving an attribute.
- `URL Assertion Passed`: For successful URL assertions.
- `URL Assertion Failed`: For failed URL assertions.

Ensure these message constants are properly defined in `log_message_util` and `exception_message_util` to avoid runtime errors.

---

## Conclusion
The `ElementAssertionUtil` is a powerful utility that simplifies element assertions in Selenium tests. It integrates with existing reporting and logging modules to provide clear feedback on test execution. By using this utility, QA engineers can ensure their web elements behave as expected during automated tests.


# ElementKeyboardInputUtil

## Overview
`ElementKeyboardInputUtil` is a utility class designed for automating keyboard input actions on web elements using Selenium WebDriver. This utility provides methods to input text into fields and clear existing text, ensuring robust and reliable interactions with web elements.

---

## Requirements

Before using `ElementKeyboardInputUtil`, ensure you have the following:

- Python 3.8+
- Selenium
- The following utility classes in your project:
  - `ElementWaitUtil`
  - `ReporterUtil`
  - `log_message_util`
  - `exception_message_util`

---

## Installation

1. Clone the repository containing the utility classes.
2. Install the necessary dependencies:

```bash
pip install selenium
```

3. Ensure your project structure includes the required utility classes in the `utils` directory.

---

## Class Methods

### `__init__(self, driver)`
Initializes the class with a WebDriver instance.

**Parameters:**
- `driver`: The WebDriver instance used to interact with the web browser.

---

### `input_element(self, locator, input_value)`
Inputs a specified value into an element located by the given locator after ensuring the element is visible.

**Parameters:**
- `locator`: The locator (e.g., XPath, CSS selector) to find the web element.
- `input_value`: The value to be entered into the element.

**Usage Example:**
```python
from selenium import webdriver
from utils.element_keyboard_input_util import ElementKeyboardInputUtil

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Initialize the utility class
keyboard_util = ElementKeyboardInputUtil(driver)

# Input text into a username field
keyboard_util.input_element("//input[@id='username']", "test_user")
```

**Error Handling:**
If an error occurs during input, it is logged using the `ReporterUtil` class.

---

### `clear_element(self, locator)`
Clears the existing value in an element located by the given locator after ensuring the element is visible.

**Parameters:**
- `locator`: The locator (e.g., XPath, CSS selector) to find the web element.

**Usage Example:**
```python
# Clear text from a password field
keyboard_util.clear_element("//input[@id='password']")
```

**Error Handling:**
If an error occurs during clearing, it is logged using the `ReporterUtil` class.

---

## Example Usage

```python
from selenium import webdriver
from utils.element_keyboard_input_util import ElementKeyboardInputUtil

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Initialize the utility class
keyboard_util = ElementKeyboardInputUtil(driver)

# Input text into a username field
keyboard_util.input_element("//input[@id='username']", "test_user")

# Clear text from a password field
keyboard_util.clear_element("//input[@id='password']")

# Close the browser
driver.quit()
```

---

## Error Reporting
Error messages are reported through the `ReporterUtil` class, which logs actions and exceptions during interactions with web elements. Ensure that `log_message_util` and `exception_message_util` are properly configured in your project.

---

## Additional Notes
- Always ensure that the locators used in the methods are accurate and match the elements on the web page.
- Utilize appropriate wait mechanisms to handle dynamic web elements and reduce flakiness in tests.


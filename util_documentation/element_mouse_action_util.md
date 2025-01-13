# ElementMouseActionsUtil

## Overview
`ElementMouseActionsUtil` is a utility class designed to handle mouse-based interactions with web elements using Selenium WebDriver. The class provides methods to click elements and handle alert pop-ups efficiently during automated browser testing.

---

## Requirements

Before using `ElementMouseActionsUtil`, ensure you have the following:

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

### `click_element(self, locator)`
Clicks on a web element specified by the locator after ensuring it is visible.

**Parameters:**
- `locator`: The locator (e.g., XPath, CSS selector) to find the web element.

**Usage Example:**
```python
from selenium import webdriver
from utils.element_mouse_actions_util import ElementMouseActionsUtil

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://example.com")

# Initialize the utility class
mouse_util = ElementMouseActionsUtil(driver)

# Click a button on the page
mouse_util.click_element("//button[@id='submit']")
```

**Error Handling:**
If an error occurs during the click action, it is logged using the `ReporterUtil` class.

---

### `click_delete_and_accept_alert(self, locator)`
Clicks on a web element specified by the locator and then accepts an alert pop-up that appears afterward.

**Parameters:**
- `locator`: The locator (e.g., XPath, CSS selector) to find the web element.

**Usage Example:**
```python
# Click a delete button and accept the alert
mouse_util.click_delete_and_accept_alert("//button[@id='delete']")
```

**Error Handling:**
If an error occurs during the alert handling, it is logged using the `ReporterUtil` class.

---

## Example Usage

```python
from selenium import webdriver
from utils.element_mouse_actions_util import ElementMouseActionsUtil

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://example.com")

# Initialize the utility class
mouse_util = ElementMouseActionsUtil(driver)

# Click a button on the page
mouse_util.click_element("//button[@id='submit']")

# Click a delete button and accept the alert
mouse_util.click_delete_and_accept_alert("//button[@id='delete']")

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


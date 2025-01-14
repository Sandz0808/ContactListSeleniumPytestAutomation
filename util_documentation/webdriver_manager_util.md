# WebDriverManager Utility Documentation

## Overview
The `WebDriverManager` class provides a streamlined way to manage browser drivers for Selenium tests. It supports Chrome, Edge, and Safari browsers, automatically downloading and setting up the appropriate drivers for each browser type. This utility simplifies the process of setting up WebDriver instances and ensures compatibility with different operating systems.

---

## Key Features
- Automatically downloads and manages browser drivers using `webdriver_manager`.
- Supports Chrome, Edge, and Safari browsers.
- Handles experimental options and browser preferences.
- Includes error handling for unsupported browsers or operating systems.

---

## Methods

### `__init__(self, browser_type)`
- **Description**: Initializes the WebDriverManager with the specified browser type.
- **Parameters**:
  - `browser_type` (str): The type of browser to use (e.g., "chrome", "edge", "safari").

### `get_driver(self)`
- **Description**: Retrieves the appropriate web driver based on the specified browser type.
- **Returns**:
  - WebDriver instance for the specified browser.
- **Raises**:
  - `ValueError` if the specified browser type is not supported.

### `get_chrome_driver(self)`
- **Description**: Sets up and returns a Chrome WebDriver instance.
- **Returns**:
  - Chrome WebDriver instance.
- **Options Set**:
  - `safebrowsing.enabled`: Enables safe browsing.

### `get_edge_driver(self)`
- **Description**: Sets up and returns an Edge WebDriver instance.
- **Returns**:
  - Edge WebDriver instance.
- **Options Set**:
  - `safebrowsing.enabled`: Enables safe browsing.
  - `excludeSwitches`: Disables automation extensions.
  - `useAutomationExtension`: Prevents the use of automation extensions.

### `get_safari_driver(self)`
- **Description**: Sets up and returns a Safari WebDriver instance. Only supported on macOS.
- **Returns**:
  - Safari WebDriver instance.
- **Special Handling**:
  - Loads cookies from a `cookies.pkl` file if it exists.
- **Raises**:
  - `EnvironmentError` if the operating system is not macOS.

---

## Folder Structure Example
```
project_root/
├── utils/
│   ├── webdriver_manager.py
│   ├── log_util.py
│   ├── config_util.py
│   └── exception_message_util.py
├── tests/
│   ├── test_login.py
│   └── test_search.py
├── logs/
└── screenshots/
```

---

## Example Usage
```python
from utils.webdriver_manager import WebDriverManager

# Initialize the WebDriverManager with the desired browser type
manager = WebDriverManager("chrome")
driver = manager.get_driver()

# Perform browser actions
driver.get("https://www.example.com")

# Close the browser
driver.quit()
```

---

## Error Handling
The `WebDriverManager` class includes error handling for unsupported browsers and operating systems:
- **ValueError**: Raised if an unsupported browser type is provided.
- **EnvironmentError**: Raised if the Safari WebDriver is requested on a non-macOS system.

---

## Dependencies
- `selenium`
- `webdriver_manager`
- `os`
- `pickle`
- `platform`

---

## Logging
The utility uses the `LoggingUtility` class to log messages during driver setup and error handling. Ensure that your logging configuration is correctly set up to capture these logs.


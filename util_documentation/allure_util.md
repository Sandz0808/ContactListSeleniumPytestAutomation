# AllureStepWithAttachment Class

## Overview
The `AllureStepWithAttachment` class is a utility to enhance your automated tests by integrating **Allure Reports** with useful attachments, such as screenshots and API responses. This class leverages context managers to ensure that each test step is logged and any important information is captured automatically.

---

## Features
- Automatically logs test steps to Allure.
- Attaches screenshots on test step failures.
- Attaches API responses (in JSON format) to Allure reports.
- Handles various exceptions during screenshot capturing, ensuring tests are resilient.

---

## Prerequisites
Before using this class, ensure you have the following:

- **Allure**: A framework for generating detailed test reports.
- **Selenium**: For taking screenshots in web automation tests.
- **ConfigReader**: A utility class to read configurations (used to get the file path for API responses).

---

## Installation
Install the required dependencies using:
```bash
pip install allure-pytest selenium
```

---

## How to Use

### 1. Logging Test Steps with Screenshots
Wrap your test steps with the `AllureStepWithAttachment` context manager to automatically log steps and take screenshots on failure.

```python
from utils.allure_util import AllureStepWithAttachment
from selenium import webdriver

driver = webdriver.Chrome()

with AllureStepWithAttachment(driver, "Opening the Home Page"):
    driver.get("https://example.com")
```

### 2. Attaching API Responses
The `attach_response` method allows you to attach API responses to the Allure report.

```python
from utils.allure_util import AllureStepWithAttachment

response_data = {
    "status": 200,
    "message": "Success",
    "data": {"id": 1, "name": "John Doe"}
}

AllureStepWithAttachment.attach_response(response_data)
```

### 3. Handling Screenshots on Failure
The `__exit__` method in the context manager ensures that a screenshot is taken if an exception occurs during the test step.

```python
try:
    with AllureStepWithAttachment(driver, "Filling the Login Form"):
        driver.find_element_by_id("username").send_keys("test_user")
        driver.find_element_by_id("password").send_keys("secure_password")
except Exception as e:
    print(f"Error: {str(e)}")
```

---

## Methods
### `__init__(self, driver, step_description)`
Initializes the context manager with the following parameters:
- `driver`: The Selenium WebDriver instance.
- `step_description`: A string describing the current test step.

### `__enter__(self)`
Starts the Allure step.

### `attach_response(data=None)`
Attaches a JSON response to the Allure report.
- **Parameters**:
  - `data` (dict, optional): The response data to attach. If `None`, it tries to load the data from the response file path specified in the config.

### `__exit__(self, exc_type, exc_val, exc_tb)`
Handles exiting the context manager, including:
- Taking screenshots on test failures.
- Handling different exceptions and attaching relevant error messages to Allure.

---

## Exception Handling
The `__exit__` method includes exception handling to cover various scenarios:
- **WebDriverException**: Captures Selenium-specific errors.
- **IOError**: Handles file-related issues.
- **General Exception**: A fallback for unforeseen errors.

Each error is logged to Allure with appropriate context.

---

## Example Configuration File (`config.ini`)
Make sure your `config.ini` file contains the necessary paths:
```ini
[paths]
response_file_path = ./responses/response.json
```

---

## Best Practices
- Always use descriptive step descriptions when initializing `AllureStepWithAttachment`.
- Ensure that your configuration file paths are correct.
- Handle exceptions gracefully to prevent test failures from being masked.

---

## Common Issues
| Issue                 | Cause                                             | Solution                                  |
|-----------------------|--------------------------------------------------|------------------------------------------|
| Screenshot not attached | WebDriver is not initialized or is `None`        | Ensure `driver` is properly initialized  |
| API response not attached | Incorrect or missing file path in `config.ini`   | Verify the file path in your configuration |
| JSON decoding error   | Malformed JSON in the response file              | Ensure the response file contains valid JSON |

---

## Version History
| Version | Changes                          |
|---------|----------------------------------|
| 1.0.0   | Initial version with core features|
| 1.1.0   | Enhanced exception handling       |

---

## License
This utility is licensed under the **MIT License**.


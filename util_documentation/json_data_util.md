# JsonDataUtil Class Documentation

## Overview
The `JsonDataUtil` class is a utility that provides methods to handle test data stored in a JSON file. It allows for loading, verifying the existence of test data files, and retrieving specific test data using keys. This utility is useful in automation frameworks where test data needs to be dynamically retrieved during test execution.

---

## Key Features
- **Load JSON test data from a file.**
- **Check if the test data file exists in the specified path.**
- **Retrieve specific test data using a key.**
- **Generate logs and reports using custom utilities.**

---

## Dependencies
- `json`
- `os`
- `pathlib`
- `utils.config_util`
- `utils.reporter_util`
- `utils.log_message_util`
- `utils.exception_message_util`

---

## Initialization
### Constructor
```python
JsonDataUtil(driver)
```
**Parameters:**
- `driver` (WebDriver): An instance of Selenium WebDriver passed to the class for reporting purposes.

---

## Configuration
The class reads the path of the test data file from the configuration file using `ConfigReader`. The test data path is defined as:
```python
TESTDATA_PATH = Path(os.getcwd()) / config_reader.get_value('paths', 'test_data_path')
```
Ensure that the path is correctly configured in your `config.ini` file under the `paths` section.

---

## Methods
### 1. `check_testdata_path()`
**Description:**
Checks if the test data file exists in the specified path.

**Returns:**
- `True` if the path exists.
- `False` if the path does not exist.

**Example Usage:**
```python
if json_util.check_testdata_path():
    print("Test data file exists.")
else:
    print("Test data file not found.")
```

---

### 2. `load_data()`
**Description:**
Loads test data from the JSON file if it hasn't been loaded already.

**Returns:**
- A dictionary containing the loaded test data.
- `None` if the file couldn't be loaded.

**Exception Handling:**
- Logs an error if the file does not exist or cannot be read.

**Example Usage:**
```python
json_data = json_util.load_data()
if json_data:
    print("Data loaded successfully.")
else:
    print("Failed to load data.")
```

---

### 3. `get_testdata(test_key)`
**Description:**
Retrieves specific test data using a key from the loaded JSON data.

**Parameters:**
- `test_key` (str): The key to retrieve data from the JSON file.

**Returns:**
- The value associated with the given key.

**Exceptions:**
- Raises `KeyError` if the key is not found in the JSON data.

**Example Usage:**
```python
try:
    valid_login_data = json_util.get_testdata("valid_login")
    print(valid_login_data)
except KeyError as e:
    print(f"Error: {e}")
```

---

## Error Handling
The class uses custom logging and reporting utilities to handle errors:
- `NO_TESTDATA_FILE_EXIST_MESSAGE`: Message logged when the test data file does not exist.
- `NO_TESTDATA_FILE_EXCEPTION_MESSAGE`: Message logged when there is an exception while reading the test data file.
- `TEST_KEY_NOT_FOUND`: Message logged when the requested key is not found in the test data.
- `VALUE_RETRIEVED_MESSAGE`: Message logged when a value is successfully retrieved.

---

## Example Usage
```python
from utils.json_data_util import JsonDataUtil

# Initialize WebDriver (example)
driver = webdriver.Chrome()

# Create an instance of JsonDataUtil
json_util = JsonDataUtil(driver)

# Load test data
json_util.load_data()

# Get specific test data
try:
    valid_login_data = json_util.get_testdata("valid_login")
    print(valid_login_data)
except KeyError as e:
    print(f"Error: {e}")
```

---

## Best Practices
- Ensure the test data path is correctly configured in the configuration file.
- Use meaningful keys in the JSON test data file to make retrieval straightforward.
- Handle exceptions appropriately to avoid test failures due to missing or incorrect test data.

---

## JSON File Structure Example
Here is an example of how your JSON test data file should be structured:
```json
{
  "valid_login": {
    "username": "test_user",
    "password": "secure_password"
  },
  "invalid_login": {
    "username": "invalid_user",
    "password": "wrong_password"
  }
}
```

---

## Logs and Reporting
The class uses the `ReporterUtil` for logging and reporting. Ensure that your `ReporterUtil` class is set up correctly to handle messages passed from the `JsonDataUtil` class.

---

## Notes
- Ensure that the `test_data_path` is correctly specified in your configuration file.
- The test data file should be in JSON format.
- Handle exceptions when calling `get_testdata` to avoid test failures.

---

## Author
This utility class was created to streamline test data management for automation frameworks using Python and Selenium.


# ConfigReader Utility

## Overview
The `ConfigReader` class is a utility designed to handle the reading of configuration files in your automation projects. It simplifies fetching configuration values from a centralized `config.ini` file and stores them in a dictionary for quick access throughout the project.

## Features
- Reads configuration from a `.ini` file.
- Loads configuration values into an easily accessible dictionary.
- Provides methods to fetch specific configuration values.
- Handles errors gracefully if sections or keys are not found in the configuration file.

---

## File Structure
```
project_root/
├── config/
│   └── config.ini
├── utils/
│   └── config_util.py
└── main.py
```

Ensure your `config.ini` file is located under the `config` directory in your project root.

---

## Usage
### Import the ConfigReader
```python
from utils.config_util import ConfigReader
```

### Initialize the ConfigReader
```python
config_reader = ConfigReader()
```

### Fetch a Configuration Value
```python
api_url = config_reader.get_value('API', 'base_url')
print(f"API Base URL: {api_url}")
```

---

## Configuration File Example
Here is an example of how your `config.ini` file should be structured:
```ini
[API]
base_url = https://api.example.com
key = your_api_key_here

[DATABASE]
host = localhost
port = 5432
username = admin
password = secret
```

---

## Class Explanation
### `__init__()`
- Initializes the `ConfigReader` class.
- Checks if the configuration file exists.
- Loads the configuration into a dictionary for quick access.

### `get_config_file_path()`
- Constructs the full path to the `config.ini` file.
- Returns the `Path` object representing the file location.

### `load_config_to_dictionary()`
- Iterates through all sections and keys in the configuration file.
- Loads the values into the `CONFIG_DICT` class attribute.

### `get_value(section, key)`
- Fetches a specific value from the configuration dictionary.
- Throws a `KeyError` if the section or key is not found.

---

## Error Handling
The `ConfigReader` class uses a logging utility (`LoggingUtility`) to provide meaningful error messages:

- **SECTION_NOT_FOUND_ERROR**: Raised when the requested section does not exist in the configuration file.
- **KEY_NOT_FOUND_ERROR**: Raised when the requested key does not exist within the specified section.

### Example Error Handling
```python
try:
    db_host = config_reader.get_value('DATABASE', 'host')
except KeyError as e:
    print(e)
```

---

## Best Practices
- Keep sensitive information such as API keys and database credentials in the `config.ini` file.
- Use `ConfigReader` to centralize your configuration management.
- Ensure the `config.ini` file is not committed to version control to protect sensitive data.

---

## Dependencies
- `configparser`: Built-in Python module for handling `.ini` files.
- `os`: For handling file paths.
- `pathlib`: For modern and flexible path handling.
- `utils.log_util.LoggingUtility`: Custom logging utility for standardized log messages.

---

## Improvements
Consider the following enhancements:
- Adding encryption for sensitive values in the configuration file.
- Introducing environment-specific configurations (e.g., `config_dev.ini`, `config_prod.ini`).
- Implementing a caching mechanism to avoid reading the file multiple times during execution.


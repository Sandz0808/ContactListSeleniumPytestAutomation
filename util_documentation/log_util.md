# LoggingUtility Class Documentation

## Overview
The `LoggingUtility` class is a custom logging utility designed for Python projects, specifically for use with pytest or other automation frameworks. It helps create structured log files, making it easier to debug issues by providing detailed logs with timestamps, log levels, and messages.

---

## Key Features
- Automatically creates log files in a `logs` directory.
- Generates log files with the current date as the filename.
- Supports logging at different levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.
- Formats log messages to include timestamps and log levels.
- Allows dynamic message formatting using templates.

---

## Dependencies
- `datetime`
- `logging`
- `os`
- `pathlib`

---

## Initialization
### Constructor
```python
LoggingUtility()
```
The constructor initializes a logger named `pytest_logger` and sets up a file handler to write log messages to a file. The log files are created in a `logs` directory in the current working directory.

---

## Methods

### 1. `initialize_log_file()`
**Description:**
This method creates the `logs` directory (if it doesn't exist) and initializes a log file with the current date as the filename.

**Returns:**
- The full path to the log file as a `Path` object.

**Example Log Filename:**
```
logs/20250114_logs.txt
```

---

### 2. `get_log_formatted_message(message_template, log_level, **kwargs)`
**Description:**
Formats a log message based on the provided template and logs it at the specified log level.

**Parameters:**
- `message_template` (str): The template for the log message.
- `log_level` (str): The log level (debug, info, warning, error, critical).
- `**kwargs`: Key-value pairs to format the message template dynamically.

**Supported Log Levels:**
- `debug`
- `info`
- `warning`
- `error`
- `critical`

**Example Usage:**
```python
log_util = LoggingUtility()
log_util.get_log_formatted_message("User {username} logged in", "info", username="test_user")
```
**Output in Log File:**
```
2025-01-14 10:00:00 - INFO - User test_user logged in
```

---

## Logs Directory Structure
The log files are stored in a `logs` directory, created automatically in the current working directory. Each log file is named with the current date to keep logs organized.

**Example Directory Structure:**
```
PycharmProjects/
├── Contact_List_App_Selenium_Python/
   └── logs/
      └── 20250114_logs.txt
```

---

## Example Usage
```python
from logging_utility import LoggingUtility

# Initialize the logging utility
log_util = LoggingUtility()

# Log an info message
log_util.get_log_formatted_message("Script started by {user}", "info", user="Sandro")

# Log an error message
log_util.get_log_formatted_message("An error occurred: {error}", "error", error="File not found")
```
**Output in Log File:**
```
2025-01-14 09:00:00 - INFO - Script started by Sandro
2025-01-14 09:05:00 - ERROR - An error occurred: File not found
```

---

## Error Handling
The `LoggingUtility` class handles errors gracefully by ensuring that log files are always created and that logs are written without interruption. It ensures that log levels are properly handled to avoid any mismatches.

---

## Best Practices
- Use descriptive log messages to make debugging easier.
- Ensure the `logs` directory has the appropriate permissions to allow writing log files.
- Utilize different log levels to separate normal operations (INFO) from potential issues (ERROR) and critical problems (CRITICAL).

---

## Notes
- The `initialize_log_file` method ensures that a new log file is created daily, keeping logs organized.
- The utility is flexible and can be used in any Python project that requires structured logging.

---

## Author
This utility was developed to help streamline logging for automation frameworks and improve debugging processes in Python projects.


# Pytest Automation Framework

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Folder Structure](#folder-structure)
- [Running Tests](#running-tests)
- [Reporting and Logs](#reporting-and-logs)
 
## Introduction
Pytest is a powerful, flexible, and open-source testing framework for Python that allows for simple unit tests as well as complex functional testing. It is designed to provide easy test execution and debugging, making it suitable for both small and large projects. Pytest supports fixtures, parameterization, and plugins for enhanced functionality.

## Features
- **Support for multiple test types** (unit, functional, integration)
- **Page Object Model (POM) implementation**
- **Screenshot capture for failed tests**
- **Test data management using json files**
- **Detailed reports and logs for test execution**

## Installation
 **Pre-requisites:**
1. **Install Python**  
    - Download and install Python on the official Python website.
    > https://www.python.org/downloads/ 
2. **Install Selenium via pip**
     - Run the following commands in the terminal to install selenium:
     ```
     pip install selenium
     ```
3. **Verify installations**  
     - Run the following commands in the terminal to confirm that Python is successfully installed:
     ```
     python --version
     pip show selenium
     ```
**Installation Steps:**
 1. **Clone the Repository**

Clone the GitHub repository to your local machine:
```bash
git clone https://github.com/julieocol/ContactListApp_Selenium_Automation
cd your-repo
```
 2. **Set Up a Virtual Environment**
To avoid conflicts with other Python projects, it's recommended to use a virtual environment.

**Create a virtual environment:**
```bash
python -m venv venv 
```
**Activate the virtual environment:**
- On Windows:
```bash
venv\Scripts\activate
```
- On masOS/Linux:
```bash
source venv/bin/activate
```
 3. **Install Poetry**
Poetry is a dependency management tool for Python. To install it, run:
```bash
pip install poetry
```
 4. **Install Project Dependencies**
Once Poetry is installed, use it to install the project dependencies defined in the pyproject.toml file:
```bash
poetry install
```
This will install all necessary dependencies, including:
- pytest
- selenium
- pytest_tagging
- pytest-html
- webdriver-manager
- allure-pytest
- Faker

Modify the following files before running test:
- config.ini file
    * Specify the target environment (e.g., staging, production, dev).
    * Adjust test timeout settings and other pytest-specific configurations as needed.

## Folder Structure
  ```
ContactListApp_Selenium_Automation        # Main Folder Directory
├── config/                               # Environment
├── data_files/                           # API Tokens
├── logs/                                 # Log Files for test execution
├── pages/                                # Page Objects
├── reports/                              # This is where the pytest, allure report and screenshots are saved
    ├── allure_html/                        # This is where index.html is generated
    ├── allure_test_result/                 # Output of the Allure report generation process
    ├── screenshots/                        # screenshots captured on every execution
├── test_data/                            # Test Data for test execution
├── tests/                                # Test scripts
    ├── api/                                # Test scripts for API 
    ├── reusable/                           # Scripts for Reusable Test
    ├── ui/                                 # Test scripts for UI
├── utils/                                # utilities function (API setup, logging text file, take screenshot)
├── conftest.py                           # Initialize and Teardown
├── pyproject.toml                        # configuration file used to customize and control test behavior
├── README.md                             # Project documentation
  ```
## Running Tests
To run all tests, use this command:
```
pytest --env staging
pytest --env prod
pytest --env dev
```

To  run tests in a specific browser, use the following commands:
```
pytest --env staging --browser chrome
pytest --env staging --browser edge
```

To run a specific test scenario, use the following commands:

| **Category** | **Tags**                        | **Description**                                                                                                                  |
|--------------|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| **API**      | `@api_delete_functionality`     | Deletes a specified resource or data from the system.                                                                            |
|              | `@api_edit_functionality`       | Allows modification or update of existing resources.                                                                             |
|              | `@api_management_functionality` | Adds a new contact to the system's contact management database, including storing personal information and contact details.      |
|              | `@api_logout_functionality`     | Logs out a user from the application, terminating their session and invalidating any active tokens or authentication credentials. |
|              | `@api_login_functionality`      | Authenticates a user by verifying their credentials (e.g., username and password) to grant access to the system.                 |
|              | `@api_signup_functionality`     | Registers a new user by creating a new account with necessary details such as email, password, and other required information.   |
| **UI**       | `@ui_login_functionality`       | Handles the user login process in the UI, including validating user credentials and granting access to the application.          |
|              | `@ui_management_functionality`  | Handles the user login process in the UI, including validating user credentials and granting access to the application.          |
|              | `@ui_edit_functionality`        | Allows users to edit existing items or information in the UI, such as updating contact details.                                  |
|              | `@ui_deletion_functionality`    | Enables the deletion of items or data from the UI                                                                                |    

```
pytest --env staging --browser chrome --tags api_delete_functionality
pytest --env staging --browser chrome --tags api_edit_functionality
pytest --env staging --browser chrome --tags api_management_functionality
pytest --env staging --browser chrome --tags api_logout_functionality
pytest --env staging --browser chrome --tags api_login_functionality
pytest --env staging --browser chrome --tags api_signup_functionality
pytest --env staging --browser chrome --tags ui_login_functionality
pytest --env staging --browser chrome --tags ui_management_functionality
pytest --env staging --browser chrome --tags ui_edit_functionality
pytest --env staging --browser chrome --tags ui_deletion_functionality
```

If you want to run a specific test, use:
```
pytest --browser chrome tests\ui\ui_user_login_functionality_tests.py
```

## Reporting and Logs
- reports/allure_test_result: This folder is the output of the Allure report generation process. It contains json files and assets needed to visualize the test results in a web browser. To open the report use the following command:
```
- pytest --alluredir=reports/allure_test_result
- allure serve reports/allure_test_result 
```
- reports/allure_html: This file serves as the main entry point for visualizing the results of your automated tests. It provides a comprehensive and interactive overview of the test execution, offering various insights to help analyze the performance and outcomes of your tests. To update the file on your latest execution run this command:
```
allure generate "reports\allure_test_result" --clean --single-file --output "reports\allure_html"
```
- Logs: 
    * Logs are stored in the logs/ folder.
    * They are generated on every execution with date and time in the format yyyy-mm-dd-hh-mm-ss
- Screenshots: 
    * Screenshots are captured automatically and saved in the report/Screenshots/ folder.
    * A new will be created on every execution and within each run folder, scenario specific folder are created containing respective testcases and steps. 

- **Sample of allure-report**
    - Download the `index.html` using this link:  
      
    - Open downloaded `index.html` in a browser.






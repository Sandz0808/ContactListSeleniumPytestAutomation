import pytest
from configparser import NoOptionError
# Don't remove this unused import, pytest hooks needs to be imported to conftest file so it can be recognized during initialization
from hooks.pytest_hooks import pytest_runtest_call, get_current_test_info
from utils.config_util import ConfigReader
from utils.webdriver_manager_util import WebDriverManager
from utils.log_util import LoggingUtility
from utils.exception_message_util import *


CONFIG_READER = ConfigReader()
LOG = LoggingUtility()


@pytest.fixture(scope="function")
def setup(request, config):
    """Setup fixture that initializes the web driver and opens the specified URL."""
    browser_name = request.config.getoption("--browser")

    driver_manager = WebDriverManager(browser_name)
    driver = driver_manager.get_driver()
    driver.maximize_window()

    try:
        normalized_env = config.lower()
        url = CONFIG_READER.get_value(f'{normalized_env}', 'url')
    except NoOptionError as e:
        raise Exception(LOG.get_log_formatted_message(SETUP_ERROR, "error"))

    driver.get(url)
    request.cls.driver = driver
    yield

    driver.close()
    driver.quit()


def pytest_addoption(parser):
    """Adds command-line options for environment and web browser selection."""
    parser.addoption("--env", action="store", default="staging", help="Environment to run tests (staging, prod, dev)")
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests (chrome, safari)")


@pytest.fixture(scope="session")
def config(request):
    """Fixture to retrieve the environment option for the session."""
    return request.config.getoption("--env")


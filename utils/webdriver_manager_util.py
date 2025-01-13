import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utils.log_util import LoggingUtility
from utils.exception_message_util import *
import pickle
import platform
from selenium.webdriver.safari.options import Options

class WebDriverManager:
    def __init__(self, browser_type):
        lower_browser = browser_type.lower()
        self.browser_type = lower_browser
        self.log = LoggingUtility()

    def get_driver(self):
        """Retrieves the appropriate web driver based on the specified browser type."""
        if self.browser_type == "chrome":
            return self.get_chrome_driver()
        elif self.browser_type == "edge":
            return self.get_edge_driver()
        elif self.browser_type == "safari":
            return self.get_safari_driver()
        else:
            raise ValueError(self.log.get_log_formatted_message(VALUE_DRIVER_ERROR, "error"))

    def get_chrome_driver(self):
        """Sets up and returns Chrome WebDriver."""
        options = webdriver.ChromeOptions()
        prefs = {
            "safebrowsing.enabled": True,
        }
        # options.add_experimental_option("prefs", prefs)
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


    def get_edge_driver(self):
        """Sets up and returns Edge WebDriver."""
        options = webdriver.EdgeOptions()
        prefs = {
            "safebrowsing.enabled": True,
        }
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

    def get_safari_driver(self):
        """Sets up and returns Safari WebDriver."""
        if platform.system() == "Darwin":  # Check if the OS is macOS
            options = Options()
            options.private = False
            options.add_argument("--enable-save-password-bubble")
            driver = webdriver.Safari(options=options)
            if os.path.exists('cookies.pkl'):
                with open('cookies.pkl', 'rb') as file:
                    cookies = pickle.load(file)
                    for cookie in cookies:
                        driver.add_cookie(cookie)

            return driver

        else:
            raise EnvironmentError(self.log.get_log_formatted_message(ENVIRONMENT_ERROR, "error"))

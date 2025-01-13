import configparser
import os
from utils.log_util import LoggingUtility
from pathlib import Path
from utils.exception_message_util import *


class ConfigReader:
    CONFIG_FILE_EXISTS = False
    CONFIG_FILE_PATH = None
    CONFIG_DICT = {}

    def __init__(self):
        if not ConfigReader.CONFIG_FILE_EXISTS:  # Check once for existence
            ConfigReader.CONFIG_FILE_PATH = ConfigReader.get_config_file_path()
            ConfigReader.CONFIG_FILE_EXISTS = ConfigReader.CONFIG_FILE_PATH.exists()
            if not ConfigReader.CONFIG_FILE_EXISTS:
                return

        self.config = configparser.ConfigParser()
        self.config.read(ConfigReader.CONFIG_FILE_PATH)
        self.load_config_to_dictionary()
        self.log = LoggingUtility()

    @staticmethod
    def get_config_file_path():
        """Constructs and returns the full path to the configuration file."""
        return Path(os.getcwd()) / "config" / "config.ini"

    def load_config_to_dictionary(self):
        """Loads configuration values into a dictionary."""
        for section in self.config.sections():
            ConfigReader.CONFIG_DICT[section] = {key: self.config.get(section, key)
                                                 for key in self.config.options(section)}

    def get_value(self, section, key):
        """
        Method to get a value from the configuration dictionary.
        :param section: Section name in the configuration dictionary.
        :param key: Key name whose value needs to be retrieved.
        :return: Value associated with the specified key in the given section.
        """
        if section not in ConfigReader.CONFIG_DICT:
            raise KeyError(self.log.get_log_formatted_message(SECTION_NOT_FOUND_ERROR, "error", section=section))

        if key not in ConfigReader.CONFIG_DICT[section]:
            raise KeyError(self.log.get_log_formatted_message(KEY_NOT_FOUND_ERROR, "error", key=key, section=section))

        return ConfigReader.CONFIG_DICT[section][key]



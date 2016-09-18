""" config for the application

Configuration variables and methods to read settings from a file.

"""


import configparser


# pylint: disable=R0903
class Config:
    """Configuration for the application.

    Reads the configuration from a file (Default options.txt)
    """

    def __init__(self, file_path="options.txt"):
        self.config_file_path = file_path

        config_parser = configparser.ConfigParser()

        if not config_parser.read(self.config_file_path, encoding='utf-8'):
            print('[config] configuration file not found.')
            return

        self.token = config_parser.get('required', 'token')
        self.prefix = config_parser.get('optional', 'prefix', fallback='!')

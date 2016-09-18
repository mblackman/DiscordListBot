import sys
import os
import configparser

class config:
    def __init__(self, file_path):
        self.config_file_path = file_path

        config = configparser.ConfigParser()

        if not config.read(self.config_file_path, encoding='utf-8'):
            print('[config] configuration file not found.')
            set_to_default()
            return

        self.token = config.get('required', 'token')
        self.prefix = config.get('optional', 'prefix', fallback='!')

class configDefaults:
    token = None
    command_prefix = '!'

# -*- coding: utf-8 -*-
"""
Handles config input parsing and creating a class to store all the information.\n
It's one solution that I currently find better than just trying to have configparser everywhere.
"""
import os
import sys
import logging
import configparser
from configparser import ConfigParser

from .auxiliaryfuncs import _v_print

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

SEIYUU_NAMES = ('inami_anju', 'saito_shuka', 'aida_rikako', 'kobayashi_aika', 'takatsuki_kanako',
                'suzuki_aina', 'suwa_nanaka', 'komiya_arisa', 'furihata_ai')
DEFAULT_CONFIG_PATH = os.path.join(os.getenv('APPDATA'), 'anicration', 'config.txt')
def _str_parser(str_list, seperator=',', strip=True, pop_check=False):
    """Converts a sets of inputs with a common seperator. strip applies `str.strip()` to all values
    It can also list.pop() the last variable if it's empty(enable it with `pop_check`)"""
    if str_list is None:
        print('Error : ' + str_list + ' is empty.')
        return None
    split_list = str_list.split(seperator)
    # Perform strip() for all values
    if strip is True:
        for (idx, name) in enumerate(split_list):
            split_list[idx] = name.strip()
    # Remove all empty values(for dangling commas)
    while split_list[len(split_list)-1] == '' and pop_check is True:
        split_list.pop()
    else:
        return split_list

class ConfigHandler():
    def __init__(self, config_file=None):
        config = ConfigParser()
        if config_file is None:
            if not os.path.exists(DEFAULT_CONFIG_PATH):
                print('Default config file does not exist. Exiting program..')
                sys.exit(1)
            else:
                config.read(DEFAULT_CONFIG_PATH)
        else:
            config.read(config_file)
        self._config = config
        self.twitter_usernames = _str_parser(config['TWITTER']['twitter_usernames'], pop_check=True)

        # [Seiyuu Twitter]
        self.verbosity = config.getint('Seiyuu Twitter', 'verbosity')
        self.data_in_pic_loc = config.getboolean('Seiyuu Twitter', 'data_loc_in_pic_folder')
        self.parser = config.getboolean('Seiyuu Twitter', 'parser')
        self.downloader = config.getboolean('Seiyuu Twitter', 'downloader')
        self.no_config = config.getboolean('Seiyuu Twitter', 'config')

        try:
            self.items = config.getint('Seiyuu Twitter', 'items')
        except ValueError:
            self.items = 0

    @property
    def twitter_id_loc(self):
        _twitter_id_loc = dict()
        for (idx, key) in enumerate(self._config['Twitter Usernames'].keys()):
            value = [x for x in self._config['Twitter Usernames'].values()][idx]
            try:
                _twitter_id_loc[value] = self._config['Picture Save Location'][key]
            except KeyError as err:
                _v_print(
                    "Parameter 'picture save location' for",
                    err, 'not found. Defaulting to None.',
                    verbosity='WARN', level=logger.warning
                )
                _twitter_id_loc[self._config['Twitter Usernames'][key]] = None
            else:
                _v_print(
                    'Sucessfully obtained', key, 'with value', value,
                    verbosity=2, level=logger.debug)
        return _twitter_id_loc

    def _print_id_loc(self):
        for (username, address) in self.twitter_id_loc:
            print(username, address)

    @property
    def keys_from_args(self):
        """For determining if auth_keys is obtained from config or input **kwargs."""
        return self._config.getboolean('AUTHENTICATION', 'keys_from_args')

    @property
    def auth_keys(self):
        """Authentication keys for Tweepy(Twitter's API)"""
        return _str_parser(self._config['AUTHENTICATION']['keys'])

    @property
    def json_loc(self):
        """Path to save Twitter API's response json files."""
        return self._config['PATHS']['json_save_location'].strip()

    @property
    def log_loc(self):
        """Saves log or parsed links."""
        return self._config['PATHS']['log_save_location'].strip()

    @property
    def pic_loc(self):
        """Path to save the downloaded pictures."""
        return self._config['PATHS']['picture_save_location'].strip()

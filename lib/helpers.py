#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Helper functions that are shared across different custom libraries.
"""

import configparser
from colors import red


try:
    CONFIG_PARSER = configparser.ConfigParser()
    CONFIG_PARSER.read("database.config")
except configparser.Error as error:
    print(red("[!] Could not open the database.config file -- make sure it exists and is readable."))
    print(red("L.. Details: {}".format(error)))

def config_section_map(section):
    """This function helps by reading a config file section and returning a dictionary object
    that can be referenced for configuration settings.
    """
    try:
        section_dict = {}
        # Parse the config file's sections into options
        options = CONFIG_PARSER.options(section)
        # Loop through each option
        for option in options:
            # Get the section and option and add it to the dictionary
            section_dict[option] = CONFIG_PARSER.get(section, option)
            if section_dict[option] == -1:
                print("[-] Skipping: {}".format(option))

        # Return the dictionary of settings and values
        return section_dict
    except configparser.Error as error:
        print(red("[!] There was an error with: {}".format(section)))
        print(red("L.. Details: {}".format(error)))

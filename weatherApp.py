# weatherApp.py

from configparser import ConfigParser

def _get_api_key():
    # Fetch the API key from the config file.
    # Gets a config file from secrets.ini
    # ini format is [openweather] [api_key]

    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]
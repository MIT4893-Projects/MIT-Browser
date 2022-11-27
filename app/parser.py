"""Python module to parse application's files"""

import json

def get_config() -> dict:
    """Read `config.json` and return a dict from it

    Returns:
        dict: parsed dictionary store config settings
    """
    with open("config.json", encoding="utf-8") as json_file:
        json_data = json.loads(json_file.read())
    return json_data

def get_stylesheet() -> dict:
    """Read `pyqt5.css` and return a str from it

    Returns:
        str: string store stylesheet
    """
    with open("pyqt5.css", encoding="utf-8") as style_file:
        return style_file.read()

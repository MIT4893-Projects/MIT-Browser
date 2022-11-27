"""Python module to parse application's files"""

import json
import re

def get_config(file_path) -> dict:
    """Read file_path and return a dict from it

    Args:
        file_path: str
    Returns:
        dict: parsed dictionary store config settings
    """
    with open(file_path, encoding="utf-8") as json_file:
        json_data = json.loads(json_file.read())
    return json_data

def get_stylesheet(file_path) -> dict:
    """Read file_path and return a str from it

    Args:
        file_path: str
    Returns:
        str: string store stylesheet
    """
    with open("pyqt5.css", encoding="utf-8") as style_file:
        return style_file.read()

def have_URL_schema(url):
    ""
    schemas = (
        "http://",
        "https://"
    )
    for schema in schemas:
        if url.startswith(schema):
            return True
    return False

def is_valid_url(url):
    regex = re.compile(
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)

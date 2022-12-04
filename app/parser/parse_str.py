"""Application's submodule to parse strings, check string consistent"""

import re

def add_url_schema(url) -> str:
    """Add URL schema if url didn't have schema"""
    schemas = (
        "http://",
        "https://"
    )
    for schema in schemas:
        if url.startswith(schema):
            return url
    return "http://" + url

def is_valid_url(url):
    """Check URL without schema is valid

    Args:
        url (str): input URL

    Returns:
        bool: check url is valid
    """
    regex = re.compile(
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)

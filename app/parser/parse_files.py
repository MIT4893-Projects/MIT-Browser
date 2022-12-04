"""Python module to parse application's files"""

import json


class Parser:
    """Class to parse files and store it"""
    __stylesheet : str
    __config : dict[str: str]

    def __init__(self):
        self.__stylesheet = ""
        self.__config = {}

    @property
    def config(self):
        """__config getter"""
        return self.__config

    @config.setter
    def config(self, file_path):
        """Read file_path and set __config to file data

        Args:
            file_path: str
        """
        with open(file_path, encoding="utf-8") as json_file:
            self.__config = json.loads(json_file.read())

    @property
    def stylesheet(self):
        """__stylesheet getter"""
        return self.__stylesheet

    @stylesheet.setter
    def stylesheet(self, file_path):
        """Read file_path and set __stylesheet to file data

        Args:
            file_path: str
        """
        with open(file_path, encoding="utf-8") as style_file:
            self.__stylesheet = style_file.read()

if __name__ == "__main__":
    parser = Parser()
    parser.config = "./../config.json"
    parser.stylesheet = "./../style.css"

    print(parser.config)
    print(parser.stylesheet)

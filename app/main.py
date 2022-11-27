"""
Main Python file for Browser Window
"""

import os
import sys
from PySide2 import (
    QtCore as QtC,
    QtWidgets as QtW,
    QtWebEngineWidgets as QtWEW
)



class Browser(QtW.QMainWindow):
    """Browser class for render HTML and browse webs

    Inherit:
        PySide2.QtWebEngineWidgets.QWebEngineView
    """

    __webview : QtWEW.QWebEngineView
    __frame_main : QtW.QFrame

    def __init__(self):
        super().__init__()

        self.__webview = QtWEW.QWebEngineView()
        self.__frame_main = QtW.QFrame()

        self.connect_methods()
        self.load_ui()
        self.option()

    def connect_methods(self):
        """Connect methods to trigger when event occur"""

        def update_window_title():
            """Update the window title when the page load finished"""
            self.setWindowTitle(self.__webview.page().title())

        self.__webview.urlChanged.connect(update_window_title)
        self.__webview.loadFinished.connect(update_window_title)

    def load_ui(self):
        """Create and add widgets to main window"""
        self.__frame_main.setLayout(QtW.QGridLayout())
        self.__frame_main.layout().setSpacing(0)
        self.__frame_main.layout().setMargin(0)
        self.__frame_main.layout().addWidget(self.__webview)

        self.setCentralWidget(self.__frame_main)

    def option(self):
        """Set options for main window"""
        self.__webview.load(QtC.QUrl("https://bing.com"))

        self.show()
        self.showMaximized()





def get_absolute_path(path):
    """Return absolute path from relative path

    Args:
        path (str): your relative path

    Returns:
        str: your absolute path
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), path))


if __name__ == "__main__":
    app = QtW.QApplication(sys.argv)

    web_view = Browser()

    app.exec_()

"""
Main Python file for Browser Window
"""

import parser
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

    class URLBar(QtW.QFrame):
        """Create an widget stands for URL bar in browser

        Inherit:
            PySide2.QtWidgets.QFrame
        """

        __last_url : str
        __button_back : QtW.QToolButton
        __button_next : QtW.QToolButton
        __button_reload : QtW.QToolButton
        __lineedit_urlbar : QtW.QLineEdit
        __parent_window : QtW.QMainWindow

        def __init__(self, parent_window):
            super().__init__()

            self.__last_url = ""
            self.__parent_window = parent_window

            self.setMinimumHeight(32)
            self.setObjectName("url-frame")
            self.setStyleSheet(STYLESHEET)

            self.setLayout(QtW.QHBoxLayout())
            self.layout().setMargin(1)
            self.layout().setSpacing(1)
            self.setSizePolicy(QtW.QSizePolicy(QtW.QSizePolicy.Expanding, QtW.QSizePolicy.Fixed))

            # Create and configure buttons
            self.__button_back = QtW.QToolButton()
            self.__button_next = QtW.QToolButton()
            self.__button_reload = QtW.QToolButton()
            for button, name, clicked in (
                (self.__button_back, "btn-back", self.forward),
                (self.__button_next, "btn-next", self.back),
                (self.__button_reload, "btn-reload", self.reload)
            ):
                button.clicked.connect(clicked)
                button.setObjectName(name)
                button.setMinimumWidth(30)
                button.setSizePolicy(QtW.QSizePolicy.Minimum, QtW.QSizePolicy.Expanding)
                button.setStyleSheet(STYLESHEET)
                self.layout().addWidget(button)

            # Create URL bar
            self.__lineedit_urlbar = QtW.QLineEdit()
            self.__lineedit_urlbar.setSizePolicy(
                QtW.QSizePolicy.Expanding, QtW.QSizePolicy.Expanding)
            self.__lineedit_urlbar.setTextMargins(10, 0, 0, 0)
            self.__lineedit_urlbar.returnPressed.connect(self.go_to_site)
            self.__lineedit_urlbar.setObjectName("urlbar")
            self.__lineedit_urlbar.setStyleSheet(STYLESHEET)
            self.layout().addWidget(self.__lineedit_urlbar)

        def go_to_site(self):
            """Load site when press ENTER or RETURN at __lineedit_urlbar"""
            self.__parent_window.load(self.__lineedit_urlbar.text())

        def set_urlbar_text(self, text):
            """Set urlbar text when site changed"""
            self.__lineedit_urlbar.setText(text.strip())
            self.__last_url = text.strip()

        def get_last_url(self):
            """Return self.__last_url"""
            return self.__last_url

        def back(self):
            """Call parent window to go to the last site"""
            self.__parent_window.webview().back()

        def forward(self):
            """Call parent window to go to the next site"""
            self.__parent_window.webview().next()

        def reload(self):
            """Call parent window to reload the current site"""
            self.__parent_window.webview().reload()

    # Attrs:
    __webview : QtWEW.QWebEngineView
    __frame_main : QtW.QFrame
    __urlbar : URLBar

    def __init__(self):
        super().__init__()

        self.__webview = QtWEW.QWebEngineView()
        self.__frame_main = QtW.QFrame()
        self.__urlbar = self.URLBar(self)

        self.connect_methods()
        self.load_ui()
        self.option()

    def connect_methods(self):
        """Connect methods to trigger when event occur"""

        def update_window_title(_q=None):
            """Update the window title when the page load finished"""
            self.setWindowTitle(self.__webview.page().title())
            self.__urlbar.set_urlbar_text(self.__webview.page().url().toString())

        self.__webview.urlChanged.connect(update_window_title)
        self.__webview.loadFinished.connect(update_window_title)

    def load_ui(self):
        """Create and add widgets to main window"""

        self.__frame_main.setLayout(QtW.QGridLayout())
        self.__frame_main.layout().setSpacing(0)
        self.__frame_main.layout().setMargin(0)
        self.__frame_main.layout().addWidget(self.__urlbar)
        self.__frame_main.layout().addWidget(self.__webview)

        self.setCentralWidget(self.__frame_main)

    def option(self):
        """Set options for main window"""

        # Default URL when start browser
        self.__webview.load(QtC.QUrl(CONFIG["homepage"]))

        self.show()

    def load(self, url:str):
        """Load site url

        Args:
            url (str): site's URL to load
        """

        # if don't have any changes on URL bar
        if url == self.__urlbar.get_last_url():
            return

        # if URL not valid, call search engine
        if not parser.is_valid_url(url):
            web_view.load(
                CONFIG["search-engine"][CONFIG["default-search-engine"]]
                    .format(url).replace(" ", "+"))
            return

        url = parser.add_url_schema(url)

        self.__webview.load(QtC.QUrl(url))

    def webview(self):
        """Return self.__webview"""
        return self.__webview




def get_absolute_path(path):
    """Return absolute path from relative path

    Args:
        path (str): your relative path

    Returns:
        str: your absolute path
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), path))


if __name__ == "__main__":
    STYLESHEET = parser.get_stylesheet("style.css")
    CONFIG = parser.get_config("config.json")

    app = QtW.QApplication(sys.argv)

    web_view = Browser()

    app.exec_()

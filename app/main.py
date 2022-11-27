"""
Main Python file for Browser Window
"""

import os
import sys
from PySide2 import (
    QtCore as QtC,
    QtGui as QtG,
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

        __button_back : QtW.QToolButton
        __button_next : QtW.QToolButton
        __lineedit_urlbar : QtW.QLineEdit

        def __init__(self):
            super().__init__()

            self.setMinimumHeight(32)
            self.setObjectName("url-frame")
            self.setStyleSheet(STYLESHEET)

            self.setLayout(QtW.QHBoxLayout())
            self.layout().setMargin(1)
            self.layout().setSpacing(1)
            self.setSizePolicy(QtW.QSizePolicy(QtW.QSizePolicy.Expanding, QtW.QSizePolicy.Fixed))

            self.__button_next = QtW.QToolButton()
            self.__button_back = QtW.QToolButton()
            self.__button_next.setIcon(QtG.QIcon('./assets/icons/next-arrow.png'))
            self.__button_back.setIcon(QtG.QIcon('./assets/icons/back-arrow.png'))
            self.__button_back.setMinimumWidth(30)
            self.__button_next.setMinimumWidth(30)
            self.__button_back.setSizePolicy(QtW.QSizePolicy.Minimum, QtW.QSizePolicy.Minimum)
            self.__button_next.setSizePolicy(QtW.QSizePolicy.Minimum, QtW.QSizePolicy.Minimum)
            self.__button_back.setObjectName("btn-back")
            self.__button_next.setObjectName("btn-next")
            self.__button_back.setStyleSheet(STYLESHEET)
            self.__button_next.setStyleSheet(STYLESHEET)
            self.layout().addWidget(self.__button_back)
            self.layout().addWidget(self.__button_next)

            self.__lineedit_urlbar = QtW.QLineEdit()
            self.__lineedit_urlbar.setSizePolicy(
                QtW.QSizePolicy.Expanding, QtW.QSizePolicy.Expanding)
            self.__lineedit_urlbar.setTextMargins(10, 0, 0, 0)
            self.__lineedit_urlbar.editingFinished.connect(self.go_to_site)
            self.__lineedit_urlbar.setObjectName("urlbar")
            self.__lineedit_urlbar.setStyleSheet(STYLESHEET)
            self.layout().addWidget(self.__lineedit_urlbar)

        def go_to_site(self):
            """Load site when press ENTER or RETURN at __lineedit_urlbar"""
            web_view.load(self.__lineedit_urlbar.text())

        def set_urlbar_text(self, text):
            """Set urlbar text when site changed"""
            self.__lineedit_urlbar.setText(text)

    __webview : QtWEW.QWebEngineView
    __frame_main : QtW.QFrame
    __urlbar : URLBar

    def __init__(self):
        super().__init__()

        self.__webview = QtWEW.QWebEngineView()
        self.__frame_main = QtW.QFrame()
        self.__urlbar = self.URLBar()

        self.connect_methods()
        self.load_ui()
        self.option()

    def connect_methods(self):
        """Connect methods to trigger when event occur"""

        def update_window_title(_q=None):
            """Update the window title when the page load finished"""
            self.setWindowTitle(self.__webview.page().title())
            print(_q)
            if _q:
                self.__urlbar.set_urlbar_text(_q.toString())

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
        self.__webview.load(QtC.QUrl("https://bing.com"))

        self.show()




def get_absolute_path(path):
    """Return absolute path from relative path

    Args:
        path (str): your relative path

    Returns:
        str: your absolute path
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), path))


if __name__ == "__main__":
    with open("pyqt5.css", encoding="utf-8") as stylesheet_file:
        STYLESHEET = stylesheet_file.read()

    app = QtW.QApplication(sys.argv)

    web_view = Browser()

    app.exec_()

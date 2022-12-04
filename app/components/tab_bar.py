"""Generate and configure tab bar with URL bar and buttons"""

from PySide6 import (
    QtWidgets as QtW,
    QtWebEngineWidgets as QtWEW,
    QtCore as QtC
)


class UrlBar(QtW.QFrame):
    """Create and modify url bar for tab bar

    Inherit:
        Pyside6.QtWidgets.QFrame
    """

    # Attrs:
    __stylesheet : str
    __urlbar : QtW.QLineEdit
    __button_back : QtW.QToolButton
    __button_forward : QtW.QToolButton
    __button_reload : QtW.QToolButton

    def __init__(self):
        super().__init__()

        self.__stylesheet = ""
        self.__urlbar = QtW.QLineEdit()
        self.__button_back = QtW.QToolButton()
        self.__button_forward = QtW.QToolButton()
        self.__button_reload = QtW.QToolButton()

        self.__init_ui()
        self.__init_options()

    def __init_ui(self):
        """Place widgets to url bar"""

        self.setLayout(QtW.QHBoxLayout())

        for widget, position, name in (
            (self.__button_back, 0, "btn-next"),
            (self.__button_forward, 1, "btn-back"),
            (self.__button_reload, 2, "btn-reload"),
            (self.__urlbar, 3, "url-bar")
        ):
            self.layout().addWidget(widget, position)
            widget.setObjectName(name)

    def __init_options(self):
        """Configure widgets with some options"""

        self.layout().setContentsMargins(4, 4, 4, 4)
        self.layout().setSpacing(4)
        
        self.setSizePolicy(QtW.QSizePolicy.Policy.Expanding, QtW.QSizePolicy.Policy.Fixed)


class Tab(QtW.QFrame):
    """Create and modify tab for tab bar

    Inherit:
        Pyside6.QtWidgets.QFrame
    """

    # Attrs:
    __webview : QtWEW.QWebEngineView

    def __init__(self, webview=QtWEW.QWebEngineView):
        super().__init__()

        self.__webview = webview

        self.__init_ui()
        self.__init_options()

    def __init_ui(self):
        """Place widgets inside tab"""
        self.setLayout(QtW.QVBoxLayout())

        self.layout().addWidget(UrlBar())
        self.layout().addWidget(self.__webview)

    def __init_options(self):
        """Configure widgets with some options"""
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)


class TabBar(QtW.QFrame):
    """Create and modify tab bar

    Inherit:
        Pyside6.QtWidgets.QFrame
    """

    # Attrs:
    __tabbar : QtW.QTabWidget
    __stylesheet : str

    def __init__(self, stylesheet):
        super().__init__()

        # Define attributes
        self.__tabbar = QtW.QTabWidget()
        self.__stylesheet = stylesheet

        # Configure object
        self.__init_ui()
        self.__init_options()

    def __init_ui(self):
        """Place widgets to tab bar"""

        # Set layouts
        self.setLayout(QtW.QGridLayout())

        # Add tab and urlbar
        self.layout().addWidget(self.__tabbar, 1, 0, 1, 1)

    def __init_options(self):
        """Configure widgets with some options"""

        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        self.setStyleSheet(self.__stylesheet)
        self.__tabbar.setStyleSheet(self.__stylesheet + "width: ")

    def add_tab(self, widget, name):
        """Add a new tab with widget and name

        Args:
            widget (PySide6.QtWidgets.QWidget): widget to add to new tab
            name (str): name of the new tab
        """
        print(self.__tabbar.tabBar().expanding())
        idx = self.__tabbar.addTab(Tab(widget), name)
        self.__tabbar.tabBar().tabInserted(idx)

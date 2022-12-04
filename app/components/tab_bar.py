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

        for widget, name in (
            (self.__button_back, "btn-back"),
            (self.__button_forward, "btn-forward"),
            (self.__button_reload, "btn-reload"),
            (self.__urlbar, "url-bar")
        ):
            self.layout().addWidget(widget)
            widget.setObjectName(name)
            widget.setStyleSheet(self.__stylesheet)

    def __init_options(self):
        """Configure widgets with some options"""

        self.layout().setContentsMargins(4, 4, 4, 4)
        self.layout().setSpacing(4)

        self.__urlbar.setTextMargins(10, 0, 10, 0)
        self.__urlbar.editingFinished.connect(self.cursor_at_first)

        self.setSizePolicy(QtW.QSizePolicy.Policy.Expanding, QtW.QSizePolicy.Policy.Fixed)

    def cursor_at_first(self):
        """Place text cursor at first character of URL bar when unfocus it"""
        self.__urlbar.setCursorPosition(0)

    @property
    def text(self):
        """Get url bar's text"""
        return self.__urlbar.text()

    @text.setter
    def text(self, url: str):
        """Set url bar's text"""
        self.__urlbar.setText(url)



class Tab(QtW.QFrame):
    """Create and modify tab for tab bar

    Inherit:
        Pyside6.QtWidgets.QFrame
    """

    # Attrs:
    __urlbar : UrlBar
    __webview : QtWEW.QWebEngineView

    def __init__(self, webview=QtWEW.QWebEngineView):
        super().__init__()

        self.__webview = webview
        self.__urlbar = UrlBar()

        self.__init_ui()
        self.__init_options()

    def __init_ui(self):
        """Place widgets inside tab"""
        self.setLayout(QtW.QVBoxLayout())

        self.layout().addWidget(self.__urlbar)
        self.layout().addWidget(self.__webview)

    def __init_options(self):
        """Configure widgets with some options"""
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

    def update_url_bar(self, event=None):
        """Update url bar when url changed"""
        if isinstance(event, QtC.QUrl):
            self.__urlbar.text = event.url()
            self.__urlbar.cursor_at_first()

    @property
    def webview(self):
        """Private webview property getter"""
        return self.__webview



class TabBar(QtW.QFrame):
    """Create and modify tab bar

    Inherit:
        Pyside6.QtWidgets.QFrame
    """

    # Attrs:
    __tabbar : QtW.QTabWidget
    __parent : QtW.QMainWindow

    def __init__(self, parent):
        super().__init__()

        # Define attributes
        self.__tabbar = QtW.QTabWidget()
        self.__parent = parent

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

    def add_tab(self, widget, name):
        """Add a new tab with widget and name

        Args:
            widget (PySide6.QtWidgets.QWidget): widget to add to new tab
            name (str): name of the new tab
        """

        tab = Tab(widget)
        index = self.__tabbar.addTab(tab, name)
        tab.webview.urlChanged.connect(tab.update_url_bar)
        tab.webview.loadFinished.connect(lambda: self.update_tab_title(index))
        tab.webview.iconChanged.connect(lambda: self.update_tab_icon(index))

    def update_tab_title(self, index):
        """Update tab title when page loaded"""
        title = self.__tabbar.widget(index).webview.title()
        self.__tabbar.tabBar().setTabText(index, title)
        self.__parent.setWindowTitle(f"{title} - MIT")

    def update_tab_icon(self, index):
        """Update tab icon when page loaded icon"""
        self.__tabbar.tabBar().setTabIcon(index, self.__tabbar.widget(index).webview.icon())

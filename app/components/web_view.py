"""Application's module to generate and configure webview for browser"""

from PySide6 import (
    QtWebEngineWidgets as QtWEW,
    QtWidgets as QtW
)

class WebView(QtWEW.QWebEngineView):
    """Create and modify web view (include HTML, CSS render and JS interpreter)

    Inherit:
        PySide6.QtWebEngineWidgets.QWebEngineView
    """

    # Attrs:
    __last_url : str

    def __init__(self):
        super().__init__()
        self.__last_url = ""

    @property
    def last_url(self) -> str:
        """__last_url's getter"""
        return self.__last_url

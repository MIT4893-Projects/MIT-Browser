"""
Main Python file for Browser Window
"""

import sys
from PySide2 import (
    QtCore as QtC,
    QtWidgets as QtW,
    QtWebEngineWidgets as QtWEW,
    # QtWebChannel as QtWC
)



class Browser(QtWEW.QWebEngineView):
    """Browser class for render HTML and browse webs

    Inherit:
        PySide2.QtWebEngineWidgets.QWebEngineView
    """



if __name__ == "__main__":
    app = QtW.QApplication(sys.argv)

    web_view = QtWEW.QWebEngineView()
    web_view.load(QtC.QUrl("./index.html"))
    web_view.show()

    app.exec_()

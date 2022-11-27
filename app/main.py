"""
Main Python file for Browser Window
"""

import os
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
    def __init__(self):
        pass



if __name__ == "__main__":
    app = QtW.QApplication(sys.argv)

    web_view = Browser()
    web_view.load(QtC.QUrl.fromLocalFile(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
    ))
    web_view.show()

    app.exec_()

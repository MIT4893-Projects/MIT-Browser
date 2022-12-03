"""Temporary main.py file"""

# LIBS
from parser import (
    parse_files,
    parse_str
)
from components import (
    main_window,
    tab_bar,
    web_view
)
from PySide2 import (
    QtWidgets as QtW
)


# CONSTANTS
CONFIG : dict[str: str]
STYLESHEET : str


if __name__ == "__main__":
    parser = parse_files.Parser()

    parser.config = "./config.json"
    parser.stylesheet = "./style.qss"

    CONFIG = parser.config
    STYLESHEET = parser.stylesheet

    app = QtW.QApplication()
    mw = main_window.MainWindow()
    tb = tab_bar.TabBar()
    tb.setStyleSheet(STYLESHEET)

    wv = web_view.WebView()
    wv.load(CONFIG["homepage"])
    tb.add_tab(wv, "New tab")
    mw.add_widget(tb)

    mw.show()
    app.exec_()

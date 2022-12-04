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
from PySide6 import (
    QtWidgets as QtW,
    QtGui as QtG
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
    mw.setStyleSheet(STYLESHEET)
    icon = QtG.QIcon(QtG.QPixmap("./assets/icons/icon.png"))
    mw.setWindowIcon(icon)

    tb = tab_bar.TabBar(mw)
    tb.setStyleSheet(STYLESHEET)

    wv = web_view.WebView()
    tb.add_tab(wv, "A long tab name")
    wv.load(CONFIG["homepage"])
    mw.add_widget(tb)

    mw.show()
    app.exec()

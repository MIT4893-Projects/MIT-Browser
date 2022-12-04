"""Generate and configure main window for browser"""

from PySide6 import (
    QtWidgets as QtW
)

class MainWindow(QtW.QMainWindow):
    """Create and modify main window

    Inherit:
        PySide2.QtWidgets.QMainWindow
    """

    # Attrs:
    __frame_main : QtW.QFrame
    __layout_main : QtW.QGridLayout

    def __init__(self):
        super().__init__()

        self.__frame_main = QtW.QFrame()
        self.__layout_main = QtW.QGridLayout()

        self.setCentralWidget(self.__frame_main)
        self.centralWidget().setLayout(self.__layout_main)

        self.init_options()

    def add_widget(self, widget: QtW.QWidget):
        """Faster way to add widget

        Args:
            widget (Pyside2.QtWidgets.QWidget): widget need to add to main window
        """
        self.centralWidget().layout().addWidget(widget)

    def init_options(self):
        """Configure widgets with some options"""
        self.centralWidget().layout().setContentsMargins(0, 0, 0, 0)
        self.centralWidget().layout().setSpacing(0)

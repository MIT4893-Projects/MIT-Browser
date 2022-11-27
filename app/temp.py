from PySide2 import (
    QtCore as QtC, 
    QtWidgets as QtW,
    QtWebEngineWidgets as QtWEW,
    QtWebChannel as QtWC
)


class Ui_MainWindow(object):
    """Create PyQt MainWindow"""
    def setup_ui(self, MainWindow):
        """Setup UI for MainWindow

        Args:
            MainWindow (QtW.QMainWindow): Your main window
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(889, 834)

        self.centralwidget = QtW.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtW.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.FR_main = QtW.QFrame(self.centralwidget)
        self.FR_main.setFrameShape(QtW.QFrame.StyledPanel)
        self.FR_main.setFrameShadow(QtW.QFrame.Raised)
        self.FR_main.setObjectName("FR_main")
        self.gridLayout.addWidget(self.FR_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslate_ui(MainWindow)
        QtC.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_ui(self, MainWindow):
        _translate = QtC.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    app = QtW.QApplication([])
    
    # main_window = QtW.QMainWindow()
    # Ui_MainWindow().setup_ui(main_window)
    # main_window.show()
    
    web = QtWEW.QWebEngineView()
    web.load(QtC.QUrl("https://youtube.com"))
    web.show()
    
    app.exec_()
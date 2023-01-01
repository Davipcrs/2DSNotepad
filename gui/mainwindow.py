from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem
import sys
from ui.ui_textEditor import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


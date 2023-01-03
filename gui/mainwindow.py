from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem
import sys
from ui.ui_textEditor import Ui_TextEditor
from ui.ui_mainWindow import Ui_MainWindow
from textEditor import TextEditor

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.changeWindow)

    def changeWindow(self):
        self.txt = TextEditor("Teste.txt")
        self.txt.show()



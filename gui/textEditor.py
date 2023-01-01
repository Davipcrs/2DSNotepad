from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem
import sys
from ui.ui_textEditor import Ui_TextEditor

class TextEditor(QMainWindow):
    def __init__(self):
        super(TextEditor, self).__init__()
        self.ui = Ui_TextEditor()
        self.ui.setupUi(self)

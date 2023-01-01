from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem
from ui.ui_textEditor import Ui_TextEditor
from app.main_func import Saving



class TextEditor(QMainWindow):
    def __init__(self):
        super(TextEditor, self).__init__()
        self.ui = Ui_TextEditor()
        self.ui.setupUi(self)

        self.ui.actionSave.clicked.connect()

    def getTextFromEditor(self):
        self.str = self.ui.mainEditor.toPlainText()
        Saving('Teste.txt', self.str)


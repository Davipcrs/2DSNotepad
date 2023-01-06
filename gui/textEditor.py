from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem
from ui.ui_textEditor import Ui_TextEditor
from app.main_func import Saving, controlFile, loadFile
from saveAs import SaveAsDialog



class TextEditor(QMainWindow):
    def __init__(self, path):
        super(TextEditor, self).__init__()
        self.ui = Ui_TextEditor()
        self.ui.setupUi(self)
        self.saveAsDialog = SaveAsDialog()
        self.arqname = None
        self.prevName = path
        self.str = None
        if self.prevName != None:
            self.str = loadFile(self.prevName)
        else:
            pass
        self.ui.mainEditor.setPlainText(self.str)
        self.ui.actionSave.triggered.connect(self.f_getTextFromEditor)

        self.ui.actionSaveAs.triggered.connect(self.f_ActionSaveAs)

    def f_getTextFromEditor(self):
        self.str = self.ui.mainEditor.toPlainText()
        Saving(self.prevName, self.str)

    def f_ActionSaveAs(self):
        self.saveAsDialog.show()
        self.saveAsDialog.ui.ConfirmpushButton.clicked.connect(self.f_getFileName)        

    def f_getFileName(self):
        self.arqname = self.saveAsDialog.ui.lineEdit.text()
        self.saveAsDialog.close()
        self.str = self.ui.mainEditor.toPlainText()
        Saving(self.arqname, self.str)
        controlFile(self.arqname)

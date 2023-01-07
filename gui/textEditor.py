from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem, QCloseEvent
from PySide6.QtCore import Signal
from ui.ui_textEditor import Ui_TextEditor
from app.main_func import Saving, loadFile
from saveAs import SaveAsDialog



    
class TextEditor(QMainWindow):
    wClosed = Signal(bool)
    def __init__(self):
        super(TextEditor, self).__init__()
        self.ui = Ui_TextEditor()
        self.ui.setupUi(self)
        self.saveAsDialog = SaveAsDialog()
        self.arqname = None
        self.prevName = None
        self.str = None
        self.ui.mainEditor.setPlainText(self.str)
        self.ui.actionSave.triggered.connect(self.f_getTextFromEditor)
        self.ui.actionSaveAs.triggered.connect(self.f_ActionSaveAs)

    def f_getTextFromEditor(self):
        if self.prevName == None:
            self.f_ActionSaveAs()
        else:
            self.str = self.ui.mainEditor.toPlainText()
            Saving(self.prevName, self.str)

    def f_ActionSaveAs(self):
        self.saveAsDialog.show()
        self.saveAsDialog.ui.ConfirmpushButton.clicked.connect(self.f_getFileName)    

    def f_getFileName(self):
        self.arqname = self.saveAsDialog.ui.lineEdit.text()
        self.saveAsDialog.close()
        self.str = self.ui.mainEditor.toPlainText()
        self.prevName = self.arqname
        Saving(self.arqname, self.str)

    def passFileName(self, prevname):
        self.prevName = prevname
        if self.prevName != None:
            self.str = loadFile(self.prevName)
        else:
            pass    

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Fechar Janela', 'Tem certeza que vai fechar a janela? Progresso pode ser perdido', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            self.wClosed.emit(event.isAccepted)

            #https://doc.qt.io/qtforpython/tutorials/basictutorial/signals_and_slots.html
            
        else:
	        event.ignore()
        
from PySide6.QtWidgets import QMainWindow, QMessageBox, QLabel, QHBoxLayout
from PySide6.QtCore import Signal
from ui.ui_textEditor import Ui_TextEditor
from app.main_func import saving, loadFile
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

        #Actions
        self.ui.actionSave.triggered.connect(self.f_getTextFromEditor)
        self.ui.actionSaveAs.triggered.connect(self.f_ActionSaveAs)
        self.ui.actionReturn.setText("Desfazer")
        self.ui.actionRFoward.setText("Refazer")
        self.ui.actionReturn.triggered.connect(self.ui.mainEditor.undo)
        self.ui.actionRFoward.triggered.connect(self.ui.mainEditor.redo)
        self.ui.actionClear.triggered.connect(self.ui.mainEditor.clear)
        self.ui.actionClose.triggered.connect(self.closeEvent)

        #StatusBar
        self.currentLineNumLabel = QLabel()
        self.totalLineNumLabel = QLabel()
        self.totalNumCharLabel = QLabel()
        self.ui.statusbar.addPermanentWidget(self.currentLineNumLabel)
        self.ui.statusbar.addWidget(self.totalLineNumLabel)
        self.ui.statusbar.addWidget(self.totalNumCharLabel)
        self.ui.statusbar.show()

        self.ui.mainEditor.textChanged.connect(self.updateTotalLine)
        self.ui.mainEditor.textChanged.connect(self.updateTotalChar)

    def f_getTextFromEditor(self):
        if self.prevName == None:
            self.f_ActionSaveAs()
        else:
            self.str = self.ui.mainEditor.toPlainText()
            saving(self.prevName, self.str)

    def f_ActionSaveAs(self):
        self.saveAsDialog.show()
        self.saveAsDialog.ui.ConfirmpushButton.clicked.connect(self.f_getFileName)
        self.saveAsDialog.ui.CancelpushButton.clicked.connect(self.saveAsDialog.close)

    def f_getFileName(self):
        self.arqname = self.saveAsDialog.ui.lineEdit.text()
        self.saveAsDialog.close()
        self.str = self.ui.mainEditor.toPlainText()
        self.prevName = self.arqname
        saving(self.arqname, self.str)

    def passFileName(self, name):
        print(name)
        self.prevName = name
        if self.prevName != None:
            self.str = loadFile(self.prevName)
            self.ui.mainEditor.setPlainText(self.str)
        else:
            pass    

    def closeEvent(self, event):
        self.saveAsDialog = SaveAsDialog()
        
        if  self.prevName == None or self.ui.mainEditor.toPlainText() != loadFile(self.prevName):
            reply = QMessageBox.question(self, 'Fechar Janela', 'Tem certeza que vai fechar a janela? Existem modificações não salvas.', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
                self.wClosed.emit(event.isAccepted)
            else:
                event.ignore()

        else:
            event.accept()
            self.wClosed.emit(event.isAccepted)

    def updateTotalLine(self):
        self.totalLineNumLabel.setText("Total de Linhas: " + str(self.ui.mainEditor.toPlainText().count("\n") + 1))
        
    def updateTotalChar(self):
        self.totalNumCharLabel.setText("Total de Caracteres: " + str(self.ui.mainEditor.toPlainText().__len__()))

    def updateCurrentLine(self):

        pass
            
        
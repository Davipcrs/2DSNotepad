from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PySide6.QtCore import QAbstractItemModel
from ui.ui_mainWindow import Ui_MainWindow
from textEditor import TextEditor
from app.main_func import loadControlDir

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.changeWindow)
        self.ui.pushButton_2.clicked.connect(self.changeWindowWithLoad)
        self.ui.pushButton.setText("Novo arquivo")
        self.ui.pushButton_2.setText("Carregar arquivo")
        self.model = QStandardItemModel()
        self.ui.listView.setModel(self.model)
        self.filename = None
        self.selectionList = self.ui.listView.selectionModel()
        self.selectionList.selectionChanged.connect(self.getFileNameWithClick)
        self.listviewAddElement()

    def changeWindow(self):
        self.txt = TextEditor(None)
        #self.refreshlist()
        self.txt.wClosed.connect(print('a'))
        self.txt.show()
        
    


    ##Add text to List.
    def listviewAddElement(self):
        #self.model = QAbstractItemModel()
        #self.model.insertColumn()
           
        self.l_str = loadControlDir()

        
        if self.l_str != None:
            for i in self.l_str:
                self.item = QStandardItem(i)
                self.model.appendRow(self.item)
        else:
            pass

    def refreshlist(self):
        if self.l_str.__sizeof__() != loadControlDir().__sizeof__():
            auxint = self.l_str.__sizeof__()
            self.l_str = loadControlDir()
            while auxint < self.l_str.__sizeof__():
                self.item = QStandardItem(self.l_str[auxint])
                self.model.appendRow(self.item)
                auxint = auxint+1

    


    def getFileNameWithClick(self):
        aux_str = self.selectionList.selection().indexes()[0]
        self.filename = aux_str.data()
        

    def changeWindowWithLoad(self):
        self.txt = TextEditor(self.filename)
        self.txt.show()
    

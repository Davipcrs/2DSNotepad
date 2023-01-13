from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PySide6.QtCore import QAbstractItemModel
from ui.ui_mainWindow import Ui_MainWindow
from textEditor import TextEditor
from app.main_func import loadControlDir, loadFile

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
        self.arr = []
        ##TextEditor Events
        self.txt = TextEditor()
        self.txt.wClosed.connect(self.refreshWindow)
        self.txt.wClosed.connect(self.txt.ui.mainEditor.clear)
        self.txt.wClosed.connect(self.show)
        self.txt.ui.actionNew.triggered.connect(self.createNewTextEditor)
        self.ui.label.setText("Quantidade de arquivos: " + str(self.model.rowCount()))
        self.ui.label_2.setText("")
        
        

    def changeWindow(self):
        self.txt.passFileName(None)
        self.txt.show()   
        self.hide()

    def changeWindowWithLoad(self):
        self.txt.passFileName(self.filename)
        self.txt.show()
        self.hide()
    

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

    def refreshWindow(self):
        auxint = self.model.rowCount()
        self.model.removeRows(0, auxint)
        self.listviewAddElement()
        self.ui.label.setText("Quantidade de arquivos: " + str(auxint))

        '''
        print(loadControlDir().__sizeof__())
        print(self.l_str.__sizeof__())
        if self.l_str.__sizeof__() != loadControlDir().__sizeof__():
            auxint = self.l_str.__sizeof__()
            self.l_str = loadControlDir()
            while auxint < self.l_str.__sizeof__():
                self.item = QStandardItem(self.l_str[auxint])
                self.model.appendRow(self.item)
                auxint = auxint+1
        '''
    


    def getFileNameWithClick(self):
        aux_str = self.selectionList.selection().indexes()[0]
        self.filename = aux_str.data()
        self.ui.textBrowser.setText(loadFile(self.filename))

    def createNewTextEditor(self):
        txt = TextEditor()
        self.arr.append(txt)
        self.arr[self.arr.__len__()-1].show()
 

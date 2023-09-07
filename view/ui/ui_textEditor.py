# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'textEditor.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_TextEditor(object):
    def setupUi(self, TextEditor):
        if not TextEditor.objectName():
            TextEditor.setObjectName(u"TextEditor")
        TextEditor.resize(1024, 832)
        self.actionSave = QAction(TextEditor)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSaveAs = QAction(TextEditor)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        self.actionNew = QAction(TextEditor)
        self.actionNew.setObjectName(u"actionNew")
        self.actionClose = QAction(TextEditor)
        self.actionClose.setObjectName(u"actionClose")
        self.actionReturn = QAction(TextEditor)
        self.actionReturn.setObjectName(u"actionReturn")
        self.actionRFoward = QAction(TextEditor)
        self.actionRFoward.setObjectName(u"actionRFoward")
        self.actionClear = QAction(TextEditor)
        self.actionClear.setObjectName(u"actionClear")
        self.centralwidget = QWidget(TextEditor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainEditor = QPlainTextEdit(self.centralwidget)
        self.mainEditor.setObjectName(u"mainEditor")

        self.verticalLayout.addWidget(self.mainEditor)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        TextEditor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TextEditor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        TextEditor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TextEditor)
        self.statusbar.setObjectName(u"statusbar")
        TextEditor.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionReturn)
        self.menuEdit.addAction(self.actionRFoward)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionClear)

        self.retranslateUi(TextEditor)

        QMetaObject.connectSlotsByName(TextEditor)
    # setupUi

    def retranslateUi(self, TextEditor):
        TextEditor.setWindowTitle(QCoreApplication.translate("TextEditor", u"Editor de Texto", None))
        self.actionSave.setText(QCoreApplication.translate("TextEditor", u"Salvar", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("TextEditor", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSaveAs.setText(QCoreApplication.translate("TextEditor", u"Salvar Como", None))
#if QT_CONFIG(shortcut)
        self.actionSaveAs.setShortcut(QCoreApplication.translate("TextEditor", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionNew.setText(QCoreApplication.translate("TextEditor", u"Novo", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("TextEditor", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("TextEditor", u"Fechar", None))
        self.actionReturn.setText(QCoreApplication.translate("TextEditor", u"Voltar", None))
#if QT_CONFIG(shortcut)
        self.actionReturn.setShortcut(QCoreApplication.translate("TextEditor", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionRFoward.setText(QCoreApplication.translate("TextEditor", u"Ir para frente", None))
#if QT_CONFIG(shortcut)
        self.actionRFoward.setShortcut(QCoreApplication.translate("TextEditor", u"Ctrl+Shift+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionClear.setText(QCoreApplication.translate("TextEditor", u"Limpar", None))
#if QT_CONFIG(shortcut)
        self.actionClear.setShortcut(QCoreApplication.translate("TextEditor", u"Ctrl+Alt+Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("TextEditor", u"File", None))
        self.menuSettings.setTitle(QCoreApplication.translate("TextEditor", u"Settings", None))
        self.menuEdit.setTitle(QCoreApplication.translate("TextEditor", u"Edit", None))
    # retranslateUi


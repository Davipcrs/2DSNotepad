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
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

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
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(250, 60))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(250, 60))

        self.horizontalLayout.addWidget(self.pushButton_2)


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
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()

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
        self.pushButton.setText(QCoreApplication.translate("TextEditor", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("TextEditor", u"PushButton", None))
        self.menuFile.setTitle(QCoreApplication.translate("TextEditor", u"File", None))
        self.menuSettings.setTitle(QCoreApplication.translate("TextEditor", u"Settings", None))
        self.menuEdit.setTitle(QCoreApplication.translate("TextEditor", u"Edit", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'saveAsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_SaveAsDialog(object):
    def setupUi(self, SaveAsDialog):
        if not SaveAsDialog.objectName():
            SaveAsDialog.setObjectName(u"SaveAsDialog")
        SaveAsDialog.resize(397, 225)
        self.gridLayout = QGridLayout(SaveAsDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(SaveAsDialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 25))

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(SaveAsDialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.lineEdit)

        self.verticalSpacer = QSpacerItem(80, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ConfirmpushButton = QPushButton(SaveAsDialog)
        self.ConfirmpushButton.setObjectName(u"ConfirmpushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ConfirmpushButton.sizePolicy().hasHeightForWidth())
        self.ConfirmpushButton.setSizePolicy(sizePolicy1)
        self.ConfirmpushButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout.addWidget(self.ConfirmpushButton)

        self.CancelpushButton = QPushButton(SaveAsDialog)
        self.CancelpushButton.setObjectName(u"CancelpushButton")
        sizePolicy1.setHeightForWidth(self.CancelpushButton.sizePolicy().hasHeightForWidth())
        self.CancelpushButton.setSizePolicy(sizePolicy1)
        self.CancelpushButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout.addWidget(self.CancelpushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 1)

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(SaveAsDialog)

        QMetaObject.connectSlotsByName(SaveAsDialog)
    # setupUi

    def retranslateUi(self, SaveAsDialog):
        SaveAsDialog.setWindowTitle(QCoreApplication.translate("SaveAsDialog", u"Salvar Como", None))
        self.label.setText(QCoreApplication.translate("SaveAsDialog", u"Coloque o nome do arquivo:", None))
        self.ConfirmpushButton.setText(QCoreApplication.translate("SaveAsDialog", u"PushButton", None))
        self.CancelpushButton.setText(QCoreApplication.translate("SaveAsDialog", u"PushButton", None))
    # retranslateUi


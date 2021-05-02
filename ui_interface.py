# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceSAPqGK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 393)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(189, 30, 441, 261))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_2.addWidget(self.textEdit)

        self.start_btn = QPushButton(self.frame)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setGeometry(QRect(380, 310, 75, 23))
        self.printbutton = QPushButton(self.frame)
        self.printbutton.setObjectName(u"printbutton")
        self.printbutton.setGeometry(QRect(270, 310, 75, 23))

        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.printbutton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))

    # retranslateUi


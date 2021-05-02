# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Splash_ScreenFAByjQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
                                           "	background-color: rgb(56, 58, 89);\n"
                                           "	color: rgb(220, 220, 220);\n"
                                           "    border-radius:20px;\n"
                                           "\n"
                                           "\n"
                                           "}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 102, 651, 71))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(40, 170, 571, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 250, 611, 31))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
                                       "	color: rgb(200, 200, 200);\n"
                                       "	background-color: rgb(98, 114, 164);\n"
                                       "    border-style:none;\n"
                                       "    border-radius:10px;\n"
                                       "    text-align:center;\n"
                                       "}\n"
                                       "QProgressBar::chunk{\n"
                                       "    border-radius:10px;\n"
                                       "	background-color: qlineargradient(spread:pad, x1:0.023, y1:0.545, x2:1, y2:0.54, stop:0 rgba(170, 85, 255, 255), stop:0.994318 rgba(255, 255, 255, 255));\n"
                                       "\n"
                                       "}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(190, 290, 301, 21))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_loading.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)

    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<strong>MTHANDIZI</strong>", None))
        self.label_description.setText(
            QCoreApplication.translate("SplashScreen", u"<strong>Deaf People can do anything</strong>", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"loading...........", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MthandiziAOZJSz.ui'
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
        MainWindow.resize(800, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMinimumSize(QSize(800, 50))
        self.main_header.setMaximumSize(QSize(16777215, 50))
        self.main_header.setStyleSheet(u"QFrame{\n"
"\n"
"background-color: rgb(0, 85, 127);\n"
"border: none;\n"
"\n"
"}")
        self.main_header.setFrameShape(QFrame.WinPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_bar_container = QFrame(self.main_header)
        self.title_bar_container.setObjectName(u"title_bar_container")
        self.title_bar_container.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.title_bar_container.setFrameShape(QFrame.StyledPanel)
        self.title_bar_container.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.title_bar_container)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 91, 31))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.title_bar_container)


        self.verticalLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setMinimumSize(QSize(800, 420))
        self.main_body.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.main_body)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMinimumSize(QSize(160, 418))
        self.left_side_menu.setMaximumSize(QSize(160, 16777215))
        self.left_side_menu.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"    border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"padding: 5px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"background-color: #000;\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(83, 0, 125);\n"
"\n"
"}")
        self.left_side_menu.setFrameShape(QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.left_side_menu.setLineWidth(1)
        self.speech_text = QPushButton(self.left_side_menu)
        self.speech_text.setObjectName(u"speech_text")
        self.speech_text.setGeometry(QRect(0, 100, 140, 41))
        self.speech_text.setStyleSheet(u"padding-left: 5px;")
        icon = QIcon()
        icon.addFile(u"Images/icons8_Voice_Recognition_50px_3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.speech_text.setIcon(icon)
        self.speech_text.setIconSize(QSize(32, 32))
        self.speech_sign = QPushButton(self.left_side_menu)
        self.speech_sign.setObjectName(u"speech_sign")
        self.speech_sign.setGeometry(QRect(0, 160, 140, 41))
        self.speech_sign.setStyleSheet(u"padding-left: 0px;")
        icon1 = QIcon()
        icon1.addFile(u"Images/icons8_Translator_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.speech_sign.setIcon(icon1)
        self.speech_sign.setIconSize(QSize(32, 32))
        self.sign_text_speech = QPushButton(self.left_side_menu)
        self.sign_text_speech.setObjectName(u"sign_text_speech")
        self.sign_text_speech.setGeometry(QRect(10, 210, 140, 40))
        icon2 = QIcon()
        icon2.addFile(u"Images/icons8_Sign_Language_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sign_text_speech.setIcon(icon2)
        self.sign_text_speech.setIconSize(QSize(36, 36))
        self.audio_text = QPushButton(self.left_side_menu)
        self.audio_text.setObjectName(u"audio_text")
        self.audio_text.setGeometry(QRect(0, 270, 140, 40))
        self.audio_text.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"Images/icons8_Audio_Book_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.audio_text.setIcon(icon3)
        self.audio_text.setIconSize(QSize(32, 32))
        self.pushButton_5 = QPushButton(self.left_side_menu)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 330, 140, 40))
        self.pushButton_5.setStyleSheet(u"padding-left: 5px;")
        icon4 = QIcon()
        icon4.addFile(u"Images/icons8_Print_50px_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.left_side_menu)

        self.center_main_items = QFrame(self.main_body)
        self.center_main_items.setObjectName(u"center_main_items")
        self.center_main_items.setMinimumSize(QSize(579, 418))
        self.center_main_items.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.center_main_items.setFrameShape(QFrame.NoFrame)
        self.center_main_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.center_main_items)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.center_main_items)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(579, 418))
        self.speechtotext = QWidget()
        self.speechtotext.setObjectName(u"speechtotext")
        self.speechtotext.setStyleSheet(u"background-color: rgb(0, 0, 75);\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.speechtotext)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.speechtotext)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 75);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(13, 48, 200);")
        self.label.setPixmap(QPixmap(u"Images/text.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_5.addWidget(self.label)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"\n"
"\n"
"QLabel{\n"
"padding: 5px 10px;\n"
"border:none;\n"
"\n"
"background-color: #000;\n"
"color: #fff;\n"
"}\n"
"")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.time_input_stt = QLineEdit(self.frame)
        self.time_input_stt.setObjectName(u"time_input_stt")
        self.time_input_stt.setStyleSheet(u"\n"
"\n"
"QLineEdit{\n"
"padding: 5px 10px;\n"
"border:none;\n"
"background-color: #000;\n"
"color: #ff0;\n"
"}\n"
"")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.time_input_stt)


        self.verticalLayout_5.addLayout(self.formLayout_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.speech_text_btn = QPushButton(self.frame)
        self.speech_text_btn.setObjectName(u"speech_text_btn")
        self.speech_text_btn.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"    border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"padding: 5px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"background-color: #000;\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(83, 0, 125);\n"
"\n"
"}")

        self.horizontalLayout_9.addWidget(self.speech_text_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)


        self.gridLayout_4.addLayout(self.verticalLayout_5, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 0, 1, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame)

        self.stackedWidget.addWidget(self.speechtotext)
        self.speechtosign = QWidget()
        self.speechtosign.setObjectName(u"speechtosign")
        self.speechtosign.setStyleSheet(u"background-color: rgb(34, 26, 150);")
        self.horizontalLayout_5 = QHBoxLayout(self.speechtosign)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.speechtosign)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 0, 75);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u"Images/388b132886a85831a52d251e2a774867.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_16)

        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"\n"
"\n"
"QLabel{\n"
"padding: 5px 10px;\n"
"border:none;\n"
"\n"
"background-color: #000;\n"
"color: #fff;\n"
"}\n"
"")

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.time_input_sts = QLineEdit(self.frame_2)
        self.time_input_sts.setObjectName(u"time_input_sts")
        self.time_input_sts.setStyleSheet(u"\n"
"\n"
"QLineEdit{\n"
"padding: 5px 10px;\n"
"border:none;\n"
"background-color: #000;\n"
"color: #ff0;\n"
"}\n"
"")

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.time_input_sts)


        self.verticalLayout_9.addLayout(self.formLayout_10)

        self.speech_sign_btn = QPushButton(self.frame_2)
        self.speech_sign_btn.setObjectName(u"speech_sign_btn")
        self.speech_sign_btn.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"    border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"padding: 5px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"background-color: #000;\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(83, 0, 125);\n"
"\n"
"}")

        self.verticalLayout_9.addWidget(self.speech_sign_btn)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")

        self.verticalLayout_9.addLayout(self.horizontalLayout_21)


        self.gridLayout_10.addLayout(self.verticalLayout_9, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.speechtosign)
        self.signtotext = QWidget()
        self.signtotext.setObjectName(u"signtotext")
        self.signtotext.setStyleSheet(u"background-color: rgb(0, 0, 75);")
        self.gridLayout_12 = QGridLayout(self.signtotext)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.signtotext)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.start_camera = QPushButton(self.frame_3)
        self.start_camera.setObjectName(u"start_camera")
        self.start_camera.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"    border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"padding: 5px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"background-color: #000;\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(83, 0, 125);\n"
"\n"
"}")

        self.gridLayout_11.addWidget(self.start_camera, 2, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"Images/family.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_24.addWidget(self.label_3)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_24)


        self.gridLayout_11.addLayout(self.horizontalLayout_23, 1, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_6, 3, 1, 1, 1)


        self.gridLayout_12.addWidget(self.frame_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.signtotext)
        self.audiototext = QWidget()
        self.audiototext.setObjectName(u"audiototext")
        self.audiototext.setStyleSheet(u"background-color: rgb(0, 0, 75);")
        self.horizontalLayout_6 = QHBoxLayout(self.audiototext)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.audiototext)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.play = QPushButton(self.frame_4)
        self.play.setObjectName(u"play")
        self.play.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"    border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"padding: 5px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"background-color: #000;\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(83, 0, 125);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.play, 2, 1, 1, 1)

        self.horizontalSlider = QSlider(self.frame_4)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"QSlider{\n"
"background-color: rgb(0, 0, 75);\n"
"\n"
"}")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider, 1, 0, 1, 4)

        self.open_file = QPushButton(self.frame_4)
        self.open_file.setObjectName(u"open_file")
        self.open_file.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"    border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"padding: 5px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"background-color: #000;\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(83, 0, 125);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.open_file, 2, 0, 1, 1)

        self.stop = QPushButton(self.frame_4)
        self.stop.setObjectName(u"stop")
        self.stop.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"    border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"padding: 5px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"background-color: #000;\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(83, 0, 125);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.stop, 2, 2, 1, 1)

        self.widget_display = QWidget(self.frame_4)
        self.widget_display.setObjectName(u"widget_display")
        self.widget_display.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.widget_display, 0, 0, 1, 4)

        self.print = QPushButton(self.frame_4)
        self.print.setObjectName(u"print")
        self.print.setStyleSheet(u"QFrame{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"    border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"padding: 5px 10px;\n"
"border:none;\n"
"border-radius:10px;\n"
"background-color: #000;\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(83, 0, 125);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.print, 2, 3, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.audiototext)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.center_main_items)

        self.right_side_menu = QFrame(self.main_body)
        self.right_side_menu.setObjectName(u"right_side_menu")
        self.right_side_menu.setMinimumSize(QSize(59, 418))
        self.right_side_menu.setMaximumSize(QSize(59, 16777215))
        self.right_side_menu.setStyleSheet(u"background-color: rgb(0, 0, 75);")
        self.right_side_menu.setFrameShape(QFrame.WinPanel)
        self.right_side_menu.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.right_side_menu)


        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMinimumSize(QSize(800, 30))
        self.main_footer.setMaximumSize(QSize(16777215, 30))
        self.main_footer.setStyleSheet(u"QFrame{\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
"border:none;\n"
"}")
        self.main_footer.setFrameShape(QFrame.WinPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.main_footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"MTHANDIZI", None))
        self.speech_text.setText(QCoreApplication.translate("MainWindow", u"Speech-Text", None))
        self.speech_sign.setText(QCoreApplication.translate("MainWindow", u"Speech-Sign", None))
        self.sign_text_speech.setText(QCoreApplication.translate("MainWindow", u"Sign-Text/Speech", None))
        self.audio_text.setText(QCoreApplication.translate("MainWindow", u"Audio-Text", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Print Document", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Translation Time", None))
        self.speech_text_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_5.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Translation Time", None))
        self.speech_sign_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.start_camera.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_3.setText("")
        self.play.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.open_file.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
    # retranslateUi


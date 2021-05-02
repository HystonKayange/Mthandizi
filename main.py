import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QPoint, QRect, QSize,
                            QTime, QUrl, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_Mthandizi import Ui_MainWindow
from speech_text import HYSTON


# Global variable

WINDOW_SIZE = 0


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Mthandizi")
        self.setIcon()

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))

        # STACKED PAGES NAVIGATION
        self.ui.speech_text.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.speechtotext))
        self.ui.speech_sign.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.speechtosign))
        self.ui.sign_text_speech.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.signtotext))
        self.ui.audio_text.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.audiototext))

        # functional buttons
        self.ui.speech_text_btn.clicked.connect(lambda: self.speech_text_btn())
        self.show()

    def restore_or_maximize_window(self):
        global WINDOW_SIZE
        win_status = WINDOW_SIZE

        if win_status == 0:
            WINDOW_SIZE = 1
            self.showMaximized()
        else:
            WINDOW_SIZE == 0
            self.showNormal()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def speech_text_btn(self):
        self.hk = HYSTON()
        Window.hide(self)
        self.hk.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

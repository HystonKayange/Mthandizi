import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QPoint, QRect, QSize,
                            QTime, QUrl, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from main import Window
from ui_Splash_Screen import Ui_SplashScreen


counter = 0


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setIcon()

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QT TIMER==== START===
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        ## TIMER IN MILLISECONDS
        self.timer.start(35)

        # lets try this
        self.ui.label_loading.setText("<strong> WELCOME</strong> TO MY APPLICATION")
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_loading.setText("<strong>LOADING</strong> "
                                                                             "DATASETS"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_loading.setText("<strong>LOADING</strong> "
                                                                             "USER INTERFACE"))

        self.show()

    def progress(self):
        global counter

        ## SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        ## CLOSE THE SCREEN AND OPEN THE APP
        if counter > 100:
            # stop timer
            self.timer.stop()

            # show main window
            self.main = Window()
            self.main.show()

            self.close()

        # increase counter
        counter += 1

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())

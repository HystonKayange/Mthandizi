import sys
import os
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QPoint, QRect, QSize,
                            QTime, QUrl, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtCore import QFileInfo
from PySide2.QtPrintSupport import QPrinter, QPrintPreviewDialog

from ui_interface import Ui_MainWindow


class HYSTON(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Mthandizi")
        self.setIcon()
        self.create_menu()
        self.ui.start_btn.clicked.connect(lambda: self.ui.textEdit.setText("Hello am hyston kayange from blantyre "
                                                                           "i know am not weathly but Lord i have you , "
                                                                           "you make awesome life for me and my family "
                                                                           "you "
                                                                           "you receive all the glory Lord i need you "
                                                                           "more everyday every hour you deseverve "
                                                                           "everything oh God "
                                                                           "be there for me as am doing this project "
                                                                           "amen father God       "))
        self.ui.printbutton.clicked.connect(self.clear)
        self.show()


    def create_menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        viewMenu = mainMenu.addMenu('View')
        editMenu = mainMenu.addMenu('Edit')
        fontMenu = mainMenu.addMenu('Font')
        helpMenu = mainMenu.addMenu('Help')

        openAction = QAction(QIcon('open.png'), "Open", self)
        openAction.setShortcut('Ctrl+O')

        saveAction = QAction(QIcon('save.png'), "Save", self)
        saveAction.setShortcut('Ctrl+S')

        exitAction = QAction(QIcon('exit.png'), "Exit", self)
        exitAction.setShortcut('Ctrl+X')

        previewAction = QAction(QIcon('printpreview.png'), "Print Preview", self)

        exitAction.triggered.connect(self.exit_app)

        previewAction.triggered.connect(self.print_preview_dialog)

        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)

        viewMenu.addAction(previewAction)

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)
    def exit_app(self):
        self.close()

    def print_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)

        previewDialog.paintRequested.connect(self.print_preview)
        previewDialog.exec_()

    def print_preview(self, printer):
        self.ui.textEdit.print_(printer)

    def clear(self):
        self.ui.textEdit.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HYSTON()
    sys.exit(app.exec_())

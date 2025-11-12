# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1073, 724)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid pink;\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 5px;\n"
"	padding: 10px 10px;\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));\n"
"}\n"
"#centralwidget {\n"
"	background-color: rgb(0, 0, 0);}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.DocumentView = QGraphicsView(self.centralwidget)
        self.DocumentView.setObjectName(u"DocumentView")
        self.DocumentView.setGeometry(QRect(10, 10, 551, 521))
        self.DocumentView.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.DocumentView.setStyleSheet(u"QGraphicsView {\n"
"	border: 3px solid pink;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	padding: 10px 10px;\n"
"}")
        self.ExcelTable = QTableWidget(self.centralwidget)
        self.ExcelTable.setObjectName(u"ExcelTable")
        self.ExcelTable.setGeometry(QRect(580, 190, 481, 251))
        self.ExcelTable.setStyleSheet(u"QTableWidget {\n"
"	border: 3px solid pink;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	padding: 10px 10px;\n"
"}")
        self.AddSelection = QPushButton(self.centralwidget)
        self.AddSelection.setObjectName(u"AddSelection")
        self.AddSelection.setGeometry(QRect(580, 460, 471, 51))
        self.AddSelection.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.Title = QLabel(self.centralwidget)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(570, 10, 461, 181))
        font = QFont()
        font.setFamilies([u"Lucida Sans"])
        font.setPointSize(36)
        font.setBold(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.Title.setFont(font)
        self.Title.setToolTipDuration(1)
        self.Title.setAutoFillBackground(False)
        self.Title.setStyleSheet(u"QLabel {\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));\n"
"}")
        self.Title.setLineWidth(1)
        self.Title.setTextFormat(Qt.TextFormat.RichText)
        self.Title.setScaledContents(True)
        self.Title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Title.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.DocumentView.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0411\u0440\u043e \u0441\u044e\u0434\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443 \u0431\u0440\u043e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.DocumentView.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u0411\u0440\u043e \u0441\u044e\u0434\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443 \u0431\u0440\u043e", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.ExcelTable.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0411\u0440\u043e \u0441\u044e\u0434\u0430 \u044d\u043a\u0441\u0435\u043b\u044c \u0444\u0438\u043b\u0435\u0441  \u0431\u0440\u043e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.AddSelection.setText(QCoreApplication.translate("MainWindow", u"Add selection to image", None))
#if QT_CONFIG(tooltip)
        self.Title.setToolTip(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u043f\u0440\u0438\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043d\u0430 \u0431\u043e\u0440\u0442\u0443", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Title.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.Title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff8da1;\">AUTOMATIZATION OF BUSINESS PROCESSES</span></p></body></html>", None))
    # retranslateUi


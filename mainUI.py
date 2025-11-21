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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1437, 861)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid pink;\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 5px;\n"
"	padding: 10px 10px;\n"
"	color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));\n"
"	\n"
"	font: 9pt \"Terminal\";\n"
"}\n"
"#centralwidget {\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(17"
                        "1, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(910, 180, 481, 251))
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"	border: 3px solid pink;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	padding: 10px 10px;\n"
"}")
        self.addSelections = QPushButton(self.centralwidget)
        self.addSelections.setObjectName(u"addSelections")
        self.addSelections.setGeometry(QRect(910, 450, 481, 51))
        self.addSelections.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(920, 0, 461, 171))
        font = QFont()
        font.setFamilies([u"Terminal"])
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setToolTipDuration(1)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"QLabel {\n"
"	\n"
"	\n"
"	\n"
"	font: 700 15pt \"Terminal\";\n"
"}")
        self.label.setLineWidth(1)
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.selectExcel = QPushButton(self.centralwidget)
        self.selectExcel.setObjectName(u"selectExcel")
        self.selectExcel.setGeometry(QRect(910, 510, 481, 51))
        self.selectExcel.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.saveImages = QPushButton(self.centralwidget)
        self.saveImages.setObjectName(u"saveImages")
        self.saveImages.setGeometry(QRect(910, 570, 481, 51))
        self.saveImages.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.addImage = QPushButton(self.centralwidget)
        self.addImage.setObjectName(u"addImage")
        self.addImage.setGeometry(QRect(20, 640, 861, 51))
        self.addImage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ImageLabel = QLabel(self.centralwidget)
        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setGeometry(QRect(18, 35, 861, 581))
        self.ImageLabel.setScaledContents(True)
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
        self.tableWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0411\u0440\u043e \u0441\u044e\u0434\u0430 \u044d\u043a\u0441\u0435\u043b\u044c \u0444\u0438\u043b\u0435\u0441  \u0431\u0440\u043e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.addSelections.setText(QCoreApplication.translate("MainWindow", u"Add selection to image", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u043f\u0440\u0438\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043d\u0430 \u0431\u043e\u0440\u0442\u0443", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">AUTOMATIZATION OF BUSINESS PROCESSES</span></p></body></html>", None))
        self.selectExcel.setText(QCoreApplication.translate("MainWindow", u"Select Excel file", None))
        self.saveImages.setText(QCoreApplication.translate("MainWindow", u"PUSH!! PUSH THIS BUUTTON!!!", None))
        self.addImage.setText(QCoreApplication.translate("MainWindow", u"Add image", None))
        self.ImageLabel.setText("")
    # retranslateUi


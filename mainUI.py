# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Uncompiled.ui'
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
        MainWindow.resize(1414, 654)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"\n"
"QPushButton {\n"
"	border: 2px  solid rgb(100, 255, 218) ;\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	padding: 10px 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"Yu Gothic UIl\";\n"
"}\n"
"#centralwidget {\n"
"	background-color: #0a192f}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(910, 180, 481, 251))
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"	border: 3px solid #64ffda;;\n"
"	background-color: transparent;\n"
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
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setToolTipDuration(1)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"QLabel {\n"
"	\n"
"	\n"
"	\n"
"	;\n"
"	font: 700 32pt \"Yu Gothic UI\";\n"
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
        self.addImage.setGeometry(QRect(20, 570, 861, 51))
        self.addImage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ImageLabel = QLabel(self.centralwidget)
        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setGeometry(QRect(18, 15, 861, 541))
        self.ImageLabel.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1300, 810, 121, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Automatization Of Business Processes", None))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">AUTOMATIZATION OF BUSINESS PROCESSES</span></p></body></html>", None))
        self.selectExcel.setText(QCoreApplication.translate("MainWindow", u"Select Excel file", None))
        self.saveImages.setText(QCoreApplication.translate("MainWindow", u"PUSH!! PUSH THIS BUUTTON!!!", None))
        self.addImage.setText(QCoreApplication.translate("MainWindow", u"Add image", None))
        self.ImageLabel.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">\u042f \u043d\u0435\u043d\u0430\u0432\u0438\u0436\u0443 \u044d\u0442\u043e \u0433\u043e\u0432\u043d\u043e</span></p></body></html>", None))
    # retranslateUi


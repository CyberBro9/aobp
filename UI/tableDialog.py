# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TableDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 300)
        Dialog.setAcceptDrops(False)
        Dialog.setStyleSheet(u"QDialog {\n"
"	background-color: #0a192f\n"
"}\n"
"QTableWidget {\n"
"	border: 3px dashed #2dd4bf;\n"
"	background-color: transparent;\n"
"	border-radius: 10px;\n"
"	padding: 10px 10px;\n"
"}\n"
"QTableWidget::item {\n"
"	background-color: #ffffff;\n"
"	font: 8px \"Inter\";\n"
"	color: #000000\n"
"}\n"
"QTableWidget QHeaderView::section {\n"
"	padding: 2px;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16px \"Inter\"")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 Excel", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412 \u044d\u0442\u043e\u043c \u043e\u043a\u043d\u0435 \u0412\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0441\u0432\u043e\u044e \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0434\u0430\u043d\u043d\u044b\u0445.", None))
    # retranslateUi


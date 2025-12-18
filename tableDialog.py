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
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(521, 288)
        Dialog.setAcceptDrops(False)
        Dialog.setStyleSheet(u"background-color: #0a192f")
        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 50, 481, 221))
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"	border: 3px solid #64ffda;;\n"
"	background-color: transparent;\n"
"	border-radius: 10px;\n"
"	padding: 10px 10px;\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 481, 31))
        font = QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 Excel", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412 \u044d\u0442\u043e\u043c \u043e\u043a\u043d\u0435 \u0412\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0441\u0432\u043e\u044e \u0442\u0430\u0431\u043b\u0438\u0446\u0443 Excel.", None))
    # retranslateUi


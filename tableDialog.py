# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TableDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(521, 288)
        Dialog.setStyleSheet(u"background-color: #0a192f")
        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 20, 481, 251))
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"	border: 3px solid #64ffda;;\n"
"	background-color: transparent;\n"
"	border-radius: 10px;\n"
"	padding: 10px 10px;\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.tableWidget.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u0411\u0440\u043e \u0441\u044e\u0434\u0430 \u044d\u043a\u0441\u0435\u043b\u044c \u0444\u0438\u043b\u0435\u0441  \u0431\u0440\u043e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi


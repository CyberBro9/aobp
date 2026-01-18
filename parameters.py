# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Parameters.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QWidget)

class Ui_Parameters(object):
    def setupUi(self, Parameters):
        if not Parameters.objectName():
            Parameters.setObjectName(u"Parameters")
        Parameters.resize(400, 300)
        Parameters.setStyleSheet(u"\n"
"        QMainWindow {\n"
"        background-color: #0a192f;\n"
"        }\n"
"        QPushButton {\n"
"        border: 2px solid rgb(100, 255, 218);\n"
"        background-color: rgba(100, 255, 218, 0.05);\n"
"        border-radius: 8px;\n"
"        padding: 12px 20px;\n"
"        color: rgb(255, 255, 255);\n"
"        font: bold 12pt \"Yu Gothic UI\";\n"
"        min-height: 45px;\n"
"        }\n"
"        QPushButton:hover {\n"
"        background-color: rgba(100, 255, 218, 0.15);\n"
"        }\n"
"        QPushButton:pressed {\n"
"        background-color: rgba(100, 255, 218, 0.2);\n"
"        }\n"
"        QListWidget {\n"
"        border: 2px solid rgb(100, 255, 218);\n"
"        background-color: rgba(16, 42, 67, 0.6);\n"
"        border-radius: 8px;\n"
"        color: rgb(255, 255, 255);\n"
"        font: 11pt \"Yu Gothic UI\";\n"
"        padding: 5px;\n"
"        }\n"
"        QLabel#ImageLabel {\n"
"        border: 2px dashed rgb(100, 255, 218);\n"
"        border-radius: 8px;\n"
"        back"
                        "ground-color: rgba(16, 42, 67, 0.6);\n"
"        }\n"
"      ")

        self.retranslateUi(Parameters)

        QMetaObject.connectSlotsByName(Parameters)
    # setupUi

    def retranslateUi(self, Parameters):
        Parameters.setWindowTitle(QCoreApplication.translate("Parameters", u"Dialog", None))
    # retranslateUi


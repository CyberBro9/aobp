# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'About.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_About(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 500)
        Dialog.setAcceptDrops(False)
        Dialog.setStyleSheet(u"QDialog {\n"
"	background-color: #F5F7FAf\n"
"}\n"
"QLabel {\n"
"	font: 16px 'Inter';\n"
"	color: #1F2937\n"
"}\n"
"QLabel#label {\n"
"	font: 24px 'Inter';\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
" QPushButton {\n"
"            background-color: rgb(79, 125, 243);\n"
"            border: 1px solid rgb(171, 196, 243);\n"
"            border-radius: 8px;\n"
"            padding: 10px 18px;\n"
"            color: #f1f5f9;\n"
"            font: 500 11pt 'Inter', 'Segoe UI', 'Yu Gothic UI';\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: rgb(105, 136, 248);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: rgb(63, 100, 194);\n"
"        }")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"image: url(:/Assets/aobp.ico)")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0410\u043a\u043a\u0440\u0435\u0434\u0438\u0442\u0430\u0446\u0438\u0438 \u0438 \u0414\u0440\u0443\u0433\u0438\u0435 \u0411\u0443\u043c\u0430\u0433\u0438 \u0434\u043b\u044f \u0411\u0438\u0437\u043d\u0435\u0441\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0440\u0441\u0438\u044f: 2.0.0", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u043f\u043e\u0437\u0438\u0442\u043e\u0440\u0438\u0439 GitHub", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u043d\u043e \u0432 2025 \u0433.", None))
    # retranslateUi


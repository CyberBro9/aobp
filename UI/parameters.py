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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QSlider, QWidget)

class Ui_Parameters(object):
    def setupUi(self, Parameters):
        if not Parameters.objectName():
            Parameters.setObjectName(u"Parameters")
        Parameters.resize(730, 338)
        Parameters.setStyleSheet(u"background-color: #0a192f;\n"
"\n"
"      ")
        self.label = QLabel(Parameters)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 231, 61))
        self.label.setStyleSheet(u"QLabel {\n"
"	font: bold 24pt \"Yu Gothic UI\"; \n"
"	padding: 10px;\n"
"	color: rgb(255, 255, 255)	\n"
"}")
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Parameters)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 411, 61))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: bold 24pt \"Yu Gothic UI\"; \n"
"	padding: 10px;\n"
"	color: rgb(255, 255, 255)	\n"
"}")
        self.changeColor = QPushButton(Parameters)
        self.changeColor.setObjectName(u"changeColor")
        self.changeColor.setGeometry(QRect(260, 30, 331, 51))
        self.changeColor.setStyleSheet(u"background-color: rgba(100, 255, 218, 0.2); border: 3px solid rgb(100, 255, 218); font: bold 14pt \"Yu Gothic UI\"; color: #64ffda;\n"
"        padding: 12px 20px;")
        self.textCenteringOptions = QComboBox(Parameters)
        self.textCenteringOptions.addItem("")
        self.textCenteringOptions.addItem("")
        self.textCenteringOptions.addItem("")
        self.textCenteringOptions.setObjectName(u"textCenteringOptions")
        self.textCenteringOptions.setGeometry(QRect(430, 120, 125, 31))
        self.textCenteringOptions.setMinimumSize(QSize(1, 0))
        self.textCenteringOptions.setStyleSheet(u"background-color: rgba(100, 255, 218, 0.2); border: 3px solid rgb(100, 255, 218); font: bold 14pt \"Yu Gothic UI\"; color: #64ffda;")
        self.textCenteringOptions.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.label_3 = QLabel(Parameters)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 180, 281, 61))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: bold 24pt \"Yu Gothic UI\"; \n"
"	padding: 10px;\n"
"	color: rgb(255, 255, 255)	\n"
"}")
        self.textSize = QSlider(Parameters)
        self.textSize.setObjectName(u"textSize")
        self.textSize.setGeometry(QRect(310, 190, 351, 41))
        self.textSize.setStyleSheet(u"background-color: rgba(100, 255, 218, 0.2); border: 3px solid rgb(100, 255, 218); font: bold 14pt \"Yu Gothic UI\"; color: #64ffda;")
        self.textSize.setMinimum(12)
        self.textSize.setSliderPosition(20)
        self.textSize.setOrientation(Qt.Orientation.Horizontal)
        self.label_4 = QLabel(Parameters)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(669, 190, 61, 40))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	font: bold 18pt \"Yu Gothic UI\"; \n"
"	padding: 10px;\n"
"	color: #64ffda;\n"
"}")
        self.colorShower = QLabel(Parameters)
        self.colorShower.setObjectName(u"colorShower")
        self.colorShower.setGeometry(QRect(600, 30, 54, 51))
        self.colorShower.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.label_5 = QLabel(Parameters)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 260, 351, 61))
        self.label_5.setStyleSheet(u"QLabel {\n"
"	font: bold 24pt \"Yu Gothic UI\"; \n"
"	padding: 10px;\n"
"	color: rgb(255, 255, 255)	\n"
"}")
        self.changeColor_2 = QPushButton(Parameters)
        self.changeColor_2.setObjectName(u"changeColor_2")
        self.changeColor_2.setGeometry(QRect(380, 270, 331, 51))
        self.changeColor_2.setStyleSheet(u"background-color: rgba(100, 255, 218, 0.2); border: 3px solid rgb(100, 255, 218); font: bold 14pt \"Yu Gothic UI\"; color: #64ffda;\n"
"        padding: 12px 20px;")

        self.retranslateUi(Parameters)

        QMetaObject.connectSlotsByName(Parameters)
    # setupUi

    def retranslateUi(self, Parameters):
        Parameters.setWindowTitle(QCoreApplication.translate("Parameters", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Parameters", u"\u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("Parameters", u"\u0426\u0435\u043d\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430:", None))
        self.changeColor.setText(QCoreApplication.translate("Parameters", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.textCenteringOptions.setItemText(0, QCoreApplication.translate("Parameters", u"\u041f\u043e \u0426\u0435\u043d\u0442\u0440\u0443", None))
        self.textCenteringOptions.setItemText(1, QCoreApplication.translate("Parameters", u"\u0421\u043f\u0440\u0430\u0432\u0430", None))
        self.textCenteringOptions.setItemText(2, QCoreApplication.translate("Parameters", u"\u0421\u043b\u0435\u0432\u0430", None))

        self.label_3.setText(QCoreApplication.translate("Parameters", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430:", None))
        self.label_4.setText(QCoreApplication.translate("Parameters", u"20", None))
        self.colorShower.setText("")
        self.label_5.setText(QCoreApplication.translate("Parameters", u"\u0413\u0430\u0439\u0434 \u043f\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435:", None))
        self.changeColor_2.setText(QCoreApplication.translate("Parameters", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u0434\u043b\u044f \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u044f", None))
    # retranslateUi


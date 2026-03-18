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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSlider, QWidget)

class Ui_Parameters(object):
    def setupUi(self, Parameters):
        if not Parameters.objectName():
            Parameters.setObjectName(u"Parameters")
        Parameters.resize(845, 275)
        Parameters.setStyleSheet(u"QDialog {\n"
"	background-color: #0a192f\n"
"}\n"
"QPushButton {\n"
"	background-color: #1e293b;\n"
"    border: 1px solid #3d4044;\n"
"    border-radius: 8px;\n"
"    padding: 10px 18px;\n"
"    color: #f1f5f9;\n"
"    font: 500 11pt 'Inter', 'Segoe UI', 'Yu Gothic UI';\n"
"    min-height: 36px;\n"
"}\n"
"QComboBox {\n"
"	background-color: #1e293b;\n"
"    border: 1px solid #3d4044;\n"
"    border-radius: 8px;\n"
"    padding: 10px 18px;\n"
"    color: #f1f5f9;\n"
"    font: 500 11pt 'Inter', 'Segoe UI', 'Yu Gothic UI';\n"
"    min-height: 36px;\n"
"}\n"
"QSlider {\n"
"	background-color: #1e293b;\n"
"    border: 1px solid #3d4044;\n"
"    border-radius: 8px;\n"
"    min-height: 36px;\n"
"}\n"
"QSlider::sub-page {\n"
"	background-color: rgba(45, 212, 191, 190);\n"
"	border: 4px solid #1e293b;\n"
"	border-radius: 8px;\n"
"}\n"
"QSlider::handle {\n"
"	border: 2px dashed #1e293b;\n"
"	background-color: rgb(45, 212, 191);\n"
"}\n"
"QSlider::handle:hover {\n"
"	border: 3px dashed #1e293b;\n"
"	background-color: #2d"
                        "3a4f;\n"
"}\n"
"QSlider::groove {\n"
"	min-height: 8px;\n"
"}\n"
"      ")
        self.formLayoutWidget = QWidget(Parameters)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 821, 261))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"	font: 24pt \"Inter\"; \n"
"	padding: 10px;\n"
"	color: rgb(255, 255, 255)	\n"
"}")
        self.label.setScaledContents(True)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.colorShower = QLabel(self.formLayoutWidget)
        self.colorShower.setObjectName(u"colorShower")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorShower.sizePolicy().hasHeightForWidth())
        self.colorShower.setSizePolicy(sizePolicy)
        self.colorShower.setBaseSize(QSize(0, 0))
        self.colorShower.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.horizontalLayout.addWidget(self.colorShower)

        self.changeColor = QPushButton(self.formLayoutWidget)
        self.changeColor.setObjectName(u"changeColor")
        self.changeColor.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.changeColor)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 24pt \"Inter\"; \n"
"	padding: 10px;\n"
"	color: rgb(255, 255, 255)	\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textSize = QSlider(self.formLayoutWidget)
        self.textSize.setObjectName(u"textSize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textSize.sizePolicy().hasHeightForWidth())
        self.textSize.setSizePolicy(sizePolicy1)
        self.textSize.setMinimum(12)
        self.textSize.setSliderPosition(20)
        self.textSize.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.textSize)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	font: 18pt \"Inter\"; \n"
"	padding: 10px;\n"
"	color: #2dd4bf;\n"
"}")
        self.label_4.setScaledContents(False)

        self.horizontalLayout_2.addWidget(self.label_4)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 24pt \"Inter\"; \n"
"	padding: 10px;\n"
"	color: rgb(255, 255, 255)	\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.textCenteringOptions = QComboBox(self.formLayoutWidget)
        self.textCenteringOptions.addItem("")
        self.textCenteringOptions.addItem("")
        self.textCenteringOptions.addItem("")
        self.textCenteringOptions.setObjectName(u"textCenteringOptions")
        sizePolicy1.setHeightForWidth(self.textCenteringOptions.sizePolicy().hasHeightForWidth())
        self.textCenteringOptions.setSizePolicy(sizePolicy1)
        self.textCenteringOptions.setMinimumSize(QSize(1, 58))
        self.textCenteringOptions.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.textCenteringOptions)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"	font: 24pt \"Inter\"; \n"
"	padding: 10px;\n"
"	color: rgb(255, 255, 255)	\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.changeColor_2 = QPushButton(self.formLayoutWidget)
        self.changeColor_2.setObjectName(u"changeColor_2")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.changeColor_2)


        self.retranslateUi(Parameters)

        QMetaObject.connectSlotsByName(Parameters)
    # setupUi

    def retranslateUi(self, Parameters):
        Parameters.setWindowTitle(QCoreApplication.translate("Parameters", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Parameters", u"\u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430:", None))
        self.colorShower.setText("")
        self.changeColor.setText(QCoreApplication.translate("Parameters", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Parameters", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430:", None))
        self.label_4.setText(QCoreApplication.translate("Parameters", u"20", None))
        self.label_2.setText(QCoreApplication.translate("Parameters", u"\u0426\u0435\u043d\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430:", None))
        self.textCenteringOptions.setItemText(0, QCoreApplication.translate("Parameters", u"\u041f\u043e \u0446\u0435\u043d\u0442\u0440\u0443", None))
        self.textCenteringOptions.setItemText(1, QCoreApplication.translate("Parameters", u"\u0421\u043f\u0440\u0430\u0432\u0430", None))
        self.textCenteringOptions.setItemText(2, QCoreApplication.translate("Parameters", u"\u0421\u043b\u0435\u0432\u0430", None))

        self.label_5.setText(QCoreApplication.translate("Parameters", u"\u0413\u0430\u0439\u0434 \u043f\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435:", None))
        self.changeColor_2.setText(QCoreApplication.translate("Parameters", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u0434\u043b\u044f \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u044f", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1256, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: #0a192f;\n"
"}\n"
"\n"
" QListWidget {\n"
"            background-color: #1e293b;\n"
"            color: #e2e8f0;\n"
"            font: 11pt 'Inter';\n"
"            padding: 8px;\n"
"        }\n"
"        QPushButton {\n"
"            background-color: #1e293b;\n"
"            border: 1px solid #3d4044;\n"
"            border-radius: 8px;\n"
"            padding: 10px 18px;\n"
"            color: #f1f5f9;\n"
"            font: 500 11pt 'Inter', 'Segoe UI', 'Yu Gothic UI';\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #2d3a4f;\n"
"            border-color: #5eead4;\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #0f172a;\n"
"        }\n"
"        QPushButton#saveImages {\n"
"            background-color: #1e293b;\n"
"            color: #f1f5f9;\n"
"            font-weight: 600;\n"
"			border: 2px dashed #2dd4bf;\n"
"        }\n"
"        QPushButton#saveImages:hover {\n"
"            border: 3px dashed #2dd"
                        "4bf;\n"
"			background-color: #2d3a4f\n"
"        }\n"
"		QPushButton#saveImages:pressed {\n"
"            background-color: #0f172a;\n"
"			border: 2px dashed #2dd4bf\n"
"        }\n"
"        QLabel#ImageLabel {\n"
"            border: 2px dashed #2dd4bf;\n"
"            border-radius: 16px;\n"
"            background-color: #1e293b;\n"
"            color: #94a3b8;\n"
"        }\n"
"        QLabel {\n"
"            color: #f1f5f9;\n"
"            font-family: 'Inter', 'Segoe UI', 'Yu Gothic UI';\n"
"        }\n"
"        QLabel#label {\n"
"            font-size: 14pt;\n"
"            font-weight: 600;\n"
"        }\n"
"        QLabel#selectionsLabel {\n"
"            font-size: 12pt;\n"
"            font-weight: 500;\n"
"            color: #94a3b8;\n"
"        }\n"
"        QStatusBar {\n"
"            background-color: #1e293b;\n"
"            color: #2dd4bf;\n"
"        }\n"
"		QComboBox {\n"
"	background-color: #1e293b;\n"
"    border: 1px solid #3d4044;\n"
"    border-radius: 8px;\n"
"    padding: 10px 1"
                        "8px;\n"
"    color: #f1f5f9;\n"
"    font: 500 11pt 'Inter', 'Segoe UI', 'Yu Gothic UI';\n"
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
"	background-color: #2d3a4f;\n"
"}\n"
"      \n"
"      ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.leftPanel = QVBoxLayout()
        self.leftPanel.setObjectName(u"leftPanel")
        self.ImageLabel = QLabel(self.centralwidget)
        self.ImageLabel.setObjectName(u"ImageLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ImageLabel.sizePolicy().hasHeightForWidth())
        self.ImageLabel.setSizePolicy(sizePolicy1)
        self.ImageLabel.setMinimumSize(QSize(400, 0))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(16)
        self.ImageLabel.setFont(font)
        self.ImageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.leftPanel.addWidget(self.ImageLabel)


        self.mainLayout.addLayout(self.leftPanel)

        self.rightPanel = QVBoxLayout()
        self.rightPanel.setSpacing(6)
        self.rightPanel.setObjectName(u"rightPanel")
        self.rightPanel.setContentsMargins(6, -1, 6, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")

        self.rightPanel.addLayout(self.gridLayout)

        self.selectionsLabel = QLabel(self.centralwidget)
        self.selectionsLabel.setObjectName(u"selectionsLabel")

        self.rightPanel.addWidget(self.selectionsLabel)

        self.selections = QListWidget(self.centralwidget)
        self.selections.setObjectName(u"selections")
        self.selections.setMinimumSize(QSize(0, 200))

        self.rightPanel.addWidget(self.selections)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_4.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.formLayout_4.setHorizontalSpacing(0)
        self.formLayout_4.setVerticalSpacing(0)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Inter\"; \n"
"	padding: 10px;\n"
"	color: rgb(255, 255, 255)	\n"
"}")
        self.label_2.setScaledContents(True)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.colorShower = QLabel(self.centralwidget)
        self.colorShower.setObjectName(u"colorShower")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.colorShower.sizePolicy().hasHeightForWidth())
        self.colorShower.setSizePolicy(sizePolicy3)
        self.colorShower.setBaseSize(QSize(0, 0))
        self.colorShower.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.horizontalLayout_5.addWidget(self.colorShower)

        self.changeColor = QPushButton(self.centralwidget)
        self.changeColor.setObjectName(u"changeColor")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.changeColor.sizePolicy().hasHeightForWidth())
        self.changeColor.setSizePolicy(sizePolicy4)
        self.changeColor.setMinimumSize(QSize(0, 0))
        self.changeColor.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.changeColor)


        self.formLayout_4.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_5)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Inter\"; \n"
"	padding: 10px;\n"
"	color: rgb(255, 255, 255)	\n"
"}")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy5)
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Inter\"; \n"
"	color: #2dd4bf;\n"
"}")
        self.label_1.setScaledContents(False)
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_1)

        self.textSize = QSlider(self.centralwidget)
        self.textSize.setObjectName(u"textSize")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.textSize.sizePolicy().hasHeightForWidth())
        self.textSize.setSizePolicy(sizePolicy6)
        self.textSize.setMinimumSize(QSize(0, 0))
        self.textSize.setAutoFillBackground(False)
        self.textSize.setMinimum(12)
        self.textSize.setSliderPosition(20)
        self.textSize.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_6.addWidget(self.textSize)


        self.formLayout_4.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_6)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	font: 12pt \"Inter\"; \n"
"	padding: 10px;\n"
"	color: rgb(255, 255, 255)	\n"
"}")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.textCenteringOptions = QComboBox(self.centralwidget)
        self.textCenteringOptions.addItem("")
        self.textCenteringOptions.addItem("")
        self.textCenteringOptions.addItem("")
        self.textCenteringOptions.setObjectName(u"textCenteringOptions")
        sizePolicy1.setHeightForWidth(self.textCenteringOptions.sizePolicy().hasHeightForWidth())
        self.textCenteringOptions.setSizePolicy(sizePolicy1)
        self.textCenteringOptions.setMinimumSize(QSize(1, 0))
        self.textCenteringOptions.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.textCenteringOptions)


        self.rightPanel.addLayout(self.formLayout_4)

        self.addSelections = QPushButton(self.centralwidget)
        self.addSelections.setObjectName(u"addSelections")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.addSelections.sizePolicy().hasHeightForWidth())
        self.addSelections.setSizePolicy(sizePolicy7)

        self.rightPanel.addWidget(self.addSelections)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.saveImages = QPushButton(self.centralwidget)
        self.saveImages.setObjectName(u"saveImages")

        self.verticalLayout.addWidget(self.saveImages)


        self.rightPanel.addLayout(self.verticalLayout)


        self.mainLayout.addLayout(self.rightPanel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        self.statusbar.setStyleSheet(u"QProgressBar {\n"
"            border: none;\n"
"            background-color: #1e293b;\n"
"            border-radius: 6px;\n"
"            text-align: center;\n"
"            color: #f1f5f9;\n"
"            font: bold 10pt 'Inter', 'Segoe UI', 'Yu Gothic UI';\n"
"            height: 12px;\n"
"        }\n"
"        QProgressBar::chunk {\n"
"            background-color: #2dd4bf;\n"
"            border-radius: 6px;\n"
"        }")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u043a\u0440\u0435\u0434\u0438\u0442\u0430\u0446\u0438\u0438 (\u0438) \u0414\u0440\u0443\u0433\u0438\u0435 \u0411\u0443\u043c\u0430\u0433\u0438 \u0434\u043b\u044f \u0411\u0438\u0437\u043d\u0435\u0441\u0430", None))
        self.ImageLabel.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043e \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.selectionsLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044f \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430:", None))
        self.colorShower.setText("")
        self.changeColor.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0442\u0435\u043a\u0441\u0442\u0430:", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430:", None))
        self.textCenteringOptions.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0446\u0435\u043d\u0442\u0440\u0443", None))
        self.textCenteringOptions.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u0430", None))
        self.textCenteringOptions.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0432\u0430", None))

        self.addSelections.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u043b\u0435 \u043d\u0430 \u0445\u043e\u043b\u0441\u0442", None))
        self.saveImages.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
    # retranslateUi


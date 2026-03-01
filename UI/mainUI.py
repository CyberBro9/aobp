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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1414, 654)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"		QPushButton {\n"
"        background-color: rgb(20,20,20);\n"
"        border-radius: 8px;\n"
"        padding: 12px 20px;\n"
"        color: rgb(255, 255, 255);\n"
"        font: bold 12pt \"Yu Gothic UI\";\n"
"        min-height: 35px;\n"
"        }\n"
"        QPushButton:hover {\n"
"        background-color: rgb(40,40,40);\n"
"        }\n"
"        QPushButton:pressed {\n"
"        background-color: rgb(80,80,80);\n"
"        }\n"
"        QListWidget {\n"
"        background-color: rgb(20,20,20);\n"
"        border-radius: 8px;\n"
"        color: rgb(255, 255, 255);\n"
"        font: 11pt \"Yu Gothic UI\";\n"
"        }\n"
"        QLabel#ImageLabel {\n"
"		border-radius: 8px;\n"
"        background-color: rgb(20,20,20);\n"
"        }\n"
"		QPushButton#saveImages {\n"
"			border: 2px dashed #0eff93;\n"
"			border-radius: 8px\n"
"		}\n"
"		QMainWindow {\n"
"			background-color: rgb(13, 13, 13)\n"
"		}\n"
"      ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(6, 6, 6, 10)
        self.leftPanel = QVBoxLayout()
        self.leftPanel.setObjectName(u"leftPanel")
        self.ImageLabel = QLabel(self.centralwidget)
        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setMinimumSize(QSize(500, 400))
        font = QFont()
        font.setPointSize(16)
        self.ImageLabel.setFont(font)
        self.ImageLabel.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.ImageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.leftPanel.addWidget(self.ImageLabel)

        self.addImage = QPushButton(self.centralwidget)
        self.addImage.setObjectName(u"addImage")
        icon = QIcon()
        icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addImage.setIcon(icon)

        self.leftPanel.addWidget(self.addImage)


        self.mainLayout.addLayout(self.leftPanel)

        self.rightPanel = QVBoxLayout()
        self.rightPanel.setSpacing(6)
        self.rightPanel.setObjectName(u"rightPanel")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")

        self.rightPanel.addLayout(self.gridLayout)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI"])
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font: bold 13pt \"Yu Gothic UI\"; padding: 2px;\n"
"color: rgb(255, 255, 255)")
        self.label.setTextFormat(Qt.TextFormat.PlainText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.rightPanel.addWidget(self.label)

        self.selectionsLabel = QLabel(self.centralwidget)
        self.selectionsLabel.setObjectName(u"selectionsLabel")
        self.selectionsLabel.setStyleSheet(u"font: bold 14pt \"Yu Gothic UI\"; padding: 5px;\n"
"color: rgb(255, 255, 255)")

        self.rightPanel.addWidget(self.selectionsLabel)

        self.selections = QListWidget(self.centralwidget)
        self.selections.setObjectName(u"selections")

        self.rightPanel.addWidget(self.selections)

        self.controlsGrid = QGridLayout()
        self.controlsGrid.setSpacing(10)
        self.controlsGrid.setObjectName(u"controlsGrid")
        self.addSelections = QPushButton(self.centralwidget)
        self.addSelections.setObjectName(u"addSelections")

        self.controlsGrid.addWidget(self.addSelections, 0, 0, 1, 1)

        self.editSettings = QPushButton(self.centralwidget)
        self.editSettings.setObjectName(u"editSettings")

        self.controlsGrid.addWidget(self.editSettings, 0, 1, 1, 1)

        self.selectExcel = QPushButton(self.centralwidget)
        self.selectExcel.setObjectName(u"selectExcel")

        self.controlsGrid.addWidget(self.selectExcel, 1, 0, 1, 1)

        self.openTableDialog = QPushButton(self.centralwidget)
        self.openTableDialog.setObjectName(u"openTableDialog")

        self.controlsGrid.addWidget(self.openTableDialog, 1, 1, 1, 1)

        self.saveImages = QPushButton(self.centralwidget)
        self.saveImages.setObjectName(u"saveImages")
        self.saveImages.setStyleSheet(u"")

        self.controlsGrid.addWidget(self.saveImages, 2, 0, 1, 2)


        self.rightPanel.addLayout(self.controlsGrid)


        self.mainLayout.addLayout(self.rightPanel)

        self.mainLayout.setStretch(0, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        self.statusbar.setStyleSheet(u"QStatusBar {\n"
"	color: #0eff93; \n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px dashed #0eff93;\n"
"	padding: 1px\n"
"}\n"
"QProgressBar {\n"
"	color: rgb(10, 10, 10)\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: #0eff93;\n"
"	border-radius: 2px\n"
"}")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u043a\u0440\u0435\u0434\u0438\u0442\u0430\u0446\u0438\u0438 (\u0438) \u0414\u0440\u0443\u0433\u0438\u0435 \u0411\u0443\u043c\u0430\u0433\u0438 \u0434\u043b\u044f \u0411\u0438\u0437\u043d\u0435\u0441\u0430", None))
        self.ImageLabel.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043e \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.addImage.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u043a\u0440\u0435\u0434\u0438\u0442\u0430\u0446\u0438\u0438 (\u0438) \u0414\u0440\u0443\u0433\u0438\u0435 \u0411\u0443\u043c\u0430\u0433\u0438 \u0434\u043b\u044f \u0411\u0438\u0437\u043d\u0435\u0441\u0430", None))
        self.selectionsLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044f \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f:", None))
        self.addSelections.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u043b\u0435", None))
        self.editSettings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0438\u0442\u044c...", None))
        self.selectExcel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b Excel", None))
        self.openTableDialog.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043e\u043a\u043d\u043e \u0442\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.saveImages.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
    # retranslateUi


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
    QListWidget, QListWidgetItem, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)
import resources_rc

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
        MainWindow.setStyleSheet(u"\n"
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
"        QListWidget::item {\n"
"        padding: 8px;\n"
"        margin: 2px;\n"
"        border-radius: 4px;\n"
"        }\n"
""
                        "        QListWidget::item:selected {\n"
"        background-color: rgba(100, 255, 218, 0.3);\n"
"        }\n"
"        QLabel#ImageLabel {\n"
"        border: 2px dashed rgb(100, 255, 218);\n"
"        border-radius: 8px;\n"
"        background-color: rgba(16, 42, 67, 0.6);\n"
"        }\n"
"      ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.leftPanel = QVBoxLayout()
        self.leftPanel.setObjectName(u"leftPanel")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.leftPanel.addWidget(self.progressBar)

        self.ImageLabel = QLabel(self.centralwidget)
        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setMinimumSize(QSize(500, 400))
        self.ImageLabel.setStyleSheet(u"color: #8892b0; font: 14pt \"Yu Gothic UI\";")
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
        self.rightPanel.setObjectName(u"rightPanel")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: bold 24pt \"Yu Gothic UI\"; padding: 10px;")
        self.label.setTextFormat(Qt.TextFormat.PlainText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.rightPanel.addWidget(self.label)

        self.selectionsLabel = QLabel(self.centralwidget)
        self.selectionsLabel.setObjectName(u"selectionsLabel")
        self.selectionsLabel.setStyleSheet(u"font: bold 14pt \"Yu Gothic UI\"; padding: 5px;")

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

        self.selectColor = QPushButton(self.centralwidget)
        self.selectColor.setObjectName(u"selectColor")

        self.controlsGrid.addWidget(self.selectColor, 0, 1, 1, 1)

        self.selectExcel = QPushButton(self.centralwidget)
        self.selectExcel.setObjectName(u"selectExcel")

        self.controlsGrid.addWidget(self.selectExcel, 1, 0, 1, 1)

        self.openTableDialog = QPushButton(self.centralwidget)
        self.openTableDialog.setObjectName(u"openTableDialog")

        self.controlsGrid.addWidget(self.openTableDialog, 1, 1, 1, 1)

        self.saveImages = QPushButton(self.centralwidget)
        self.saveImages.setObjectName(u"saveImages")
        self.saveImages.setStyleSheet(u"background-color: rgba(100, 255, 218, 0.2); border: 3px solid rgb(100, 255, 218); font: bold 14pt \"Yu Gothic UI\"; color: #64ffda;")

        self.controlsGrid.addWidget(self.saveImages, 2, 0, 1, 2)


        self.rightPanel.addLayout(self.controlsGrid)


        self.mainLayout.addLayout(self.rightPanel)

        self.mainLayout.setStretch(0, 3)
        self.mainLayout.setStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        self.statusbar.setStyleSheet(u"color: #64ffda; background-color: rgba(16, 42, 67, 0.8);")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Automatization Of Business Processes", None))
        self.ImageLabel.setText(QCoreApplication.translate("MainWindow", u"No image loaded", None))
        self.addImage.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c1 Add Image", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"AUTOMATIZATION OF BUSINESS PROCESSES", None))
        self.selectionsLabel.setText(QCoreApplication.translate("MainWindow", u"Selections List:", None))
        self.addSelections.setText(QCoreApplication.translate("MainWindow", u"Add Selection to Image", None))
        self.selectColor.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.selectExcel.setText(QCoreApplication.translate("MainWindow", u"Select Excel File", None))
        self.openTableDialog.setText(QCoreApplication.translate("MainWindow", u"Open Table Window", None))
        self.saveImages.setText(QCoreApplication.translate("MainWindow", u"Save Images", None))
    # retranslateUi


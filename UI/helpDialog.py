# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'helpDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_HelpDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(980, 460)
        Dialog.setStyleSheet(u"QDialog {\n"
"	background: #F5F7FAf;\n"
"}\n"
"QLabel {\n"
"	font: 20pt 'InterI';\n"
"    color: #1F2937;\n"
"    padding-bottom: 8px;\n"
"    border-bottom: 2px solid #64ffda;\n"
"}\n"
"QPushButton {\n"
"            background-color: rgb(79, 125, 243);\n"
"            border: 1px solid rgb(171, 196, 243);\n"
"            border-radius: 8px;\n"
"            padding: 10px 18px;\n"
"            color: #f1f5f9;\n"
"            font: 500 11pt 'Inter', 'Segoe UI', 'Yu Gothic UI';\n"
"          }\n"
"          QPushButton:hover {\n"
"            background-color: rgb(105, 136, 248);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: rgb(63, 100, 194);\n"
"        }\n"
"        QTabBar::tab {\n"
"            color: #1F2937;\n"
"            font: 12pt 'Inter';\n"
"            padding: 8px 20px;\n"
"            margin-right: 8px;\n"
"        }\n"
"        QTabBar::tab:selected {\n"
"            color: rgb(79, 125, 243);\n"
"            border-bottom: 3px solid rgb(79, 125, 243);\n"
"     "
                        "   }\n"
"        QTabBar::tab:hover {\n"
"            color: rgb(105, 136, 248);\n"
"        }\n"
"QTextEdit {\n"
"    color: #1F2937;\n"
"    font: 12pt 'Inter';\n"
"}")
        self.mainLayout = QVBoxLayout(Dialog)
        self.mainLayout.setSpacing(20)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(25, 25, 25, 25)
        self.titleLabel = QLabel(Dialog)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setStyleSheet(u"")

        self.mainLayout.addWidget(self.titleLabel)

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tab_intro = QWidget()
        self.tab_intro.setObjectName(u"tab_intro")
        self.introLayout = QVBoxLayout(self.tab_intro)
        self.introLayout.setObjectName(u"introLayout")
        self.textIntro = QTextEdit(self.tab_intro)
        self.textIntro.setObjectName(u"textIntro")
        self.textIntro.setReadOnly(True)

        self.introLayout.addWidget(self.textIntro)

        self.tabWidget.addTab(self.tab_intro, "")
        self.tab_step1 = QWidget()
        self.tab_step1.setObjectName(u"tab_step1")
        self.step1Layout = QVBoxLayout(self.tab_step1)
        self.step1Layout.setObjectName(u"step1Layout")
        self.textStep1 = QTextEdit(self.tab_step1)
        self.textStep1.setObjectName(u"textStep1")
        self.textStep1.setReadOnly(True)

        self.step1Layout.addWidget(self.textStep1)

        self.tabWidget.addTab(self.tab_step1, "")
        self.tab_step3 = QWidget()
        self.tab_step3.setObjectName(u"tab_step3")
        self.step3Layout = QVBoxLayout(self.tab_step3)
        self.step3Layout.setObjectName(u"step3Layout")
        self.textStep3 = QTextEdit(self.tab_step3)
        self.textStep3.setObjectName(u"textStep3")
        self.textStep3.setReadOnly(True)

        self.step3Layout.addWidget(self.textStep3)

        self.tabWidget.addTab(self.tab_step3, "")
        self.tab_step4 = QWidget()
        self.tab_step4.setObjectName(u"tab_step4")
        self.step4Layout = QVBoxLayout(self.tab_step4)
        self.step4Layout.setObjectName(u"step4Layout")
        self.textStep4 = QTextEdit(self.tab_step4)
        self.textStep4.setObjectName(u"textStep4")
        self.textStep4.setReadOnly(True)

        self.step4Layout.addWidget(self.textStep4)

        self.tabWidget.addTab(self.tab_step4, "")
        self.tab_step5 = QWidget()
        self.tab_step5.setObjectName(u"tab_step5")
        self.step5Layout = QVBoxLayout(self.tab_step5)
        self.step5Layout.setObjectName(u"step5Layout")
        self.textStep5 = QTextEdit(self.tab_step5)
        self.textStep5.setObjectName(u"textStep5")
        self.textStep5.setReadOnly(True)

        self.step5Layout.addWidget(self.textStep5)

        self.tabWidget.addTab(self.tab_step5, "")
        self.tab_step6 = QWidget()
        self.tab_step6.setObjectName(u"tab_step6")
        self.step6Layout = QVBoxLayout(self.tab_step6)
        self.step6Layout.setObjectName(u"step6Layout")
        self.textStep6 = QTextEdit(self.tab_step6)
        self.textStep6.setObjectName(u"textStep6")
        self.textStep6.setReadOnly(True)

        self.step6Layout.addWidget(self.textStep6)

        self.tabWidget.addTab(self.tab_step6, "")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.settingsLayout = QVBoxLayout(self.tab_settings)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.textSettings = QTextEdit(self.tab_settings)
        self.textSettings.setObjectName(u"textSettings")
        self.textSettings.setReadOnly(True)

        self.settingsLayout.addWidget(self.textSettings)

        self.tabWidget.addTab(self.tab_settings, "")
        self.tab_data = QWidget()
        self.tab_data.setObjectName(u"tab_data")
        self.dataLayout = QVBoxLayout(self.tab_data)
        self.dataLayout.setObjectName(u"dataLayout")
        self.textData = QTextEdit(self.tab_data)
        self.textData.setObjectName(u"textData")
        self.textData.setReadOnly(True)

        self.dataLayout.addWidget(self.textData)

        self.tabWidget.addTab(self.tab_data, "")
        self.tab_support = QWidget()
        self.tab_support.setObjectName(u"tab_support")
        self.supportLayout = QVBoxLayout(self.tab_support)
        self.supportLayout.setObjectName(u"supportLayout")
        self.textSupport = QTextEdit(self.tab_support)
        self.textSupport.setObjectName(u"textSupport")
        self.textSupport.setReadOnly(True)

        self.supportLayout.addWidget(self.textSupport)

        self.tabWidget.addTab(self.tab_support, "")

        self.mainLayout.addWidget(self.tabWidget)

        self.bottomLayout = QHBoxLayout()
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.closeButton = QPushButton(Dialog)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setStyleSheet(u"")

        self.bottomLayout.addWidget(self.closeButton)


        self.mainLayout.addLayout(self.bottomLayout)


        self.retranslateUi(Dialog)
        self.closeButton.clicked.connect(Dialog.accept)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.textIntro.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u0430\u043d\u043d\u043e\u0435 \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u043f\u043e\u043c\u043e\u0436\u0435\u0442 \u0432\u0430\u043c \u043f\u043e\u043d\u044f\u0442\u044c \u0430\u0437\u044b \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u0438 \u043f\u043e\u0437\u0432\u043e\u043b\u0438\u0442 \u0432\u0430\u043c \u043d\u0430\u0447\u0430\u0442\u044c \u0441\u043e\u0437"
                        "\u0434\u0430\u0432\u0430\u0442\u044c \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u044b \u0431\u044b\u0441\u0442\u0440\u043e \u0438 \u044d\u0444\u0444\u0435\u043a\u0442\u0438\u0432\u043d\u043e \u043a\u0430\u043a \u043c\u043e\u0436\u043d\u043e \u0441\u043a\u043e\u0440\u0435\u0435.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0427\u0442\u043e\u0431\u044b \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u043a \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u0443, \u043d\u0430\u0436\u043c\u0438\u0442\u0435: &quot;\u0421\u043f\u0440\u0430\u0432\u043a\u0430 -&gt; \u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435&quot;.</p></body></html>", None))
        self.textIntro.setPlainText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u043d\u043d\u043e\u0435 \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u043f\u043e\u043c\u043e\u0436\u0435\u0442 \u0432\u0430\u043c \u043f\u043e\u043d\u044f\u0442\u044c \u0430\u0437\u044b \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u0438 \u043f\u043e\u0437\u0432\u043e\u043b\u0438\u0442 \u0432\u0430\u043c \u043d\u0430\u0447\u0430\u0442\u044c \u0441\u043e\u0437\u0434\u0430\u0432\u0430\u0442\u044c \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u044b \u0431\u044b\u0441\u0442\u0440\u043e \u0438 \u044d\u0444\u0444\u0435\u043a\u0442\u0438\u0432\u043d\u043e \u043a\u0430\u043a \u043c\u043e\u0436\u043d\u043e \u0441\u043a\u043e\u0440\u0435\u0435.\n"
"\u0427\u0442\u043e\u0431\u044b \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u043a \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u0443, \u043d\u0430\u0436\u043c\u0438\u0442\u0435: \"\u0421\u043f\u0440\u0430\u0432\u043a\u0430 -> \u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e"
                        " \u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435\".", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_intro), QCoreApplication.translate("Dialog", u"01 \u0412\u0432\u0435\u0434\u0435\u043d\u0438\u0435", None))
        self.textStep1.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0423\u0431\u0435\u0434\u0438\u0442\u0435\u0441\u044c \u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0445 \u0444\u0430\u0439\u043b\u043e\u0432:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bott"
                        "om:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u2022 \u0424\u0430\u0439\u043b \u0448\u0430\u0431\u043b\u043e\u043d\u0430: \u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043c\u0430\u043a\u0435\u0442\u0430 \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u0430/\u0434\u0438\u043f\u043b\u043e\u043c\u0430 (\u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u043c\u044b\u0435 \u0444\u043e\u0440\u043c\u0430\u0442\u044b: JPEG, PNG \u0438 \u0434\u0440\u0443\u0433\u0438\u0435).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u2022 \u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0434\u0430\u043d\u043d\u044b\u0445: \u0434\u043e\u043a"
                        "\u0443\u043c\u0435\u043d\u0442 \u0442\u0430\u0431\u043b\u0438\u0447\u043d\u043e\u0433\u043e \u0444\u043e\u0440\u043c\u0430\u0442\u0430 (.xlsx, .xls, .ods \u0438 \u0434\u0440\u0443\u0433\u0438\u0435), \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0438\u0439 \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u0435\u0439 (\u0424\u0418\u041e, \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043a\u0443\u0440\u0441\u0430, \u0434\u0430\u0442\u0430 \u0438 \u0442.\u0434.).</p></body></html>", None))
        self.textStep1.setPlainText(QCoreApplication.translate("Dialog", u"\u0423\u0431\u0435\u0434\u0438\u0442\u0435\u0441\u044c \u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0445 \u0444\u0430\u0439\u043b\u043e\u0432:\n"
"\n"
"    \u2022 \u0424\u0430\u0439\u043b \u0448\u0430\u0431\u043b\u043e\u043d\u0430: \u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043c\u0430\u043a\u0435\u0442\u0430 \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u0430/\u0434\u0438\u043f\u043b\u043e\u043c\u0430 (\u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u043c\u044b\u0435 \u0444\u043e\u0440\u043c\u0430\u0442\u044b: JPEG, PNG \u0438 \u0434\u0440\u0443\u0433\u0438\u0435).\n"
"\n"
"    \u2022 \u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0434\u0430\u043d\u043d\u044b\u0445: \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442 \u0442\u0430\u0431\u043b\u0438\u0447\u043d\u043e\u0433\u043e \u0444\u043e\u0440\u043c\u0430\u0442\u0430 (.xlsx, .xls, .od"
                        "s \u0438 \u0434\u0440\u0443\u0433\u0438\u0435), \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0438\u0439 \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u0435\u0439 (\u0424\u0418\u041e, \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043a\u0443\u0440\u0441\u0430, \u0434\u0430\u0442\u0430 \u0438 \u0442.\u0434.).", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_step1), QCoreApplication.translate("Dialog", u"02 \u041f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0430", None))
        self.textStep3.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0427\u0442\u043e\u0431\u044b \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0448\u0430\u0431\u043b\u043e\u043d, \u043d\u0430\u0436\u043c\u0438\u0442\u0435: \u00ab\u0424\u0430\u0439\u043b -&gt; \u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435\u00bb \u0432 \u043b\u0435\u0432\u043e\u043c \u0432\u0435\u0440\u0445\u043d\u0435\u043c \u0443"
                        "\u0433\u043b\u0443. \u0412 \u043e\u0442\u043a\u0440\u044b\u0432\u0448\u0435\u043c\u0441\u044f \u043e\u043a\u043d\u0435 \u043f\u0440\u043e\u0432\u043e\u0434\u043d\u0438\u043a\u0430 \u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0412\u0430\u0448\u0435\u043c\u0443 \u0444\u0430\u0439\u043b\u0443-\u0448\u0430\u0431\u043b\u043e\u043d\u0443. \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u0441\u044f \u0432 \u0440\u0430\u0431\u043e\u0447\u0435\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b.</p></body></html>", None))
        self.textStep3.setPlainText(QCoreApplication.translate("Dialog", u"\u0427\u0442\u043e\u0431\u044b \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0448\u0430\u0431\u043b\u043e\u043d, \u043d\u0430\u0436\u043c\u0438\u0442\u0435: \u00ab\u0424\u0430\u0439\u043b -> \u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435\u00bb \u0432 \u043b\u0435\u0432\u043e\u043c \u0432\u0435\u0440\u0445\u043d\u0435\u043c \u0443\u0433\u043b\u0443. \u0412 \u043e\u0442\u043a\u0440\u044b\u0432\u0448\u0435\u043c\u0441\u044f \u043e\u043a\u043d\u0435 \u043f\u0440\u043e\u0432\u043e\u0434\u043d\u0438\u043a\u0430 \u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0412\u0430\u0448\u0435\u043c\u0443 \u0444\u0430\u0439\u043b\u0443-\u0448\u0430\u0431\u043b\u043e\u043d\u0443. \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u0441\u044f \u0432 \u0440\u0430\u0431\u043e\u0447\u0435\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u043f\u0440\u043e\u0433\u0440"
                        "\u0430\u043c\u043c\u044b.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_step3), QCoreApplication.translate("Dialog", u"04 \u0428\u0430\u0431\u043b\u043e\u043d", None))
        self.textStep4.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0427\u0442\u043e\u0431\u044b \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435, \u043d\u0430\u0436\u043c\u0438\u0442\u0435: \u00ab\u0424\u0430\u0439\u043b -&gt; \u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0434\u0430\u043d\u043d\u044b\u0445\u00bb \u0432 \u043b\u0435\u0432\u043e\u043c \u0432\u0435\u0440\u0445\u043d\u0435\u043c"
                        " \u0443\u0433\u043b\u0443. \u0412 \u043e\u0442\u043a\u0440\u044b\u0432\u0448\u0435\u043c\u0441\u044f \u043e\u043a\u043d\u0435 \u043f\u0440\u043e\u0432\u043e\u0434\u043d\u0438\u043a\u0430 \u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0412\u0430\u0448\u0435\u043c\u0443 \u0442\u0430\u0431\u043b\u0438\u0447\u043d\u043e\u043c\u0443 \u0444\u0430\u0439\u043b\u0443. \u041f\u0440\u0438 \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u043d\u0438\u0438 \u0434\u0430\u043d\u043d\u044b\u0445, \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u044b (\u0442\u043e \u0435\u0441\u0442\u044c 1-\u044b\u0439 \u0440\u044f\u0434 \u0442\u0430\u0431\u043b\u0438\u0446\u044b) \u0431\u0443\u0434\u0443\u0442 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043e\u0439 \u0432 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435 \u043f\u043e\u043b\u0435\u0439"
                        " \u0434\u043b\u044f \u0432\u0441\u0442\u0430\u0432\u043a\u0438 \u043d\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435.</p></body></html>", None))
        self.textStep4.setPlainText(QCoreApplication.translate("Dialog", u"\u0427\u0442\u043e\u0431\u044b \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435, \u043d\u0430\u0436\u043c\u0438\u0442\u0435: \u00ab\u0424\u0430\u0439\u043b -> \u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0434\u0430\u043d\u043d\u044b\u0445\u00bb \u0432 \u043b\u0435\u0432\u043e\u043c \u0432\u0435\u0440\u0445\u043d\u0435\u043c \u0443\u0433\u043b\u0443. \u0412 \u043e\u0442\u043a\u0440\u044b\u0432\u0448\u0435\u043c\u0441\u044f \u043e\u043a\u043d\u0435 \u043f\u0440\u043e\u0432\u043e\u0434\u043d\u0438\u043a\u0430 \u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0412\u0430\u0448\u0435\u043c\u0443 \u0442\u0430\u0431\u043b\u0438\u0447\u043d\u043e\u043c\u0443 \u0444\u0430\u0439\u043b\u0443. \u041f\u0440\u0438 \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u043d\u0438\u0438 \u0434\u0430\u043d\u043d\u044b\u0445, \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432 \u0442"
                        "\u0430\u0431\u043b\u0438\u0446\u044b (\u0442\u043e \u0435\u0441\u0442\u044c 1-\u044b\u0439 \u0440\u044f\u0434 \u0442\u0430\u0431\u043b\u0438\u0446\u044b) \u0431\u0443\u0434\u0443\u0442 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043e\u0439 \u0432 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435 \u043f\u043e\u043b\u0435\u0439 \u0434\u043b\u044f \u0432\u0441\u0442\u0430\u0432\u043a\u0438 \u043d\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_step4), QCoreApplication.translate("Dialog", u"05 \u0414\u0430\u043d\u043d\u044b\u0435", None))
        self.textStep5.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412 \u043f\u0440\u0430\u0432\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0430 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d \u0431\u043b\u043e\u043a \u00ab\u041f\u043e\u043b\u044f \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f\u00bb. \u0414\u0430\u043d\u043d\u044b\u0439 \u0431\u043b\u043e\u043a \u0441"
                        "\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u0441\u043f\u0438\u0441\u043e\u043a \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432 \u0412\u0430\u0448\u0435\u0433\u043e \u0442\u0430\u0431\u043b\u0438\u0447\u043d\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0430.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u2022 \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e\u0435 \u043f\u043e\u043b\u0435 (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u00ab\u0424\u0418\u041e\u00bb).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u2022 \u041a\u043b\u0438\u043a\u043d\u0438\u0442\u0435 \u043b\u0435\u0432\u043e\u0439 \u043a\u043d\u043e\u043f"
                        "\u043a\u043e\u0439 \u043c\u044b\u0448\u0438 \u0432 \u0442\u0443 \u043e\u0431\u043b\u0430\u0441\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f, \u043a\u0443\u0434\u0430 \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u0432\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u2022 \u041d\u0430 \u043c\u0435\u0441\u0442\u0435 \u043a\u043b\u0438\u043a\u0430 \u043f\u043e\u044f\u0432\u0438\u0442\u0441\u044f \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u044d\u0442\u043e\u0433\u043e \u043f\u043e\u043b\u044f. \u041f\u0440\u0438 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0438 \u043a\u043e\u043d\u0435\u0447\u043d\u044b\u0445 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439, \u0434\u0430\u043d\u043d\u044b\u0435, \u043d\u0430\u0445\u043e\u0434\u044f\u0449"
                        "\u0438\u0435\u0441\u044f \u043f\u043e\u0434 \u044d\u0442\u0438\u043c \u043f\u043e\u043b\u0435\u043c \u0432 \u0412\u0430\u0448\u0435\u0439 \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u0431\u0443\u0434\u0443\u0442 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u043d\u044b. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u2022 \u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044e \u0434\u043b\u044f \u0432\u0441\u0435\u0445 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0445 \u043f\u043e\u043b\u0435\u0439 (\u0434\u0430\u0442\u0430, \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f \u0438 \u0442.\u0434.).</p></body></html>", None))
        self.textStep5.setPlainText(QCoreApplication.translate("Dialog", u"\u0412 \u043f\u0440\u0430\u0432\u043e\u0439 \u0447\u0430\u0441\u0442\u0438 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0430 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d \u0431\u043b\u043e\u043a \u00ab\u041f\u043e\u043b\u044f \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f\u00bb. \u0414\u0430\u043d\u043d\u044b\u0439 \u0431\u043b\u043e\u043a \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u0441\u043f\u0438\u0441\u043e\u043a \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432 \u0412\u0430\u0448\u0435\u0433\u043e \u0442\u0430\u0431\u043b\u0438\u0447\u043d\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0430.\n"
"\n"
"    \u2022 \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e\u0435 \u043f\u043e\u043b\u0435 (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u00ab\u0424\u0418\u041e\u00bb).\n"
"    \u2022 \u041a\u043b\u0438\u043a\u043d\u0438\u0442\u0435 \u043b\u0435\u0432\u043e\u0439 \u043a\u043d\u043e"
                        "\u043f\u043a\u043e\u0439 \u043c\u044b\u0448\u0438 \u0432 \u0442\u0443 \u043e\u0431\u043b\u0430\u0441\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f, \u043a\u0443\u0434\u0430 \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u0432\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435.\n"
"    \u2022 \u041d\u0430 \u043c\u0435\u0441\u0442\u0435 \u043a\u043b\u0438\u043a\u0430 \u043f\u043e\u044f\u0432\u0438\u0442\u0441\u044f \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u044d\u0442\u043e\u0433\u043e \u043f\u043e\u043b\u044f. \u041f\u0440\u0438 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0438 \u043a\u043e\u043d\u0435\u0447\u043d\u044b\u0445 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439, \u0434\u0430\u043d\u043d\u044b\u0435, \u043d\u0430\u0445\u043e\u0434\u044f\u0449\u0438\u0435\u0441\u044f \u043f\u043e\u0434 \u044d\u0442\u0438\u043c \u043f\u043e\u043b\u0435\u043c \u0432 \u0412\u0430"
                        "\u0448\u0435\u0439 \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u0431\u0443\u0434\u0443\u0442 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u043d\u044b. \n"
"    \u2022 \u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044e \u0434\u043b\u044f \u0432\u0441\u0435\u0445 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0445 \u043f\u043e\u043b\u0435\u0439 (\u0434\u0430\u0442\u0430, \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f \u0438 \u0442.\u0434.).", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_step5), QCoreApplication.translate("Dialog", u"06 \u041f\u043e\u043b\u044f", None))
        self.textStep6.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0430</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u043e \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0438 \u0432\u0435\u0440\u0441\u0442\u043a\u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a"
                        "\u043d\u043e\u043f\u043a\u0443 \u00ab\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u00bb.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u2022 \u0412 \u043f\u043e\u044f\u0432\u0438\u0432\u0448\u0435\u043c\u0441\u044f \u043e\u043a\u043d\u0435 \u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u0446\u0435\u043b\u0435\u0432\u0443\u044e \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0433\u043e\u0442\u043e\u0432\u044b\u0445 \u0444\u0430\u0439\u043b\u043e\u0432.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u2022 \u0412 \u0443\u043a\u0430\u0437\u0430\u043d"
                        "\u043d\u043e\u043c \u0412\u0430\u043c\u0438 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0441\u043e\u0437\u0434\u0430\u0441\u0442 \u043f\u0430\u043f\u043a\u0443 \u0441 \u0438\u043c\u0435\u043d\u0435\u043c \u0444\u043e\u0440\u043c\u0430\u0442\u0430 Output-\u0414\u0414-\u041c\u041c-\u0413\u0413 \u0427\u0427\u041c\u041c\u0421\u0421, \u0432 \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u0431\u0443\u0434\u0443\u0442 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u044b \u0432\u0441\u0435 \u0441\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f.</p></body></html>", None))
        self.textStep6.setPlainText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0430\n"
"\u041f\u043e \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0438 \u0432\u0435\u0440\u0441\u0442\u043a\u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \u00ab\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u00bb.\n"
"\n"
"    \u2022 \u0412 \u043f\u043e\u044f\u0432\u0438\u0432\u0448\u0435\u043c\u0441\u044f \u043e\u043a\u043d\u0435 \u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u0446\u0435\u043b\u0435\u0432\u0443\u044e \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0433\u043e\u0442\u043e\u0432\u044b\u0445 \u0444\u0430\u0439\u043b\u043e\u0432.\n"
"    \u2022 \u0412 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u043c \u0412\u0430\u043c\u0438 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0438 \u043f"
                        "\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0441\u043e\u0437\u0434\u0430\u0441\u0442 \u043f\u0430\u043f\u043a\u0443 \u0441 \u0438\u043c\u0435\u043d\u0435\u043c \u0444\u043e\u0440\u043c\u0430\u0442\u0430 Output-\u0414\u0414-\u041c\u041c-\u0413\u0413 \u0427\u0427\u041c\u041c\u0421\u0421, \u0432 \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u0431\u0443\u0434\u0443\u0442 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u044b \u0432\u0441\u0435 \u0441\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_step6), QCoreApplication.translate("Dialog", u"07 \u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435", None))
        self.textSettings.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043b\u044f \u043f\u0440\u0438\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0442\u0435\u043a\u0441\u0442\u0430 \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0435 \u0441 \u043a\u043e\u0440\u043f\u043e\u0440\u0430\u0442\u0438\u0432\u043d\u044b\u043c \u0441\u0442\u0438\u043b\u0435\u043c \u0438\u043b\u0438 \u043b\u0438\u0447\u043d\u044b\u043c\u0438 \u043f\u0440\u0435\u0434"
                        "\u043f\u043e\u0447\u0442\u0435\u043d\u0438\u044f\u043c\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0434 \u0440\u0430\u0437\u0434\u0435\u043b\u043e\u043c \u00ab\u041f\u043e\u043b\u044f \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f\u00bb.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u0430\u043d\u043d\u044b\u0439 \u0440\u0430\u0437\u0434\u0435\u043b \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u2022 \u0418\u0437\u043c\u0435\u043d\u044f\u0442\u044c \u0446\u0435\u043d\u0442\u0440\u0438\u0440\u043e"
                        "\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u2022 \u0420\u0435\u0433\u0443\u043b\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 ;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u2022 \u0412\u044b\u0431\u0438\u0440\u0430\u0442\u044c \u0446\u0432\u0435\u0442\u043e\u0432\u0443\u044e \u043f\u0430\u043b\u0438\u0442\u0440\u0443 \u0442\u0435\u043a\u0441\u0442\u0430.</p></body></html>", None))
        self.textSettings.setPlainText(QCoreApplication.translate("Dialog", u"\u0414\u043b\u044f \u043f\u0440\u0438\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0442\u0435\u043a\u0441\u0442\u0430 \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0435 \u0441 \u043a\u043e\u0440\u043f\u043e\u0440\u0430\u0442\u0438\u0432\u043d\u044b\u043c \u0441\u0442\u0438\u043b\u0435\u043c \u0438\u043b\u0438 \u043b\u0438\u0447\u043d\u044b\u043c\u0438 \u043f\u0440\u0435\u0434\u043f\u043e\u0447\u0442\u0435\u043d\u0438\u044f\u043c\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0434 \u0440\u0430\u0437\u0434\u0435\u043b\u043e\u043c \u00ab\u041f\u043e\u043b\u044f \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f\u00bb.\n"
"\n"
"\u0414\u0430\u043d\u043d\u044b\u0439 \u0440\u0430\u0437\u0434\u0435\u043b \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442:\n"
"    \u2022 \u0418\u0437\u043c\u0435\u043d\u044f\u0442\u044c \u0446\u0435\u043d\u0442\u0440\u0438\u0440\u043e"
                        "\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430;\n"
"    \u2022 \u0420\u0435\u0433\u0443\u043b\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 ;\n"
"    \u2022 \u0412\u044b\u0431\u0438\u0440\u0430\u0442\u044c \u0446\u0432\u0435\u0442\u043e\u0432\u0443\u044e \u043f\u0430\u043b\u0438\u0442\u0440\u0443 \u0442\u0435\u043a\u0441\u0442\u0430.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), QCoreApplication.translate("Dialog", u"08 \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.textData.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412 \u0441\u043b\u0443\u0447\u0430\u0435 \u043e\u0431\u043d\u0430\u0440\u0443\u0436\u0435\u043d\u0438\u044f \u043d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445 (\u043e\u043f\u0435\u0447\u0430\u0442\u043a\u0438, \u043e\u0440\u0444\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043e\u0448\u0438\u0431\u043a\u0438) \u0432"
                        " \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043d\u043e\u0439 \u0442\u0430\u0431\u043b\u0438\u0446\u0435, \u043d\u0435 \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u0437\u0430\u043a\u0440\u044b\u0432\u0430\u0442\u044c \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0443 \u0438 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u2022 \u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \u00ab\u0424\u0430\u0439\u043b -&gt; \u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0434\u0430\u043d\u043d\u044b\u0445\u00bb"
                        ".</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u2022 \u041d\u0430 \u044d\u043a\u0440\u0430\u043d\u0435 \u043e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u0441\u044f \u0432\u0441\u0442\u0440\u043e\u0435\u043d\u043d\u044b\u0439 \u0440\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u0434\u0430\u043d\u043d\u044b\u0445.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u2022 \u0412\u043d\u0435\u0441\u0438\u0442\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0435 \u0438\u0441\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u043d\u0435\u043f\u043e\u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0435\u043d\u043d\u043e \u0432 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b.</p></body></html>", None))
        self.textData.setPlainText(QCoreApplication.translate("Dialog", u"\u0412 \u0441\u043b\u0443\u0447\u0430\u0435 \u043e\u0431\u043d\u0430\u0440\u0443\u0436\u0435\u043d\u0438\u044f \u043d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445 (\u043e\u043f\u0435\u0447\u0430\u0442\u043a\u0438, \u043e\u0440\u0444\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043e\u0448\u0438\u0431\u043a\u0438) \u0432 \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043d\u043e\u0439 \u0442\u0430\u0431\u043b\u0438\u0446\u0435, \u043d\u0435 \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u0437\u0430\u043a\u0440\u044b\u0432\u0430\u0442\u044c \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0443 \u0438 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e.\n"
"\n"
"    \u2022 \u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \u00ab\u0424\u0430\u0439\u043b -> \u0418\u0437"
                        "\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0434\u0430\u043d\u043d\u044b\u0445\u00bb.\n"
"    \u2022 \u041d\u0430 \u044d\u043a\u0440\u0430\u043d\u0435 \u043e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u0441\u044f \u0432\u0441\u0442\u0440\u043e\u0435\u043d\u043d\u044b\u0439 \u0440\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u0434\u0430\u043d\u043d\u044b\u0445.\n"
"    \u2022 \u0412\u043d\u0435\u0441\u0438\u0442\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0435 \u0438\u0441\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u043d\u0435\u043f\u043e\u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0435\u043d\u043d\u043e \u0432 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data), QCoreApplication.translate("Dialog", u"09 \u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440", None))
        self.textSupport.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0415\u0441\u043b\u0438 \u043f\u0440\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0438 \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438 \u0432\u043e\u0437\u043d\u0438\u043a\u0430\u044e\u0442 \u043e\u0448\u0438\u0431\u043a\u0438 \u0438\u043b\u0438 \u0441\u0431\u043e\u0438 \u0432 \u0440\u0430\u0431\u043e\u0442\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f"
                        ", \u043f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u0441\u043e\u0437\u0434\u0430\u0439\u0442\u0435 \u041f\u0440\u043e\u0431\u043b\u0435\u043c\u0443 \u0432 \u043d\u0430\u0448\u0435\u043c \u0440\u0435\u043f\u043e\u0437\u0438\u0442\u043e\u0440\u0438\u0438 GitHub.</p></body></html>", None))
        self.textSupport.setPlainText(QCoreApplication.translate("Dialog", u"\u0415\u0441\u043b\u0438 \u043f\u0440\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0438 \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438 \u0432\u043e\u0437\u043d\u0438\u043a\u0430\u044e\u0442 \u043e\u0448\u0438\u0431\u043a\u0438 \u0438\u043b\u0438 \u0441\u0431\u043e\u0438 \u0432 \u0440\u0430\u0431\u043e\u0442\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f, \u043f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u0441\u043e\u0437\u0434\u0430\u0439\u0442\u0435 \u041f\u0440\u043e\u0431\u043b\u0435\u043c\u0443 \u0432 \u043d\u0430\u0448\u0435\u043c \u0440\u0435\u043f\u043e\u0437\u0438\u0442\u043e\u0440\u0438\u0438 GitHub.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_support), QCoreApplication.translate("Dialog", u"10 \u041f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430", None))
        self.closeButton.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi


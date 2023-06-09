# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'theme_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout)
import files_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(577, 304)
        icon = QIcon()
        icon.addFile(u":/ico/icon/coffee.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.frame)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"   /* QPUSHBUTTON */\n"
"    QPushButton#pushButton_close {\n"
"        background: rgb(255, 96, 92);\n"
"    }\n"
"    QPushButton#pushButton_close:hover {\n"
"        background: rgb(232, 86, 84);\n"
"    }\n"
"\n"
"\n"
"    QPushButton#pushButton_hide {\n"
"        background: rgb(255, 189, 68);\n"
"    }\n"
"\n"
"    QPushButton#pushButton_hide:hover{\n"
"        background: rgb(229, 151, 61);\n"
"    }\n"
"\n"
"    QPushButton#pushButton_maximum {\n"
"        background: rgb(0, 202, 78);\n"
"    }\n"
"\n"
"    QPushButton#pushButton_maximum:hover {\n"
"        background:rgb(0, 176, 67);\n"
"    }")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame_main)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 35))
        self.frame_title.setMaximumSize(QSize(16777215, 35))
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.frame_title_btn = QFrame(self.frame_title)
        self.frame_title_btn.setObjectName(u"frame_title_btn")
        self.frame_title_btn.setFrameShape(QFrame.NoFrame)
        self.frame_title_btn.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_title_btn)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_close = QPushButton(self.frame_title_btn)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMinimumSize(QSize(16, 16))
        self.pushButton_close.setMaximumSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.pushButton_close)

        self.pushButton_hide = QPushButton(self.frame_title_btn)
        self.pushButton_hide.setObjectName(u"pushButton_hide")
        self.pushButton_hide.setMinimumSize(QSize(16, 16))
        self.pushButton_hide.setMaximumSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.pushButton_hide)


        self.horizontalLayout_4.addWidget(self.frame_title_btn, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_title)

        self.frame_content = QFrame(self.frame_main)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setAutoFillBackground(False)
        self.frame_content.setStyleSheet(u"")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_input = QFrame(self.frame_content)
        self.frame_input.setObjectName(u"frame_input")
        self.frame_input.setFrameShape(QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_input)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.pushButton_dark = QPushButton(self.frame_input)
        self.pushButton_dark.setObjectName(u"pushButton_dark")
        self.pushButton_dark.setMinimumSize(QSize(260, 165))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_dark.setFont(font)
        self.pushButton_dark.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.pushButton_dark)

        self.pushButton_light = QPushButton(self.frame_input)
        self.pushButton_light.setObjectName(u"pushButton_light")
        self.pushButton_light.setMinimumSize(QSize(260, 165))
        self.pushButton_light.setFont(font)
        self.pushButton_light.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.pushButton_light)


        self.verticalLayout_2.addWidget(self.frame_input)

        self.frame_btn = QFrame(self.frame_content)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMinimumSize(QSize(0, 40))
        self.frame_btn.setMaximumSize(QSize(16777215, 40))
        self.frame_btn.setFrameShape(QFrame.NoFrame)
        self.frame_btn.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_btn)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 10)
        self.label = QLabel(self.frame_btn)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(111, 16777215))

        self.horizontalLayout_7.addWidget(self.label)

        self.comboBox_size = QComboBox(self.frame_btn)
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.setObjectName(u"comboBox_size")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        self.comboBox_size.setFont(font1)

        self.horizontalLayout_7.addWidget(self.comboBox_size)

        self.pushButton_ok = QPushButton(self.frame_btn)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setMinimumSize(QSize(110, 25))
        self.pushButton_ok.setFont(font)

        self.horizontalLayout_7.addWidget(self.pushButton_ok, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_btn)


        self.verticalLayout.addWidget(self.frame_content)


        self.horizontalLayout_2.addWidget(self.frame_main)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Ch\u1ecdn giao di\u1ec7n", None))
#if QT_CONFIG(tooltip)
        self.pushButton_close.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_close.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_hide.setToolTip(QCoreApplication.translate("Dialog", u"minimumsize", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_hide.setText("")
        self.pushButton_dark.setText("")
        self.pushButton_light.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Ch\u1ecdn k\u00edch c\u1ee1</span></p></body></html>", None))
        self.comboBox_size.setItemText(0, QCoreApplication.translate("Dialog", u"V\u1eeba m\u00e0n h\u00ecnh", None))
        self.comboBox_size.setItemText(1, QCoreApplication.translate("Dialog", u"Nh\u1ecf", None))
        self.comboBox_size.setItemText(2, QCoreApplication.translate("Dialog", u"Full m\u00e0n h\u00ecnh", None))

        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"Ti\u1ebfp t\u1ee5c", None))
    # retranslateUi


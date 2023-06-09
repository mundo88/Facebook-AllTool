# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\app\widget\ui\theme_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(577, 304)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/icon/coffee.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_main = QtWidgets.QFrame(self.frame)
        self.frame_main.setStyleSheet("   /* QPUSHBUTTON */\n"
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
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_title = QtWidgets.QFrame(self.frame_main)
        self.frame_title.setMinimumSize(QtCore.QSize(0, 35))
        self.frame_title.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_title_btn = QtWidgets.QFrame(self.frame_title)
        self.frame_title_btn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_title_btn.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_title_btn.setObjectName("frame_title_btn")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_title_btn)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_close = QtWidgets.QPushButton(self.frame_title_btn)
        self.pushButton_close.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton_close.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton_close.setText("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_5.addWidget(self.pushButton_close)
        self.pushButton_hide = QtWidgets.QPushButton(self.frame_title_btn)
        self.pushButton_hide.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton_hide.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButton_hide.setText("")
        self.pushButton_hide.setObjectName("pushButton_hide")
        self.horizontalLayout_5.addWidget(self.pushButton_hide)
        self.horizontalLayout_4.addWidget(self.frame_title_btn, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addWidget(self.frame_title)
        self.frame_content = QtWidgets.QFrame(self.frame_main)
        self.frame_content.setAutoFillBackground(False)
        self.frame_content.setStyleSheet("")
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_input = QtWidgets.QFrame(self.frame_content)
        self.frame_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_input.setObjectName("frame_input")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_input)
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_dark = QtWidgets.QPushButton(self.frame_input)
        self.pushButton_dark.setMinimumSize(QtCore.QSize(260, 165))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_dark.setFont(font)
        self.pushButton_dark.setStyleSheet("")
        self.pushButton_dark.setText("")
        self.pushButton_dark.setObjectName("pushButton_dark")
        self.horizontalLayout_6.addWidget(self.pushButton_dark)
        self.pushButton_light = QtWidgets.QPushButton(self.frame_input)
        self.pushButton_light.setMinimumSize(QtCore.QSize(260, 165))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_light.setFont(font)
        self.pushButton_light.setStyleSheet("")
        self.pushButton_light.setText("")
        self.pushButton_light.setObjectName("pushButton_light")
        self.horizontalLayout_6.addWidget(self.pushButton_light)
        self.verticalLayout_2.addWidget(self.frame_input)
        self.frame_btn = QtWidgets.QFrame(self.frame_content)
        self.frame_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_btn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btn.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_btn.setObjectName("frame_btn")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_btn)
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 10)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.frame_btn)
        self.label.setMaximumSize(QtCore.QSize(111, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.comboBox_size = QtWidgets.QComboBox(self.frame_btn)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.comboBox_size.setFont(font)
        self.comboBox_size.setObjectName("comboBox_size")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_size)
        self.pushButton_ok = QtWidgets.QPushButton(self.frame_btn)
        self.pushButton_ok.setMinimumSize(QtCore.QSize(110, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ok.setFont(font)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_7.addWidget(self.pushButton_ok, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_btn)
        self.verticalLayout.addWidget(self.frame_content)
        self.horizontalLayout_2.addWidget(self.frame_main)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Chọn giao diện"))
        self.pushButton_close.setToolTip(_translate("Dialog", "<html><head/><body><p>Close</p></body></html>"))
        self.pushButton_hide.setToolTip(_translate("Dialog", "minimumsize"))
        self.label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Chọn kích cỡ</span></p></body></html>"))
        self.comboBox_size.setItemText(0, _translate("Dialog", "Vừa màn hình"))
        self.comboBox_size.setItemText(1, _translate("Dialog", "Nhỏ"))
        self.comboBox_size.setItemText(2, _translate("Dialog", "Full màn hình"))
        self.pushButton_ok.setText(_translate("Dialog", "Tiếp tục"))
import files_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\app\widget\ui\comment.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(755, 533)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("    QPlainTextEdit {\n"
"        background-color: rgb(249, 249, 249);\n"
"        border-radius: 5px;\n"
"        color: rgb(71, 75, 78);\n"
"        border: 2px solid rgb(150, 150, 150);\n"
"        padding: 10px;\n"
"    }\n"
"    QPlainTextEdit:hover {\n"
"          border: 2px solid rgb(138, 180, 248);\n"
"    }\n"
"    QPlainTextEdit:focus {\n"
"         border: 2px solid  rgb(138, 180, 248);\n"
"    }\n"
"    QScrollBar:horizontal {\n"
"        border: none;\n"
"        background:  rgb(231, 234, 237);\n"
"        height: 14px;\n"
"        margin: 0px 21px 0 21px;\n"
"        border-radius: 0px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:horizontal {\n"
"        background: rgb(85, 170, 255);\n"
"        min-width: 25px;\n"
"        border-radius: 7px\n"
"    }\n"
"    QScrollBar::add-line:horizontal {\n"
"        border: none;\n"
"        background: rgb(231, 234, 237) ;\n"
"        width: 20px;\n"
"        border-top-right-radius: 7px;\n"
"        border-bottom-right-radius: 7px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"    QScrollBar::sub-line:horizontal {\n"
"        border: none;\n"
"        background: rgb(231, 234, 237);\n"
"        width: 20px;\n"
"        border-top-left-radius: 7px;\n"
"        border-bottom-left-radius: 7px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"    {\n"
"         background: none;\n"
"    }\n"
"    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"    {\n"
"         background: none;\n"
"    }\n"
"     QScrollBar:vertical {\n"
"        border: none;\n"
"        background:  rgb(231, 234, 237);\n"
"        width: 14px;\n"
"        margin: 21px 0 21px 0;\n"
"        border-radius: 0px;\n"
"     }\n"
"     QScrollBar::handle:vertical {  \n"
"        background: rgb(85, 170, 255);\n"
"        min-height: 25px;\n"
"        border-radius: 7px\n"
"     }\n"
"     QScrollBar::add-line:vertical {\n"
"         border: none;\n"
"        background:  rgb(231, 234, 237);\n"
"         height: 20px;\n"
"        border-bottom-left-radius: 7px;\n"
"        border-bottom-right-radius: 7px;\n"
"         subcontrol-position: bottom;\n"
"         subcontrol-origin: margin;\n"
"     }\n"
"     QScrollBar::sub-line:vertical {\n"
"        border: none;\n"
"        background:  rgb(231, 234, 237);\n"
"        height: 20px;\n"
"        border-top-left-radius: 7px;\n"
"        border-top-right-radius: 7px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"     }\n"
"     QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"        background: none;\n"
"     }\n"
"\n"
"     QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"        background: none;\n"
"     }")
        self.plainTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_cmt = QtWidgets.QPushButton(self.frame)
        self.pushButton_cmt.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_cmt.setMaximumSize(QtCore.QSize(50000, 300))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cmt.setFont(font)
        self.pushButton_cmt.setStyleSheet("QPushButton {\n"
"    \n"
"    color : rgb(255,255,255);\n"
"    border:none;\n"
"    background-color: rgb(75, 104, 133);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"    padding-right:3px;\n"
"}")
        self.pushButton_cmt.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_cmt.setObjectName("pushButton_cmt")
        self.horizontalLayout.addWidget(self.pushButton_cmt)
        self.pushButton_cmt_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_cmt_2.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_cmt_2.setMaximumSize(QtCore.QSize(50000, 300))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cmt_2.setFont(font)
        self.pushButton_cmt_2.setStyleSheet("QPushButton {\n"
"    \n"
"    color : rgb(255,255,255);\n"
"    border:none;\n"
"    background-color: rgb(75, 104, 133);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"    padding-right:3px;\n"
"}")
        self.pushButton_cmt_2.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_cmt_2.setObjectName("pushButton_cmt_2")
        self.horizontalLayout.addWidget(self.pushButton_cmt_2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Comment"))
        self.pushButton_cmt.setText(_translate("Dialog", "Nhập comment"))
        self.pushButton_cmt.setShortcut(_translate("Dialog", "Ctrl+B"))
        self.pushButton_cmt_2.setText(_translate("Dialog", "Xáo trộn cmt"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mutiple_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 85)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setSpecialValueText("")
        self.spinBox.setProperty("showGroupSeparator", True)
        self.spinBox.setMaximum(10)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setDisplayIntegerBase(10)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.pushButton_newapp = QtWidgets.QPushButton(Dialog)
        self.pushButton_newapp.setMinimumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_newapp.setFont(font)
        self.pushButton_newapp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_newapp.setStyleSheet("QPushButton {\n"
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
        self.pushButton_newapp.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_newapp.setObjectName("pushButton_newapp")
        self.horizontalLayout.addWidget(self.pushButton_newapp)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tạo phiên bản app"))
        self.pushButton_newapp.setText(_translate("Dialog", "Mở"))
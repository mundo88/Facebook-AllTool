# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpinBox,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(743, 713)
        MainWindow.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/ico/icon/coffee.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setMinimumSize(QSize(70, 0))
        self.btn_toggle_menu.setMaximumSize(QSize(70, 65))
        self.btn_toggle_menu.setToolTipDuration(-3)
        self.btn_toggle_menu.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_4.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 35))
        self.frame_top_btns.setStyleSheet(u"border-bottom: 1px solid rgb(75, 104, 133)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.pushButton = QPushButton(self.frame_label_top_btns)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(24, 24))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.pushButton)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet(u"")
        self.label_title_bar_top.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_8.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setStyleSheet(u"border: none;")
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.btn_close)


        self.horizontalLayout_8.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_top_info.setStyleSheet(u"")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_gr_3 = QPushButton(self.frame_top_info)
        self.pushButton_gr_3.setObjectName(u"pushButton_gr_3")
        self.pushButton_gr_3.setMinimumSize(QSize(0, 25))
        self.pushButton_gr_3.setMaximumSize(QSize(115, 20))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.pushButton_gr_3.setFont(font1)
        self.pushButton_gr_3.setStyleSheet(u"")
        self.pushButton_gr_3.setFlat(True)

        self.horizontalLayout_11.addWidget(self.pushButton_gr_3)

        self.frame_3 = QFrame(self.frame_top_info)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setSpacing(7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 8, 0)
        self.pushButton_login = QPushButton(self.frame_3)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setMinimumSize(QSize(0, 25))
        self.pushButton_login.setMaximumSize(QSize(16777215, 20))
        self.pushButton_login.setFont(font1)
        self.pushButton_login.setStyleSheet(u"")
        self.pushButton_login.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton_login)

        self.pushButton_get_info = QPushButton(self.frame_3)
        self.pushButton_get_info.setObjectName(u"pushButton_get_info")
        self.pushButton_get_info.setMinimumSize(QSize(0, 25))
        self.pushButton_get_info.setMaximumSize(QSize(16777215, 20))
        self.pushButton_get_info.setFont(font1)
        self.pushButton_get_info.setStyleSheet(u"")
        self.pushButton_get_info.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton_get_info)

        self.pushButton_gr = QPushButton(self.frame_3)
        self.pushButton_gr.setObjectName(u"pushButton_gr")
        self.pushButton_gr.setMinimumSize(QSize(0, 25))
        self.pushButton_gr.setMaximumSize(QSize(16777215, 20))
        self.pushButton_gr.setFont(font1)
        self.pushButton_gr.setStyleSheet(u"")
        self.pushButton_gr.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton_gr)

        self.pushButton_get_id = QPushButton(self.frame_3)
        self.pushButton_get_id.setObjectName(u"pushButton_get_id")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_get_id.sizePolicy().hasHeightForWidth())
        self.pushButton_get_id.setSizePolicy(sizePolicy3)
        self.pushButton_get_id.setMinimumSize(QSize(0, 25))
        self.pushButton_get_id.setMaximumSize(QSize(16777215, 20))
        self.pushButton_get_id.setFont(font1)
        self.pushButton_get_id.setToolTipDuration(-3)
        self.pushButton_get_id.setStyleSheet(u"")
        self.pushButton_get_id.setAutoDefault(False)
        self.pushButton_get_id.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton_get_id)

        self.pushButton_view = QPushButton(self.frame_3)
        self.pushButton_view.setObjectName(u"pushButton_view")
        self.pushButton_view.setMinimumSize(QSize(0, 25))
        self.pushButton_view.setMaximumSize(QSize(16777215, 20))
        self.pushButton_view.setFont(font1)
        self.pushButton_view.setStyleSheet(u"")
        self.pushButton_view.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton_view)


        self.horizontalLayout_11.addWidget(self.frame_3, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_top_info)


        self.horizontalLayout_4.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy4)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_7 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setStyleSheet(u"")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_menus)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_7.addWidget(self.frame_menus)

        self.btn_toggle_comment_2 = QPushButton(self.frame_left_menu)
        self.btn_toggle_comment_2.setObjectName(u"btn_toggle_comment_2")
        sizePolicy.setHeightForWidth(self.btn_toggle_comment_2.sizePolicy().hasHeightForWidth())
        self.btn_toggle_comment_2.setSizePolicy(sizePolicy)
        self.btn_toggle_comment_2.setMinimumSize(QSize(0, 65))
        self.btn_toggle_comment_2.setMaximumSize(QSize(70, 65))
        self.btn_toggle_comment_2.setToolTipDuration(-3)
        self.btn_toggle_comment_2.setStyleSheet(u"background-image: url(:/24x24/icon/24x24/cil-comment-square.png);\n"
"background-repeat:none;\n"
"background-position:center;")

        self.verticalLayout_7.addWidget(self.btn_toggle_comment_2)

        self.btn_toggle_comment = QPushButton(self.frame_left_menu)
        self.btn_toggle_comment.setObjectName(u"btn_toggle_comment")
        sizePolicy.setHeightForWidth(self.btn_toggle_comment.sizePolicy().hasHeightForWidth())
        self.btn_toggle_comment.setSizePolicy(sizePolicy)
        self.btn_toggle_comment.setMinimumSize(QSize(0, 65))
        self.btn_toggle_comment.setMaximumSize(QSize(70, 65))
        self.btn_toggle_comment.setToolTipDuration(-3)
        self.btn_toggle_comment.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.btn_toggle_comment)

        self.btn_toggle_options = QPushButton(self.frame_left_menu)
        self.btn_toggle_options.setObjectName(u"btn_toggle_options")
        sizePolicy.setHeightForWidth(self.btn_toggle_options.sizePolicy().hasHeightForWidth())
        self.btn_toggle_options.setSizePolicy(sizePolicy)
        self.btn_toggle_options.setMinimumSize(QSize(0, 65))
        self.btn_toggle_options.setMaximumSize(QSize(70, 65))
        self.btn_toggle_options.setToolTipDuration(-3)
        self.btn_toggle_options.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.btn_toggle_options)


        self.horizontalLayout_18.addWidget(self.frame_left_menu)

        self.stackedWidget_2 = QStackedWidget(self.frame_center)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(0, 0))
        self.stackedWidget_2.setMaximumSize(QSize(350, 16777215))
        self.stackedWidget_2.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_26 = QVBoxLayout(self.page)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(10, 10, 10, 0)
        self.frame_options = QFrame(self.page)
        self.frame_options.setObjectName(u"frame_options")
        self.frame_options.setMinimumSize(QSize(0, 0))
        self.frame_options.setMaximumSize(QSize(370, 16777215))
        self.frame_options.setStyleSheet(u"")
        self.frame_options.setFrameShape(QFrame.NoFrame)
        self.frame_options.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_options)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_options)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 300))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_input_link = QLineEdit(self.frame)
        self.lineEdit_input_link.setObjectName(u"lineEdit_input_link")
        self.lineEdit_input_link.setMinimumSize(QSize(0, 40))
        self.lineEdit_input_link.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_input_link.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.lineEdit_input_link)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(-1, -1, 0, 0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setStyleSheet(u"background-image: url(:/40x40/icon/40x40/angry.png);\n"
"background-repeat : none repeat")

        self.gridLayout_4.addWidget(self.label_2, 0, 7, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(1052, 1250))
        self.label_3.setStyleSheet(u"background-image: url(:/40x40/icon/40x40/Like.png);\n"
"background-repeat : none repeat")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setStyleSheet(u"background-image: url(:/40x40/icon/40x40/loving.png);\n"
"background-repeat : none repeat")

        self.gridLayout_4.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setStyleSheet(u"background-image: url(:/40x40/icon/40x40/tim.png);\n"
"background-repeat : none repeat")

        self.gridLayout_4.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(40, 40))
        self.label_8.setStyleSheet(u"background-image: url(:/40x40/icon/40x40/sad.png);\n"
"background-repeat : none repeat")

        self.gridLayout_4.addWidget(self.label_8, 0, 6, 1, 1)

        self.checkBox_loving = QCheckBox(self.frame)
        self.checkBox_loving.setObjectName(u"checkBox_loving")
        self.checkBox_loving.setMaximumSize(QSize(25, 25))
        self.checkBox_loving.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_loving.setAutoFillBackground(False)
        self.checkBox_loving.setStyleSheet(u"")
        self.checkBox_loving.setChecked(True)
        self.checkBox_loving.setTristate(False)

        self.gridLayout_4.addWidget(self.checkBox_loving, 1, 2, 1, 1)

        self.checkBox_haha = QCheckBox(self.frame)
        self.checkBox_haha.setObjectName(u"checkBox_haha")
        self.checkBox_haha.setMaximumSize(QSize(25, 25))
        self.checkBox_haha.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_haha.setAutoFillBackground(False)
        self.checkBox_haha.setStyleSheet(u"")
        self.checkBox_haha.setChecked(False)
        self.checkBox_haha.setTristate(False)

        self.gridLayout_4.addWidget(self.checkBox_haha, 1, 3, 1, 1)

        self.checkBox_tim = QCheckBox(self.frame)
        self.checkBox_tim.setObjectName(u"checkBox_tim")
        self.checkBox_tim.setMaximumSize(QSize(25, 25))
        self.checkBox_tim.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_tim.setAutoFillBackground(False)
        self.checkBox_tim.setStyleSheet(u"")
        self.checkBox_tim.setChecked(True)
        self.checkBox_tim.setTristate(False)

        self.gridLayout_4.addWidget(self.checkBox_tim, 1, 1, 1, 1)

        self.checkBox_like = QCheckBox(self.frame)
        self.checkBox_like.setObjectName(u"checkBox_like")
        self.checkBox_like.setMaximumSize(QSize(25, 25))
        self.checkBox_like.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_like.setAutoFillBackground(False)
        self.checkBox_like.setStyleSheet(u"")
        self.checkBox_like.setChecked(True)
        self.checkBox_like.setTristate(False)

        self.gridLayout_4.addWidget(self.checkBox_like, 1, 0, 1, 1)

        self.checkBox_sad = QCheckBox(self.frame)
        self.checkBox_sad.setObjectName(u"checkBox_sad")
        self.checkBox_sad.setMaximumSize(QSize(25, 25))
        self.checkBox_sad.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_sad.setAutoFillBackground(False)
        self.checkBox_sad.setStyleSheet(u"")
        self.checkBox_sad.setTristate(False)

        self.gridLayout_4.addWidget(self.checkBox_sad, 1, 6, 1, 1)

        self.checkBox_angry = QCheckBox(self.frame)
        self.checkBox_angry.setObjectName(u"checkBox_angry")
        self.checkBox_angry.setMaximumSize(QSize(25, 25))
        self.checkBox_angry.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_angry.setAutoFillBackground(False)
        self.checkBox_angry.setStyleSheet(u"")
        self.checkBox_angry.setTristate(False)

        self.gridLayout_4.addWidget(self.checkBox_angry, 1, 7, 1, 1)

        self.checkBox_wow = QCheckBox(self.frame)
        self.checkBox_wow.setObjectName(u"checkBox_wow")
        self.checkBox_wow.setMaximumSize(QSize(25, 25))
        self.checkBox_wow.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_wow.setAutoFillBackground(False)
        self.checkBox_wow.setStyleSheet(u"")
        self.checkBox_wow.setTristate(False)

        self.gridLayout_4.addWidget(self.checkBox_wow, 1, 4, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(40, 40))
        self.label_7.setStyleSheet(u"background-image: url(:/40x40/icon/40x40/wow.png);\n"
"background-repeat : none repeat")

        self.gridLayout_4.addWidget(self.label_7, 0, 3, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setStyleSheet(u"background-image: url(:/40x40/icon/40x40/haha.png);\n"
"background-repeat : none repeat")

        self.gridLayout_4.addWidget(self.label_6, 0, 4, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.spinBox_delay_to = QSpinBox(self.frame)
        self.spinBox_delay_to.setObjectName(u"spinBox_delay_to")
        self.spinBox_delay_to.setMinimumSize(QSize(0, 30))
        self.spinBox_delay_to.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        self.spinBox_delay_to.setFont(font2)
        self.spinBox_delay_to.setStyleSheet(u"")
        self.spinBox_delay_to.setAlignment(Qt.AlignCenter)
        self.spinBox_delay_to.setMaximum(3600)
        self.spinBox_delay_to.setValue(3)

        self.gridLayout.addWidget(self.spinBox_delay_to, 0, 3, 1, 1)

        self.label_muiten = QLabel(self.frame)
        self.label_muiten.setObjectName(u"label_muiten")
        self.label_muiten.setMinimumSize(QSize(0, 0))
        self.label_muiten.setMaximumSize(QSize(30, 30))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_muiten.setFont(font3)
        self.label_muiten.setStyleSheet(u"QLabel {\n"
"\n"
"background-image: url(:/16x16/icon/16x16/cil-arrow-right.png);\n"
"background-position: center;\n"
"background-repeat: no-reperat;\n"
"border: none;\n"
"background-color: rgb(75, 104, 133);\n"
"border-radius:5px\n"
"}\n"
"")
        self.label_muiten.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_muiten, 0, 2, 1, 1)

        self.spinBox_delay_from = QSpinBox(self.frame)
        self.spinBox_delay_from.setObjectName(u"spinBox_delay_from")
        self.spinBox_delay_from.setMinimumSize(QSize(0, 30))
        self.spinBox_delay_from.setMaximumSize(QSize(16777215, 30))
        self.spinBox_delay_from.setFont(font2)
        self.spinBox_delay_from.setStyleSheet(u"")
        self.spinBox_delay_from.setAlignment(Qt.AlignCenter)
        self.spinBox_delay_from.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox_delay_from.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.spinBox_delay_from.setMaximum(3600)
        self.spinBox_delay_from.setValue(0)

        self.gridLayout.addWidget(self.spinBox_delay_from, 0, 1, 1, 1)

        self.label_delay = QLabel(self.frame)
        self.label_delay.setObjectName(u"label_delay")
        self.label_delay.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.label_delay.setFont(font4)
        self.label_delay.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_delay, 0, 0, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_page = QCheckBox(self.frame)
        self.checkBox_page.setObjectName(u"checkBox_page")
        self.checkBox_page.setMinimumSize(QSize(0, 0))
        self.checkBox_page.setMaximumSize(QSize(16777215, 30))
        self.checkBox_page.setFont(font4)
        self.checkBox_page.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_page.setAutoFillBackground(False)
        self.checkBox_page.setStyleSheet(u"")
        self.checkBox_page.setTristate(False)

        self.horizontalLayout.addWidget(self.checkBox_page)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_10)

        self.spinBox_page = QSpinBox(self.frame)
        self.spinBox_page.setObjectName(u"spinBox_page")
        self.spinBox_page.setMinimumSize(QSize(0, 30))
        self.spinBox_page.setMaximumSize(QSize(50, 30))
        self.spinBox_page.setFont(font2)
        self.spinBox_page.setStyleSheet(u"")
        self.spinBox_page.setAlignment(Qt.AlignCenter)
        self.spinBox_page.setMaximum(7)
        self.spinBox_page.setValue(2)

        self.horizontalLayout.addWidget(self.spinBox_page)


        self.verticalLayout_22.addLayout(self.horizontalLayout)

        self.checkBox_likeCmt = QCheckBox(self.frame)
        self.checkBox_likeCmt.setObjectName(u"checkBox_likeCmt")
        self.checkBox_likeCmt.setFont(font4)
        self.checkBox_likeCmt.setAutoFillBackground(False)
        self.checkBox_likeCmt.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.checkBox_likeCmt)

        self.checkBox_repCmt = QCheckBox(self.frame)
        self.checkBox_repCmt.setObjectName(u"checkBox_repCmt")
        self.checkBox_repCmt.setFont(font4)
        self.checkBox_repCmt.setAutoFillBackground(False)
        self.checkBox_repCmt.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.checkBox_repCmt)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_timer = QCheckBox(self.frame)
        self.checkBox_timer.setObjectName(u"checkBox_timer")
        self.checkBox_timer.setMinimumSize(QSize(0, 0))
        self.checkBox_timer.setFont(font4)
        self.checkBox_timer.setAutoFillBackground(False)
        self.checkBox_timer.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.checkBox_timer)

        self.spinBox_hour = QSpinBox(self.frame)
        self.spinBox_hour.setObjectName(u"spinBox_hour")
        self.spinBox_hour.setMinimumSize(QSize(0, 30))
        self.spinBox_hour.setFont(font2)
        self.spinBox_hour.setStyleSheet(u"")
        self.spinBox_hour.setAlignment(Qt.AlignCenter)
        self.spinBox_hour.setMaximum(23)
        self.spinBox_hour.setValue(20)

        self.horizontalLayout_2.addWidget(self.spinBox_hour)

        self.label_muiten_2 = QLabel(self.frame)
        self.label_muiten_2.setObjectName(u"label_muiten_2")
        self.label_muiten_2.setMinimumSize(QSize(0, 0))
        self.label_muiten_2.setMaximumSize(QSize(30, 30))
        self.label_muiten_2.setFont(font3)
        self.label_muiten_2.setStyleSheet(u"QLabel {\n"
"\n"
"background-image: url(:/16x16/icon/16x16/cil-arrow-right.png);\n"
"background-position: center;\n"
"background-repeat: no-reperat;\n"
"border: none;\n"
"background-color: rgb(75, 104, 133);\n"
"border-radius:5px\n"
"}\n"
"")
        self.label_muiten_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_muiten_2)

        self.spinBox_miunute = QSpinBox(self.frame)
        self.spinBox_miunute.setObjectName(u"spinBox_miunute")
        self.spinBox_miunute.setMinimumSize(QSize(0, 30))
        self.spinBox_miunute.setFont(font2)
        self.spinBox_miunute.setStyleSheet(u"")
        self.spinBox_miunute.setAlignment(Qt.AlignCenter)
        self.spinBox_miunute.setMaximum(59)
        self.spinBox_miunute.setValue(20)

        self.horizontalLayout_2.addWidget(self.spinBox_miunute)


        self.verticalLayout_22.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(20)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.pushButton_like = QPushButton(self.frame_options)
        self.pushButton_like.setObjectName(u"pushButton_like")
        self.pushButton_like.setMinimumSize(QSize(0, 40))
        self.pushButton_like.setFont(font4)
        self.pushButton_like.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_like.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_like.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color : rgb(255,255,255);\n"
"	border:none;\n"
"	background-color: rgb(75, 104, 133);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	padding-right:3px;\n"
"}")
        self.pushButton_like.setIconSize(QSize(24, 24))
        self.pushButton_like.setCheckable(False)
        self.pushButton_like.setAutoRepeat(False)
        self.pushButton_like.setAutoDefault(False)
        self.pushButton_like.setFlat(False)

        self.gridLayout_2.addWidget(self.pushButton_like, 2, 3, 1, 1)

        self.pushButton_comment = QPushButton(self.frame_options)
        self.pushButton_comment.setObjectName(u"pushButton_comment")
        self.pushButton_comment.setMinimumSize(QSize(0, 40))
        self.pushButton_comment.setFont(font4)
        self.pushButton_comment.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_comment.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color : rgb(255,255,255);\n"
"	border:none;\n"
"	background-color: rgb(75, 104, 133);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	padding-right:3px;\n"
"}")
        self.pushButton_comment.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.pushButton_comment, 3, 0, 1, 1)

        self.pushButton_stop = QPushButton(self.frame_options)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setMinimumSize(QSize(0, 40))
        self.pushButton_stop.setFont(font4)
        self.pushButton_stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_stop.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color : rgb(255,255,255);\n"
"	border:none;\n"
"	background-color: rgb(75, 104, 133);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	padding-right:3px;\n"
"}")
        self.pushButton_stop.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.pushButton_stop, 3, 3, 1, 1)

        self.pushButton_checkvia = QPushButton(self.frame_options)
        self.pushButton_checkvia.setObjectName(u"pushButton_checkvia")
        self.pushButton_checkvia.setMinimumSize(QSize(0, 40))
        self.pushButton_checkvia.setFont(font4)
        self.pushButton_checkvia.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_checkvia.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color : rgb(255,255,255);\n"
"	border:none;\n"
"	background-color: rgb(75, 104, 133);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	padding-right:3px;\n"
"}")
        self.pushButton_checkvia.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.pushButton_checkvia, 2, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)


        self.verticalLayout_26.addWidget(self.frame_options)

        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_27 = QVBoxLayout(self.page_2)
        self.verticalLayout_27.setSpacing(10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(-1, 15, -1, 10)
        self.plainTextEdit_cmt = QPlainTextEdit(self.page_2)
        self.plainTextEdit_cmt.setObjectName(u"plainTextEdit_cmt")
        self.plainTextEdit_cmt.setMinimumSize(QSize(0, 100))
        self.plainTextEdit_cmt.setFont(font2)
        self.plainTextEdit_cmt.setStyleSheet(u"")
        self.plainTextEdit_cmt.setFrameShape(QFrame.NoFrame)
        self.plainTextEdit_cmt.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.verticalLayout_27.addWidget(self.plainTextEdit_cmt)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_cmt = QPushButton(self.page_2)
        self.pushButton_cmt.setObjectName(u"pushButton_cmt")
        self.pushButton_cmt.setMinimumSize(QSize(0, 40))
        self.pushButton_cmt.setMaximumSize(QSize(50000, 300))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(15)
        font5.setBold(True)
        self.pushButton_cmt.setFont(font5)
        self.pushButton_cmt.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color : rgb(255,255,255);\n"
"	border:none;\n"
"	background-color: rgb(75, 104, 133);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	padding-right:3px;\n"
"}")
        self.pushButton_cmt.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.pushButton_cmt)

        self.pushButton_cmt_2 = QPushButton(self.page_2)
        self.pushButton_cmt_2.setObjectName(u"pushButton_cmt_2")
        self.pushButton_cmt_2.setMinimumSize(QSize(0, 40))
        self.pushButton_cmt_2.setMaximumSize(QSize(50000, 300))
        self.pushButton_cmt_2.setFont(font5)
        self.pushButton_cmt_2.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color : rgb(255,255,255);\n"
"	border:none;\n"
"	background-color: rgb(75, 104, 133);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	padding-right:3px;\n"
"}")
        self.pushButton_cmt_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.pushButton_cmt_2)


        self.verticalLayout_27.addLayout(self.horizontalLayout_3)

        self.stackedWidget_2.addWidget(self.page_2)

        self.horizontalLayout_18.addWidget(self.stackedWidget_2)

        self.frame_tab_content = QFrame(self.frame_center)
        self.frame_tab_content.setObjectName(u"frame_tab_content")
        self.frame_tab_content.setMinimumSize(QSize(0, 0))
        self.frame_tab_content.setFrameShape(QFrame.NoFrame)
        self.frame_tab_content.setFrameShadow(QFrame.Plain)
        self.verticalLayout_24 = QVBoxLayout(self.frame_tab_content)
        self.verticalLayout_24.setSpacing(5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 10, 5)
        self.frame_tabwidget = QFrame(self.frame_tab_content)
        self.frame_tabwidget.setObjectName(u"frame_tabwidget")
        self.frame_tabwidget.setStyleSheet(u"")
        self.frame_tabwidget.setFrameShape(QFrame.NoFrame)
        self.frame_tabwidget.setFrameShadow(QFrame.Plain)
        self.verticalLayout_23 = QVBoxLayout(self.frame_tabwidget)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_btn = QFrame(self.frame_tabwidget)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMinimumSize(QSize(0, 70))
        self.frame_btn.setMaximumSize(QSize(16777215, 70))
        self.frame_btn.setFont(font2)
        self.frame_btn.setFrameShape(QFrame.NoFrame)
        self.frame_btn.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btn)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_new_2 = QPushButton(self.frame_btn)
        self.pushButton_new_2.setObjectName(u"pushButton_new_2")
        self.pushButton_new_2.setMinimumSize(QSize(0, 35))
        self.pushButton_new_2.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_new_2.setFont(font)
        self.pushButton_new_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_new_2.setToolTipDuration(-3)
        self.pushButton_new_2.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color : rgb(255,255,255);\n"
"	border:none;\n"
"	background-color: rgb(75, 104, 133);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	padding-right:3px;\n"
"}")
        self.pushButton_new_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_new_2)

        self.pushButton_new = QPushButton(self.frame_btn)
        self.pushButton_new.setObjectName(u"pushButton_new")
        self.pushButton_new.setMinimumSize(QSize(0, 35))
        self.pushButton_new.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_new.setFont(font)
        self.pushButton_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_new.setToolTipDuration(-3)
        self.pushButton_new.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color : rgb(255,255,255);\n"
"	border:none;\n"
"	background-color: rgb(75, 104, 133);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	padding-right:3px;\n"
"}")
        self.pushButton_new.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_new)

        self.pushButton_account = QPushButton(self.frame_btn)
        self.pushButton_account.setObjectName(u"pushButton_account")
        self.pushButton_account.setMinimumSize(QSize(0, 35))
        self.pushButton_account.setFont(font)
        self.pushButton_account.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_account.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color : rgb(255,255,255);\n"
"	border:none;\n"
"	background-color: rgb(75, 104, 133);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	padding-right:3px;\n"
"}")
        self.pushButton_account.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_account)

        self.pushButton_reload = QPushButton(self.frame_btn)
        self.pushButton_reload.setObjectName(u"pushButton_reload")
        self.pushButton_reload.setMinimumSize(QSize(0, 35))
        self.pushButton_reload.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_reload.setFont(font)
        self.pushButton_reload.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_reload.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color : rgb(255,255,255);\n"
"	border:none;\n"
"	background-color: rgb(75, 104, 133);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	padding-right:3px;\n"
"}")
        self.pushButton_reload.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_reload)


        self.verticalLayout_23.addWidget(self.frame_btn)

        self.frame_2 = QFrame(self.frame_tabwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"")
        self.verticalLayout_25 = QVBoxLayout(self.tab)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        icon1 = QIcon()
        icon1.addFile(u":/24x24/icon/24x24/uncheck.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        __qtablewidgetitem.setIcon(icon1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        if (self.tableWidget.rowCount() < 15):
            self.tableWidget.setRowCount(15)
        self.tableWidget.setObjectName(u"tableWidget")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(False)
        self.tableWidget.setFont(font6)
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setIconSize(QSize(0, 0))
        self.tableWidget.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(15)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(28)
        self.tableWidget.verticalHeader().setDefaultSectionSize(28)
        self.tableWidget.verticalHeader().setHighlightSections(True)

        self.verticalLayout_25.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab, "")

        self.horizontalLayout_6.addWidget(self.tabWidget)


        self.verticalLayout_23.addWidget(self.frame_2)


        self.verticalLayout_24.addWidget(self.frame_tabwidget)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(20)
        self.gridLayout_6.setVerticalSpacing(0)
        self.lineEdit = QLineEdit(self.frame_tab_content)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 25))
        font7 = QFont()
        font7.setPointSize(10)
        self.lineEdit.setFont(font7)

        self.gridLayout_6.addWidget(self.lineEdit, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_tab_content)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 25))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setItalic(False)
        self.pushButton_2.setFont(font8)

        self.gridLayout_6.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.label = QLabel(self.frame_tab_content)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setFont(font8)

        self.gridLayout_6.addWidget(self.label, 0, 4, 1, 1)


        self.verticalLayout_24.addLayout(self.gridLayout_6)


        self.horizontalLayout_18.addWidget(self.frame_tab_content)


        self.verticalLayout.addWidget(self.frame_center)

        self.frame_grip = QFrame(self.frame_main)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 30))
        self.frame_grip.setStyleSheet(u"")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setMinimumSize(QSize(0, 0))
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(10, 0, 5, 0)
        self.labelBoxlocation_9 = QLabel(self.frame_label_bottom)
        self.labelBoxlocation_9.setObjectName(u"labelBoxlocation_9")
        self.labelBoxlocation_9.setMinimumSize(QSize(30, 25))
        self.labelBoxlocation_9.setMaximumSize(QSize(30, 20))
        self.labelBoxlocation_9.setFont(font3)
        self.labelBoxlocation_9.setStyleSheet(u"QLabel {\n"
"	background-position: center;\n"
"	background-image: url(:/16x16/icon/16x16/cil-link-broken.png);\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color:transparent\n"
"}\n"
"")

        self.horizontalLayout_26.addWidget(self.labelBoxlocation_9)

        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setMinimumSize(QSize(0, 0))
        font9 = QFont()
        self.label_credits.setFont(font9)
        self.label_credits.setStyleSheet(u"")

        self.horizontalLayout_26.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMinimumSize(QSize(0, 0))
        self.label_version.setMaximumSize(QSize(16777215, 16777215))
        self.label_version.setFont(font9)
        self.label_version.setStyleSheet(u"")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.label_version)


        self.horizontalLayout_25.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(25, 25))
        self.frame_size_grip.setMaximumSize(QSize(25, 25))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icon/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_25.addWidget(self.frame_size_grip)


        self.verticalLayout.addWidget(self.frame_grip)


        self.verticalLayout_6.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_get_id.setDefault(False)
        self.stackedWidget_2.setCurrentIndex(0)
        self.pushButton_like.setDefault(False)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QAuto", None))
#if QT_CONFIG(tooltip)
        self.btn_toggle_menu.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#bcc0c3;\">Giao di\u1ec7n s\u00e1ng</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_toggle_menu.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Xem chi ti\u1ebft phi\u00ean b\u1ea3n t\u1ea1i \u0111\u00e2y", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"MD", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.pushButton_gr_3.setText(QCoreApplication.translate("MainWindow", u"M\u1edf nhi\u1ec1u app", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0103ng nh\u1eadp", None))
        self.pushButton_get_info.setText(QCoreApplication.translate("MainWindow", u"Qu\u00e9t th\u00f4ng tin", None))
        self.pushButton_gr.setText(QCoreApplication.translate("MainWindow", u"Auto join group", None))
#if QT_CONFIG(tooltip)
        self.pushButton_get_id.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>L\u1ea5y id fanpage , trang c\u00e1 nh\u00e2n , group facebook</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_get_id.setText(QCoreApplication.translate("MainWindow", u"Get ID", None))
        self.pushButton_view.setText(QCoreApplication.translate("MainWindow", u"C\u00e0i \u0111\u1eb7t hi\u1ec3n th\u1ecb", None))
#if QT_CONFIG(tooltip)
        self.btn_toggle_comment_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#bcc0c3;\">Nh\u1eadp comment</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_toggle_comment_2.setText("")
#if QT_CONFIG(shortcut)
        self.btn_toggle_comment_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btn_toggle_comment.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#bcc0c3;\">Nh\u1eadp comment</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_toggle_comment.setText("")
#if QT_CONFIG(shortcut)
        self.btn_toggle_comment.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btn_toggle_options.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#bcc0c3;\">C\u00e0i \u0111\u1eb7t chung</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_toggle_options.setText("")
        self.lineEdit_input_link.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp link...", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_5.setText("")
        self.label_4.setText("")
        self.label_8.setText("")
        self.checkBox_loving.setText("")
        self.checkBox_haha.setText("")
        self.checkBox_tim.setText("")
        self.checkBox_like.setText("")
        self.checkBox_sad.setText("")
        self.checkBox_angry.setText("")
        self.checkBox_wow.setText("")
        self.label_7.setText("")
        self.label_6.setText("")
        self.label_muiten.setText("")
        self.label_delay.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e3n c\u00e1ch", None))
        self.checkBox_page.setText(QCoreApplication.translate("MainWindow", u"D\u00f9ng page", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 l\u01b0\u1ee3ng", None))
        self.checkBox_likeCmt.setText(QCoreApplication.translate("MainWindow", u"Like top comment", None))
        self.checkBox_repCmt.setText(QCoreApplication.translate("MainWindow", u"Comment t\u00ecnh hu\u1ed1ng", None))
        self.checkBox_timer.setText(QCoreApplication.translate("MainWindow", u"H\u1eb9n gi\u1edd", None))
        self.label_muiten_2.setText("")
        self.pushButton_like.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ea1y Like", None))
        self.pushButton_comment.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ea1y cmt", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"D\u1eebng", None))
#if QT_CONFIG(shortcut)
        self.pushButton_stop.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_checkvia.setText(QCoreApplication.translate("MainWindow", u"Check Via", None))
        self.plainTextEdit_cmt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp n\u1ed9i dung comment..", None))
        self.pushButton_cmt.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp cmt", None))
#if QT_CONFIG(shortcut)
        self.pushButton_cmt.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_cmt_2.setText(QCoreApplication.translate("MainWindow", u"X\u00e1o tr\u1ed9n cmt", None))
#if QT_CONFIG(tooltip)
        self.pushButton_new_2.setToolTip(QCoreApplication.translate("MainWindow", u"T\u1ea1o file m\u1edbi", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_new_2.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u d\u1eef li\u1ec7u", None))
#if QT_CONFIG(shortcut)
        self.pushButton_new_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButton_new.setToolTip(QCoreApplication.translate("MainWindow", u"T\u1ea1o file m\u1edbi", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_new.setText(QCoreApplication.translate("MainWindow", u"T\u1ea1o file", None))
#if QT_CONFIG(shortcut)
        self.pushButton_new.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButton_account.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_account.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp t\u00e0i kho\u1ea3n", None))
#if QT_CONFIG(shortcut)
        self.pushButton_account.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_reload.setText(QCoreApplication.translate("MainWindow", u"L\u00e0m m\u1edbi", None))
#if QT_CONFIG(shortcut)
        self.pushButton_reload.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip) || QT_CONFIG(whatsthis)
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
#endif
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem.setToolTip(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn t\u1ea5t c\u1ea3", None));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        ___qtablewidgetitem.setWhatsThis(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn t\u1ea5t c\u1ea3", None));
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"STT", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"UID", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"M\u1eadt kh\u1ea9u", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 BM", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Cookie", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"N\u1ed9i dung CMT", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u1ea2nh", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"M\u1eb7c \u0111\u1ecbnh", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm uid...", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Hi\u1ec3n th\u1ecb CP", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"T\u1ed5ng \u0111\u00e3 ch\u1ecdn : 0", None))
        self.labelBoxlocation_9.setText("")
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Registered by: MD ", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"V2.3.1", None))
    # retranslateUi


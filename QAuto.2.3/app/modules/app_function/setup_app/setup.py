from app.modules.packages.pyqt5_modules import *
from app.widget.window import ShowMutipleApp
from pathlib import Path


GLOBAL_STATE = 0

class MainFunction:

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status ==0:
            self.showMaximized()

            GLOBAL_STATE = 1

            self.verticalLayout_6.setContentsMargins(0,0,0,0)

        else:
            GLOBAL_STATE = 0 

            self.verticalLayout_6.setContentsMargins(10,10,10,10)
            self.showNormal()
            self.resize(self.width()+1,self.height()+1)


    def returStatus():
    	return GLOBAL_STATE

    def setupUiMain(self):

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)        


        self.sizegrip = QSizeGrip(self.frame_size_grip)
        self.sizegrip.setStyleSheet(r"QSizeGrip {width:10px;height:10px;margin:7px} ")


    def moveWindow(self,event):
        # MOVE WINDOW
        if MainFunction.returStatus() == 1 :
            MainFunction.maximize_restore(self)        
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self,event):
        self.dragPos = event.globalPos()


    def setUpLogin(self):
        self.menu_login = QMenu()
        ag = QActionGroup(self)
        ag.setExclusive(True)

        self.action_cookie = ag.addAction(QAction('Cookie', self.menu_login,checkable=True,checked=True))
        self.action_uid = ag.addAction( QAction('Uid|Pass|Mã BM', self.menu_login,checkable=True))

        self.menu_login.addAction(self.action_cookie)
        self.menu_login.addAction(self.action_uid)

        return self.menu_login






        #  ### button hiển thị chế độ xem bảng

        # self.pushButton_log.setMenu(self.setUpLogin())

    def setupButton(self):

            

        self.pushButton_cmt.clicked.connect(self.importComment)

        self.pushButton_cmt_2.clicked.connect(self.shuffleComment)

        
        self.pushButton_new_2.clicked.connect(self.modifyAccount)


        #### pushbutton show tạo file mới
        self.pushButton_new.clicked.connect(self.NewFile)


        #### pushbutton show dialog nhập nick
        self.pushButton_account.clicked.connect(self.NewAccount)



        self.pushButton_gr_3.clicked.connect(self.NewApp)


        self.btn_toggle_comment_2.clicked.connect(self.NewComment)

        #### button tải lại danh sách
        self.pushButton_reload.clicked.connect(lambda:self.importAccount(self.tabWidget.tabText(self.indexFile())))


        #### button dừng luồng
        self.pushButton_stop.clicked.connect(self.stop)
        



        #### button checkvia
        self.pushButton_checkvia.clicked.connect(self.checkcookie)

        #### button auto like
        self.pushButton_like.clicked.connect(self.auto_like)

        #### button auto comment
        self.pushButton_comment.clicked.connect(self.auto_comment)

        #### button auto login
        self.pushButton_login.clicked.connect(self.auto_login)

        #### button auto login
        self.pushButton_get_info.clicked.connect(self.get_infomation)


        #### xóa file
        self.tabWidget.tabCloseRequested.connect(lambda currentIndex:self.removeFile(currentIndex))


        #### Phím tắt space chọn checkbox theo selection
        QShortcut(QKeySequence("Space"), self.tabWidget).activated.connect(self.selectCheckbox)

        QShortcut(QKeySequence("Ctrl+N"), self.tabWidget).activated.connect(self.duplicateFile) 

        QShortcut(QKeySequence("Ctrl+W"), self.tabWidget).activated.connect(lambda:self.removeFile(self.tabWidget.currentIndex())) 

        QShortcut(QKeySequence("Ctrl+O"), self.tabWidget).activated.connect(self.NewComment)

        #### Phím tắt f3 chọn sticker
        QShortcut(QKeySequence("F3"), self.tabWidget).activated.connect(self.NewSticker)


        #### Phím tắt f4 chọn sticker
        QShortcut(QKeySequence("F4"), self.tabWidget).activated.connect(self.openImage) 

        ### button tắt appp
        self.btn_close.clicked.connect(self.close)

        ### button thu gọn app xuống thanh sidebar
        self.btn_minimize.clicked.connect(self.showMinimized)

        ### button phóng to app
        self.btn_maximize_restore.clicked.connect(self.maximize_restore)

        ### button chuyển tab
        self.btn_toggle_comment.clicked.connect(lambda:self.stackedWidget_2.setCurrentWidget(self.page_2))
      
        self.btn_toggle_options.clicked.connect(lambda:self.stackedWidget_2.setCurrentWidget(self.page))

        self.btn_toggle_comment_2.clicked.connect(self.NewComment)
        

        ### event dy chuyển cửa sổ 
        self.label_title_bar_top.mouseMoveEvent = self.moveWindow


        ### button đổi giao diện dark - light
        self.btn_toggle_menu.clicked.connect(self.themeChange)




        self.pushButton_view.clicked.connect(self.TableView)

        self.tabWidget.currentChanged.connect(self.lenChecked) #changed tab!


        self.checkBox_page.stateChanged.connect(self.state_changed)



        self.pushButton_2.clicked.connect(lambda:self.view('CP'))

        self.lineEdit.textChanged.connect(self.find_uid)   

        
        

    def state_changed(self):
        if self.checkBox_page.isChecked():
            self.checkBox_repCmt.setChecked(False)
            self.checkBox_likeCmt.setChecked(False)            
            self.checkBox_repCmt.setEnabled(False)
            self.checkBox_likeCmt.setEnabled(False)
        else:            
            self.checkBox_repCmt.setEnabled(True)
            self.checkBox_likeCmt.setEnabled(True)            
        return     



    def closeEvent(self, event):
        message = QMessageBoxX(
            icon="question",
            boldtext="Thoát",
            text="Bạn chắc chắn muốn thoát trương trình",
            ok=True,
            cancel=True,
            stylesheet = self.styleSheet()
            )
        if message.exec() == 1:
            event.accept()
        else:
            event.ignore()

        
    def NewFile(self) :
        ### hiển thị giao diện chọn sticker
        self.newfile = ShowNewFile(self.styleSheet())

        ### gán command tạo file cho button tạo file
        self.newfile.uiFile.pushButton_createfile.clicked.connect(self.createFile)

        self.newfile.uiFile.pushButton_importaccount.clicked.connect(lambda:[self.newfile.close(),self.NewAccount()])

        self.newfile.uiFile.close_account.clicked.connect(self.newfile.close)

        self.newfile.exec()


    def NewAccount(self) :
        ### hiển thị giao diện chọn sticker
        self.form_account = ShowNewAccount(self.styleSheet())


        ### setup combobox cửa sổ nhập tài khoản

        self.form_account.uiAccount.comboBox_file.addItems(self.tabWidget.tabText(i) for i in range(self.tabWidget.count()))
        self.form_account.uiAccount.comboBox_file.setCurrentText(self.tabWidget.tabText(self.indexFile()))

        # xóa item mặc định
        index = self.form_account.uiAccount.comboBox_file.findText("Mặc định")
        self.form_account.uiAccount.comboBox_file.removeItem(index)
        
        # ### setup button cửa sổ nhập tài khoản

        # button tắt cửa sổ 
        self.form_account.uiAccount.pushButton_close.clicked.connect(self.form_account.close)

        # button thêm file mới
        self.form_account.uiAccount.pushButton_newfile.clicked.connect(self.NewFile)
        
        # button nhập tài khoản
        self.form_account.uiAccount.pushButton_save.clicked.connect(lambda:self.saveNewAcount()) 

        self.form_account.uiAccount.close_account.clicked.connect(self.form_account.close)

        self.form_account.exec()





    def TableView(self):
        ### hiển thị giao diện cài đặt hiển thị nick
        self.form_tableview = ShowTableView(self.styleSheet())  
        self.form_tableview.close_account.clicked.connect(self.form_tableview.close)
        self.form_tableview.pushButton.clicked.connect(self.ViewTable)
        self.form_tableview.exec() 

        

    def NewSticker(self) :
        ### hiển thị giao diện chọn sticker
        index = self.indexFile()
        file = self.tabWidget.tabText(index)

        self.sticker = StickerWindow(self.tableList[file]['table']) 
        self.sticker.show()    

    def NewComment(self):
        self.commentWindow = ShowComment()
        
        self.commentWindow.setWindowIcon(QIcon(':/ico/icon/coffee.ico'))

        self.commentWindow.ui.pushButton_cmt.clicked.connect(self.importComment_dialog)

        self.commentWindow.ui.pushButton_cmt_2.clicked.connect(self.shuffleComment_dialog)

        self.commentWindow.show()

        
    def NewApp(self):
        self.newapp = ShowMutipleApp()
        
        self.newapp.setWindowIcon(QIcon(':/ico/icon/coffee.ico'))
        self.newapp.ui.pushButton_newapp.clicked.connect(self.mutilpleApp)
        self.newapp.show()








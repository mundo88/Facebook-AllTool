from app.modules.packages.pyqt5_modules import *
import os
from pathlib import Path
import shutil


class Table(object):

    def indexFile(self):
        return self.tabWidget.currentIndex()



    def setupTable(self):

        self.checked = True

        #thêm tab
        [self.addProjectTab(i.replace('.txt','')) for i in os.listdir('data')]

        self.hidenColumn()
        index = self.indexFile()
        self.tableList[self.tabWidget.tabText(index)] = {'table':self.tableWidget ,'checkbox':''}
        self.tabWidget.setTabVisible(0, False)
 
        
        

        # set button context menu policy
        self.frame_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.frame_2.customContextMenuRequested.connect(lambda point:self.context_menu_table(point))

        
            

        for i in range(self.tabWidget.count()):
            self.importAccount(self.tabWidget.tabText(i))     



    @QtCore.pyqtSlot()
    def importAccount(self,file:str) ->str:
        path = f"data/{file}.txt"

        if os.path.isfile(path):
            with open(path,'r',encoding = 'utf-8') as f :
                datas =  list(filter(None,f.readlines()))
        else:
            self.tableList[file]['table'].setRowCount(0)
            return    
        count = len(datas)
        self.tableList[file]['table'].setRowCount(count)

        list_cb = list()

        for i in range(count):

            self.tableList[file]['table'].setRowHidden(i, False)
            
            self.checkbox_item = QTableWidgetItem()

            self.checkbox_item.setCheckState(Qt.Unchecked)
            
            list_cb.append(self.checkbox_item)   


            stt = QTableWidgetItem(str(i+1))
            stt.setTextAlignment(Qt.AlignCenter) 
            

            name = datas[i].split('|')[0].strip()

            uid = datas[i].split('|')[1].strip()
            password = datas[i].split('|')[2].strip()
            _2fa = datas[i].split('|')[3].strip()
            cookie = datas[i].split('|')[4].strip()


            self.tableList[file]['table'].setItem(i, 0, self.checkbox_item) 

            self.tableList[file]['table'].setItem(i, 1, stt)

            self.tableList[file]['table'].setItem(i, 2, QTableWidgetItem(name))

            self.tableList[file]['table'].setItem(i, 3, QTableWidgetItem(uid))

            self.tableList[file]['table'].setItem(i, 4, QTableWidgetItem(password))

            self.tableList[file]['table'].setItem(i, 5, QTableWidgetItem(_2fa))

            self.tableList[file]['table'].setItem(i, 6, QTableWidgetItem(cookie))

            self.tableList[file]['table'].setItem(i, 7, QTableWidgetItem(''))

            self.tableList[file]['table'].setItem(i, 8, QTableWidgetItem(''))

            self.tableList[file]['table'].setItem(i, 9, QTableWidgetItem(''))

        self.tableList[file]['checkbox'] = list_cb
        self.lenChecked()

        return    
    

    def saveNewAcount(self):
        file = self.form_account.uiAccount.comboBox_file.currentText()
        plainText = self.form_account.uiAccount.plainTextEdit_acc.toPlainText()
        account = list(filter(None,plainText.split('\n')))
        datas = list()
        if len(account) == 0 :
            message = QMessageBoxX(
                icon="warning",
                boldtext="Tài khoản trống",
                text="Vui lòng nhập nick vào ô trống",
                ok=True,
                cancel=False,
                stylesheet = self.styleSheet()
                )
            message.exec()
            return
        elif self.form_account.uiAccount.comboBox_file.currentText() =='':
            message = QMessageBoxX(
                icon="warning",
                boldtext="File not found",
                text="Vui lòng chọn file trước khi nhập nick",
                ok=True,
                cancel=False,
                stylesheet = self.styleSheet()
                )
            message.exec()

            return     
        elif  self.form_account.uiAccount.comboBox.currentText() == 'Cookie':
            if 'c_user' not in plainText.strip() or '|' in plainText.strip() :
                message = QMessageBoxX(
                    icon="warning",
                    boldtext="Sai định dạng",
                    text="Vui lòng chọn đúng định dạng nhập nick",
                    ok=True,
                    cancel=False,
                    stylesheet = self.styleSheet()
                    )
                message.exec()
                return 
            for cookie in account:    
                name = ''
                uid = cookie.split('c_user=')[-1].split(';')[0]
                password = ''
                _2fa = ''
                data = f'{name}|{uid}|{password}|{_2fa}|{cookie}'
                datas.append(data)
        elif  self.form_account.uiAccount.comboBox.currentText() == 'Uid|pass|2fa|cookie':
            if '|' not in plainText.strip().strip():
                message = QMessageBoxX(
                    icon="warning",
                    boldtext="Sai định dạng",
                    text="Vui lòng chọn đúng định dạng nhập nick",
                    ok=True,
                    cancel=False,
                    stylesheet = self.styleSheet()
                    )
                message.exec()
                return 
            for text in account:    
                name = ''
                uid = text.split('|')[0]
                password = text.split('|')[1]
                _2fa = text.split('|')[2]
                cookie = text.split('|')[3]
                data = f'{name}|{uid}|{password}|{_2fa}|{cookie}'
                datas.append(data)       


        with open('data/'+file+'.txt','a',encoding='utf-8') as f:
            for data in datas:
                f.write(data+'\n')

        message = QMessageBoxX(
            icon="information",
            boldtext="Nhập thành công",
            text=f"Nhập thành công {len(datas)} tài khoản",
            ok=True,
            cancel=True,
            stylesheet = self.styleSheet()
            )
        message.exec()
      
        
        if message !=1:
        	self.form_account.close()
        for i in range(self.tabWidget.count()):
            if self.tabWidget.tabText(i) == file:
                self.tabWidget.setCurrentIndex(i)

        self.importAccount(file)

        return
    

    def createFile(self):
        index = self.indexFile()
        file = self.newfile.uiFile.lineEdit_file.text().strip()
        if os.path.isfile(f"data/{file}.txt"):
            message = QMessageBoxX(
                icon="warning",
                boldtext="File đã tồn tại",
                text=f"File {file} đã tồn tại, vui lòng chọn tên khác",
                ok=True,
                cancel=False,
                stylesheet = self.styleSheet()
                )
            message.exec()
            return
        elif file =='' and file != 'Mặc định':   
            message = QMessageBoxX(
                icon="warning",
                boldtext="Cảnh báo",
                text=f"Không thể tạo file",
                ok=True,
                cancel=False,
                stylesheet = self.styleSheet()
                )
            message.exec()    
            return

        elif '/' in file or '\\' in file:   
            message = QMessageBoxX(
                icon="warning",
                boldtext="Lỗi kí tự",
                text=f"Không thể tạo file",
                ok=True,
                cancel=False,
                stylesheet = self.styleSheet()
                )
            message.exec()    
            return 

        else:  
            open(f'data/{file}.txt','w+',encoding='utf-8').close()

        message = QMessageBoxX(
            icon="information",
            boldtext="Tạo thành công",
            text=f"Tạo thành công file {file}",
            ok=True,
            cancel=False,
            stylesheet = self.styleSheet()
            )
        message.exec()  

        
        self.tabWidget.setCurrentIndex(self.addProjectTab(file))


        try:
            self.form_account.uiAccount.comboBox_file.insertItem(-1,file)
            self.form_account.uiAccount.comboBox_file.setCurrentText(file)
        except:
            pass
        self.newfile.close()
        return

    def duplicateFile(self):
        index = self.indexFile()
        file = self.tabWidget.tabText(index)
        current_folder = f"{Path().absolute()}//data//"
        path_defout  = f"{current_folder}{file}.txt"
        uniq = 1
        path = path_defout
        while os.path.exists(path):
            path = f'{current_folder}{file}{uniq}.txt'
            uniq += 1
        shutil.copyfile(path_defout, path)
        self.tabWidget.setCurrentIndex(self.addProjectTab(tabname=file+str(uniq-1)))
        self.importAccount(file+str(uniq-1))

    def modifyAccount(self):
        index = self.indexFile()
        file = self.tabWidget.tabText(index)
        if file == '' or file == 'Mặc định':
            message = QMessageBoxX(
                icon="warning",
                boldtext="Cảnh báo",
                text=f"Lỗi không thể lưu",
                ok=True,
                cancel=False,
                stylesheet = self.styleSheet()
                )
            message.exec_() 
            return         
        with open(f'data/{file}.txt','w',encoding='utf-8') as f:
            for row in range(self.tableList[file]['table'].rowCount()):
                name = self.tableList[file]['table'].item(row,2).text().strip()
                uid  = self.tableList[file]['table'].item(row,3).text().strip()
                password = self.tableList[file]['table'].item(row,4).text().strip()
                _2fa = self.tableList[file]['table'].item(row,5).text().strip()
                cookie = self.tableList[file]['table'].item(row,6).text().strip()
                data = f'{name}|{uid}|{password}|{_2fa}|{cookie}\n'
                f.write(data)
        message = QMessageBoxX(
            icon="information",
            boldtext="Lưu thành công",
            text=f"Cập nhật dữ liệu thành công",
            ok=True,
            cancel=False,
            stylesheet = self.styleSheet()
            )
        message.exec_() 
    

    @QtCore.pyqtSlot()
    def removeFile(self,currentIndex):

        file = self.tabWidget.tabText(currentIndex).strip() 
        if file =='':
            message = QMessageBoxX(
                icon="warning",
                boldtext="Cảnh báo",
                text=f"Không thể xóa file {file}",
                ok=True,
                cancel=False,
                stylesheet = self.styleSheet()
                )
            message.exec()             
            return
        message = QMessageBoxX(
            icon="question",
            boldtext="Xóa file",
            text=f"Bạn chắc chắn muốn xóa file {file}",
            ok=True,
            cancel=True,
            stylesheet = self.styleSheet()
            )
        
        if message.exec() == 1 and file != 'Mặc định':
            os.remove(f"data/{file}.txt")
            self.tabWidget.removeTab(currentIndex)

            self.tableList.pop(file)
        return


    def selectCheckbox(self):
        ind = self.indexFile()
        key = self.tabWidget.tabText(ind)
        try:
            indexes = list(set(index.row() for index in self.tableList[key]['table'].selectedIndexes()))
            for index in indexes:
                if self.tableList[key]['checkbox'][index].checkState() == Qt.Unchecked:
                    self.tableList[key]['checkbox'][index].setCheckState(Qt.Checked)
                else:
                    self.tableList[key]['checkbox'][index].setCheckState(Qt.Unchecked)
        except Exception as e :
            print(e)
        self.lenChecked()
        return 
    

    def getChecked(self):
        index = self.indexFile()
        file = self.tabWidget.tabText(index)
        return [check_box.row() for check_box in self.tableList[file]['checkbox'] if check_box.checkState() == Qt.Checked]
        
    def lenChecked(self):
        self.label.setText('Tổng số nick đã chọn : '+str(len(self.getChecked())))
        self.find_uid()
    


    def onHeaderClicked(self, logicalIndex):
        index = self.indexFile()
        file = self.tabWidget.tabText(index)
        checkbox = self.tableList[file]['checkbox']
        path = ":/24x24/icon/24x24/uncheck.png"

        if logicalIndex == 0:
            if self.checked:
                for cb in checkbox:
                    cb.setCheckState(QtCore.Qt.Checked) 
                self.checked = False
                path = ":/24x24/icon/24x24/checked.png"

            else:
                self.checked = True  
                path = ":/24x24/icon/24x24/uncheck.png"
 
                for cb in checkbox:
                    cb.setCheckState(QtCore.Qt.Unchecked)

                    
        item_ = QTableWidgetItem()
        icon = QIcon()
        icon.addPixmap(QPixmap(path))
        item_.setIcon(icon)   

        self.tableList[file]['table'].setHorizontalHeaderItem(0, item_)
        self.lenChecked()

    @QtCore.pyqtSlot()
    def chooseRow(self,selection):
        index = self.indexFile()
        file = self.tabWidget.tabText(index)
        [cb.setCheckState(Qt.Unchecked) for cb in self.tableList[file]['checkbox']]
        [self.tableList[file]['checkbox'][row].setCheckState(Qt.Checked) for row in selection]
        self.lenChecked()


    def importComment(self):
        index = self.indexFile()
        content = list(filter(None,self.plainTextEdit_cmt.toPlainText().split('\n'))) 
        file = self.tabWidget.tabText(index)
        cblist =  self.getChecked()
        for i in range(len(cblist)):
            try:
                self.tableList[file]['table'].setItem(cblist[i],7,QTableWidgetItem(content[i]))
            except:
                break
        self.stackedWidget_2.setCurrentWidget(self.page)
        return

    def importComment_dialog(self):
        index = self.indexFile()
        content = list(filter(None,self.commentWindow.ui.plainTextEdit.toPlainText().split('\n'))) 
        file = self.tabWidget.tabText(index)
        cblist =  self.getChecked()
        for i in range(len(cblist)):
            try:
                self.tableList[file]['table'].setItem(cblist[i],7,QTableWidgetItem(content[i]))
            except:
                break
        self.stackedWidget_2.setCurrentWidget(self.page)
        return


    def deleteValue(self):
        index = self.indexFile()
        file = self.tabWidget.tabText(index)
        selection = list(set(self.tableList[file]['table'].selectedIndexes()))
        colum = self.tableList[file]['table'].currentColumn()
        for r in selection:
            item = QTableWidgetItem("")
            self.tableList[file]['table'].setItem(r.row(), colum, item)


    def value(self):
        index = self.indexFile()
        rows = self.getChecked()
        file = self.tabWidget.tabText(index)
        datas = list()
        for row in rows:
            uid  = self.tableList[file]['table'].item(row,3).text().strip()
            password = self.tableList[file]['table'].item(row,4).text().strip()
            _2fa = self.tableList[file]['table'].item(row,5).text().strip()
            cookie = self.tableList[file]['table'].item(row,6).text().strip()
            content = self.tableList[file]['table'].item(row,7).text().strip()
            image = self.tableList[file]['table'].item(row,8).text().strip()
            data = f'{row}|{uid}|{password}|{_2fa}|{cookie}|{content}|{image}|'
            datas.append(data)

        return datas
        

    def openImage(self):
        index = self.indexFile()
        file = self.tabWidget.tabText(index)
        row = self.tableList[file]['table'].currentRow()
        if self.tableList[file]['table'].currentColumn() == 8:
            fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Image Files (*.jpg);;Image Files (*.png);;Image Files (*.jpeg);;All Files (*)")
            if fileName:
                self.tableList[file]['table'].setItem(row,8,QTableWidgetItem(fileName))
        return


    def removeAccount(self):
        index = self.indexFile()
        file = self.tabWidget.tabText(index)
        remove_list = []
        index_list = [QtCore.QPersistentModelIndex(model_index) for model_index in self.tableList[file]['table'].selectionModel().selectedRows()]

        try:
            files = f'data/{file}.txt'
            with open(files,'r+',encoding='utf-8') as f :
                datas = list(filter(None,[i.replace('\n','') for i in f.readlines()]))
            for index in index_list:
                name = self.tableList[file]['table'].item(index.row(),2).text().strip()
                uid  = self.tableList[file]['table'].item(index.row(),3).text().strip()
                password = self.tableList[file]['table'].item(index.row(),4).text().strip()
                _2fa = self.tableList[file]['table'].item(index.row(),5).text().strip()
                cookie = self.tableList[file]['table'].item(index.row(),6).text().strip()
                data = f'{name}|{uid}|{password}|{_2fa}|{cookie}'  
                self.tableList[file]['table'].removeRow(index.row())              
                remove_list.append(data) 


            list_cb = []    
            for i in range(self.tableList[file]['table'].rowCount()):
                stt = QTableWidgetItem(str(i+1))
                stt.setTextAlignment(Qt.AlignCenter) 
                self.tableList[file]['table'].setItem(i, 1, stt)
                self.checkbox_item = QTableWidgetItem()
                self.checkbox_item.setCheckState(Qt.Unchecked)
                list_cb.append(self.checkbox_item) 
                self.tableList[file]['table'].setItem(i, 0, self.checkbox_item) 
            self.tableList[file]['checkbox'] = list_cb 


            for data in remove_list:
                datas.remove(data)

            with open(files,'w+',encoding='utf-8') as f :
                for re in datas:
                    f.write(re+'\n')
        except Exception as e:
            print(e)
        return

    
    def shuffleComment(self):
        comment = list(filter(None,self.plainTextEdit_cmt.toPlainText().split('\n')))
        random.shuffle(comment)
        self.plainTextEdit_cmt.setPlainText('\n'.join(comment))

    def shuffleComment_dialog(self):
        comment = list(filter(None,self.commentWindow.ui.plainTextEdit.toPlainText().split('\n')))
        random.shuffle(comment)
        self.commentWindow.ui.plainTextEdit.setPlainText('\n'.join(comment))

        
    @QtCore.pyqtSlot()
    def view(self,text):
        index = self.indexFile()
        file = self.tabWidget.tabText(index)
        for row in range(self.tableList[file]['table'].rowCount()):
            if text == 'CP':
                item = self.tableList[file]['table'].item(row, 9)
                self.tableList[file]['table'].setRowHidden(row, text not in item.text())
            else:
               self.tableList[file]['table'].setRowHidden(row, False)
               
        if text =='CP' :       
            self.pushButton_2.clicked.connect(lambda:self.view('All'))
            self.pushButton_2.setText('Hiển thị tất cả nick')
        else:
            self.pushButton_2.clicked.connect(lambda:self.view('CP'))
            self.pushButton_2.setText('Hiển thị nick check point')
        return


    def ViewTable(self):
        data= {
            "stt":        self.form_tableview.stt.isChecked(),
            "name":       self.form_tableview.name.isChecked(),
            "uid":        self.form_tableview.uid.isChecked(),
            "pass":       self.form_tableview.passw.isChecked(),
            "2fa":        self.form_tableview._2fa.isChecked(),
            "cookie":     self.form_tableview.cookie.isChecked(),
            "comment":    self.form_tableview.comment.isChecked(),
            "img":        self.form_tableview.img.isChecked(),
            "status":     self.form_tableview.status.isChecked()
            }
        json_object = json.dumps(data, indent = 4)
        with open("settings/table.json", "w") as outfile:
            outfile.write(json_object)          
        self.hidenColumn()    
        message = QMessageBoxX(
            icon="information",
            boldtext="Đã lưu",
            text=f"Lưu thành công chế độ hiển thị bảng",
            ok=True,
            cancel=False,
            stylesheet = self.styleSheet()
            )
        message.exec()
    @QtCore.pyqtSlot()  
    def hidenColumn(self):
        with open('settings/table.json', 'r') as openfile:
            view = json.load(openfile)
        for key in self.tableList:
            self.tableList[key]['table'].setColumnHidden(1,view['stt'] is not True)   
            self.tableList[key]['table'].setColumnHidden(2,view['name']is not True)       
            self.tableList[key]['table'].setColumnHidden(3,view['uid']is not True)
            self.tableList[key]['table'].setColumnHidden(4,view['pass']is not True)
            self.tableList[key]['table'].setColumnHidden(5,view['2fa']is not True)
            self.tableList[key]['table'].setColumnHidden(6,view['cookie']is not True)
            self.tableList[key]['table'].setColumnHidden(7,view['comment']is not True)
            self.tableList[key]['table'].setColumnHidden(8,view['img']is not True)
            self.tableList[key]['table'].setColumnHidden(9,view['status']is not True)


    def addProjectTab(self,tabname):
        tab = QWidget()
        
        horizontalLayout = QHBoxLayout(tab)
        horizontalLayout.setContentsMargins(0, 2, 0, 0)
        horizontalLayout.setSpacing(0)  

        self.tableWidget = QTableWidget(tab)
        self.tableList[tabname] = {'table':self.tableWidget ,'checkbox':''}

        horizontalLayout.addWidget(self.tableWidget)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)        
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.verticalHeader().setVisible(False)
        
        _translate = QtCore.QCoreApplication.translate





        item = QTableWidgetItem()
        icon10 = QIcon()
        icon10.addPixmap(QPixmap(":/24x24/icon/24x24/uncheck.png"), QIcon.Normal, QIcon.Off)
        item.setIcon(icon10)
        item.setToolTip(_translate("MainWindow", "Chọn tất cả"))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item) 

        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item) 

        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)

        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)

        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)

        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "STT"))

        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tên"))

        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "UID"))

        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Mật khẩu"))

        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Mã BM"))

        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Cookie"))

        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Nội dung CMT"))

        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Ảnh"))

        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Trạng thái"))

        self.tableWidget.horizontalHeader().setDefaultSectionSize(110)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(28)
        self.tableWidget.setColumnWidth(0, 30)
        self.tableWidget.setColumnWidth(1, 40)


        self.tableWidget.horizontalHeader().sectionClicked.connect(lambda logicalIndex :self.onHeaderClicked(logicalIndex))
        
        self.tableWidget.doubleClicked.connect(lambda:self.openImage())

        
        with open('settings/table.json', 'r') as openfile:
            view = json.load(openfile)
        for key in self.tableList:
            self.tableWidget.setColumnHidden(1,view['stt'] is not True)   
            self.tableWidget.setColumnHidden(2,view['name']is not True)       
            self.tableWidget.setColumnHidden(3,view['uid']is not True)
            self.tableWidget.setColumnHidden(4,view['pass']is not True)
            self.tableWidget.setColumnHidden(5,view['2fa']is not True)
            self.tableWidget.setColumnHidden(6,view['cookie']is not True)
            self.tableWidget.setColumnHidden(7,view['comment']is not True)
            self.tableWidget.setColumnHidden(8,view['img']is not True)
            self.tableWidget.setColumnHidden(9,view['status']is not True)

        return self.tabWidget.addTab(tab, tabname)

    
    def context_menu_table(self, point):
        index = self.indexFile()
        file = self.tabWidget.tabText(index)
        ### gán context menu cho table widget


        # get số dòng được quét trên table
        selection = [r.row() for r in self.tableList[file]['table'].selectedIndexes()]
        selection.sort()
        selection = list(set(selection))
        r = len(selection)

        ### tạo menu cho table widget
        self.MenuTable = QMenu(self.frame_2)


        # chọn các dòng đã bôi đen
        choose_row = QAction(f'Chọn {r} dòng bôi đen ++',self)

        choose_row.setShortcut('Space')

        choose_row.triggered.connect(lambda action: self.chooseRow(selection))

        self.MenuTable.addAction(choose_row) 

        # chọn tất cả các dòng
        choose_row_all = QAction('Chọn tất cả', self)
        
        choose_row_all.triggered.connect(lambda action:self.onHeaderClicked(0))

        self.MenuTable.addAction(choose_row_all) 



        # bỏ chọn tất cả các dòng
        deselect_all = QAction('Bỏ chọn tất cả', self)
        
        deselect_all.triggered.connect(lambda action:self.onHeaderClicked(0))
        
        self.MenuTable.addAction(deselect_all) 

        # tải lại table
        _reload = QAction('Làm mới bảng', self)

        _reload.setShortcut('F5')

        _reload.triggered.connect(lambda action:self.importAccount(file))

        self.MenuTable.addAction(_reload) 

        # duplicate files
        _duplicate = QAction('Nhân đôi tab', self)

        _duplicate.setShortcut('Ctrl+N')

        _duplicate.triggered.connect(lambda action:self.duplicateFile())

        self.MenuTable.addAction(_duplicate) 


        self.MenuTable.addSeparator()

        # mở MenuTable chọn sticker
        show_sticker = QAction('Chọn sticker', self)
        show_sticker.setShortcut('F3')
        show_sticker.triggered.connect(lambda action:self.NewSticker())
        self.MenuTable.addAction(show_sticker) 


        # chọn ảnh 
        show_image = QAction('Chọn ảnh', self)

        show_image.setShortcut('F4')

        show_image.triggered.connect(lambda action:self.openImage())

        self.MenuTable.addAction(show_image) 

        self.MenuTable.addSeparator()


        # MenuTable phân nhánh hiển thị
        self.view_menu = QMenu(self.frame_2)

        # chọn dòng
        self.view_menu.setTitle('Hiển thị')

        self.MenuTable.addMenu(self.view_menu)

        view_cp = QAction('Hiển thị CP', self)

        view_cp.triggered.connect(lambda action:self.view('CP'))

        self.view_menu.addAction(view_cp)

        view_all = QAction('Hiển thị tất cả', self)

        view_all.triggered.connect(lambda action:self.view('all'))

        self.view_menu.addAction(view_all)

        self.MenuTable.addSeparator()


        # Xóa tài khoản
        removeRow = QAction(f'Xóa {r} tài khoản bôi đen', self) 
        removeRow.triggered.connect(lambda action:self.removeAccount())

        self.MenuTable.addAction(removeRow)


        
        # hiển thị menu 
        self.MenuTable.exec_(self.frame_2.mapToGlobal(point))   


    def keyPressEvent(self, event):
        ### sự kiện copy và xóa trên table widget
        index = self.indexFile()
        file = self.tabWidget.tabText(index)
        self.tableList[file]['table'].keyPressEvent(event)
        
        if event.key() == Qt.Key.Key_C and (event.modifiers() & Qt.KeyboardModifier.ControlModifier):
            index_list = [QtCore.QPersistentModelIndex(model_index) for model_index in self.tableList[file]['table'].selectionModel().selectedRows()]
            copy_text = ''
            for c in index_list:
                text = self.tableList[file]['table'].item(c.row(), 7).text()+'\n'
                if text.strip() != '':
                    copy_text += text
            QApplication.clipboard().setText(copy_text)
         ### dán item    
        elif event.key() == Qt.Key_V and (event.modifiers() & Qt.ControlModifier):
            text = QApplication.clipboard().text().split('\n')
            i = 0
            index_list = [QtCore.QPersistentModelIndex(model_index) for model_index in self.tableList[file]['table'].selectionModel().selectedRows()]
            for cell in index_list:
                try:
                    self.tableList[file]['table'].setItem(cell.row(),7, QTableWidgetItem(text[i]))
                    i+=1
                except Exception as e:
                    pass
        ### xóa item
        elif event.type() == QEvent.KeyPress and event.matches(QKeySequence.Delete):
            self.deleteValue()
        return

    def find_uid(self):
        name = self.lineEdit.text().strip()

        index = self.indexFile()
        file = self.tabWidget.tabText(index)

        for row in range(self.tableList[file]['table'].rowCount()):
            item = self.tableList[file]['table'].item(row, 3)
            self.tableList[file]['table'].setRowHidden(row, name not in item.text())  
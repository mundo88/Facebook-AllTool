from app.modules.app_ui.main_ui import *

from app.modules.packages.pyqt5_modules import *

from app.tool.cookie_func import *

from app.tool.auto_like import *

from app.tool.auto_comment import *

from app.tool.auto_login import *

from app.tool.get_info import *

from concurrent.futures import ThreadPoolExecutor, as_completed


import concurrent.futures.thread

import urllib.request

# from pyunpack import Archive
# from patoolib import extract_archive



import shutil

stop_thread = False

from dowload_ui import *


class Stop:
    def stop(self):
        global stop_thread
        stop_thread = True
        message = QMessageBoxX(
            icon="information",
            boldtext="Dừng",
            text=f"Đã dừng luồng",
            ok=True,
            cancel=False,
            stylesheet = self.styleSheet()
            )
        message.exec()     
        return


class MainWindow(QMainWindow,
                Ui_MainWindow,
                MainFunction,
                SettingsMain,
                Table,Settings,
                Stop
    ):
    """docstring for MainWindow"""
    
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)

        self.theme_path = self.getPath('theme.json')

        self.table_path = self.getPath('table.json')

        read_theme = self.readSettings(self.theme_path)


        self.theme = read_theme['theme']
        self.setSize = read_theme['size']
        self.theme_state = read_theme['state']
        if self.theme== 'light':
            self.setStyleSheet(style.light_theme)
        else:
            self.setStyleSheet(style.dark_theme)

        self.resize(self.setSize[0], self.setSize[1])
            
        print(self.setSize)
        self.tableList = dict()


        #### setup main window

        self.setupUi(self)


        self.setupUiMain()

        self.setupTime()

        self.setupTable()

        self.setupButton()

        

        self.pushButton_get_id.clicked.connect(lambda:self.open_getid(
                                    'https://github.com/modunn/Qc/releases/download/1.0/Qid.zip',
                                    'Qid'))
       



        self.pushButton_gr.clicked.connect(lambda:self.open_qjoingroup(
                                        'https://github.com/modunn/Qc/releases/download/1.0/QJoinGroup.zip',
                                        'QJoinGroup'))



        self.pushButton.clicked.connect(self.version)


    def resizeEvent(self, event):
        data = self.readSettings(self.theme_path)

        data["size"] = (self.width(),self.height())
        self.writeSettings(self.theme_path,data)
        QMainWindow.resizeEvent(self, event)


    def mutilpleApp(self):
        path = f"{Path().absolute()}\QMain.exe"
        count = self.newapp.ui.spinBox.value()
        for i in range(count):
            os.startfile(path)

        message = QMessageBoxX(
            icon="information",
            boldtext="Đã xong",
            text=f"Đã mở xong {count} app",
            ok=True,
            cancel=False,
            stylesheet = self.styleSheet()
            )
        message.exec()
        return


    @QtCore.pyqtSlot(int,int, str,str,str,bool)
    def status(self,row,column,text,color,file,boolean=False)  :


        if color=='blue':
            if self.theme_state: 
                r,g,b = (0, 0, 255)
            else:
                r,g,b = (136, 194, 247)

        elif color=='red':
            if self.theme_state: 
                r,g,b = (255, 0, 0)
            else:
                r,g,b = (255, 117, 117)  
        elif color =='normal':
            if self.theme_state: 
                r,g,b = (0, 0, 0)
            else:
                r,g,b = (255, 255, 255) 

        it = QTableWidgetItem(text)
        it.setForeground(QBrush(QColor(r,g,b)))   
        self.tableList[file]['table'].setItem(row, column, it)    

        if boolean:
            try:
                self.tableList[file]['checkbox'][row].setCheckState(QtCore.Qt.Unchecked)
            except:
                pass



    def readSettings(self,path):
        with open(path, 'r') as openfile:
            json_object = json.load(openfile) 
        return json_object

    def writeSettings(self,json_file,item):
        json_object = json.dumps(item, indent = 4)
        with open(json_file, "w") as outfile:
            outfile.write(json_object)  

    def themeChange(self):
        if self.theme_state:
            self.setStyleSheet(style.dark_theme)
            self.theme = 'dark'
            self.theme_state = False
        else:
            self.theme = 'light'
            self.theme_state = True
            self.setStyleSheet(style.light_theme)
        data= {'theme':self.theme,'state':self.theme_state}  
        data['size'] = (self.width(),self.height())
        self.writeSettings(self.theme_path,data)  

    def checkcookie(self):
        global stop_thread

        stop_thread = False

        thread = QThread(self)

        index = self.indexFile()

        file = self.tabWidget.tabText(index)

        self.checkVia = ThreadVia(self.value(),file)

        self.checkVia.moveToThread(thread)

        thread.started.connect(self.checkVia.run)

        self.checkVia.finished.connect(thread.quit)

        self.checkVia.new_signal.connect(self.status)


        thread.start()

    def auto_like(self):
        global stop_thread

        stop_thread = False


        settings = self.valueSettings()
        if settings['link'] =='':
            message = QMessageBoxX(
                icon="warning",
                boldtext="Lỗi link",
                text="Vui lòng nhập link bài viết",
                ok=True,
                cancel=False,
                stylesheet = self.styleSheet()
                )
            message.exec()

            return
        elif 'https://' not in  settings['link']:
            message = QMessageBoxX(
                icon="warning",
                boldtext="Lỗi link",
                text="Vui lòng kiểm tra lại link bài viết",
                ok=True,
                cancel=False,
                stylesheet = self.styleSheet()
                )
            message.exec()

            return

        elif len(settings['emoji']) <=0:
            message = QMessageBoxX(
                icon="warning",
                boldtext="Lỗi cảm xúc",
                text="Vui lòng chọn cảm xúc cần auto",
                ok=True,
                cancel=False,
                stylesheet = self.styleSheet()
                )
            message.exec()

            return            
        elif settings['timer']:
            if settings['timer_delay'] == False:
                message = QMessageBoxX(
                    icon="warning",
                    boldtext="Hẹn giờ lỗi",
                    text="Thời gian hẹn giờ phải lớn hơn thời gian hiện tại",
                    ok=True,
                    cancel=False,
                    stylesheet = self.styleSheet()
                    )
                message.exec()
                return


        thread = QThread(self)

        datas = self.value()

        index = self.indexFile()

        file = self.tabWidget.tabText(index)

        

        self.autoLike = ThreadReaction(datas,settings,file)

        self.autoLike.moveToThread(thread)

        thread.started.connect(self.autoLike.run)

        self.autoLike.finished.connect(thread.quit)

        self.autoLike.new_signal.connect(self.status)

        thread.start()

    def auto_comment(self):
        global stop_thread

        stop_thread = False


        settings = self.valueSettings()
        if settings['link'] =='':
            message = QMessageBoxX(
                icon="warning",
                boldtext="Lỗi link",
                text="Vui lòng nhập link bài viết",
                ok=True,
                cancel=False,
                stylesheet = self.styleSheet()
                )
            message.exec()

            return
        elif 'https://' not in  settings['link']:
            message = QMessageBoxX(
                icon="warning",
                boldtext="Lỗi link",
                text="Vui lòng kiểm tra lại link bài viết",
                ok=True,
                cancel=False,
                stylesheet = self.styleSheet()
                )
            message.exec()

            return
          
        elif settings['timer']:
            if settings['timer_delay'] == False:
                message = QMessageBoxX(
                    icon="warning",
                    boldtext="Hẹn giờ lỗi",
                    text="Thời gian hẹn giờ phải lớn hơn thời gian hiện tại",
                    ok=True,
                    cancel=False,
                    stylesheet = self.styleSheet()
                    )
                message.exec()
                return


        thread = QThread(self)

        datas = self.value()

        index = self.indexFile()

        file = self.tabWidget.tabText(index)

        

        self.autoComment = ThreadComment(datas,settings,file)

        self.autoComment.moveToThread(thread)

        thread.started.connect(self.autoComment.run)

        self.autoComment.finished.connect(thread.quit)

        self.autoComment.new_signal.connect(self.status)

        thread.start()

    def auto_login(self):

        thread = QThread(self)

        datas = self.value()

        index = self.indexFile()

        file = self.tabWidget.tabText(index)

        link = self.lineEdit_input_link.text().strip()

        self.autologin = ThreadLogin(datas,link,file)

        self.autologin.moveToThread(thread)

        thread.started.connect(self.autologin.run)

        self.autologin.finished.connect(thread.quit)

        self.autologin.new_signal.connect(self.status)


        thread.start()

    def get_infomation(self):
        thread = QThread(self)

        index = self.indexFile()

        file = self.tabWidget.tabText(index)

        self.checkInfo = ThreadInfo(self.value(),file)

        self.checkInfo.moveToThread(thread)

        thread.started.connect(self.checkInfo.run)

        self.checkInfo.finished.connect(thread.quit)

        self.checkInfo.new_signal.connect(self.status)


        thread.start()

    def open_getid(self,the_url,icon):
        isFile = os.path.isfile(f'{icon}/{icon}.exe')
        data = {'theme':self.theme}
        if isFile:
            with open(f'{icon}/settings/settings.json', 'w') as f:
                json.dump(data, f,indent=4)              
            os.startfile(os.getcwd()+f"/{icon}/{icon}.exe")
        else: 
            message = QMessageBoxX(
                icon="information",
                boldtext="Thông báo",
                text=f"App chưa có, bạn có muốn tải về?",
                ok=True,
                cancel=True,
                stylesheet = self.styleSheet()
                )
            if message.exec()==1:

                if not os.path.isdir(icon):
                    os.mkdir(icon)
                Processbar(self.styleSheet(),self.theme,the_url,icon).exec()
              

    def open_qjoingroup(self,the_url,icon):
        isFile = os.path.isfile(f'{icon}/{icon}.exe')
        data = {'theme':self.theme}
        if isFile:    
            os.startfile(os.getcwd()+f"/{icon}")
        else: 
            message = QMessageBoxX(
                icon="information",
                boldtext="Thông báo",
                text=f"App chưa có, bạn có muốn tải về?",
                ok=True,
                cancel=True,
                stylesheet = self.styleSheet()
                )
            if message.exec()==1:
                if not os.path.isdir(icon):
                    os.mkdir(icon)
                Processbar(self.styleSheet(),self.theme,the_url,icon).exec()



    def version(self):
        message = QMessageBoxX(
            icon="information",
            boldtext="Thông tin phiên bản 2.3.1",
            text=f"\n- Sửa lỗi đăng nhập bằng cookie\n\n- Thêm chức năng quét thông tin\n\n- Thêm chức năng get id facebook",
            ok=True,
            cancel=False,
            stylesheet = self.styleSheet()
            )
        message.exec()





class ThreadVia(QtCore.QThread,CheckCookie):
    finished = QtCore.pyqtSignal()
    new_signal = QtCore.pyqtSignal(int,int, str,str,str,bool)
    
    def __init__(self,datas,file,*args, **kwargs):
        super().__init__()
        self.datas = datas
        self.file = file
        self.headers ={
            'authority': 'mbasic.facebook.com',
            'sec-ch-ua-mobile': '?1',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
            }

    def run(self):

        QApplication.processEvents()     
        with ThreadPoolExecutor(max_workers=30) as executor:
            [executor.submit(self.check,data) for data in self.datas]
                 
        self.finished.emit()     
        return




class ThreadReaction(QtCore.QThread,
                    ReactionPersonal,
                    ReactionPage
    ):
    finished = QtCore.pyqtSignal()
    new_signal = QtCore.pyqtSignal(int,int,str,str,str,bool)
    def __init__(self,datas,settings,file):
        QtCore.QThread.__init__(self)
        self.file = file
        self.datas = datas
        self.settings = settings
        self.url_raw = 'https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id='
    def run(self):
        global stop_thread
        QApplication.processEvents()   
        if self.settings['timer']:
            for rows in self.datas:
                self.new_signal.emit(int(rows.split('|')[0]),9,f'Chạy sau {self.settings["timer_delay"]} giây','normal',self.file,False)
            QtCore.QThread.sleep(self.settings['timer_delay'])
        for data in self.datas:          
            if stop_thread:
                stop_thread = False
                
                break            
            thread = threading.Thread(target=self.like,args=(data,))
            if threading.active_count()-1 == 10:
                thread.start()
                thread.join()
            else:
                thread.start()
            QtCore.QThread.sleep(self.settings['delay'])
        self.finished.emit()

class ThreadComment(QtCore.QThread,AutoComment):
    finished = QtCore.pyqtSignal()
    new_signal = QtCore.pyqtSignal(int,int, str,str,str,bool)
    def __init__(self,datas,settings,file):
        QtCore.QThread.__init__(self)
        self.file = file
        self.datas = datas
        self.settings = settings
    def run(self):
        global stop_thread
        QApplication.processEvents()   
        if self.settings['timer']:
            for rows in self.datas:
                self.new_signal.emit(int(rows.split('|')[0]),9,f'Chạy sau {self.settings["timer_delay"]} giây','normal',self.file,False)
            QtCore.QThread.sleep(self.settings['timer_delay'])
        for data in self.datas:          
            if stop_thread:
                stop_thread = False
                break
            thread = threading.Thread(target=self.comment,args=(data,))
            if threading.active_count()-1 == 10:
                thread.start()
                thread.join()
            else:
                thread.start()
            QtCore.QThread.sleep(self.settings['delay'])
        self.finished.emit()

class ThreadLogin(QtCore.QThread,LogIn):
    finished = QtCore.pyqtSignal()
    new_signal = QtCore.pyqtSignal(int,int, str,str,str,bool)
    def __init__(self,datas,link,file):
        QtCore.QThread.__init__(self)
        self.path = 'chromedriver.exe'
        self.datas = datas
        self.link = link
        self.file = file

    def run(self):
        global stop_thread
        a = 1
        position_x = 0
        position_y = 0  
        for data in self.datas:
            if stop_thread:
                return            
            thread = threading.Thread(target=self.login_cookie,args=(data,position_x,position_y))
            thread.start()
            time.sleep(1)
            position_x +=50
            position_y += 35
            if a % 6 ==0:
                position_x +=200
                position_y = 0
            a+=1
            time.sleep(1)

class ThreadInfo(QtCore.QThread,GetInfo):
    finished = QtCore.pyqtSignal()
    new_signal = QtCore.pyqtSignal(int,int, str,str,str,bool)
    def __init__(self,datas,file):
        QtCore.QThread.__init__(self)
        self.datas = datas
        self.file = file

    def run(self):
        QApplication.processEvents()     
        with ThreadPoolExecutor(max_workers=30) as executor:
            for data in self.datas:
                executor.submit(self.getInfomation,data)
                 
        self.finished.emit()     
        return

class Processbar(QDialog,Ui_Dialog):
    def __init__(self,stylesheet,theme,the_url,icon,parent=None):
        super(Processbar,self).__init__(parent=parent)
        self.setupUi(self)

        ### ẩn titbar gốc của hệ điều hành
        self.setWindowFlags(Qt.FramelessWindowHint)

        ### loại bỏ phần thừa của window , để lại frame main
        self.setAttribute(Qt.WA_TranslucentBackground,True)


        self.setStyleSheet(stylesheet)

        ### đổ bóng cho cửa sổ 
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(10)
        self.shadow.setOffset(0, 0)
        self.shadow.setColor(QColor(0, 0, 0, 180))
        self.frame_main_download.setGraphicsEffect(self.shadow)

        self.pushButton_close.clicked.connect(self.close)


        self.pushButton_cancel.clicked.connect(self.cancelX)


        self.pushButton_hide.clicked.connect(self.showMinimized)

        self.theme = theme


        ### gán hàm dy chuyển app cho frame title
        self.frame_titlebar.mouseMoveEvent = self.moveWindow 

        self.progressBar.setValue(5)
        self.icon = icon
        self.frame_icon.setStyleSheet("border-image: url(:/images/icon/images/dowload.png);")    
        ### tạo processbar dowload


        self.the_filesize = requests.get(the_url, stream=True).headers['Content-Length']
        the_filepath = self.icon+'/'+self.icon+'.zip'
        the_fileobj = open(the_filepath, 'wb')

        #### Create a download thread
        self.downloadThread = downloadThread(the_url, self.the_filesize, the_fileobj, buffer=10240)
        self.downloadThread.download_prosess_signal.connect(self.set_progressbar_value)
        self.downloadThread.msgX.connect(self.msg)
        self.downloadThread.start()
        self.label.setText(f'Đang tải {self.icon}...')
        self.label_2.setText(f'Kích cỡ {round((int(self.the_filesize)/1024000),2)} MB - Dự kiến tải trong 1 phút ...')

    @QtCore.pyqtSlot()        
    def msg(self):        
        message = QMessageBoxX(
            icon="warning",
            boldtext="Lỗi mạng",
            text=f"Đã xảy ra vấn đề, vui lòng tải lại",
            ok=True,
            cancel=False,
            stylesheet = self.styleSheet()
            )
        message.exec()
        self.close()
    # Setting progress bar
    QtCore.pyqtSlot(int,int)  
    def set_progressbar_value(self, value,text):
        if value == 100:
            shutil.unpack_archive(f'{self.icon}/{self.icon}.zip', self.icon)

            message = QMessageBoxX(
                icon="information",
                boldtext="Thông báo",
                text=f"Download thành công {self.icon}",
                ok=True,
                cancel=False,
                stylesheet = self.styleSheet()
                )
            message.exec() 
            self.close()
            data = {'theme':self.theme}
            try:
                with open(f'{self.icon}/settings/settings.json', 'w') as f:
                    json.dump(data, f,indent=4)  
            except:
                pass
            os.startfile(os.getcwd()+f"/{self.icon}")
            
            return    
        self.progressBar.setFormat(f'Đang tải {round((text/1024000),2)} MB trên tổng {round((int(self.the_filesize)/1024000),2)} MB ...')
        if value >=5:
            self.progressBar.setValue(value+1)


    def moveWindow(self,event):     
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self,event):
        self.dragPos = event.globalPos()

    def cancelX(self):
        message = QMessageBoxX(
            icon="question",
            boldtext="Dừng tải?",
            text=f"Bạn chắc chắn muốn dừng tải {self.icon}",
            ok=True,
            cancel=True,
            stylesheet = self.styleSheet()
            )
        if message.exec()==1: 
            self.close()
        return   


##################################################################
#Download thread
##################################################################
class downloadThread(QtCore.QThread):
    download_prosess_signal = QtCore.pyqtSignal(int,int)  
    msgX = QtCore.pyqtSignal()  
    def __init__(self, url, filesize, fileobj, buffer):
        super(downloadThread, self).__init__()
        self.url = url
        self.filesize = filesize
        self.fileobj = fileobj
        self.buffer = buffer


    def run(self):
        try:
            rsp = requests.get(self.url, stream=True)               #Streaming download mode
            offset = 0
            for chunk in rsp.iter_content(chunk_size=self.buffer):
                if not chunk: break
                self.fileobj.seek(offset)                       #Setting Pointer Position
                self.fileobj.write(chunk)                           #write file
                offset = offset + len(chunk)
                proess = offset / int(self.filesize) * 100
                self.download_prosess_signal.emit(int(proess),offset)      #Sending signal

            #######################################################################
            self.fileobj.close()    #Close file
            self.exit(0)            #Close thread

        except Exception as e:
            self.exit(0)
            print(e)

        
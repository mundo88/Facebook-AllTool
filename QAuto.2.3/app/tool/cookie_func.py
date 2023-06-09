from app.modules.packages.pyqt5_modules import *


class CheckCookie:
    @QtCore.pyqtSlot()        
    def check(self,data):
        row = int(data.split('|')[0])
        cookie = data.split('|')[4]
        self.new_signal.emit(row,9,'Đang tải...','normal',self.file,False)
        self.headers['cookie'] = cookie
        try:
            self.b = requests.get('https://mbasic.facebook.com', headers= self.headers)
        except Exception as e:
            self.new_signal.emit(row,9,'error 404','red',self.file,True)
            return
        if 'fb_dtsg' in self.b.text:
            text = 'Cookie live'  
            color =  'blue'
            
        else:
            text = 'CP' 
            color =  'red'
        try:      
            self.new_signal.emit(row,9,text,color,self.file,True)
        except Exception as e:
            print(e)
        return 


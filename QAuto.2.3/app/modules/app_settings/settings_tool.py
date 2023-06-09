
from app.modules.packages.pyqt5_modules import *




class Settings:

    def setupTime(self):
        ### set time cho check box và spinbox hẹn giờ
        self.spinBox_hour.setValue(int(datetime.now().strftime("%H")))

        self.spinBox_miunute.setValue(int(datetime.now().strftime("%M")))
        self.spinBox_hour.setEnabled(False)
        self.spinBox_miunute.setEnabled(False)

        self.checkBox_timer.clicked.connect(lambda:Settings.insertTime(self))

    def insertTime(self):
        self.spinBox_hour.setValue(int(datetime.now().strftime("%H")))
        self.spinBox_miunute.setValue(int(datetime.now().strftime("%M"))) 

        if self.checkBox_timer.isChecked():
            self.spinBox_hour.setEnabled(True)
            self.spinBox_miunute.setEnabled(True)   
        else:
            self.spinBox_hour.setEnabled(False)
            self.spinBox_miunute.setEnabled(False)                   

    def timer(self):
        h = self.spinBox_hour.value()
        m = self.spinBox_miunute.value()
        s = (3660*int(datetime.now().strftime("%H"))) + (60*int(datetime.now().strftime("%M")))
        ss =  (3660*int(h) + (60*int(m)))    
        sss = ss-s  
        if sss < 0 :
            return False 
        return sss

    def emoji(self):
        list_emoji = []
        if self.checkBox_like.isChecked() : list_emoji.append(0)
           
        if self.checkBox_tim.isChecked() :list_emoji.append(1)
            
        if self.checkBox_loving.isChecked() :list_emoji.append(2)
            
        if self.checkBox_haha.isChecked() :list_emoji.append(4)
            
        if self.checkBox_wow.isChecked() :list_emoji.append(3)
            
        if self.checkBox_sad.isChecked() :list_emoji.append(5)   
            
        if self.checkBox_angry.isChecked() :list_emoji.append(6)
            
        return list_emoji     

    def valueSettings(self):
        settings = {
                'link': self.lineEdit_input_link.text().strip().replace('www','mbasic'),
                'emoji': Settings.emoji(self),
                'delay': random.randint(self.spinBox_delay_from.value(),self.spinBox_delay_to.value()),
                'page': self.checkBox_page.isChecked(),
                'page_number': self.spinBox_page.value(),
                'like_comment':self.checkBox_likeCmt.isChecked(),
                'rep_comment' :self.checkBox_repCmt.isChecked(),
                'timer':self.checkBox_timer.isChecked(),
                'timer_delay': Settings.timer(self),
        }
        return settings


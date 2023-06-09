from app_func import *
from app.modules.app_ui.theme_ui import *


light = '''
    QFrame#frame_title {
        border-top-left-radius:8px;
        border-top-right-radius:8px;
        background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 rgb(229, 229, 229),
                stop: 1 rgb(205, 205, 205));
         border-top: 1px solid rgb(244, 244, 244);
         border-bottom: 1px solid rgb(167, 167, 167);
    }
    QFrame#frame_title_btn QPushButton {
        border-radius:8px;
    }
    QPushButton#pushButton_ok {
        color:rgb(255, 255, 255);
        border-top: 1px solid rgb(76, 162, 249);
        border-bottom: 1px solid rgb(3, 92, 255);
        border-left: 1px solid rgb(37, 127, 252);
        border-right: 1px solid rgb(37, 127, 252);
        background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 137, 255, 255), stop:1 rgba(189, 227, 255, 255));
        border-radius:8px;
   }
    QPushButton#pushButton_ok:hover {
        border-top: 1px solid rgb(172, 172, 172);
        border-bottom: 1px solid rgb(129, 129, 129);
        border-left: 1px solid rgb(165, 165, 165);
        border-right: 1px solid rgb(165, 165, 165);
    }
    
    QPushButton#pushButton_ok:pressed {
        background: rgb(235, 235, 235);
        border-top: 1px solid rgb(142, 142, 142);
        border-bottom: 1px solid rgb(99, 99, 99);
        border-left: 1px solid rgb(135, 135, 135);
        border-right: 1px solid rgb(135, 135, 135);
    }
    /* QFRAME */
    QFrame#frame {
        background-color: rgb(255, 255, 255);
        border-radius:8px;
    }
'''

dark = '''
    /* QFRAME */
    QFrame#frame {
       background: rgba(50, 50, 50, 1);
        border-radius:8px;
    }
    QFrame#frame_title {
        border-top-left-radius:8px;
        border-top-right-radius:8px;
        color: rgb(205, 205, 205);
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(67, 67, 67),
            stop: 1 rgb(56, 56, 56));
        border: 1px solid rgb(91, 91, 91);
        border-top: 1px solid rgb(121, 121, 121);
        border-bottom: 1px solid rgb(35, 35, 35);
    }

    QFrame#frame_title_btn QPushButton {
        border-radius:8px;
    }
    /* QPUSHBUTTON */
    QPushButton#pushButton_close {
        background: rgb(255, 96, 92);
    }
    QPushButton#pushButton_close:hover {
        background: rgb(232, 86, 84);
    }


    QPushButton#pushButton_hide {
        background: rgb(255, 189, 68);
    }

    QPushButton#pushButton_hide:hover{
        background: rgb(229, 151, 61);
    }

    QPushButton#pushButton_maximum {
        background: rgb(0, 202, 78);
    }

    QPushButton#pushButton_maximum:hover {
        background:rgb(0, 176, 67);
    }

    QPushButton#pushButton_ok {
        color:rgb(255, 255, 255);
        border-top: 1px solid rgb(76, 162, 249);
        border-bottom: 1px solid rgb(3, 92, 255);
        border-left: 1px solid rgb(37, 127, 252);
        border-right: 1px solid rgb(37, 127, 252);
        background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 137, 255, 255), stop:1 rgba(189, 227, 255, 255));
        border-radius:8px;
   }
    QPushButton#pushButton_ok:hover {
        border-top: 1px solid rgb(172, 172, 172);
        border-bottom: 1px solid rgb(129, 129, 129);
        border-left: 1px solid rgb(165, 165, 165);
        border-right: 1px solid rgb(165, 165, 165);
    }
    
    QPushButton#pushButton_ok:pressed {
        background: rgb(235, 235, 235);
        border-top: 1px solid rgb(142, 142, 142);
        border-bottom: 1px solid rgb(99, 99, 99);
        border-left: 1px solid rgb(135, 135, 135);
        border-right: 1px solid rgb(135, 135, 135);
    }
'''

class MainTheme(QDialog,Ui_Dialog):
    def __init__(self):
        super(MainTheme,self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground) 
         
        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_hide.clicked.connect(self.showMinimized)

        self.pushButton_ok.clicked.connect(self.themeChange)


        self.shadow =QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,100))

        self.frame.setGraphicsEffect(self.shadow)


        self.frame_title.mouseMoveEvent = self.moveWindow   


        self.changeBorder(True)
        self.pushButton_dark.clicked.connect(lambda:self.changeBorder(False))
        self.pushButton_light.clicked.connect(lambda:self.changeBorder(True))
    def changeBorder(self,state):
        if state:
            self.pushButton_light.setStyleSheet('''
                background-image: url(:/images/icon/images/light_theme.png);
                border : 3px solid rgb(85, 170, 255);
                border-radius:8px;''')
            self.pushButton_dark.setStyleSheet('''
                background-image: url(:/images/icon/images/dark_theme.png);
                border : 3px solid rgb(52, 59, 72);border-radius:8px;;''')
            self.data= {'theme':'light','state':True}

            self.shadow =QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0,120,255))
            self.pushButton_light.setGraphicsEffect(self.shadow)
            self.pushButton_dark.setGraphicsEffect(None)
            self.setStyleSheet(light)
        else:
            self.pushButton_light.setStyleSheet('''
                background-image: url(:/images/icon/images/light_theme.png);
                border : 3px solid rgb(52, 59, 72);border-radius:8px;;''')

            self.pushButton_dark.setStyleSheet('''
                background-image: url(:/images/icon/images/dark_theme.png);
                border : 3px solid rgb(85, 170, 255);border-radius:8px;''')
            self.shadow =QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0,120,255))
            self.pushButton_dark.setGraphicsEffect(self.shadow)  
            self.pushButton_light.setGraphicsEffect(None)          
            self.data= {'theme':'dark','state':False}
            self.setStyleSheet(dark)



    def moveWindow(self,event):
        # MOVE WINDOW        
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
    def mousePressEvent(self,event):
        self.dragPos = event.globalPos()

    def themeChange(self):
        sizeSet = { "vừa màn hình" : (1395,713),
                "nhỏ" : (855,713),
                "full màn hình" : (1920,1080)
        }
        print(sizeSet[(self.comboBox_size.currentText().lower())])
        self.data['size'] = sizeSet[(self.comboBox_size.currentText().lower())]
        print(self.data['size'])
        json_object = json.dumps(self.data, indent = 4)
        with open("settings/theme.json", "w") as outfile:
            outfile.write(json_object)
        self.showApp()


    def showApp(self):
        mainui = MainWindow()
        mainui.show()
        self.close()
        mainui.version()    


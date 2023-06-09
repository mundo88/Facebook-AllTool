from app.modules.packages.pyqt5_modules import *


from .file_ui import Ui_Dialog as UiFile

from .account_ui import Ui_Dialog as UiAccount

from .view_ui import Ui_Dialog as UiTableView

from .comment import Ui_Dialog as UiComment
from .mutiple_app import Ui_Dialog as MutipleApp


class ShowNewAccount(QDialog):
    def __init__(self,styleSheet):
        super(ShowNewAccount,self).__init__()

        ### set up và hiển thị giao diện tạo nhập tài khoản
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground) 

        self.setStyleSheet(styleSheet)
        
        self.uiAccount = UiAccount()
        self.uiAccount.setupUi(self) 

        # self.form_account.setWindowFlags(Qt.FramelessWindowHint)

        self.shadow =QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,120,255))

        self.uiAccount.frame_main.setGraphicsEffect(self.shadow)

        self.uiAccount.label.mouseMoveEvent = self.moveWindow 

        self.effect = QGraphicsOpacityEffect(self)
        self.showAnimation = QPropertyAnimation(self.effect, b"opacity")
        self.showAnimation.setDuration(80)
        self.showAnimation.setStartValue(0)
        self.showAnimation.setEndValue(1)
        self.setGraphicsEffect(self.effect)
        self.showAnimation.start(QtCore.QAbstractAnimation.DeleteWhenStopped)
        self.showAnimation.finished.connect(self.effect.deleteLater)


    def moveWindow(self,event):
        # MOVE WINDOW        
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
    def mousePressEvent(self,event):
        self.dragPos = event.globalPos()



class ShowTableView(QDialog,UiTableView):
    def __init__(self,styleSheet):
        super(ShowTableView,self).__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        ### set up và hiển thị giao diện tạo file mới 
        self.setStyleSheet(styleSheet)

        self.setupUi(self)



        self.shadow =QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,120,255))

        self.frame_view.setGraphicsEffect(self.shadow)

        
        self.effect = QGraphicsOpacityEffect(self)
        self.showAnimation = QPropertyAnimation(self.effect, b"opacity")
        self.showAnimation.setDuration(100)
        self.showAnimation.setStartValue(0)
        self.showAnimation.setEndValue(1)
        self.setGraphicsEffect(self.effect)
        self.showAnimation.start(QtCore.QAbstractAnimation.DeleteWhenStopped)
        self.showAnimation.finished.connect(self.effect.deleteLater)

        self.label.mouseMoveEvent = self.moveWindow 


        with open('settings/table.json', 'r') as openfile:
            view = json.load(openfile)

        self.stt.setChecked(view['stt'])
        self.name.setChecked(view['name'])
        self.uid.setChecked(view['uid'])
        self.passw.setChecked(view['pass'])
        self._2fa.setChecked(view['2fa'])
        self.cookie.setChecked(view['cookie'])
        self.comment.setChecked(view['comment'])
        self.img.setChecked(view['img'])
        self.status.setChecked(view['status'])



    def mousePressEvent(self,event):
        self.dragPos = event.globalPos()   
             
    def moveWindow(self,event):
        # MOVE WINDOW        
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()



class ShowNewFile(QDialog):
    def __init__(self,styleSheet):
        super(ShowNewFile,self).__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        ### set up và hiển thị giao diện tạo file mới 
        self.setStyleSheet(styleSheet)

        self.uiFile = UiFile()

        self.uiFile.setupUi(self) 

        self.shadow =QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,120,255))

        self.uiFile.frame_main.setGraphicsEffect(self.shadow)

        self.uiFile.label.mouseMoveEvent = self.moveWindow 
        self.effect = QGraphicsOpacityEffect(self)
        self.showAnimation = QPropertyAnimation(self.effect, b"opacity")
        self.showAnimation.setDuration(150)
        self.showAnimation.setStartValue(0)
        self.showAnimation.setEndValue(1)
        self.setGraphicsEffect(self.effect)
        self.showAnimation.start(QtCore.QAbstractAnimation.DeleteWhenStopped)
        self.showAnimation.finished.connect(self.effect.deleteLater)


    def moveWindow(self,event):
        # MOVE WINDOW        
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
    def mousePressEvent(self,event):
        self.dragPos = event.globalPos()


class ShowComment(QDialog):
    def __init__(self):
        super(ShowComment,self).__init__()
        self.ui = UiComment()
        self.ui.setupUi(self)
        self.setWindowFlags(
			QtCore.Qt.Window
			)
        
class ShowMutipleApp(QDialog):
    def __init__(self):
        super(ShowMutipleApp,self).__init__()
        self.ui = MutipleApp()
        self.ui.setupUi(self)
        self.setWindowFlags(
			QtCore.Qt.Window
			)

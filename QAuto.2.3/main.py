from theme import *
from selenium import webdriver



if __name__=='__main__':
    app = QApplication(sys.argv)
    if os.path.isfile(f"settings/theme.json"):
        mainui = MainWindow()
        mainui.show() 
    else:
        main = MainTheme()
        main.show()
    sys.exit(app.exec_())




light_theme = '''

    QWidget {
        border:none;
        font-family : Arial

    }

    QWidget#messagebox_container,QFrame#frame_main_download{
        background: rgb(235, 235, 235);
        border-radius: 5px;
    }
    QLabel#messagebox_boldtext {
        font-size:16px;
        font-weight: bold;
    }
    QLabel#messagebox_text {
        font-size:14px;
    }

    QWidget#titlebar,QFrame#frame_titlebar{
        color: rgb(50, 50, 50);
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(229, 229, 229),
            stop: 1 rgb(205, 205, 205));
        border-top: 1px solid rgb(244, 244, 244);
        border-bottom: 1px solid rgb(167, 167, 167);
        border-top-left-radius: 7px;
        border-top-right-radius: 7px;
    }


    QFrame#frame_title_btn QPushButton {
        border-radius:8px;
    }
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

    QPushButton#messagebox_ok {
        color: white;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(108, 179, 250),
            stop: 1 rgb(6, 155, 255));
        border-top: 1px solid rgb(76, 162, 249);
        border-bottom: 1px solid rgb(3, 92, 255);
        border-left: 1px solid rgb(37, 127, 252);
        border-right: 1px solid rgb(37, 127, 252);
    }


    QPushButton#blue_button {
        color: white;
        border-radius:5px;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(108, 179, 250),
            stop: 1 rgb(6, 155, 255));
        border-top: 1px solid rgb(76, 162, 249);
        border-bottom: 1px solid rgb(3, 92, 255);
        border-left: 1px solid rgb(37, 127, 252);
        border-right: 1px solid rgb(37, 127, 252);
    }

    QPushButton#blue_button:hover {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(128, 199, 255),
            stop: 1 rgb(26, 175, 255));
        border-top: 1px solid rgb(96, 182, 255);
        border-bottom: 1px solid rgb(23, 112, 255);
        border-left: 1px solid rgb(57, 147, 255);
        border-right: 1px solid rgb(57, 147, 255);
    }

    QPushButton#blue_button:pressed {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(108, 179, 250),
            stop: 1 rgb(6, 155, 255));
        border-top: 1px solid rgb(76, 162, 249);
        border-bottom: 1px solid rgb(3, 92, 255);
        border-left: 1px solid rgb(37, 127, 252);
        border-right: 1px solid rgb(37, 127, 252);
    }

    QPushButton#blue_button:disabled {
        color: white;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(200, 200, 200),
            stop: 1 rgb(180, 180, 180));
        border-top: 1px solid rgb(222, 222, 222);
        border-bottom: 1px solid rgb(179, 179, 179);
        border-left: 1px solid rgb(215, 215, 215);
        border-right: 1px solid rgb(215, 215, 215);
    }


    QPushButton#cancel_button {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(242, 242, 242),
            stop: 1 rgb(233, 233, 233));
        font-size: 14px;
        border-top: 1px solid rgb(202, 202, 202);
        border-bottom: 1px solid rgb(159, 159, 159);
        border-left: 1px solid rgb(195, 195, 195);
        border-right: 1px solid rgb(195, 195, 195);
        border-radius: 6px;
        padding: 2px 10px;
    }
    
    QPushButton#cancel_button:hover {
        border-top: 1px solid rgb(172, 172, 172);
        border-bottom: 1px solid rgb(129, 129, 129);
        border-left: 1px solid rgb(165, 165, 165);
        border-right: 1px solid rgb(165, 165, 165);
    }
    
    QPushButton#cancel_button:pressed {
        background: rgb(235, 235, 235);
        border-top: 1px solid rgb(142, 142, 142);
        border-bottom: 1px solid rgb(99, 99, 99);
        border-left: 1px solid rgb(135, 135, 135);
        border-right: 1px solid rgb(135, 135, 135);
    }

    






    QPushButton#btn_toggle_menu{
       background-image:url(:/24x24/icon/24x24/cil-moon.png);

    }


    QPushButton#btn_toggle_comment{
       background-image:url(:/24x24/icon/24x24/cil-comment-bubble.png);
    }
    QPushButton#btn_toggle_options{
        background-image: url(:/24x24/icon/24x24/cil-settings.png);
    }

    QPushButton#btn_toggle_menu:hover ,#btn_toggle_comment_2:hover {
      background-color: rgb(33, 37, 43);

    }
    QPushButton#btn_toggle_menu:pressed {    
       background-color: rgb(85, 170, 255);
    }

    QPushButton#btn_toggle_comment:hover {
      background-color: rgb(33, 37, 43);
    }
    QPushButton#btn_toggle_comment:pressed {    
       background-color: rgb(85, 170, 255);
    }

    QPushButton#btn_toggle_options:hover {
      background-color: rgb(33, 37, 43);
    }
    QPushButton#btn_toggle_options:pressed {    
       background-color: rgb(85, 170, 255);
    }


    QPushButton#btn_minimize{
        background-image: url(:/16x16/icon/16x16/cil-window-minimize_dark.png);
     }

     QPushButton#btn_maximize_restore{
        background-image: url(:/16x16/icon/16x16/cil-window-maximize-dark.png);
    }

    QPushButton#btn_close,#close_account{
        background-image: url(:/16x16/icon/16x16/cil-x-dark.png);
    }



     QFrame#frame_top_info QPushButton {
        color:rgb(71, 75, 78);
        background-color: transparent
    }


    QFrame#frame_top_info QPushButton:hover {
        color: rgb(172, 172, 172);
    }
    QFrame#frame_top_info QPushButton:pressed {
        color :rgb(56, 142, 240);
    } 



    QPushButton {
        background-position: center;
        background-repeat: no-reperat;
        border: none;
        background-color: transparent
    }
    QPushButton:hover {
        background-color: rgb(217, 217, 217);
    }
    QPushButton:pressed {   
        background-color: rgb(168, 168, 168);
    }



    QPushButton#pushButton_cancel {
        color:rgb(0, 0, 0);
        border-top: 3px solid rgb(76, 162, 249);
        border-bottom: 3px solid rgb(3, 92, 255);
        border-left: 3px solid rgb(37, 127, 252);
        border-right: 3px solid rgb(37, 127, 252);
        background-color:rgb(255, 255, 255);
        border-radius:8px;
   }
    QPushButton#pushButton_cancel:hover {
        border-top: 1px solid rgb(172, 172, 172);
        border-bottom: 1px solid rgb(129, 129, 129);
        border-left: 1px solid rgb(165, 165, 165);
        border-right: 1px solid rgb(165, 165, 165);
    }
    
    QPushButton#pushButton_cancel:pressed {
        background: rgb(235, 235, 235);
        border-top: 1px solid rgb(142, 142, 142);
        border-bottom: 1px solid rgb(99, 99, 99);
        border-left: 1px solid rgb(135, 135, 135);
        border-right: 1px solid rgb(135, 135, 135);
    }


    
    QFrame#frame_main,#frame_view{
        background-color:rgb(248, 251, 254) ;
        border:1px solid rgb(75, 104, 133)
    }


    QPushButton#pushButton_2{
       color:rgb(71, 75, 78)
    }

    QFrame#frame_top,#frame_left_menu{
        background-color:rgb(75, 104, 133) ;
    }
    QFrame#frame_top_info {
        
        background-color: rgb(242, 242, 242);
    }
    QFrame#frame_dialog_file {
        background-color:rgb(248, 251, 254) ;
    }
    QLabel {
        color:rgb(71, 75, 78)
    }
    QFrame#frame_2{
        background-color:rgb(231, 234, 237);
        border:none;
    }

    QFrame#frame_grip,#frame_top_right,#frame_title {
        
        background-color: rgb(249, 249, 249);
    }


    QLineEdit {
        border: 2px solid rgb(150, 150, 150);
        background-color: rgb(249, 249, 249);
        border-radius: 5px;
        padding-left: 10px;
        color: rgb(71, 75, 78);
    }
    QLineEdit:hover {
        border: 2px solid rgb(138, 180, 248);
        
    }
    QLineEdit:focus {
        border: 2px solid  rgb(138, 180, 248);
        
    }

    QPlainTextEdit {
        background-color: rgb(249, 249, 249);
        border-radius: 5px;
        color: rgb(71, 75, 78);
        border: 2px solid rgb(150, 150, 150);
        padding: 10px;
    }
    QPlainTextEdit:hover {
          border: 2px solid rgb(138, 180, 248);
    }
    QPlainTextEdit:focus {
         border: 2px solid  rgb(138, 180, 248);
    }
    QScrollBar:horizontal {
        border: none;
        background:  rgb(231, 234, 237);
        height: 14px;
        margin: 0px 21px 0 21px;
        border-radius: 0px;
    }

    QScrollBar::handle:horizontal {
        background: rgb(85, 170, 255);
        min-width: 25px;
        border-radius: 7px
    }
    QScrollBar::add-line:horizontal {
        border: none;
        background: rgb(231, 234, 237) ;
        width: 20px;
        border-top-right-radius: 7px;
        border-bottom-right-radius: 7px;
        subcontrol-position: right;
        subcontrol-origin: margin;
    }
    QScrollBar::sub-line:horizontal {
        border: none;
        background: rgb(231, 234, 237);
        width: 20px;
        border-top-left-radius: 7px;
        border-bottom-left-radius: 7px;
        subcontrol-position: left;
        subcontrol-origin: margin;
    }
    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
    {
         background: none;
    }
    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
    {
         background: none;
    }
     QScrollBar:vertical {
        border: none;
        background:  rgb(231, 234, 237);
        width: 14px;
        margin: 21px 0 21px 0;
        border-radius: 0px;
     }
     QScrollBar::handle:vertical {  
        background: rgb(85, 170, 255);
        min-height: 25px;
        border-radius: 7px
     }
     QScrollBar::add-line:vertical {
         border: none;
        background:  rgb(231, 234, 237);
         height: 20px;
        border-bottom-left-radius: 7px;
        border-bottom-right-radius: 7px;
         subcontrol-position: bottom;
         subcontrol-origin: margin;
     }
     QScrollBar::sub-line:vertical {
        border: none;
        background:  rgb(231, 234, 237);
        height: 20px;
        border-top-left-radius: 7px;
        border-top-right-radius: 7px;
        subcontrol-position: top;
        subcontrol-origin: margin;
     }
     QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
        background: none;
     }

     QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
     }


    QCheckBox {color: rgb(71,75,78);}

    QCheckBox::indicator {
        border: 3px solid rgb(71,75,78); 
        width: 15px;
        height: 15px;
        border-radius: 10px;
       
        
        
        
    }
    QCheckBox::indicator:hover {
        border-radius: 0px;
            
    }
    QCheckBox::indicator:checked {
        background: 3px solid rgb(75, 104, 133);
        border: 3px solid rgb(100, 139, 177);   
        background-image: url(:/16x16/icon/16x16/cil-check-alt.png);
        
    }

    QTableWidget {  
        background-color:rgb(249, 251, 253);
        border-top : 3px solid rgb(255, 255, 255);
        border-left: 1px solid rgb(210, 210, 210);

        color: rgb(71, 75, 78);
        font-size:12px;
    }
    QTableWidget::item{
        border-color: rgb(44, 49, 60);
        padding-left: 5px;
        padding-right: 5px;
        gridline-color: rgb(44, 49, 60);
    }
    QTableWidget::item:selected{
        background-color:rgb(66, 132, 198)
    }

    QHeaderView::section{
        border-style: none;
        border-bottom: 1px solid rgb(44, 49, 60);
        border-right: 1px solid rgb(231, 234, 237);
    }
    QTableWidget::horizontalHeader {    
        background-color: rgb(81, 255, 0);
    }
    QHeaderView::section:horizontal {
        font-size:14px;
        background-color: rgb(75, 104, 133);
        color :  rgb(249, 249, 249);
        padding: 4px;

    }
    QHeaderView::section:vertical
    {
        border: 1px solid rgb(44, 49, 60);
    }
    QTabWidget::tab-bar {
        alignment: left;
    }
     QTabBar::tab {
        font-size:14px;
        background-color:rgb(231, 234, 237);
        color:rgb(71, 75, 78);
        padding : 5px;
        width : 150px;
        height : 22px;
        border:none;
    }

    QTabBar::tab:selected {
        background-color: rgb(255, 255, 255);
        border: none;

    }
    QTabWidget::pane { 
        top:0px;

    }

    QTabBar QToolButton {
        border: none;
    }

    QTabBar::close-button {
        background-image: url(:/16x16/icon/16x16/cil-x-dark.png);
        subcontrol-position: right; 
    }
  
     QMenu {
        border: 1px solid gray; 
        background-color: rgb(250, 250, 250);
        color: #000; 
        padding: 10px;
        font-size:13px;
        font-family:Arial
    }
    QMenu:selected {
        background-color:rgb(75, 104, 133) ;
        border : 1px solid rgb(4, 104, 204);

        color: #fff;
    }

  
    QSpinBox {
        background-color: rgb(231, 234, 237);
        border-radius: 5px;
        border: 2px solid rgb(144, 151, 157);

        color:  rgb(71, 75, 78);
    }
    QSpinBox:hover {
        border: 2px solid rgb(64, 71, 88);
    }
    QSpinBox:focus {
        border: 2px solid rgb(91, 101, 124);
    }
    /* COMBOBOX */
    QComboBox{
        background-color:rgb(75, 104, 133);
        border-radius: 5px;
        padding: 5px;
        padding-left: 10px;
        color: rgb(248, 251, 254);   
        
    }
    QComboBox:hover{
        
        border: 2px solid rgb(85, 170, 255);
    }
    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 25px; 
        border-left-width: 3px;
        border-left-color: rgba(215, 234, 255, 1);
        border-left-style: solid;
        border-top-right-radius: 3px;
        border-bottom-right-radius: 3px;    
        background-image:url(:/16x16/icon/16x16/cil-arrow-bottom.png);
        background-position: center;
        background-repeat: no-reperat;
     }
    QComboBox QAbstractItemView {
        color: rgb(0, 0, 0);   
        background-color: rgb(255, 255, 255);
        padding: 10px;
        selection-background-color: rgb(0, 149, 255);
        border:none;
    }
    
    QPushButton::menu-indicator{ image:none;}







    QProgressBar {
        min-height: 16px;
        max-height: 16px;
        border-radius: 8px;
        background: rgb(222, 222, 222);
    }
    QProgressBar::chunk {
        border-radius: 8px;
        background-color:rgb(62, 148, 251);
    }
        
    '''




dark_theme = """

    QWidget {
        border:none;
        font-family : Arial;
    }

    QWidget#container {
        background: rgba(50, 50, 50, 1);
        border-radius: 5px;
        border: 1px solid rgb(91, 91, 91);
    }

    QWidget#messagebox_container,QFrame#frame_main_download{
        background: rgba(50, 50, 50, 1);
        border-radius: 5px;
        border: 1px solid rgb(91, 91, 91);
    }
    
    QWidget#titlebar,QFrame#frame_titlebar{
        font-size: 16px;
        color: rgb(205, 205, 205);
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(67, 67, 67),
            stop: 1 rgb(56, 56, 56));
        border: 1px solid rgb(91, 91, 91);
        border-top: 1px solid rgb(121, 121, 121);
        border-bottom: 1px solid rgb(35, 35, 35);
        border-top-left-radius: 7px;
        border-top-right-radius: 7px;
    }


    QLabel#messagebox_boldtext {
        font-size: 16px;
        font-weight: bold;
    }

    QLabel#messagebox_text {
        font-size:14px;
    }

    /*QPUSH BUTTON */

    QFrame#frame_title_btn QPushButton {
        border-radius:7px;

    }
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



    QPushButton#pushButton_2{
       color:rgb(188, 192, 195)
    }

    QPushButton#messagebox_ok {
        color: white;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(108, 179, 250),
            stop: 1 rgb(6, 155, 255));
        border-top: 1px solid rgb(76, 162, 249);
        border-bottom: 1px solid rgb(3, 92, 255);
        border-left: 1px solid rgb(37, 127, 252);
        border-right: 1px solid rgb(37, 127, 252);
    }


    QPushButton#blue_button {
        color: white;
        border-radius:5px;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(108, 179, 250),
            stop: 1 rgb(6, 155, 255));
        border-top: 1px solid rgb(76, 162, 249);
        border-bottom: 1px solid rgb(3, 92, 255);
        border-left: 1px solid rgb(37, 127, 252);
        border-right: 1px solid rgb(37, 127, 252);
    }

    QPushButton#blue_button:hover {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(128, 199, 255),
            stop: 1 rgb(26, 175, 255));
        border-top: 1px solid rgb(96, 182, 255);
        border-bottom: 1px solid rgb(23, 112, 255);
        border-left: 1px solid rgb(57, 147, 255);
        border-right: 1px solid rgb(57, 147, 255);
    }

    QPushButton#blue_button:pressed {
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(108, 179, 250),
            stop: 1 rgb(6, 155, 255));
        border-top: 1px solid rgb(76, 162, 249);
        border-bottom: 1px solid rgb(3, 92, 255);
        border-left: 1px solid rgb(37, 127, 252);
        border-right: 1px solid rgb(37, 127, 252);
    }

    QPushButton#blue_button:disabled {
        color: white;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(200, 200, 200),
            stop: 1 rgb(180, 180, 180));
        border-top: 1px solid rgb(222, 222, 222);
        border-bottom: 1px solid rgb(179, 179, 179);
        border-left: 1px solid rgb(215, 215, 215);
        border-right: 1px solid rgb(215, 215, 215);
    }


    QPushButton#cancel_button {
        color : #000;
        background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 rgb(242, 242, 242),
            stop: 1 rgb(233, 233, 233));
        font-size: 14px;
        border-top: 1px solid rgb(202, 202, 202);
        border-bottom: 1px solid rgb(159, 159, 159);
        border-left: 1px solid rgb(195, 195, 195);
        border-right: 1px solid rgb(195, 195, 195);
        border-radius: 6px;
        padding: 2px 10px;
    }
    
    QPushButton#cancel_button:hover {
        border-top: 1px solid rgb(172, 172, 172);
        border-bottom: 1px solid rgb(129, 129, 129);
        border-left: 1px solid rgb(165, 165, 165);
        border-right: 1px solid rgb(165, 165, 165);
    }
    
    QPushButton#cancel_button:pressed {
        background: rgb(235, 235, 235);
        border-top: 1px solid rgb(142, 142, 142);
        border-bottom: 1px solid rgb(99, 99, 99);
        border-left: 1px solid rgb(135, 135, 135);
        border-right: 1px solid rgb(135, 135, 135);
    }

    







    QPushButton#btn_toggle_menu{
       background-image:url(:/24x24/icon/24x24/sun.png);
    }


    QPushButton#btn_toggle_comment{
       background-image:url(:/24x24/icon/24x24/cil-comment-bubble.png);
    }
    QPushButton#btn_toggle_options{
        background-image: url(:/24x24/icon/24x24/cil-settings.png);
    }


    QPushButton#btn_minimize{
        background-image: url(:/16x16/icon/16x16/cil-window-minimize.png);
    }
    QPushButton#btn_maximize_restore{
        background-image: url(:/16x16/icon/16x16/cil-window-maximize.png);
    }
    QPushButton#btn_close,#close_account{
        background-image: url(:/16x16/icon/16x16/cil-x.png);
    }


    QPushButton {
        background-position: center;
        background-repeat: no-reperat;
        border: none;
        background-color: transparent
    }
    QPushButton:hover {
        background-color: rgb(33, 37, 43);
    }
    QPushButton:pressed {   
        background-color: rgb(85, 170, 255);
    }

    QPushButton#pushButton_cancel {
        color:rgb(0, 0, 0);
        border-top: 3px solid rgb(76, 162, 249);
        border-bottom: 3px solid rgb(3, 92, 255);
        border-left: 3px solid rgb(37, 127, 252);
        border-right: 3px solid rgb(37, 127, 252);
        background-color:rgb(255, 255, 255);
        border-radius:8px;
   }
    QPushButton#pushButton_cancel:hover {
        border-top: 1px solid rgb(172, 172, 172);
        border-bottom: 1px solid rgb(129, 129, 129);
        border-left: 1px solid rgb(165, 165, 165);
        border-right: 1px solid rgb(165, 165, 165);
    }
    
    QPushButton#pushButton_cancel:pressed {
        background: rgb(235, 235, 235);
        border-top: 1px solid rgb(142, 142, 142);
        border-bottom: 1px solid rgb(99, 99, 99);
        border-left: 1px solid rgb(135, 135, 135);
        border-right: 1px solid rgb(135, 135, 135);
    }





    /*QFRAME */
    QFrame#frame_top_info QPushButton {
        background-color: transparent;
        color:rgb(188, 192, 195);

    }


    QFrame#frame_top_info QPushButton:hover {

         color: rgb(136, 194, 247);
    }
    QFrame#frame_top_info QPushButton:pressed {
         color :rgb(56, 142, 240);
    } 


    
    QFrame#frame_main,#frame_view{
        background-color:rgb(39, 44, 54) ;
        border:1px solid rgb(75, 104, 133);

    }
    QFrame#frame_top,#frame_left_menu{
        background-color:rgb(27, 29, 35) ;

    }

    QFrame#frame_grip,#frame_top_right,#frame_title {
        background-color: rgb(27, 29, 35)



    }

    QFrame#frame_top_info {
        background-color: rgb(39, 44, 54);
    }

    QFrame#frame_2{
        background-color:rgb(231, 234, 237);
        border:none;
    }

    QFrame#frame_center{
        
        background-color: rgb(41, 45, 56);
    }

    QFrame#frame_2{
        background-color:rgb(37, 39, 44);
        border:none;
        border-left: 1px solid rgb(27, 29, 35)
    }
    QFrame#frame_dialog_file {
        background-color: rgb(41, 45, 56);
    }
    /*QLABEL */
    QLabel {
        color:rgb(188, 192, 195)
    }


    /*QLINE EDIT */
    QLineEdit {
        background-color: rgb(41, 45, 56);
        border-radius: 5px;
        border: 2px solid rgb(150, 150, 150);
        padding-left: 10px;
        color: rgb(255, 255, 255);
    }
    QLineEdit:hover {
        border: 2px solid rgb(138, 180, 248);
        
    }
    QLineEdit:focus {
        border: 2px solid  rgb(138, 180, 248);
        
    }

     /*QPLAINTEXTEDIT */
    QPlainTextEdit {
        background-color: rgb(27, 29, 35);
        border-radius: 5px;
        color: rgb(188, 192, 195);
        padding: 10px;
    }
    QPlainTextEdit:hover {
        border: 2px solid rgb(64, 71, 88);
    }
    QPlainTextEdit:focus {
        border: 2px solid rgb(91, 101, 124);
    }


    /*QSCROLLBAR */
    QScrollBar:horizontal {
        border: none;
        background: rgb(52, 59, 72);
        height: 14px;
        margin: 0px 21px 0 21px;
        border-radius: 0px;
    }

    QScrollBar::handle:horizontal {
        background: rgb(85, 170, 255);
        min-width: 25px;
        border-radius: 7px
    }
    QScrollBar::add-line:horizontal {
        border: none;
        background: rgb(55, 63, 77);
        width: 20px;
        border-top-right-radius: 7px;
        border-bottom-right-radius: 7px;
        subcontrol-position: right;
        subcontrol-origin: margin;
    }
    QScrollBar::sub-line:horizontal {
        border: none;
        background: rgb(55, 63, 77);
        width: 20px;
        border-top-left-radius: 7px;
        border-bottom-left-radius: 7px;
        subcontrol-position: left;
        subcontrol-origin: margin;
    }
    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
    {
         background: none;
    }
    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
    {
         background: none;
    }
     QScrollBar:vertical {
        border: none;
        background: rgb(52, 59, 72);
        width: 14px;
        margin: 21px 0 21px 0;
        border-radius: 0px;
     }
     QScrollBar::handle:vertical {  
        background: rgb(85, 170, 255);
        min-height: 25px;
        border-radius: 7px
     }
     QScrollBar::add-line:vertical {
         border: none;
        background: rgb(55, 63, 77);
         height: 20px;
        border-bottom-left-radius: 7px;
        border-bottom-right-radius: 7px;
         subcontrol-position: bottom;
         subcontrol-origin: margin;
     }
     QScrollBar::sub-line:vertical {
        border: none;
        background: rgb(55, 63, 77);
         height: 20px;
        border-top-left-radius: 7px;
        border-top-right-radius: 7px;
         subcontrol-position: top;
         subcontrol-origin: margin;
     }
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
         background: none;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
         background: none;
    }


    /*QCHECKBOX */
    QCheckBox {color: rgb(188, 192, 195);}
    QCheckBox::indicator {
       border: 3px solid rgb(75, 104, 133); 
        width: 15px;
        height: 15px;
        border-radius: 10px;
        background: rgb(44, 49, 60);
        color: rgb(188, 192, 195);
        
        
        
    }
    QCheckBox::indicator:hover {
        border-radius: 0px;
            
    }
    QCheckBox::indicator:checked {

        background: 3px solid rgb(52, 59, 72);
        border: 3px solid rgb(138, 180, 248);   
        background-image: url(:/16x16/icon/16x16/cil-check-alt.png);
        
    }

    /*QTABLEWIDGET */
    QTableWidget {  
        background-color: rgb(39, 44, 54);
        gridline-color: rgb(44, 49, 60);
        font-size:12px;
        
        border-top : 3px solid rgb(255, 255, 255);
        gridline-color: rgb(54, 74, 91); 
        color: rgb(188, 192, 195);
    }
    QTableWidget::item{
        border-color: rgb(44, 49, 60);
        padding-left: 5px;
        padding-right: 5px;
        gridline-color: rgb(44, 49, 60);
    }
    QTableWidget::item:selected{
        background-color:rgb(66, 132, 198)
    }

    QHeaderView::section{
        Background-color: rgb(39, 44, 54);
        border: 1px solid rgb(44, 49, 60);
        border-style: none;
        border-bottom: 1px solid rgb(44, 49, 60);
        border-right: 1px solid rgb(74, 75, 77);
    }
    QTableWidget::horizontalHeader {    
        background-color: rgb(81, 255, 0);
    }
    QHeaderView::section:horizontal
    {
        
        background-color: rgb(27, 29, 35);
        color :rgb(188, 192, 195);
        padding: 4px;
        font-size:14px;

    }
    QHeaderView::section:vertical
    {
        border: 1px solid rgb(44, 49, 60);
    }



    /*QTABWIDGET */
    QTabBar::tab:selected {
        background-color: rgb(255, 255, 255);
        color:rgb(0, 0, 0);
        border: none;
    }
    QTabWidget::pane { 
        top:0px;

    }
    QTabBar QToolButton {
        border: none;

    }

    QTabBar::close-button {  
        background-image: url(:/16x16/icon/16x16/cil-x-dark.png);
        subcontrol-position: right; 

    }
    QTabWidget::tab-bar {
        alignment: left;
    }
    QTabBar::tab {
        font-size:14px;
        background-color:rgb(37, 39, 44);
        color: rgb(188, 192, 195);
        padding : 5px;
        width : 180px;
        height : 22px;
        border: none;
        
        
    }

    /*QMENU */
    QMenu {
        border: 1px solid gray; 
        background-color: rgb(250, 250, 250);
        color: #000; 
        padding: 10px;
        font-size:13px;
        font-family:Arial
    }
    QMenu:selected {
        background-color:rgb(75, 104, 133) ;
        border : 1px solid rgb(4, 104, 204);
        color: #fff;
    }

    /*QSPINBOX */
    QSpinBox {
        background-color: rgb(27, 29, 35);
        border-radius: 5px;
        border: 2px solid rgb(27, 29, 35);
        padding-left: 10px;
        
        color: rgb(188, 192, 195);
    }
    QSpinBox:hover {
        border: 2px solid rgb(64, 71, 88);
    }
    QSpinBox:focus {
        border: 2px solid rgb(91, 101, 124);
    }


    /* COMBOBOX */
    QComboBox{
        background-color: rgb(27, 29, 35);
        border-radius: 5px;
        padding: 5px;
        padding-left: 10px;
        color: rgb(188, 192, 195);
        
    }
    QComboBox:hover{
        border: 2px solid rgb(64, 71, 88);
    }
    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 25px; 
        border-left-width: 3px;
        border-left-color: rgba(39, 44, 54, 150);
        border-left-style: solid;
        border-top-right-radius: 3px;
        border-bottom-right-radius: 3px;    
        background-image:url(:/16x16/icon/16x16/cil-arrow-bottom.png);
        background-position: center;
        background-repeat: no-reperat;
     }
    QComboBox QAbstractItemView {
        color: rgb(85, 170, 255);   
        background-color: rgb(27, 29, 35);
        padding: 10px;
        selection-background-color: rgb(39, 44, 54);
        border:none;
    }
    QPushButton::menu-indicator{ image:none;}








    QProgressBar {
        min-height: 16px;
        max-height: 16px;
        border-radius: 8px;
        background: rgb(222, 222, 222);
    }
    QProgressBar::chunk {
        border-radius: 8px;
        background-color:rgb(62, 148, 251);
    }
    
"""



# class CheckBoxStyle(QProxyStyle):
#     def subElementRect(self, element, option, widget=None):
#         r = super().subElementRect(element, option, widget)
#         if element == QStyle.SE_ItemViewItemCheckIndicator:
#             r.moveCenter(option.rect.center())
#         return r

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     checkbox_style = CheckBoxStyle(app.style())
#     app.setStyle(checkbox_style)        
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
pyuic5 .\app\widget\ui\main_ui.ui -o .\app\modules\app_ui\main_ui.py
pyuic5 .\app\widget\ui\theme_ui.ui -o .\app\modules\app_ui\theme_ui.py 

pyuic5 .\app\widget\ui\file_ui.ui -o .\app\widget\file_ui.py
pyuic5 .\app\widget\ui\account_ui.ui -o .\app\widget\account_ui.py
pyuic5 .\app\widget\ui\view_ui.ui -o .\app\widget\view_ui.py 
pyuic5 .\app\widget\ui\comment.ui -o .\app\widget\comment.py 
pyuic5 .\app\widget\ui\dowload_ui.ui -o  dowload_ui.py
pyrcc5 files.qrc -o files_rc.py
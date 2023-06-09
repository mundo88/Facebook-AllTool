
import json
import os


# APP SETTINGS
class SettingsMain:
    # APP PATH
    # ///////////////////////////////////////////////////////////////
    def getPath(self,json_file):
        app_path = os.path.abspath(os.getcwd()+'/settings')
        settings_path = os.path.normpath(os.path.join(app_path, json_file))
        if not os.path.isfile(settings_path):
            print(f"WARNING: \"settings.json\" not found! check in the folder {settings_path}")
        return settings_path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys,re




class LogIn:
    def ChromeOptions(self,position_x,position_y):
        option=  Options()
        option.add_argument(f"--window-position={position_x},{position_y}")
        option.add_argument(("--window-size=800,850"))
        option.add_argument("--disable-infobars")  
        option.add_argument("--disable-gpu") 
        option.add_argument("--no-sandbox") 
        option.add_experimental_option("detach", True) 
        option.add_experimental_option("excludeSwitches", ["enable-automation"])     
        driver = webdriver.Chrome(options = option,executable_path= self.path)
        driver.get('https://www.facebook.com')
        return driver
                    
    def login_cookie(self,data,position_x,position_y):
        cookie = data.split('|')[4]
        row = int(data.split('|')[0])
        try:
            driver = self.ChromeOptions(position_x,position_y)
            self.new_signal.emit(row,9,'Đang tải...','normal',self.file,False)    
            c_user_find = r'c_user=(.*?);'
            c_user = re.findall(c_user_find,cookie)[0]

            fr_find = r'fr=(.*?);'
            fr = re.findall(fr_find,cookie)[0]

            xs_find=  r'xs=(.*?);'
            xs=re.findall(xs_find,cookie)[0]

            # datr_find=  r'datr=(.*?);'
            # datr=re.findall(datr_find,cookie)[0]

            # sb_find=  r'sb=(.*?);'
            # sb=re.findall(sb_find,cookie)[0]  
            cookies = [
                    {'domain': '.facebook.com', 'expiry': 1641582421, 'httpOnly': True, 
                    'name': 'fr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': fr},

                    {'domain': '.facebook.com', 'expiry': 1665342422, 'httpOnly': True, 
                    'name': 'xs', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': xs},

                    {'domain': '.facebook.com', 'expiry': 1663617479, 'httpOnly': False, 
                    'name': 'c_user', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': c_user},

                    # {'domain': '.facebook.com', 'expiry': 1696330754, 'httpOnly': True, 
                    # 'name': 'datr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': datr},

                    # {'domain': '.facebook.com', 'expiry': 1696406314, 'httpOnly': True, 
                    # 'name': 'sb', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': sb} ,  
                    ]

            #add cookie vào chrome    
            for c in cookies:
                driver.add_cookie(c)
            driver.get('https://www.facebook.com')
            if 'fb_dtsg' in driver.page_source:
                if self.link !='':
                    driver.get(self.link)
                self.new_signal.emit(row,9,'Đăng nhập thành công','blue',self.file,True) 

            else:
                self.new_signal.emit(row,9,'CP','red',self.file,True)
            return
        except:
            self.new_signal.emit(row,9,'Lỗi','red',self.file,True)
            return
        


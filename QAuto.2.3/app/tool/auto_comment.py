import requests
from bs4 import BeautifulSoup
import re
import lxml
import urllib.request
from PyQt5 import QtCore



class AutoComment:
    @QtCore.pyqtSlot() 
    def get_data(self,headers,row): 
        self.new_signal.emit(row,9,'Đang tải...','normal',self.file,False)    
        try:
            r = requests.get(self.settings['link'], headers=headers)
            to_ken = r'actions_(.*?)"+?'
            post_id_ = re.findall(to_ken,r.text)
            post_id = post_id_[0] 

            link_get = f'https://m.facebook.com/mbasic/comment/advanced/?target_id={post_id}&pap=1&at=compose&photo_comment=1&paipv=1&_rdr'
            
            t = requests.get(link_get, headers=headers)
            
            soup = BeautifulSoup(t.text, 'lxml')
            
            fb_dtsg = soup.find(attrs={"name": "fb_dtsg"})["value"]
            
            jazoest = soup.find(attrs={"name": "jazoest"})["value"]
            

            #get form chứa link hành động comment
            abs_action = soup.find(name='form', action=re.compile(r'comment'))['action']


            # get link requests comment
            action = urllib.parse.urljoin(self.settings['link'], abs_action)
            
            return {'fb_dtsg':fb_dtsg,
                    'jazoest':jazoest,
                    'action':action}
        except Exception as e:
            self.new_signal.emit(row,9,'CP','red',self.file,True)
            print(e)

            return False

    @QtCore.pyqtSlot()         
    def comment(self,data):
        headers ={
            'Host': 'mbasic.facebook.com',
            'upgrade-insecure-requests': '1',
            'save-data': 'on',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': data.split('|')[4],
        }

        row = int(data.split('|')[0])

        img = data.split('|')[6].strip()

        content = data.split('|')[5].strip()

        if '~' in content:
            comment_text = content.split('~')[0].strip()
            sticker = content.split('~')[-1].strip()
        else:
            comment_text = content
            sticker = ''

       
        
        soup = self.get_data(headers,row)
        data_upload = {
            'jazoest':soup['jazoest'],
            'fb_dtsg':soup['fb_dtsg'],
            'comment_text':comment_text,
            'sticker_id': sticker
            }

        if not soup == 0:
            if self.settings['rep_comment']:
                comment_id = self.settings['link'].split('comment_id=')[1]
                link_action = soup['action']+ '&parent_comment_id='+comment_id
            else:
                link_action = soup['action']



            if img != '':
                try:
                    if 'https://' in img :             
                        files = {'photosrc':urllib.request.urlopen(img).read()} 
                    else:
                        files = {'photosrc':open(img,'rb')} 
                except Exception as e:
                    self.new_signal.emit(row,9,'Lỗi ảnh','red',self.file,False)
                    return
            else:
                files = {} 




            a = requests.post(url=link_action,data=data_upload,headers=headers,files=files)
            if a.status_code ==200:
                self.new_signal.emit(row,9,'Comment thành công','blue',self.file,True)
            else:
                self.new_signal.emit(row,9,'Comment thất bại','red',self.file,True)
        
        return    
            

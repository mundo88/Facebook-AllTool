import requests
from bs4 import BeautifulSoup
import lxml
from PyQt5 import QtCore


class GetInfo:

    @QtCore.pyqtSlot()    
    def getInfomation(self,data):

        row = int(data.split('|')[0])
        uid = data.split('|')[1]
        headers ={
            'authority': 'm.facebook.com',
            'sec-ch-ua-mobile': '?1',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'cookie': data.split('|')[4],
            }
        self.new_signal.emit(row,9,'Đang quét thông tin...','normal',self.file,True)   
        try: 
            a = requests.get(f'https://m.facebook.com/profile.php?id={uid}&_rdr',headers=headers).text
            soup = BeautifulSoup(a,'lxml')
            name = soup.title.text

            if 'Facebook' in name:
                self.new_signal.emit(row,9,'CP','red',self.file,True)
                return
            self.new_signal.emit(row,2,name,'blue',self.file,False)
            self.new_signal.emit(row,9,'Quét info ok!','blue',self.file,True)
        except Exception as e:
            print(e) 
            self.new_signal.emit(row,9,'Lỗi mạng','red',self.file,False)
        return



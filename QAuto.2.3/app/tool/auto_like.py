from app.modules.packages.pyqt5_modules import *

class ReactionPersonal:
    def get_id(self,headers,row):
        self.new_signal.emit(row,9,'Đang tải...','normal',self.file,False)
        nn = requests.get(self.settings['link'],headers=headers).text
        to_ken = r'actions_(.*?)"+?'
        ids = re.findall(to_ken,nn)
        try:  
            self.id = ids[0]
            return self.id
        except: 
            self.new_signal.emit(row,9,'CP','red',self.file,True)
        return False


    def get_link_reaction(self,headers,row):
        _id = self.get_id(headers,row)
        if _id is not False:
            if self.settings['like_comment']: 
                self.new_signal.emit(row,9,'Like top comment','normal',self.file,False)
                id_comment = self.settings['link'].split('comment_id=')[-1]
                self.url= self.url_raw + _id + '_' + id_comment
            else:
                self.url=self.url_raw + _id

            get_list = requests.get(self.url,headers=headers).text
            return get_list
        return False 


    @QtCore.pyqtSlot()    
    def like(self,data):
        row = int(data.split('|')[0])
        cookie = data.split('|')[4]
        headers = {
        'authority': 'mbasic.facebook.com',
        'scheme':'https',
        'method': 'GET',
        'save-data': 'on',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'cookie': cookie,
        'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
        'upgrade-insecure-requests':'1'
        }
        text = 'Nick cá nhân đã like'
        color = 'normal'        
        try:
            get_list = self.get_link_reaction(headers,row)
            if get_list is not False:
                if 'Gỡ' in get_list:  
                    self.new_signal.emit(row,9,'Nick cá nhân đã like','normal',self.file,True)
                else:  
                    soup = BeautifulSoup(get_list,'lxml') 
                    links_react=[]
                    for a in soup.find_all('a',href=True): 
                        if 'ufi/reaction/' in a['href']:
                            links_react.append('https://mbasic.facebook.com'+a['href'])
                    reaction_list = [links_react[i] for i in self.settings['emoji']]        
                    url_react = random.choice(reaction_list)
                    if requests.get(url_react, headers= headers).status_code ==200:
                        text = 'Like thành công'
                        color = 'blue'
                    else:
                        text = 'Like thất bại'
                        color = 'red'
                if self.settings['page']:
                    self.new_signal.emit(row,9,text,color,self.file,False)
                    self.url_reaction = self.url_raw + str(self.id)
                    self.like_page(headers,row)
                    pass
                else:
                    self.new_signal.emit(row,9,text,color,self.file,True)
        except Exception as e:
            print(e)
            self.new_signal.emit(row,9,'Lỗi mạng','red',self.file,False)
        return    


          
class ReactionPage:
    def Get_id_page(self,headers,row):
        list_page_id = []
        headers['authority'] = 'm.facebook.com'
        url = 'https://m.facebook.com/pages/launchpoint/owned_pages/?ref=bookmarks&from=pages_nav_home'
        r = requests.get(url,headers = headers).text
        if 'rootcontainer' not in r:
            self.new_signal.emit(row,9,f'Sai link','normal',self.file,False)
            return False     
        to_ken = r'page_id%22%3A(.*?)%+?'
        token = re.findall(to_ken,r)
        for id_page in list(set(token)):
            list_page_id.append(id_page)
        return list_page_id


    def Check_like(self,headers,row):
        list_page_id = self.Get_id_page(headers,row)
        list_not_like = []
        if list_page_id:
            for i in range(len(list_page_id)):
                kq = requests.get(self.settings['link']+"&av="+list_page_id[i], headers=headers).text
                if 'KhKjWpav6OA' in kq:
                    list_not_like.append(list_page_id[i])
                    self.new_signal.emit(row,9,f'{len(list_not_like)} page chưa like','normal',self.file,False)
                else:
                    self.new_signal.emit(row,9,f'Page {list_page_id[i]} lỗi','red',self.file,False)
            if len(list_not_like) <= 0:
                state = True 
            else:
                state = False
            self.new_signal.emit(row,9,f'{len(list_not_like)} page chưa like','normal',self.file,state)
            return list_not_like
        return False 

    @QtCore.pyqtSlot()    
    def like_page(self,headers,row):
        self.new_signal.emit(row,9,'Like bằng page','normal',self.file,False)
        idpage = self.Check_like(headers,row)
        if idpage:
            if len(idpage) ==0:
                self.new_signal.emit(row,9,'Đã like full page','normal',self.file,True)
                return 
            elif len(idpage) <= self.settings['page_number']:
                Total_page = len(idpage)
            else:
                Total_page = self.settings['page_number']
            self.new_signal.emit(row,9,f'Like bằng {Total_page} page','normal',self.file,False)    
            count = 0
            for i in range(Total_page):
                rf = requests.get(self.url_reaction+'&av='+str(idpage[i]), headers=headers).text
                soup = BeautifulSoup(rf,'lxml')
                links_react = []
                for a in soup.find_all('a',href=True):
                    if 'ufi/reaction/' in a['href']:
                        links_react.append('https://mbasic.facebook.com'+a['href'])
                list_camxuc = [links_react[i] for i in self.settings['emoji']]
                url_react = random.choice(list_camxuc)
                if requests.get(url_react, headers= headers).status_code==200:
                    count+=1
                    self.new_signal.emit(row,9,f'Like ok {count} page','blue',self.file,False)  
            self.new_signal.emit(row,9,f'Like ok {count} page','blue',self.file,True)      
            return

        return                

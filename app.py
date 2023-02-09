# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:46:22 2023

@author: zanot
"""

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
import random as rd
import requests
from bs4 import BeautifulSoup

KV = ('''
#:import Clipboard kivy.core.clipboard.Clipboard
<Slider>:
    canvas:
        Color:
            rgb: 1, 0, 0
        BorderImage:
            border: (0, 18, 0, 18) if self.orientation == 'horizontal' else (18, 0, 18, 0)
            pos: (self.x + self.padding, self.center_y - sp(18)) if self.orientation == 'horizontal' else (self.center_x - 18, self.y + self.padding)
            size: (max(self.value_pos[0] - self.padding * 2 - sp(16), 0), sp(36)) if self.orientation == 'horizontal' else (sp(36), max(self.value_pos[1] - self.padding * 2 - sp(16), 0))
            source: 'atlas://data/images/defaulttheme/slider{}_background{}'.format(self.orientation[0], '_disabled' if self.disabled else '')

  
PageLayout:
    
    BoxLayout:
        orientation: 'vertical'
                
        Label:
            size_hint: .2, .1
            text: 'Lust Selexxxtor'
                
        BoxLayout:
            orientation: 'horizontal'
            
            BoxLayout:                                           
                orientation: 'vertical' 
                
                Label:
                    text: 'Input'
                BoxLayout:                                       
                    orientation: 'vertical'
                    Slider:                                 
                        id: min
                        min: 0.
                        max: 15.
                        value: 5.
                        step: 1.
                        
                    Label:
                        text: 'mininimum duration: {}'.format(min.value)
                    
                BoxLayout:                                       
                    orientation: 'vertical'
                    Slider:
                        id: max
                        min: 5.
                        max: 60.
                        value: 20.
                        step: 1.
                    Label:
                        text: 'maximum duration: {}'.format(max.value)
                
                MDLabel:
                    text: 'Select your site: '
                    
                BoxLayout: 
                    adaptive_size: True
                    spacing: "15dp"
                    pos_hint: {"center_x": .5, "center_y": .5}
    
                    ToggleButton:
                        id: m
                        allow_no_selection: False
                        size_hint_x: None
                        width: self.texture_size[0]
                        padding_x: '5dp'
                        text: "Youporn"
                        group: "a"
                        on_press: app.yp()
                      
                
                    ToggleButton:
                        id: m
                        allow_no_selection: False
                        size_hint_x: None
                        width: self.texture_size[0]
                        padding_x: '5dp'
                        text: "Pornhub"
                        group: "a"
                        on_press: app.ph()
                
                    ToggleButton:
                        id: m
                        allow_no_selection: False
                        size_hint_x: None
                        width: self.texture_size[0]
                        padding_x: '5dp'
                        text: "Xvideos"
                        group: "a"
                        on_press: app.xv()
                
                MDTextField:
                    id: keywords 
                    hint_text: 'Keywords'
                            
                MDRaisedButton:
                    id: generate
                    text: "Generate my URLs"
                    size_hint_x: 1
                    on_press: app.scrape()
                
            GridLayout:
                cols: 3
                rows: 3
                Label:
                    id: output1
                    text: 'Outuput1'
                Label:
                    id: link1
                    text: "Link1"
                BoxLayout:
                    MDRaisedButton:
                        size_hint_x: .1
                        size_hint_y: .1
                        pos_hint: {"center_x": .5, "center_y": .5}
                        text: 'Copy'
                        on_release:
                            Clipboard.copy(link1.text)
                            
                Label:
                    id: output2
                    text: 'Outuput2'
                Label:
                    id: link2
                    text: 'Link2'    
                BoxLayout:
                    MDRaisedButton:
                        size_hint_x: .1
                        size_hint_y: .1
                        pos_hint: {"center_x": .5, "center_y": .5}
                        text: 'Copy'
                        on_release:
                            Clipboard.copy(link2.text)  
                Label:
                    id: output3
                    text: 'Outuput3'
                Label:
                    id: link3
                    text: 'Link3'
                BoxLayout:
                    MDRaisedButton:
                        size_hint_x: .1
                        size_hint_y: .1
                        pos_hint: {"center_x": .5, "center_y": .5}
                        text: 'Copy'
                        on_release:
                            Clipboard.copy(link3.text)
''')

        
class LSXXX(MDApp):    
    
    def build(self):
        self.title = "Lust Selexxxtor"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "400"
        return Builder.load_string(KV)
    
    def ph(self):
        self.url = "https://it.pornhub.com/", 
        return self.url
        
    def yp(self):
        self.url = "https://www.youporn.com"
        return self.url
    
    def xv(self):
        self.url = "https://www.xvideos.com/"
        return self.url
            
    def scrape(self):
        
        self.keywords = self.root.ids["keywords"].text.strip().split()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
        
####### pornhub ##################################
        
        if self.url == "https://it.pornhub.com/":
            
            # add keywords:
            self.url = self.url + "video/search?search="
            for kw in self.keywords:
                self.url = self.url + "kw+"
            self.url = self.url[:-1]
            
            # add duration:
            self.url = self.url + "&min_duration=" + self.root.ids["min"].text + "&max_duration=" + self.root.ids["max"].text
            
            # scrap the obtained website:
            
            self.response = requests.get(self.url, headers=self.headers)
            self.soup = BeautifulSoup(self.response.content, "html.parser")
            
            # titles
            titles = self.soup.find_all("div", title=True)
            titles_yp = [x["title"] for x in titles]
            titles_yp = titles_yp[3:]
            
            # link
            links=[]
            for a in self.soup.find_all('a', href=True):
                links.append(a['href'])
            links_def = []
            for i in links:
                if "view_video.php" in i:
                    links_def.append(i) 
            links = ["https://it.pornhub.com" + x for x in links_def]
            
            
            self.root.ids["output1"].text = self.tit1
            self.root.ids["output2"].text = self.tit2
            self.root.ids["output3"].text = self.tit3
            # da ritornare sarebbero: durata, titolo e URL
            prova = self.root.ids["keywords"].text
            print(prova)
            self.root.ids["link1"].text = self.url1
            self.root.ids["link2"].text = self.url2
            self.root.ids["link3"].text = self.url3
 
####### youporn ##################################
        
 
        elif self.url == "https://www.youporn.com":
            
            pass
        
####### xvideos ##################################
        
        elif self.url == "https://www.xvideos.com/":
            
            pass

if __name__ == '__main__':
    LSXXX().run()
    
    
    
    
    
# ----------------------------------------------------------------------------

# titles: 
# xvideos:   ###############################
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
# }
# url = "https://www.xvideos.com/?k=mifl&sort=relevance&durf=3-10min"
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, "html.parser")
# titles = soup.find_all("p", class_ = "title")
# titles_xv = [x.get_text() for x in titles]


# yp:   ###############################
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
# }
# url = "https://www.youporn.com/search/?search-btn=&query=milf"
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, "html.parser")
# titles = soup.find_all("div", title=True)
# titles_yp = [x["title"] for x in titles]
# titles_yp = titles_yp[3:]

# ph:   ############################### 
 # headers = {
 #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
 # }
 # url = "https://pornhub.com/video/search?search=milf&min_duration=10&max_duration=30"
 # response = requests.get(url, headers=headers)
 # soup = BeautifulSoup(response.content, "html.parser")
 # titles = soup.find_all("a", title = True)
 # titles_ph = [x["title"] for x in titles]
 # titles_ph = titles_ph[:-3]   

# ----------------------------------------------------------------------------

# link:
# xvideos:  ###############################
# url = "https://www.xvideos.com/?k=mifl&sort=relevance&durf=3-10min"
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, "html.parser")
# urls = []
# for a in soup.find_all('a', href=True):
#      urls.append(a['href'])
# urls_def = []
# for i in urls:
#     if "videos" in i:
#         next 
#     elif "video" in i:
#         urls_def.append(i)
     
# urls_xv = ["https://xvideos.com" + x for x in urls_def]
# print(urls_xv)
    
    
# ph: ##################################### 
# url = "https://it.pornhub.com/video/search?search=milf&min_duration=10&max_duration=30"
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, "html.parser")
# urls=[]
# for a in soup.find_all('a', href=True):
#     urls.append(a['href'])
# urls_def = []
# for i in urls:
#     if "view_video.php" in i:
#         urls_def.append(i) 
# urls = ["https://it.pornhub.com" + x for x in urls_def]


# yp: #####################################

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
# }
# url = "https://www.youporn.com/search/?search-btn=&query=milf"
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, "html.parser")
# urls = []
# for a in soup.find_all('a', href=True):
#      urls.append(a['href'])
# urls_def = []
# for i in urls:
#     if "watch" in i:
#         urls_def.append(i)     
# urls_yp = ["https://youporn.com" + x for x in urls_def]
# print(urls_yp)


# ----------------------------------------------------------------------------


# keyword:
# xvideos ####################
# url + "/?k=" + chr(keyword)

# pornhub  ####################
# url = url + "/video/search?search=" + chr(keyword)

# youporn  ####################
# url = url + "search/?search-btn=&query=" + chr(keyword)

# -------------------------------------------------------------------------- 

# durata:
# xvideos ####################
# url = url + "&sort=relevance&durf=" + chr(tempo minimo) +"-" + chr(tempo massimo) + "min"

# pornhub  ####################
# url = url + "&min_duration=" + chr(tempo minimo) + "&max_duration=" + chr(tempo massimo)

# youporn  ####################
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
# }
# max_time = 15
# min_time = 5
# url = "https://www.youporn.com/search/?search-btn=&query=milf"
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, "html.parser")
# duration = soup.find_all("div", class_="video-duration")
# duration_yp = [int(x.get_text()[0:2]) for x in duration]


# -----------------------------------------------------------------------------------


# randomize
# import random as rd
# def randomize(x):
#     x1 = rd.uniform(0, len(...))
#     x2 = rd.uniform(0, len(...))
#     x3 = rd.uniform(0, len(...))
#     while x1 == x2 or x1 == x3 or x2 == x3:
#         x1 = rd.uniform(0, len(...))
#         x2 = rd.uniform(0, len(...))
#         x3 = rd.uniform(0, len(...))
#     return list(x1, x2, x3)


# -----------------------------------------------------------------------------------





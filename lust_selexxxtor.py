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

  
<MyLayout>:

    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height

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
                        size_hint_x: None
                        width: self.texture_size[0]
                        padding_x: '5dp'
                        text: "Youporn"
                        group: "a"
                        on_press: root.yp()
                      
                
                    ToggleButton:
                        size_hint_x: None
                        width: self.texture_size[0]
                        padding_x: '5dp'
                        text: "Pornhub"
                        group: "a"
                        on_press: root.ph()
                
                    ToggleButton:
                        size_hint_x: None
                        width: self.texture_size[0]
                        padding_x: '5dp'
                        text: "Xvideos"
                        group: "a"
                        on_press: root.xv()
                
                MDTextField:
                    id: keywords 
                    hint_text: 'Keywords'
                            
                MDRaisedButton:
                    id: generate
                    text: "Generate my URLs"
                    size_hint_x: 1
                    on_press: root.scrape()
                
            GridLayout:
                cols: 1
                rows: 9
                
                BoxLayout:
                    orientation: 'vertical'
                
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
                            
                BoxLayout:
                    orientation: 'vertical'            
                    Label:
                        id: output2
                        text: 'Output2'
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
                            
                BoxLayout:
                    orientation: 'vertical'
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

Builder.load_string(KV)

class MyLayout(Widget):
  
  def scrape(self):
  self.keywords = "".join(self.ids.keywords.text).strip().split()
self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}


####### pornhub ##################################

if "".join(self.url) == "https://it.pornhub.com/":
  
  # add keywords:
  
  self.url = "".join(self.url)+ "video/search?search="
for kw in self.keywords:
  self.url = self.url + kw +"+"
self.url = self.url[:-1]

# add duration:
# self.url = self.url + "&min_duration=" + str(int(self.ids.min.value)) + "&max_duration=" + str(int(self.ids.max.value))

# scrap the obtained website:

self.response = requests.get(self.url, headers=self.headers)
self.soup = BeautifulSoup(self.response.content, "html.parser")

# titles
titles = self.soup.find_all("a", title = True)
titles_ph = [x["title"] for x in titles]
titles_ph = titles_ph[:-3]

# links
links = self.soup.find_all("a", title = True)
links_ph = [x["href"] for x in links]
links_def = []
for i in links_ph:
  if "view_video.php" in i:
  links_def.append(i) 
links_ph = ["https://pornhub.com" + str(x) for x in links_def]

a = round(rd.uniform(0, len(links_ph)-1))
b = round(rd.uniform(0, len(links_ph)-1))
c = round(rd.uniform(0, len(links_ph)-1))

self.ids.link1.text = links_ph[a]
self.ids.link2.text = links_ph[b]
self.ids.link3.text = links_ph[c]
self.ids.output1.text = titles_ph[a]
self.ids.output2.text = titles_ph[b]
self.ids.output3.text = titles_ph[c]



####### xvideos ##################################

elif "".join(self.url) == "https://www.xvideos.com/":
  
  # add keywords:
  
  self.url = "".join(self.url)+ "?k="
for kw in self.keywords:
  self.url = self.url + kw + "+"
self.url = self.url[:-1]

# add duration:
self.url = self.url + "&sort=relevance&durf=" + str(int(self.ids.min.value)) + "-" + str(int(self.ids.max.value)) +"min"

# scrap the obtained website:

self.response = requests.get(self.url, headers=self.headers)
self.soup = BeautifulSoup(self.response.content, "html.parser")

# titles
titles = self.soup.find_all("p", class_ = "title")
titles_xv = [x.get_text() for x in titles]

# links
links = self.soup.find_all("a", title = True)
links_xv = [x["href"] for x in links]
links_def = []
for i in links_xv:
  if "videos" in i:
  next 
elif "video" in i:
  links_def.append(i)

links_xv = ["https://xvideos.com" + x for x in links_def]


a = round(rd.uniform(0, len(links_xv)-1))
b = round(rd.uniform(0, len(links_xv)-1))
c = round(rd.uniform(0, len(links_xv)-1))

self.ids.link1.text = links_xv[a]
self.ids.link2.text = links_xv[b]
self.ids.link3.text = links_xv[c]
self.ids.output1.text = titles_xv[a]
self.ids.output2.text = titles_xv[b]
self.ids.output3.text = titles_xv[c]

####### youporn ##################################


# yp:   ###############################
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
# }
# url = "https://www.youporn.com/search/?search-btn=&query=milf"
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, "html.parser")


elif "".join(self.url) == "https://www.youporn.com/":
  
  # add keywords:
  
  self.url = "".join(self.url)+ "search/?search-btn=&query="
for kw in self.keywords:
  self.url = self.url + kw + "+"
self.url = self.url[:-1]

# scrape the obtained website:

self.response = requests.get(self.url, headers=self.headers)
self.soup = BeautifulSoup(self.response.content, "html.parser")

# titles
titles = self.soup.find_all("div", title = True)
titles_yp = [x["title"] for x in titles]
titles_yp = titles_yp[2:]        

# links
links = self.soup.find_all('a', href=True)
links_yp = [x["href"] for x in links]
links_def = []
for i in links_yp:
  if "watch-history" in i:
  next
elif "watch" in i:
  links_def.append(i)     
links_yp = ["https://youporn.com" + x for x in links_def]
# links_yp[1:]

a = round(rd.uniform(0, len(titles_yp)-1))
b = round(rd.uniform(0, len(titles_yp)-1))
c = round(rd.uniform(0, len(titles_yp)-1))

self.ids.link1.text = links_yp[a]
self.ids.link2.text = links_yp[b]
self.ids.link3.text = links_yp[c]
self.ids.output1.text = titles_yp[a]
self.ids.output2.text = titles_yp[b]
self.ids.output3.text = titles_yp[c]

print(self.url)
print(titles_yp[0])
print(len(titles_yp))
print(len(links_yp))
print(titles_yp)
print(links_yp)




def ph(self):
  self.url = "https://it.pornhub.com/", 
return self.url

def yp(self):
  self.url = "https://www.youporn.com/"
return self.url

def xv(self):
  self.url = "https://www.xvideos.com/"
return self.url



class LSXXX(MDApp):    
  
  def build(self):
  self.title = "Lust Selexxxtor"
self.theme_cls.theme_style = "Dark"
self.theme_cls.primary_palette = "Red"
self.theme_cls.primary_hue = "400"

return MyLayout ()

# class LSXXX(MDApp):    

#     def build(self):
#         self.title = "Lust Selexxxtor"
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "Red"
#         self.theme_cls.primary_hue = "400"
#         return Builder.load_string(KV)

#     def ph(self):
#         self.url = "https://pornhub.com/", 
#         return self.url

#     def yp(self):
#         self.url = "https://www.youporn.com"
#         return self.url

#     def xv(self):
#         self.url = "https://www.xvideos.com/"
#         return self.url

#     def scrape(self):
#         self.keywords = self.root.ids["keywords"].text.strip().split()
#         self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

# # ####### pornhub ##################################

#         # if self.url == "https://pornhub.com/":

#             # add keywords:
#             # self.url = "".join(self.url)+ "video/search?search="
#             # for kw in self.keywords:
#             #     self.url = self.url + "kw+"
#             # self.url = self.url[:-1]

#             # # # add duration:
#             # # self.url = self.url + "&min_duration=" + str(self.root.ids["min"].value) + "&max_duration=" + str(self.root.ids["max"].value)

#             # # scrap the obtained website:

#             # self.response = requests.get(self.url, headers=self.headers)
#             # self.soup = BeautifulSoup(self.response.content, "html.parser")

#             # # titles
#             # titles = self.soup.find_all("div", title=True)
#             # titles_ph = [x["title"] for x in titles]
#             # titles_ph = titles_ph[3:]

#             # # link
#             # links=[]
#             # for a in self.soup.find_all('a', href=True):
#             #     links.append(a['href'])
#             # links_def = []
#             # for i in links:
#             #     if "view_video.php" in i:
#             #         links_def.append(i) 
#             # links = ["https://pornhub.com" + str(x) for x in links_def]


#             # self.app.ids["link1"].text = "prova1"
#             # self.ids.link2.text = "prova1"
#             # self.ids.link3.text = "prova1"
#             # da ritornare sarebbero: durata, titolo e URL
#             # prova = self.root.ids["keywords"].text
#             # print(prova)
#             # self.root.ids["link1"].text = self.url1
#             # self.root.ids["link2"].text = self.url2
#             # self.root.ids["link3"].text = self.url3

# ####### youporn ##################################


#         # elif self.url == "https://www.youporn.com":

#         #     pass

# ####### xvideos ##################################

#         # elif self.url == "https://www.xvideos.com/":

#         #     pass

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





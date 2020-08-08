# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 10:05:22 2020

@author: mayan
"""

import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


urls = pd.read_csv('Video_URLS.csv')
urls = urls.drop("Unnamed: 0" , axis=1)

urls = urls.values.tolist()

Views= []
Uploaded_date = []
Likes = []
Dislikes =[]


for i in range(len(urls)):
  uClient = uReq(urls[i])
  page_html = uClient.read()
  uClient.close()
  beautiful_soup = (page_html, "html.parser")
 
  containers = beautiful_soup.findAll("div" , {"class" :"style-scope ytd-video-primary-info-renderer})
                                        
    Views.append(soup.find("span", attrs={"class": "view-count"}).text)
                                                
    Uploaded_date.append(soup.find("div", {"id": "date"}).text[1:]
    
    
  
   text_yt_formatted_strings = soup.find_all("yt-formatted-string", {"id": "text", "class": "ytd-toggle-button-renderer"})
   
   likes.append(ext_yt_formatted_strings[0].text)

    dislikes.append(text_yt_formatted_strings[1].text)
    
    
   Result = pd.DataFrame({'Urls' : [urls],
                                'Views' : [Views],
                                'Uploaded_date' : [Uploaded_date]
                                'Likes' : [Likes],
                                'Dislikes' : [Dislikes]
                            }, 
                                columns=['urls', 'Views','Uploaded_Dates','Likes', 'Dislikes'])
   
   
   Result.to_csv('Output_data.csv')
    
   
    



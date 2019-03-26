# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:44:33 2019

@author: Rohan
"""
# Subtitle Findler
import requests
from bs4 import BeautifulSoup
count = 0
usearch = input("Movie Name? : ")
search_url = "https://www.yifysubtitles.com/search?q="+usearch.replace(" ","+")
base_url = "https://www.yifysubtitles.com"
print(search_url)
resp = requests.get(search_url)
soup = BeautifulSoup(resp.content, 'lxml')
for link in soup.find_all("div",{"class": "media-body"}):       
    imdb = link.find('a')['href']                           #to find out movie url     
    movie_url = base_url+imdb                                   
    print("Movie URL : {}".format(movie_url))               #print the url to verify 
 
    next_page = requests.get(movie_url)                         
    soup2 = BeautifulSoup(next_page.content,'lxml')
    for links in soup2.find_all("tr",{"class": "high-rating"}): 
        for flags in links.find("td", {"class": "flag-cell"}):  
            if flags.text == "English":                         
                for dlink in links.find_all("td",{"class": "download-cell"}):   
                    half_link = dlink.find('a')['href']    #to find subtitle     
                    subtitle = base_url + half_link
                    if len(half_link) > 0:                  #print the link to subtitle file
                        print("Movie subtitle-link:  {}".format(subtitle))
                    else:
                        print("No Subtitle found!!! Thank You for visiting")
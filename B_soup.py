#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 14:23:34 2023

@author: nagatangeti
"""

from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html)
#title = soup.find('span','articletitle').string

for story_heading in soup.find_all(class_="story-heading"): 
   
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())
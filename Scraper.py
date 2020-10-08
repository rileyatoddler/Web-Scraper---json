# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:37:46 2020

@author: riley
"""

from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import numpy as np
import requests
import json
import csv
import io


global directory

dirRaw = []
directory = [[]]
url = "https://best-start.org/regions?id=21"
headers = {
    'Accept': '*/*',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Referer':"https://best-start.org/regions?id=21"}
response = requests.get(url=url, headers=headers)
jsonData = response.text
jsonData = json.loads(jsonData)
pageLen = len(jsonData)
for j in range(0,pageLen):
    name = jsonData[j]['name']#name
    address = jsonData[j]['address']#address
    street = jsonData[j]['street']#street
    dirRaw.append(name) #follow the order of column labels
    dirRaw.append(address)
    dirRaw.append(street)
    directory.append(dirRaw)
    dirRaw = []

file = io.open('directory.csv','w',encoding="utf-8", newline = '')
writer = csv.writer(file)
writer.writerow(['Name','Address','Street'])
for i in range(len(directory)):
    writer.writerow(directory[i])
file.close()
print('Saved')

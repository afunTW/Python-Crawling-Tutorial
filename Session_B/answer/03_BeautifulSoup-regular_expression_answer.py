
# coding: utf-8

# # SESSION B: 爬蟲實戰與資料分析

# In[1]:

# Session B 會用到的套件 (不包含資料分析部分)
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


# 
# ## 範例 03: BeautifulSoup + regular expression
# 
# 透過 BeautifulSoup 加上 regular expression ，能夠輕鬆的找出所有符合您規則的標籤、屬性或是內容。
# 
# 與 regular expression 的 **re.findall()** 不同在於，這邊必須使用 **re.compile**，如此一來 BeautifulSoup 就會知道您要使用 regular expression，並且回傳所有符合條件的標籤、屬性或是內容。

# In[2]:

# 萬年起手式
import requests
from bs4 import BeautifulSoup
import re

response = requests.get("https://jimmy15923.github.io/example_page")
soup = BeautifulSoup(response.text, 'lxml')


# In[3]:

soup.find_all(re.compile("t(d|r)"))  # 找出所有 td 或 tr 的標籤


# In[4]:

soup.find_all("", {"class":re.compile("z+")})    # 找出所有屬性為 class 且值包含至少一個 z 以上的標籤


# In[5]:

print(soup.find_all("", text=re.compile("python")))  # 找出所有 text 內容包含 python 文字的標籤


# ## 練習 03: BeautifulSoup + regular expression (8 mins)

# Q1. [範例網頁中](https://jimmy15923.github.io/example_page)可以看到有許多超連結，請找出那些超連結的網址是以資料協會網站開頭的標籤("http://foundation.datasci.tw/...")

# In[6]:

import requests
from bs4 import BeautifulSoup
import re


# In[7]:

# your codes
response = requests.get("https://jimmy15923.github.io/example_page")
soup = BeautifulSoup(response.text, 'lxml')
print(soup.find_all("", href=re.compile("http://foundation.datasci.tw/")))


# Q2. 請觀察[518 黃頁網](http://yp.518.com.tw/service-life.html?ctf=10)，並找出所有位在新北市的店家地址

# In[8]:

import requests
from bs4 import BeautifulSoup
import re


# In[9]:

# your codes
response = requests.get("https://jimmy15923.github.io/518")
soup = BeautifulSoup(response.text, 'lxml')
print(soup.find_all("li", class_="comp_loca", text=re.compile("新北")))


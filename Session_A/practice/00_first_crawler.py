
# coding: utf-8

# # SESSION A: 爬蟲基本介紹

# In[2]:

# Session A 用到的套件，如果有 import error，請打開 Anaconda Prompt 並參考 https://github.com/afunTW/dsc-crawling 的教學安裝套件
from bs4 import BeautifulSoup
import requests
import re


# ### 簡單的 Python 教學 (本課程會用到的部分，有 Python 基礎的同學可以跳過) 

# python 的資料形態，本課程會用到的主要有兩種 
# 1. List (串列)，把資料一個一個存在中括號 [ ] 裡面 
# 2. Dictionary (字典)，把資料透過 key:value 的方式存在一個大括號 {} 裡面

# In[2]:

example_list = [1, 2, 3]
print(type(example_list))
print(example_list)


# In[3]:

example_dictionay = {"a":1, "b":2, "c":3}
print(type(example_dictionay))
print(example_dictionay)


# #### python 的 loop 寫法
# 
# 進到 list (串列)裡面，依序把裡面的值取出來

# In[4]:

example_list = [1, 2, 3]
for num in example_list:
    print(num)


# 另一種簡潔的 loop 寫法

# In[5]:

[num for num in example_list]


# #### 建立新 list
# 
# 進到 list (串列)裡面，依序把值取出來並+1，再放回 list 裡面，最後將這個 list 存成一個新的 new_example_list

# In[6]:

example_list = [1, 2, 3]
print([num + 1 for num in example_list])
new_example_list = [num + 1 for num in example_list] #　把加過 1 的新 list 存成新的 new_example_list 變數


# ---
# ## 範例 00:  第一支爬蟲程式
# 如何透過程式，取出[範例網頁](https://jimmy15923.github.io/example_page)中的大標題「Python 爬蟲實戰」?
# 
# 請打開[範例網頁: https://jimmy15923.github.io/example_page](https://jimmy15923.github.io/example_page)，並在「Python 爬蟲實戰」的文字上按右鍵 → 檢查，可以看到這段文字被包在 h1 的標籤中

# In[ ]:

# import 套件


# 用 requests 抓取網頁 https://jimmy15923.github.io/example_page 並存在 response


# 用 BS4 解析 HTML 並把結果回傳 soup (lxml 是 BeautifulSoup 的解析器，預設是使用 html.parser，但是 lxml 的速度及性能較佳)


# 印出 h1 標籤


# ### requests 的函數
# requests 後的結果我們已經存成 response 這個變數，可以用許多 requests 內建的函數來了解 requets 回傳的結果 (可以輸入 response. 再按 tab 來看有甚麼函數)
# * [requests 官方文檔](http://docs.python-requests.org/en/master/)

# In[8]:

# 確認 requests 的結果
print(response.status_code)


# In[9]:

# 確認目標網站的編碼 (requets 會自動猜測目標網站的編碼，若猜測錯誤會顯示亂碼，需要手動修改)
print(response.encoding)


# In[10]:

# 目標網站的 HTML
response.text


# ## 練習 00: 淺嘗 BeautifulSoup

# In[11]:

# please insert the codes from slides, you can press shift + enter or ctrl + enter to run this cell
# your codes



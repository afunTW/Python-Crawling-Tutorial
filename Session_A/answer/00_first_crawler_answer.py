
# coding: utf-8

# ## 範例 00:  第一支爬蟲程式
# 如何透過程式，取出[範例網頁](https://jimmy15923.github.io/example_page)中的大標題「Python 爬蟲實戰」?
# 
# 請打開[範例網頁: https://jimmy15923.github.io/example_page](https://jimmy15923.github.io/example_page)，並在「Python 爬蟲實戰」的文字上按右鍵 → 檢查，可以看到這段文字被包在 h1 的標籤中

# In[ ]:

# import 套件
import requests
from bs4 import BeautifulSoup

# 用 requests 抓取網頁 https://jimmy15923.github.io/example_page 並存在 response
response = requests.get("https://jimmy15923.github.io/example_page")

# 用 BS4 解析 HTML 並把結果回傳 soup (lxml 是 BeautifulSoup 的解析器，預設是使用 html.parser，但是 lxml 的速度及性能較佳)
soup = BeautifulSoup(response.text, "lxml")

# 印出 h1 標籤
print(soup.find("h1"))


# ## 練習 00: 淺嘗 BeautifulSoup

# In[ ]:

# please insert the codes from slides, you can press shift + enter or ctrl + enter to run this cell
# your codes

print(soup.find("h1"))
print(soup.h1)
print(soup.html.h1)
print(soup.body.h1)
print(soup.html.body.h1)


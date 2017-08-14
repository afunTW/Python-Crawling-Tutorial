
# coding: utf-8

# ## 範例 05 : 使用 pandas 儲存資料
# 
# pandas 是 Python 中處理數據非常強大的一個函式庫，不論是讀寫 Data、清洗、轉換、分析等，均有許多方便好用的函數幫忙，熟悉 pandas 可以說是用 Python 做資料分析的第一步!
# 
# 範例 05 將會帶大家學習如何使用 pandas 將我們抓取的資料存成結構化的數據
# 
# 補充資料
# * [pandas 官方文檔](https://pandas.pydata.org/pandas-docs/stable/index.html)
# * [pandas tutourials](http://pandas.pydata.org/pandas-docs/version/0.15.2/tutorials.html)
# * [10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/10min.html)
# * [Python for Data Analysis 電子書](http://www3.canisius.edu/~yany/python/Python4DataAnalysis.pdf)

# ### 1. 使用 columns 來建立 DataFrame

# In[1]:

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# 將要查詢的資料寫成 dictionary
form_data = {
 "StartStation":"2f940836-cedc-41ef-8e28-c2336ac8fe68",
 "EndStation":"9c5ac6ca-ec89-48f8-aab0-41b738cb1814",
 "SearchDate":"2017/08/14",
 "SearchTime":"21:30", 
 "SearchWay":"DepartureInMandarin"}

response_post = requests.post("https://www.thsrc.com.tw/tw/TimeTable/SearchResult", data = form_data) # 使用 POST
soup_post = BeautifulSoup(response_post.text, "lxml") # 用 BeautifulSoup 解析網頁


# In[2]:

train_number = [tag.text for tag in soup_post.find_all("td", class_="column1")] # 找出所有 td 標籤 屬性 class=column1 的內容，並存成 List
departure = [tag.text for tag in soup_post.find_all("td", class_="column3")] # 找出所有 td 標籤 屬性 class=column3 的內容，並存成 List
arrival = [tag.text for tag in soup_post.find_all("td", class_="column4")] # 找出所有 td 標籤 屬性 class=column4 的內容，並存成 List
travel_time = [tag.text for tag in soup_post.find_all("td", class_="column2")] # 找出所有 td 標籤 屬性 class=column2 的內容，並存成 List


# In[3]:

highspeed_df = pd.DataFrame({"車次":train_number,
                          "出發時間":departure,
                          "抵達時間":arrival,
                          "行車時間":travel_time}, columns = ["車次", "出發時間", "抵達時間", "行車時間"])


# In[4]:

highspeed_df 


# In[5]:

highspeed_df.to_csv("csv_results/demo6_highspeed_schedule_cp950.csv", index = False, encoding = "cp950")


# ### 2. 使用 rows 來建立 DataFrame

# In[6]:

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# 將要查詢的資料寫成 dictionary
form_data = {
 "StartStation":"2f940836-cedc-41ef-8e28-c2336ac8fe68",
 "EndStation":"9c5ac6ca-ec89-48f8-aab0-41b738cb1814",
 "SearchDate":"2017/08/14",
 "SearchTime":"21:30", 
 "SearchWay":"DepartureInMandarin"}

response_post = requests.post("https://www.thsrc.com.tw/tw/TimeTable/SearchResult", data = form_data) # 使用 POST
soup_post = BeautifulSoup(response_post.text, "lxml") # 用 BeautifulSoup 解析網頁


# In[7]:

highspeed_df = pd.DataFrame(columns = ["車次", "出發時間", "抵達時間", "行車時間"]) # 先建立好 DataFrame 


# In[8]:

for i in range(3):
    print(i)
    row = soup_post.find_all("table", class_="touch_table")[i] # table 這個標籤包含所有行車資訊，我們用 index 一個一個 by row 取出來
    row_contents = [tag.text for tag in row.find_all("td", class_= re.compile("column"))] # 一個 row 有包含其他資訊，我們只要選出 class 包含 column 的 內容
    highspeed_df.loc[i] = row_contents # DataFrame 中， 第 i 行的值等於 row_text


# In[9]:

highspeed_df 


# In[10]:

# for windows
highspeed_df.to_csv("csv_results/demo6_highspeed_schedule_cp950.csv", index = False, encoding = "cp950")

# for linux
highspeed_df.to_csv("csv_results/demo6_highspeed_schedule_utf8.csv", index = False, encoding = "utf-8")


# ## 練習 05 : 使用 pandas 將抓下來的資訊儲存成表格
# 
# 請觀察[518 黃頁網](http://yp.518.com.tw/service-life.html?ctf=10)，並將店名、地址及電話三個欄位抓下來，並存成表格如 PPT 所示
# * 觀察店名、地址及電話都藏在哪些標籤底下? 有共用的屬性嗎?
# * 選擇要用 Rows 或 Columns 來組成 DataFrame
# * 請將檔案儲存在 csv_results 這個資料夾

# In[11]:

# your codes


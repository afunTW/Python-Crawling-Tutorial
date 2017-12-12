
# coding: utf-8

# ---
# ## 範例 06: 爬蟲實戰練習 (15~20 mins)
# 接下來就是大家今天的實戰練習時間囉! 這邊的練習會希望大家能夠自行透過觀察網頁，把目標網頁的資訊爬取回來，並存成 CSV 以利後續的分析。
# 
# 今天大家要爬取的目標網頁共有兩個
# 1. [台北票房觀測站 - 年度排名 (2016+2017)](http://www.taipeibo.com/year/2017) 的票房資料
# 2. [Yahoo電影評論](https://tw.movies.yahoo.com/movieinfo_main.html/id=6664)，包含電影名稱、評論文字、評論星等
# 
# 以下的範例 code 會示範如何抓下[年度周末冠軍](http://www.taipeibo.com/yearly)的網頁資訊，各位強者同學們如果已經躍躍欲試的話可以跳過以下的提示 code，直接開始練習囉!
# 
# 如果真的沒有頭緒的話可以參考以下的 code

# In[1]:

import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:

response = requests.get("http://www.taipeibo.com/yearly") # 取得網頁
response.encoding ="utf-8" # 設定 encoding = 'utf-8' (如果不設定，會發生甚麼事情呢?)
soup = BeautifulSoup(response.text, 'lxml') # 用 BS4 parse 網頁


# In[3]:

# 在觀察網頁之後，發現表格中每一列的文字都躲在 tr 標籤底下，並用 td 包起來。

all_rows = soup.table.find_all("tr") # 找出所有 tr 標籤，並存成 list
print(all_rows[:2]) # 印出前兩筆資料


# In[4]:

column_name_tag = all_rows[0] # 標題名稱的標籤就是 all_rows 的第一筆資料 


# In[5]:

print([text for text in column_name_tag.stripped_strings]) # 把使用 strpped_strings 取出來的值印出來，可以看到就是我們想要的標題
column_name = [text for text in column_name_tag.stripped_strings] # 把這些標題存成 column_name 這個變數


# In[6]:

movie_df = pd.DataFrame(columns = column_name) # 建立一個空的 DataFrame，標題等於剛剛抓下來的 column_name
movie_df


# In[7]:

movie_df = pd.DataFrame(columns = column_name) # 第一個 row 為標題
for i, row in enumerate(all_rows[1:]): # 從第二個 row 開始 iterate (因為第一個 row 是標題)
    data_want = [s for s in row.stripped_strings]
    print(data_want)
    movie_df.loc[i] = data_want # 設定 DataFrame 的第 i 個 row 是我們抓下來的資訊


# In[8]:

movie_df.head() # 大功告成! 就只剩把 DataFrame 存起來就好，那接下來就請聰明的各位來練習一下囉!


# ## 練習 06-1: 台北票房觀測站爬蟲
# 請將 2016 [年度排名](http://www.taipeibo.com/year/2016)與 2017 的[年度排名](http://www.taipeibo.com/year/2017) 網頁分別抓下來 並合併後存成一個 csv 檔案，請將檔案儲存至 csv_results/ 這個資料夾底下
# 
# Hint
# * DF = df1.append(df2) 
# 這段 code 可以把兩個 DataFrame 垂直合併成一個新的 DF

# In[9]:

# your codes
import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("http://www.taipeibo.com/year/2016")
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")

# 標題名稱藏在第一個 tr 標籤底下
print([col for col in soup.table.find("tr").stripped_strings])
col_name =  [col for col in soup.table.find("tr").stripped_strings]

# 建立空 DataFrame，標題名稱為 col_name
sale_df= pd.DataFrame(columns = [col_name])

# 每一個 row 的資料都藏在 table 底下的 tr 標籤，用 all_rows 把全部的 rows 都存起來
all_rows = [row for row in soup.table.find_all("tr")]

# loop 全部的 row (除了第一個是標題)，把每個 row 的底下的文字存進 DataFrame 的第 i 列
for i, row in enumerate(all_rows[1:]):
    sale_df.loc[i] = [s for s in row.stripped_strings]
    
sale_df.head()


# ## 練習 06-2: Yahoo 電影評論爬蟲 (20~25 mins)
# 
# 請仔細觀察 Yahoo 電影評論的網頁，您將需要把任何一部在票房排行榜上您喜歡的電影的
# 1. 電影名稱 
# 2. 每條評論文字
# 3. 每條評論星等
# 
# 都爬取下來並存成 CSV，請將檔案儲存至 csv_results/ 這個資料夾底下，如果沒有頭緒要抓哪部，可以試試[玩命關頭8](https://tw.movies.yahoo.com/movieinfo_review.html/id=6664)
# 
# 
# 這題的可能會稍微比較有挑戰一些，如果卡住請大家不要灰心，可以與旁邊的同學討論或是隨時舉手請問助教，以下是一些提示
# 1. 請先觀察每一頁評論的網址 (URL) 都是甚麼，有沒有甚麼特殊的規律?
# 2. 如果要抓取總共有幾頁評論，要怎麼抓取哪個標籤呢?
# 3. 評論文字都藏在哪些標籤裡?
# 4. 評論有幾顆星星好像找不到? 試試找其他方向，說不定在意想不到的地方喔
# 5. 如何把每一頁抓完的評論 list 合併成一個 大 list? 可以使用 big_list.extend(small_list)，可以把許多小 list merge 成一個大的 list
# 
# **如果真的沒有頭緒的話，可以先把問題簡化，嘗試看看把其中一頁的評論抓下來試試看!**

# In[11]:

import sys
# your codes
response = requests.get("https://tw.movies.yahoo.com/movieinfo_review.html/id=6664")
soup = BeautifulSoup(response.text, "html.parser")

# 找到該電影共有幾頁評論
page = int(soup.find("div", {"class":"page_numbox"}).find_all("a")[-2].text)

# 建立空 list，準備儲存所有的評論文字及星等
comment_all = []
star_all = []

# 建立空 DataFrame 設定好 columns 名稱
comment_df = pd.DataFrame(columns =  ["movie", "comments", "star"])
    
# 電影名稱的則是在 div 標籤，屬性 class=inform_title
movie_name = soup.find("div", {"class":"inform_title"}).text

# 對每頁的評論送 requests，並把評論文字、星等抓下來，存進剛剛建好的空 list
for i in range(1, page):
    sys.stdout.write("\r正在抓取玩命關頭電影評論第 " + str(i) + " 頁")
    response = requests.get("https://tw.movies.yahoo.com/movieinfo_review.html/id=6664?sort=update_ts&order=desc&page=" + str(i) )
    soup = BeautifulSoup(response.text, "html.parser")

    # 評論文字存在 span 且沒有任何屬性的標籤裡，把每個人的評論先存成 list，再把這個 list 放進 comment_all 裡面
    comment = [x.find("span", {"class":None}).text for x in soup.find_all("div", {"class":"usercom_inner _c"})]
    comment_all.extend(comment)

    # 要抓取評論星等，首先定位出每個評論所在的位置，觀察後發現在 div 標籤，屬性 class=usercom_inner _c，評論星等就在這個 div 裡的 inputs 標籤
    star = [comment.find("input", {"name":"score"})['value'] for comment in soup.find_all("div", {"class":"usercom_inner _c"})]
    star_all.extend(star)

# 建立 DataFrame
comment_df = pd.DataFrame({"comments":comment_all,
                           "movie":movie_name,
                          "star":star_all})

# 看最後五筆資料
comment_df.tail()


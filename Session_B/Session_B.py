
# coding: utf-8

# # SESSION B: 爬蟲實戰與資料分析

# In[1]:

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
response = requests.get("https://jimmy15923.github.io/example_page")
soup = BeautifulSoup(response.text, 'lxml')


# In[3]:

soup.find_all(re.compile("t(d|r)"))  # 找出所有 td 或 tr 的標籤


# In[4]:

soup.find_all("", {"class":re.compile("z+")})    # 找出所有屬性為 class 且值包含至少一個 z 以上的標籤


# In[5]:

print(soup.find_all("", text = re.compile("python")))  # 找出所有 text 內容包含 python 文字的標籤


# ## 練習 03: BeautifulSoup + regular expression (8 mins)

# 請找出[範例網頁中](https://jimmy15923.github.io/example_page)，所有標籤且其屬性 href 的值是以資料科學協會網站為開頭 ("http://foundation.datasci.tw/...")

# In[6]:

# your codes


# 請觀察[518 黃頁網](http://yp.518.com.tw/service-life.html?ctf=10)，並找出所有位在新北市的店家地址

# In[7]:

# your codes


# -------------------------
# ## 範例 04: 如何使用 POST
# 
# 請打開[高鐵時刻表](https://www.thsrc.com.tw/tw/TimeTable/SearchResult)的網頁，並按照 slides 的介紹，觀察 requests 的方式

# In[8]:

# 這是我們還沒有給任何 form_data 的 requests
response = requests.get("https://www.thsrc.com.tw/tw/TimeTable/SearchResult")
print(response.encoding)
soup = BeautifulSoup(response.text, "lxml")


# In[9]:

# 觀察 option 裡面的 value
soup.find_all("option", {"value":re.compile("[a-z0-9]{8}-[a-z0-9]{4}")})


# In[10]:

# 在還沒給任何 form_data 之前，我們是看不到搜尋後的結果的
print(soup.find("section", class_ = "result_table"))


# In[11]:

# 將 form_data 透過 post 的方式進行 requests
form_data = {"StartStation":"2f940836-cedc-41ef-8e28-c2336ac8fe68",
             "EndStation":"e6e26e66-7dc1-458f-b2f3-71ce65fdc95f",
             "SearchDate":"2017/08/13",
             "SearchTime":"20:30",
             "SearchWay":"DepartureInMandarin"}
response_post = requests.post("https://www.thsrc.com.tw/tw/TimeTable/SearchResult", data = form_data)
soup_post = BeautifulSoup(response_post.text, "lxml")


# In[12]:

# 用同樣的搜尋條件，可以看到搜尋後的結果
soup_post.find("section", class_ = "result_table").find("tr")


# ## 練習 04: 如何使用 POST (8 mins)
# 請運用 POST 方式，找出 2017 年 8 月 14 日 21:30，**南港站**到**台南站**共有幾個班次?
# 
# Hint: 先到高鐵時刻表網站，實際查詢之後，看看班次的資訊都藏在哪些 tags 裡面

# In[13]:

# your codes

# 將要查詢的資料寫成 dictionary


# requests 改用 POST，並放入剛剛寫好的 dictionary




# ---
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

# In[14]:

# 將要查詢的資料寫成 dictionary
form_data = {
 "StartStation":"2f940836-cedc-41ef-8e28-c2336ac8fe68",
 "EndStation":"9c5ac6ca-ec89-48f8-aab0-41b738cb1814",
 "SearchDate":"2017/08/14",
 "SearchTime":"21:30", 
 "SearchWay":"DepartureInMandarin"}

response_post = requests.post("https://www.thsrc.com.tw/tw/TimeTable/SearchResult", data = form_data) # 使用 POST
soup_post = BeautifulSoup(response_post.text, "lxml") # 用 BeautifulSoup 解析網頁


# In[15]:

train_number = [tag.text for tag in soup_post.find_all("td", class_="column1")] # 找出所有 td 標籤 屬性 class=column1 的內容，並存成 List
departure = [tag.text for tag in soup_post.find_all("td", class_="column3")] # 找出所有 td 標籤 屬性 class=column3 的內容，並存成 List
arrival = [tag.text for tag in soup_post.find_all("td", class_="column4")] # 找出所有 td 標籤 屬性 class=column4 的內容，並存成 List
travel_time = [tag.text for tag in soup_post.find_all("td", class_="column2")] # 找出所有 td 標籤 屬性 class=column2 的內容，並存成 List


# In[16]:

highway_df = pd.DataFrame({"車次":train_number,
                          "出發時間":departure,
                          "抵達時間":arrival,
                          "行車時間":travel_time}, columns = ["車次", "出發時間", "抵達時間", "行車時間"])


# In[17]:

highway_df 


# In[18]:

highway_df.to_csv("csv_results/demo6_highway_schedule.csv", index = False, encoding = "cp950")


# ### 2. 使用 rows 來建立 DataFrame

# In[19]:

# 將要查詢的資料寫成 dictionary
form_data = {
 "StartStation":"2f940836-cedc-41ef-8e28-c2336ac8fe68",
 "EndStation":"9c5ac6ca-ec89-48f8-aab0-41b738cb1814",
 "SearchDate":"2017/08/14",
 "SearchTime":"21:30", 
 "SearchWay":"DepartureInMandarin"}

response_post = requests.post("https://www.thsrc.com.tw/tw/TimeTable/SearchResult", data = form_data) # 使用 POST
soup_post = BeautifulSoup(response_post.text, "lxml") # 用 BeautifulSoup 解析網頁


# In[20]:

highway_df = pd.DataFrame(columns = ["車次", "出發時間", "抵達時間", "行車時間"]) # 先建立好 DataFrame 


# In[21]:

for i in range(3):
    print(i)
    row = soup_post.find_all("table", class_="touch_table")[i] # table 這個標籤包含所有行車資訊，我們用 index 一個一個 by row 取出來
    row_contents = [tag.text for tag in row.find_all("td", class_= re.compile("column"))] # 一個 row 有包含其他資訊，我們只要選出 class 包含 column 的 內容
    highway_df.loc[i] = row_contents # DataFrame 中， 第 i 行的值等於 row_text


# In[22]:

highway_df 


# In[23]:

# for windows
highway_df.to_csv("csv_results/demo6_highway_schedule.csv", index = False, encoding = "cp950")

# for linux
highway_df.to_csv("csv_results/demo6_highway_schedule.csv", index = False, encoding = "utf-8")


# ## 練習 05 : 使用 pandas 將抓下來的資訊儲存成表格
# 
# 請觀察[518 黃頁網](http://yp.518.com.tw/service-life.html?ctf=10)，並將店名、地址及電話三個欄位抓下來，並存成表格如 PPT 所示
# * 觀察店名、地址及電話都藏在哪些標籤底下? 有共用的屬性嗎?
# * 選擇要用 Rows 或 Columns 來組成 DataFrame
# * 請將檔案儲存在 csv_results 這個資料夾

# In[24]:

# your codes


# ---
# ## 範例 06: 爬蟲實戰練習
# 接下來就是大家今天的實戰練習時間囉! 這邊的練習會希望大家能夠自行透過觀察網頁，把目標網頁的資訊爬取回來，並存成 CSV 以利後續的分析。
# 今天大家要爬取的目標網頁共有兩個
# 1. [台北票房觀測站 (2016+2017)](http://www.taipeibo.com/year/2017) 的票房資料
# 2. [Yahoo電影評論](https://tw.movies.yahoo.com/movieinfo_main.html/id=6664)，包含電影名稱、評論文字、評論星等
# 
# 以下的範例 code 會示範如何抓下[年度周末冠軍](http://www.taipeibo.com/yearly)的網頁資訊，各位強者同學們已經躍躍欲試的話可以跳過以下的範例，直接開始練習喔!
# 
# 如果真的沒有頭緒的話可以參考以下的 code

# In[25]:

res = requests.get("http://www.taipeibo.com/yearly") # 取得網頁
res.encoding ="utf-8" # 設定 encoding = 'utf-8' (如果不設定，會發生甚麼事情呢?)
soup = BeautifulSoup(res.text, 'lxml') # 用 BS4 parse 網頁


# In[26]:

# 在觀察網頁之後，發現表格中每一列的文字都躲在 tr 標籤底下，並用 td 包起來。

all_rows = soup.table.find_all("tr") # 找出所有 tr 標籤，並存成 list
print(all_rows[:2]) # 印出前兩筆資料


# In[27]:

column_name_tag = all_rows[0] # 標題名稱的標籤就是 all_rows 的第一筆資料 


# In[28]:

print([text for text in column_name_tag.stripped_strings]) # 把使用 strpped_strings 取出來的值印出來，可以看到就是我們想要的標題
column_name = [text for text in column_name_tag.stripped_strings] # 把這些標題存成 column_name 這個變數


# In[29]:

movie_df = pd.DataFrame(columns = column_name) # 建立一個空的 DataFrame，標題等於剛剛抓下來的 column_name
movie_df


# In[30]:

movie_df = pd.DataFrame(columns = column_name) # 第一個 row 為標題
for i, row in enumerate(all_rows[1:]): # 從第二個 row 開始 iterate (因為第一個 row 是標題)
    data_want = [s for s in row.stripped_strings]
    print(data_want)
    movie_df.loc[i] = data_want # 設定 DataFrame 的第 i 個 row 是我們抓下來的資訊


# In[31]:

movie_df.head() # 大功告成! 就只剩把 DataFrame 存起來就好，那接下來就請聰明的各位來練習一下囉!


# ## 練習 06-1: 台北票房觀測站爬蟲
# 請將 2016 [年度排名](http://www.taipeibo.com/year/2016)與 2017 的[年度排名](http://www.taipeibo.com/year/2017) 網頁分別抓下來 並合併後存成一個 csv 檔案
# 
# Hint
# * DF = df1.append(df2) 
# 這段 code 可以把兩個 DataFrame 合併成一個新的 DF

# In[32]:

# your codes



# ## 練習 06-2: Yahoo 電影評論爬蟲
# 
# 請仔細觀察 Yahoo 電影評論的網頁，您將需要把任何一部在票房排行榜上您喜歡的電影的
# 1. 電影名稱 
# 2. 每條評論文字
# 3. 每條評論星等
# 
# 都爬取下來並存成 CSV，如果沒有頭緒要抓哪部，可以試試[玩命關頭8](https://tw.movies.yahoo.com/movieinfo_review.html/id=6664)
# 
# 
# 這題的可能會稍微比較有挑戰一些，如果卡住請大家不要灰心，可以與旁邊的同學討論或是隨時舉手請問助教，以下是一些提示
# 1. 請先觀察每一頁評論的網址 (URL) 都是甚麼，有沒有甚麼特殊的規律?
# 2. 如果要抓取總共有幾頁評論，要怎麼抓取哪個標籤呢?
# 3. 評論文字都藏在哪些標籤裡?
# 4. 評論有幾顆星星好像找不到? 試試找其他地方，說不定在意想不到的地方喔
# 5. 如何把每一頁抓完的評論 list 合併成一個 大 list? 可以使用 big_list.extend(small_list)，可以把許多小 list merge 成一個大的 list
# 
# **如果真的沒有頭緒的話，可以先把問題簡化，嘗試看看把其中一頁的評論抓下來試試看!**

# In[33]:

# your codes



# -----
以下 codes 僅供參考，會將所有票房排行榜 200 部電影的 yahoo 電影評論全部抓下來，並存成 CSV (請不要在今天執行，以免影響網路速度與 yahoo 電影流量)

with open("data/all_movie_id.json", 'r', encoding="utf-8") as f:
    movie_id = json.load(f)
    
movie_name_list = pd.read_csv("data/movies_box_office.csv")["中文片名"]
success = []
all_df = []
for x in movie_name_list:
    print("開始爬取: ", x)
    id = movie_id[x]
    response = requests.get("https://tw.movies.yahoo.com/movieinfo_review.html/id=" + str(id))
    soup = BeautifulSoup(response.text, "html.parser")
    if soup.find("div", {"class":"page_numbox"}) != None:
        page = int(soup.find("div", {"class":"page_numbox"}).find_all("a")[-2].text)
        
        comment_all = []
        star_all = []
        comment_df = pd.DataFrame(columns =  ["movie", "comments", "star"])

        for i in range(1, page):
            response = requests.get("https://tw.movies.yahoo.com/movieinfo_review.html/id=" + id + "?sort=create_ts&order=desc&page=" + str(i) )
            soup = BeautifulSoup(response.text, "html.parser")

            comment = [x.find("span").text for x in soup.find_all("div", {"class":"usercom_inner _c"})]
            comment_all.extend(comment)

            star = [comment.find("input", {"name":"score"})['value'] for comment in soup.find_all("div", {"class":"usercom_inner _c"})]
            star_all.extend(star)

        movie_name = soup.find("div", {"class":"inform_title"}).text
        comment_df = pd.DataFrame({"comments":comment_all,
                                   "movie":movie_name,
                                  "star":star_all})
        if len(comment_df)!= 0:
            success.append(x) 
    else:
        comment_all = []
        star_all = []
        comment_df = pd.DataFrame(columns =  ["movie", "comments", "star"])
        
        comment = [x.find("span").text for x in soup.find_all("div", {"class":"usercom_inner _c"})]
        comment_all.extend(comment)

        star = [comment.find("input", {"name":"score"})['value'] for comment in soup.find_all("div", {"class":"usercom_inner _c"})]
        star_all.extend(star)

        movie_name = soup.find("div", {"class":"inform_title"}).text
        comment_df = pd.DataFrame({"comments":comment_all,
                                   "movie":movie_name,
                                  "star":star_all})
        if len(comment_df)!= 0:
            success.append(x) 
    
    all_df.append(comment_df)
    
movies_comments = pd.concat(all_df, axis=0)
movies_comments.to_csv("data/movies_comments_crawled.csv", index = False, encoding="utf-8")
# ---
# 
# ## 範例 07: 資料清理與分析
# 
# 到這邊我們已經將需要的票房資料與評論星等、內容都爬下來囉!
# 
# 在進入分析之前，我們需要對抓下來的資料做一些簡單的清洗

# ### 1. 票房資料清洗
# 票房的資料可以看到是以 str 儲存，為了方便之後的分析，要轉成數字型態 float or int

# In[34]:

movie_box = pd.read_csv("data/movies_box_office.csv")
movie_box.head()


# In[35]:

movie_box["平均票房"] = movie_box["平均票房"].str.replace(",", "").astype("float")
movie_box["累積票房"] = movie_box["累積票房"].str.replace(",", "").astype("float")


# In[36]:

movie_box.head()


# In[37]:

movie_box.to_csv("data/movies_box_office_revised.csv", index = False, encoding="utf-8") # 儲存清洗後的資料


# ### 2. 評論資料清洗
# 電影名稱那邊可以看到中文跟英文都並在一起，透過 pandas 簡單的 split 函數可以拆開來

# In[38]:

movies_comments = pd.read_csv("data/movies_comments.csv")
movies_comments.head()


# In[39]:

movies_comments["movie"].str.split("\n", 2, expand=True).head()


# In[40]:

movies_comments["movie_cht"] = movies_comments["movie"].str.split("\n", 2, expand=True)[0] # 拆開的第一部份存成 movie_cht
movies_comments["movie_eng"] = movies_comments["movie"].str.split("\n", 2, expand=True)[1] # 拆開的第二部份存成 movie_eng
del movies_comments["movie"]


# In[41]:

movies_comments.head()


# In[42]:

movies_comments.to_csv("data/movies_comments_revised.csv", index = False, encoding="utf-8") # 儲存清洗後的資料


# ## 範例 08: 文字探勘與文字雲
# 範例 08 會利用 jieba, wordcloud 這兩個套件，帶大家玩一些簡單的文字探勘，並用文字雲把斷詞後的結果畫出來

# In[43]:

import jieba
import jieba.analyse
import numpy as np
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
from PIL import Image
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] # 設定 matplotlib 的中文字體
jieba.set_dictionary('data/dict.txt.big')  # 設定 jiebe 使用斷詞的語料庫


# In[44]:

movies_comments = pd.read_csv("data/movies_comments_revised.csv")
neg = movies_comments[(movies_comments["star"] == 1)]  # 取出所有一顆星的評論
pos = movies_comments[(movies_comments["star"] == 5)]  # 取出所有五顆星的評論


# In[45]:

neg_text = ''.join(neg["comments"])  # 將 list of string 轉變成一個大字串
pos_text = ''.join(pos["comments"])  # 將 list of string 轉變成一個大字串


# In[46]:

jieba.add_word('不好看') # 加上不好看這個詞


# In[47]:

neg_list = jieba.cut(neg_text)  # 將大字串斷詞後變成一個 list
pos_list = jieba.cut(pos_text)  # 將大字串斷詞後變成一個 list


# In[48]:

with open('data/stop_words.txt','r', encoding='utf-8') as f:
    stopwords = f.readlines()
    stopwords = [x.replace("\n","") for x in stopwords]
    
neg_text_filtered = ' '.join([word for word in neg_list if word not in stopwords]) #將停止詞濾掉
pos_text_filtered = ' '.join([word for word in pos_list if word not in stopwords]) #將停止詞濾掉


# In[49]:

neg_text_list = [item for item in neg_text_filtered.split(" ") if item.split()] #保留非空白的詞
pos_text_list = [item for item in pos_text_filtered.split(" ") if item.split()] #保留非空白的詞


# In[50]:

neg_counter = Counter(neg_text_list) # Counter 可以幫忙對 list 做記數
print(neg_counter.most_common(20))


# In[51]:

pos_counter = Counter(pos_text_list) # Counter 可以幫忙對 list 做記數
print(pos_counter.most_common(20))


# In[52]:

mask_use = "data/circle_mask.png" # 可以改成 "data/Alice_mask.jpg"，在重新執行程式，看看文字雲會怎麼變化
mask = np.array(Image.open(mask_use))


# In[53]:

wordcloud = WordCloud(background_color="white", # 設定背景顏色
                      mask=mask, # 決定圖片的形狀
                      max_font_size=100, # 字體大小
                      font_path='data/NotoSansCJKtc-Black.otf', # 設定字型
                      random_state=38).fit_words(neg_counter) # 丟入文字

plt.imshow(wordcloud, interpolation='bilinear')
plt.title("一顆星評論")
plt.axis("off")
plt.savefig("plots/one_star_wordcloud.png", dpi = 700)
plt.show()


# In[54]:

wordcloud = WordCloud(background_color="white",
                      mask=mask, max_font_size=100, 
                      font_path='data/NotoSansCJKtc-Black.otf', 
                      random_state=38).fit_words(pos_counter)

plt.imshow(wordcloud, interpolation='bilinear')
plt.title("五顆星評論")
plt.axis("off")
plt.savefig("plots/five_star_wordcloud.png", dpi = 700)
plt.show()


# ### 透過 TF - IDF 進行文字分析

# In[55]:

jieba.analyse.set_stop_words(stop_words_path='data/stop_words.txt')


# In[56]:

pos_words = jieba.analyse.extract_tags(pos_text, 500, withWeight=True)
print("TF-IDF 正面評價詞: ", pos_words[:20])


# In[57]:

neg_words = jieba.analyse.extract_tags(neg_text, 500, withWeight=True)
print("TF-IDF 負面評價詞: ", neg_words[:20])


# In[58]:

# 經過 TF-IDF 篩選過之後的文字雲
wordcloud = WordCloud(background_color="white", 
                      mask=mask,
                      max_font_size=100,
                      font_path='data/NotoSansCJKtc-Black.otf', 
                      random_state=8).fit_words(dict(neg_words))

plt.imshow(wordcloud, interpolation='bilinear')
plt.title("一顆星評論")
plt.axis("off")
plt.savefig("plots/one_star_wordcloud_tfidf.png", dpi = 700)
plt.show()


# In[59]:

# 經過 TF-IDF 篩選過之後的文字雲
wordcloud = WordCloud(background_color="white",
                      mask=mask,
                      max_font_size=100,
                      font_path='data/NotoSansCJKtc-Black.otf', 
                      random_state=8).fit_words(dict(pos_words)) 

plt.imshow(wordcloud, interpolation='bilinear')
plt.title("五顆星評論")
plt.axis("off")
plt.savefig("plots/five_star_wordcloud_tfidf.png", dpi = 700)
plt.show()


# ---
# ## 範例 09: 票房資料分析
# 範例 09 會示範利用常見的 regression 與 classification 對我們的票房資料做一些資料分析
# 
# regression 使用 linear regression，classification 則會使用 decision tree

# In[60]:

# import 套件
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from scipy.stats import pearsonr


# In[61]:

movie_box = pd.read_csv("data/movies_box_office_revised.csv")  # 讀取票房資料


# In[62]:

movie_box.head()


# In[63]:

movie_box["平均星等"] = movies_comments.groupby("movie_cht", sort=False)["star"].mean().values # 將平均星等放進票房資料的 DF
movie_box.head()


# In[64]:

# 切 training data 跟 testing data
X_train, X_test, y_train, y_test = train_test_split(movie_box["平均星等"], np.log10(movie_box["平均票房"]), random_state = 22)

# 建立 LinearRegression 模型
reg = LinearRegression()

# 放進 traingin data 進行訓練 (因為只有一個自變數，新版的 sklearn 必須做 reshape)
reg.fit(X = X_train.values.reshape(-1, 1), y = y_train)

# 用 testing data 做 prediction
y_pred = reg.predict(X_test.values.reshape(-1, 1))

# 算出 testing data 與預測結果的 correlation
print(pearsonr(y_pred, y_test)[0])


# In[65]:

# 把全部的 data 畫上 fit 之後的線
reg.fit(X = movie_box["平均星等"].values.reshape(-1, 1), y = np.log10(movie_box["平均票房"]))
y_pred = reg.predict(movie_box["平均星等"].values.reshape(-1, 1))

plt.plot(movie_box["平均星等"], np.log10(movie_box["平均票房"]), ".")
plt.plot(movie_box["平均星等"], y_pred)
plt.xlabel("評論星等")
plt.ylabel("平均票房 (log10)")
plt.savefig("plots/scatter_plot_star_movie.png", dpi = 700)
plt.tight_layout
plt.show()


# ### 1. 加上更多 features
# 加上評論數量、映期等其他 features，看看 performace 會不會變好

# In[66]:

movie_box["評論數量"] = movies_comments.groupby("movie_cht", as_index=False, sort=False).size().values


# In[67]:

movie_box.head()


# In[68]:

# 做 train/test split
X_train, X_test, y_train, y_test = train_test_split(movie_box[["評論數量", "平均星等", "映期"]], np.log10(movie_box["平均票房"]), random_state = 22)

# 訓練模型
reg.fit(X = X_train, y = y_train)

# 用 testing data 做預測
y_pred = reg.predict(X_test)

# 算出 testing data 與預測結果的 correlation
print(pearsonr(y_pred, y_test)[0])


# In[69]:

# 把預測結果畫成 Scatter plot
plt.scatter(x=y_pred, y=y_test)
plt.xlabel("y_pred")
plt.ylabel("y_true")
plt.text(6.9, 6.05, "六弄咖啡館")
plt.show()


# ## 2. 改成分類問題

# In[70]:

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# In[71]:

movie_box.head()


# In[72]:

movie_box["叫座"] = (movie_box["平均票房"] > movie_box["平均票房"].median()) * 1  # 設定 叫座 = 平均票房大於中位數


# In[73]:

X_train, X_test, y_train, y_test = train_test_split(movie_box[["評論數量", "平均星等", "映期"]], movie_box["叫座"], random_state = 22)


# In[74]:

clf = DecisionTreeClassifier(max_depth=3) # 限定最大深度不得超過 3 
clf.fit(X_train, y_train)


# In[75]:

print("feature importance")
print("評論數量: ",clf.feature_importances_[0])
print("平均星等: ",clf.feature_importances_[1])
print("映期: ",clf.feature_importances_[2])


# In[76]:

y_pred = clf.predict(X_test)  # 使用 testing data 做預測


# In[77]:

print("準確率: ", accuracy_score(y_test, y_pred)) # 計算 testing data 的準確率


# ### 簡單的 EDA

# In[78]:

# 評價低卻在票房排行榜上的電影
plt.rcParams['font.sans-serif']=['SimHei'] # 使用微軟正黑體
movies_comments.groupby("movie_cht")["star"].mean().sort_values().head(30).plot.bar()
plt.ylabel("average star")
plt.tight_layout()
plt.savefig("plots/average_star.png", dpi = 500)
plt.show()


# In[79]:

# 2016 與 2017 的平均票房差異 (2017 年度還沒結束)
movie_box.groupby("年度", as_index=False, sort=False)["平均票房"].mean()


# In[80]:

# 平均票房排行榜
movie_box.sort_values(by="平均票房", ascending=False)[["中文片名", "平均票房"]][:10].plot("中文片名", "平均票房", kind="bar")
plt.show()


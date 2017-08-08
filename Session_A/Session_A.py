
# coding: utf-8

# In[1]:

from bs4 import BeautifulSoup
import requests
import re


# # SESSION A: 爬蟲基本介紹

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


# 用 requests 抓取網頁並存在 response


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



# ---

# ---
# ## 範例 01: BeautifulSoup 的常用函數
# 將 HTML 抓下來後，其本身就是一個很大的字串，也當然可以用 regular expression 找出想要的資訊，But to make your life easier，我們可以使用 BeautifulSoup 這個 HTML parser，幫助解析 HTML，並使用許多便捷的 function，讓我們能夠更簡單的找到目標資訊
# 
# 小故事: 關於 BeautifulSoup 的名稱，是來自《愛麗絲夢遊仙境》裡一首詩的名稱，是由下圖中的左邊那隻假的海龜 (The Mock Turtle) 所唱出來的
# ![BS4](data/bs4.jpg)
# 補充資料
# 
# * 更多 BeautifulSoup 的 funcion 請參考[官方文檔 (有中文版)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
# 
# 以下的範例會示範兩個常用的函數: find(), find_all()

# In[12]:

response = requests.get("https://jimmy15923.github.io/example_page")
soup = BeautifulSoup(response.text, 'lxml')


# In[13]:

print(soup.find("td"))  # 找出第一個名為 td 的標籤
print("\n") # 換行符號，讓兩個 Print 的結果中間可以隔一個空行
print(soup.find("td").text)     # 找出第一個名為 td 的標籤並印出其文字內容


# In[14]:

print(type(soup.find_all("td"))) # find_all 回傳的是 list
print("\n")
print(soup.find_all("td")) # 找出所有 td 的標籤，並回傳 list


# In[15]:

print(soup.find_all("", {"class":"zzz"}))     # 不指定標籤，但找出所有屬性 class = "zzz" 的標籤
print("\n")
print(soup.find_all("", class_="zzz"))     # 不同寫法 但有一樣的結果


# In[16]:

print(soup.find_all("td")[2])  # 找到所有 td 的標籤，然後在第三個 (python index 從 0 開始) td 標籤中，再找出 a 標籤
print("\n")
print(soup.find_all("td")[2].find("a")) 


# In[17]:

print(soup.find_all(text = "python_crawler"))   # 找出所有標籤文字內容等於 python_crawler 的次數


# In[18]:

print(soup.find("a").attrs)     # 以 Dictionary (字典) 的形式儲存標籤的屬性
print(soup.find("a")['href'])     # 找出標籤屬性中的超連結


# In[19]:

print(soup.find("h1").text)


# ## 練習 01: 基本的 BeautifulSoup 使用 (8 mins)

# 請觀察範例網頁後，嘗試回答以下的問題
# 
# 
#     
#     jupyter notebook 的幾個實用 hotkey
#     * alt+enter: 執行 cell 並往下新增一個 cell
#     * shift+enter: 執行 cell 並往下一個 cell (不新增)
#     * esc+a: 往上新增一個 cell
#     * esc+b: 往下新增一個 cell
#     * esc+d+d (d 按兩次): 刪除 cell

# In[20]:

# 範例網頁: "https://jimmy15923.github.io/example_page"
# 1. 發送 requests.get，並將結果存在 response (或自己定義喜歡變數也可以)
# your codes
response = 

# 2. 將 response 的 HTML 文字放進 BeautifulSoup，並將結果存在 soup (或自己定義喜歡變數也可以)
# your codes
soup = 


# Q1. 請計算範例網頁中，共含有幾個名為 "td" 的標籤 (tags)?
# 
# Hint: Python 的 len() 函數可以幫忙計算 list 的長度。
# e.g. len([1,1,1]) 會回傳 3

# In[21]:

# your codes


# Q2. 請找出標籤 div，屬性 id = "id1" 的文字內容?

# In[22]:

# your codes


# Q3. 請找出 列3欄3 背後的超連結網址? (請使用 BeautifulSoup + 右鍵→檢查 來找，不要偷偷從網頁點開來看連結喔^^)

# In[23]:

# your codes


# ---
# ## 範例 02: regular expression
# regular expression 是在搜尋大量文字時非常好用的工具，可以快速回傳符合您要求的文字
# 
# 例如尋找任何像是電話號碼、E-mail 信箱的文字
# 
# 範例 02 會透過一些簡單的練習帶您了解 regular expression
# 
# 
# 
# 補充資料
# 
# * [更詳盡的 regular expression 符號解釋](https://atedev.wordpress.com/2007/11/23/%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%A4%BA%E5%BC%8F-regular-expression/)
# * [regular expression 線上練習網站](https://regexone.com/)
# * [常見的 regular expression 寫法](https://www.analyticsvidhya.com/blog/2017/03/extracting-information-from-reports-using-regular-expressons-library-in-python/)
# * 如果想擷取中文的 regular expression，可用[\u4e00-\u9fa5]，會幫你找出所有中文字，其結果如同英文的 [A-Z]

# regular expression 的符號意義
# ![BS4](data/reg.png)

# ### 以下的練習您可以使用 Python 內建的 re 套件，也可以使用這個[線上regular expression 測試器](https://regex101.com/)，可以看到比較互動式的結果，使用方法只要把 test_string 裡的內容複製到網頁下方的 TEST STRING 空格，然後在網頁上方的空格輸入您的  regular expression，就可以看到匹配的結果，左邊的 FLAVOR 記得選擇 python

# ### 範例 02-1:  *, +, {} 的用法
# \* 代表前面的字元可出現零次以上，而 + 則是代表前面的字元至少要出現一次以上，{m,n} 則是代表前面的字元可出現 m 次 ~ n 次

# In[24]:

pattern = "a+b*c"
test_string = 'find aabc, ac, skip abb, dd'
re.findall(pattern, test_string)


# ### 練習 02-1: *, +, {} 的用法
# 找出 abbbbc, bc，但不包含 c, acc
# 
# Hint: 思考一下要尋找的文字跟要濾除的文字，在字母之間有甚麼差異，先把 find 寫出來，再想辦法去掉要 skip 

# In[ ]:

### your codes
pattern = ""
test_string = 'find abbbbc, bc, skip c, acc'
re.findall(pattern, test_string)


# ### 範例 02-2: 找到英數字
# 中括號代表的意思是「這個字元可以是括號內的任何一個」，以數字為例，[0-9]代表這個字元可以是 0~9 之間的任意數字，如果是 [a-z] 則代表是小寫字母 a~z 之間的任意文字，聰明的你，應該可以猜出 [A-Z] 代表的是甚麼意思吧?

# In[26]:

pattern = "[0-9]+"
test_string = '12 drummers drumming, 11 pipers piping, 10 lords a-leaping'
re.findall(pattern, test_string)


# ### 練習 02-2: 找到英數字
# 在 test_string 中找出所有數字

# In[ ]:

# your codes
pattern = ""
test_string = 'abc123xyz, de123fine"123", test = 123'
re.findall(pattern, test_string)


# ### 範例 02-3: 找到文字
# 當有指定的文字需要搜尋，可透過 [ ] 搭配 *, + ,{} 進行搜尋

# In[28]:

pattern = "[cmf]an"
test_string = 'find: can, man, fan, skip: dan, ran, pan'
re.findall(pattern, test_string)


# In[29]:

pattern = "jim{2,5}y"
test_string = 'find: jimmy, jimmmy, jimmmmmy, skip: jimy'
re.findall(pattern, test_string)


# ### 練習 02-3: 找到文字
# 在 test_string 中找出 ABi, BBc, CNn，但不包含 ai, be, cd
# 
# Hint: 如果只找到一個大寫字母，想想甚麼符號代表可出現一次以上?

# In[ ]:

# your codes
pattern = ""
test_string = 'find: ABi, BBc, CNn, skip: ai, be, cd'
re.findall(pattern, test_string)


# ### 範例 02-4: 跳脫符號
# 當想要搜尋的字元，在 regular expression 已經是保留字的時候，就要使用跳脫符號
# 
# 例如你想要搜尋符合 "+" (點)的文字，但是 "+" 在 regular expression 是代表出現一次以上的意思
# 
# 這時在 "+" 前面加上 "\" (跳脫符號)，這樣做的話 regular expression 就會知道你是要尋找 "+" 

# In[31]:

pattern = ".{3}\."
test_string = 'find: 591., dot., yes., skip: non!'
re.findall(pattern, test_string)


# ### 練習 02-4: 跳脫符號
# 在 test_string 中找到 A+c, B+d, C+x

# In[ ]:

# your codes
pattern = ""
test_string = 'find: A+c, B+d, C+x'
re.findall(pattern, test_string)


# ### 範例 02-5: 條件式搜尋
# 當希望不同的搜尋條件都能夠符合時，可以使用「|」這個符號，代表左右邊只要任一一個條件符合，就會回傳

# In[33]:

pattern = "I love cats|I love dogs"
test_string = 'find: I love cats, I love dogs, skip: I love logs, I love cogs'
re.findall(pattern, test_string)


# ### 練習 02-5: 條件式搜尋
# 在 test_string 中找到 jimy, jimmmy, 但不包含 jimmy, jimmmmy

# In[ ]:

# your codes
pattern = ""
test_string = 'find: jimy, jimmmy, skip: jimmy, jimmmmy'
re.findall(pattern, test_string)


# ###  範例 02-6: Email 搜尋

# In[35]:

email_text = """
Big Data Analytics/ Deep LearningSocial Computing / Computational Social Science / Crowdsourcing
Multimediaand Network SystemsQuality of ExperienceInformation SecurityPh.D. candidate at NTU EEchihfan02-27883799#1602Camera CalibrationComputer VisionData
Analysiscmchang02-27883799#1671System OptimizationMachine LearningyusraBig data
analysiscclin02-27883799#1668Data Analysisrusi02-27883799#1668Government Procurement ActFinancial
Managementkatekuen02-27883799#1602AdministrationEvent Planningseanyu02-27883799#1668Data 
AnalysisPsychology & NeuroscienceMarketingxinchinchenEmbedded Systemkyoyachuan062602-27883799
#1601FinTechActuarial ScienceData Analysiskai0604602-27883799#1601Data AnalysisMachine Learningchloe02-27839427Accountingafun02-27883799 afun@iis.sinica.edu.tw
#1673Data AnalysisWeb developmentyunhsu198902-27883799#1668MarketingTIGP Ph.D. Fellow at Academia Sinica & NCCUbaowalyMachine LearningData AnalysisSocial Computingchangyc1427883799#1678
Data Analysisjimmy1592302-2788379 jimmy15923@iis.sinica.com.tw#1688Data AnalysisjasontangAnalysisMachine Learninguchen02-27883799#1668Deep Learningpjwu02-27883799#1604Computational PhotographyData Analysis
"""


# In[36]:

re.findall("([A-Za-z0-9._]+@[A-Za-z.]+(com|edu)\.tw)", email_text)


# ## 練習 02: regular expression (8 mins)

# 請觀察[518 黃頁網](http://yp.518.com.tw/service-life.html?ctf=10)，並找出所有店家的電話號碼 (包含分機)
# 
# Hint
# * 想要的資訊都藏在哪些標籤下?
# * 把所有可能包含電話的標籤內容全部找出來後，用下面的 code 變成一個字串
# * text = " ".join(text_list)，這段 code 可以將 list of string 全部變為一個字串
# * 變成字串後就可以用剛剛學的 re.findall() 找出我們要的目標囉!

# In[37]:

# 如果忘記怎麼寫 requests 或 BeautifulSoup，可以參考

# response = requests.get("http://yp.518.com.tw/service-life.html?ctf=10")
# print(response.encoding)

# soup = BeautifulSoup(response.text, "lxml")


# In[38]:

# your codes


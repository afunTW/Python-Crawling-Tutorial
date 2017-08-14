
# coding: utf-8

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

# ### 以下的練習您可以使用 python 內建的 re 套件，也可以使用這個[線上regular expression 測試器](https://regex101.com/)，可以看到比較互動式的結果，使用方法只要把 test_string 裡的內容複製到網頁下方的 TEST STRING 空格，然後在網頁上方的空格輸入您的  regular expression，就可以看到匹配的結果，左邊的 FLAVOR 記得選擇 python

# ### 範例 02-1:  *, +, {} 的用法
# \* 代表前面的字元可出現零次以上，而 + 則是代表前面的字元至少要出現一次以上，{m,n} 則是代表前面的字元可出現 m 次 ~ n 次

# In[24]:

pattern = "a+b*c"
test_string = 'find aabc, ac, skip abb, dd'
re.findall(pattern, test_string)


# ### 練習 02-1: *, +, {} 的用法
# 在 test_string 中找出 abbbbc, bc，但不包含 c, acc
# 
# Hint: 思考一下要尋找的文字跟要濾除的文字，在字母之間有甚麼差異，先把 find 寫出來，再想辦法去掉要 skip 

# In[20]:

### your codes
pattern = "a*b+c"
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

# In[21]:

# your codes
pattern = "[1-3]+"
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

# In[22]:

# your codes
pattern = "[A-Z]+[a-z]"
test_string = 'find: ABi, BBc, CNn, skip: ai, be, cd'
re.findall(pattern, test_string)


# ### 範例 02-4: 跳脫符號
# 當想要搜尋的字元，在 regular expression 已經是保留字的時候，就要使用跳脫符號
# 
# 例如你想要搜尋符合 "+" (加號) 這個文字，但是 "+" 在 regular expression 是代表出現一次以上的意思
# 
# 這時在 "+" 前面加上 "\" (跳脫符號)，這樣做的話 regular expression 就會知道你是要尋找 "+" 

# In[31]:

pattern = ".{3}\."
test_string = 'find: 591., dot., yes., skip: non!'
re.findall(pattern, test_string)


# ### 練習 02-4: 跳脫符號
# 在 test_string 中找到 A+c, B+d, C+x

# In[23]:

# your codes
pattern = "[A-Z]\+[a-z]"
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

# In[24]:

# your codes
pattern = "jimy|jim{3}y"
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


# In[2]:

# your codes
import requests
from bs4 import BeautifulSoup

response = requests.get("http://yp.518.com.tw/service-life.html?ctf=10") # requests 518 網頁 並拿到 response
print(response.encoding) # 印出 encoding 結果
soup = BeautifulSoup(response.text, "lxml")  # 將 HTML 丟給 BeautifulSoup 作解析


# In[ ]:

all_phone_text = [tag.text for tag in soup.find_all("li",class_="comp_tel")]

all_phone_text ="".join(all_phone_text)

phone_number = re.findall("0[1-9]+-[0-9]+", all_phone_text)
print(phone_number)


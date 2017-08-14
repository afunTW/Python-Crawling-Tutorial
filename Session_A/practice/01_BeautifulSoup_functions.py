
# coding: utf-8

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

# In[3]:

response = requests.get("https://jimmy15923.github.io/example_page")
soup = BeautifulSoup(response.text, 'lxml')


# In[4]:

print(soup.find("td"))  # 找出第一個名為 td 的標籤
print("\n") # 換行符號，讓兩個 Print 的結果中間可以隔一個空行
print(soup.find("td").text)     # 找出第一個名為 td 的標籤並印出其文字內容


# In[5]:

print(type(soup.find_all("td"))) # find_all 回傳的是 list
print("\n")
print(soup.find_all("td")) # 找出所有 td 的標籤，並回傳 list


# In[6]:

print(soup.find_all("", {"class":"zzz"}))     # 不指定標籤，但找出所有屬性 class = "zzz" 的標籤
print("\n")
print(soup.find_all("", class_="zzz"))     # 不同寫法 但有一樣的結果


# In[8]:

print(soup.find_all("td")[2].prettify())  # 找到所有 td 的標籤，然後在第三個 (python index 從 0 開始) td 標籤中，再找出 a 標籤
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

# 請觀察[範例網頁](https://jimmy15923.github.io/example_page)後，嘗試回答以下的問題
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
# 1. 發送 requests.get，並將結果存在 response (或自己定義喜歡的變數也可以)
# your codes
response = 

# 2. 將 response 的 HTML 文字放進 BeautifulSoup，並將結果存在 soup (或自己定義喜歡的變數也可以)
# your codes
soup = 


# Q1. 請計算範例網頁中，共含有幾個名為 "td" 的標籤 (tags)?
# 
# Hint: Python 的 len() 函數可以幫忙計算 list 的長度。
# e.g. len([1,1,1]) 會回傳 3

# In[21]:

# your codes


# Q2. 請找出**標籤 div，屬性 id = "id1"** 的文字內容?

# In[22]:

# your codes


# Q3. 請找出**列3欄3**背後的超連結網址? (請使用 BeautifulSoup + 右鍵→檢查 來找到那個標籤，不要偷偷從網頁點開連結來看喔^^)

# In[23]:

# your codes


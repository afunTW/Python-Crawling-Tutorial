import requests
from bs4 import BeautifulSoup
from urllib.request import build_opener
from urllib.request import install_opener
from urllib.request import urlretrieve

# 取得目標網頁
response = requests.get('https://gushi.tw/hu-shih-memorial-hall/')

# 透過 Beautifulsoup 解析網頁
soup = BeautifulSoup(response.text, 'lxml')

# 取得所有的 p tag 與 img tag
text = soup.find_all('p')
image = soup.find_all('img')

# 檢查第一個 img tag
print(u'圖片 tag:')
print(image[0].prettify())

# 取得第一個圖片位置資訊
print(u'圖片位置資訊:')
print(image[0]['src'])

# 增加 opener 偽裝成瀏覽器發送請求
opener = build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36')]
install_opener(opener)

# 下載圖片
urlretrieve(image[0]['src'], 'logo.png')

import requests
from bs4 import BeautifulSoup
from urllib.request import build_opener
from urllib.request import install_opener
from urllib.request import urlretrieve

# 取得目標網頁
response = requests.get('https://gushi.tw/hu-shih-memorial-hall/')

# 透過 Beautifulsoup 解析網頁
soup = BeautifulSoup(response.text, 'lxml')

# 取得所有的圖片 tag
image = # 請透過 Beautifulsoup 找到所有的圖片 tag

# 檢查第一個 img tag
print(u'圖片 tag:')
print(image[0].prettify())

# 增加 opener 偽裝成瀏覽器發送請求
opener = build_opener()
opener.addheaders = # 請尋找自己的 User-Agent 並填入
install_opener(opener)

# 下載圖片
urlretrieve(, ) # 請填入要下載的圖片位置與存檔的檔案名稱

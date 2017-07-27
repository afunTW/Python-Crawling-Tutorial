import requests
from bs4 import BeautifulSoup


# 取得目標網頁
response = requests.get('https://gushi.tw/hu-shih-memorial-hall/')

# 透過 Beautifulsoup 解析網頁
soup = BeautifulSoup(response.text, 'lxml')

# 取得所有的 p tag 與 img tag
text = soup.find_all('p')
image = soup.find_all('img')

# 檢查第四個 p tag 內容
print(u'文字 tag:')
print(text[3].prettify())

# 取得第四個 p tag 文字資訊
print(u'文字資訊:')
print(text[3].text)

print('----------')
# 檢查第一個 img tag
print(u'圖片 tag:')
print(image[0].prettify())

# 取得第一個圖片位置資訊
print(u'圖片位置資訊:')
print(image[0]['src'])

import re
import requests

from bs4 import BeautifulSoup
from urllib.parse import urlparse

url = 'http://140.112.115.12/exam/graduate'
response = requests.get(url)
soup = BeautifulSoup(response.text)

# 取得所有 img tag 中 src 符合 application-pdf.png 片段的
images = soup.find_all('img',{'src': re.compile('application-pdf\.png')})

# 查看網頁網址的拆解片段
print(response.url, '\n\n', urlparse(response.url), '\n-----\n')

# 查看第1張圖片網址的拆解片段
image_url = images[0].parent['href']
print(image_url, '\n\n', urlparse(image_url))

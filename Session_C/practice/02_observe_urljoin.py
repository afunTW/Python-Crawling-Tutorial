import re
import requests

from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin

url = 'http://140.112.115.12/exam/graduate'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# 取得所有 img tag 中 src 符合 application-pdf.png 片段的
images = 

# 查看網頁網址的拆解片段
print('original url: {}'.format(response.url))
print('urlparse url: {}'.format(urlparse(response.url)))
print()

# 查看第 1 張圖片網址的拆解片段
image_url = 
print('original url: {}'.format(image_url))
print('urlparse url: {}'.format(urlparse(image_url)))
print()

# 取得絕對路徑
print(urljoin(response.url, image_url))
# print(urljoin(response.url, '106g/'))
# print(urljoin(response.url, '/106g/'))
# print(urljoin(response.url, '//facebook.com'))
# print(urljoin(response.url, '../'))
# print(urljoin(response.url, '../../'))

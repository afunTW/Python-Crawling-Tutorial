import requests

from bs4 import BeautifulSoup
from PIL import Image
from urllib.request import urlretrieve

# 透過 streaming 的方式取得圖片
url = 'http://imgur.com/rqCqA.png'
response = requests.get(url, stream=True)
print(url)

# 根據 Image.open 所需格式讀取圖片, 並取得圖片副檔名
image = Image.open(response.raw)
print(image.format)

# 根據 '/' 將網址分段
split_url = url.split('/')
print(split_url)

# 從分段的網址中取得原始檔案名稱
orig_filename = split_url[-1]
print(orig_filename)

# 從原始檔案名稱中根據 '.' 分成檔名跟副檔名
split_filename = orig_filename.split('.')
print(split_filename)

# 取得原始檔名
filename = split_filename[0]
print(filename)

# 組合原始檔名與正確的副檔名
download_filename = '{}.{}'.format(filename, image.format.lower())
print(download_filename)

# 下載圖片
urlretrieve(url, download_filename)

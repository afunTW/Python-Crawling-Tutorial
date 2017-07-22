import requests
from bs4 import BeautifulSoup
from PIL import Image

# 透過 streaming 的方式取得圖片
url = 'http://imgur.com/rqCqA.png'
response = requests.get(url, stream=True)

# 根據 Image.open 所需格式讀取圖片, 並取得圖片副檔名
image = Image.open(response.raw)
print(image.format)

# from io import BytesIO
# # 取得圖片
# url = 'http://imgur.com/rqCqA.png'
# response = requests.get(url)
# # 根據 Image.open 所需格式讀取圖片, 並取得圖片副檔名
# image = Image.open(BytesIO(response.content))
# print(image.format)

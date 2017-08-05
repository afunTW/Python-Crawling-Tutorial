import requests

from PIL import Image
from urllib.request import urlretrieve

# 透過 streaming 的方式取得圖片
url = 'http://imgur.com/rqCqA.png'
response = 
print('url:', url)

# 根據 Image.open 所需格式讀取圖片, 並取得圖片副檔名
image = 
print('get image format:', image.format)

# 根據 '/' 將網址分段
split_url = 
print('split url by "/":', split_url)

# 從分段的網址中取得原始檔案名稱
orig_filename = 
print('filename: ', orig_filename)

# 從原始檔案名稱中根據 '.' 分成檔名跟副檔名
split_filename = 
print('split filename by ".":', split_filename)

# 取得原始檔名
filename = 
print('filename:', filename)

# 組合原始檔名與正確的副檔名
download_filename = 
print('concate filename:', download_filename)

# 下載圖片
urlretrieve( )


# # BONUS: 不透過 stream 讓 Image 讀圖片的方式
# from io import BytesIO
# # 取得圖片
# url = 'http://imgur.com/rqCqA.png'
# response = requests.get(url)
# # 根據 Image.open 所需格式讀取圖片, 並取得圖片副檔名
# image = Image.open(BytesIO(response.content))
# print(image.format)

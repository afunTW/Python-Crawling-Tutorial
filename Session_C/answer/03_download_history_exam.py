import re
import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlretrieve

url = 'http://140.112.115.12/exam/graduate'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# 取得所有 img tag 中 src 符合 application-pdf.png 片段的
images = soup.find_all('img',{'src': re.compile('application-pdf\.png')})

# 顯示進度的 callback
def check_percentage(chunk, chunk_size, remote_size):
    percentage = 100.0 * chunk * chunk_size / remote_size
    if percentage > 100.0:
        percentage = 100.0
    print('Download...{:.2f}%'.format(percentage))

for image in images:
    # 將相對路徑轉換成絕對路徑
    real_url = urljoin(response.url, image.parent['href'])

    # 做字串處理取得檔名
    filename = real_url.split('/')[-1]
    filename = filename.split('&')[0]

   # 下載檔案
    print('Download file: {}'.format(filename))
    urlretrieve(real_url, filename, check_percentage)

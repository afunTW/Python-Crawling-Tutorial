import re
import requests

from bs4 import BeautifulSoup

url = 'http://140.112.115.12/exam/graduate'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# 取得所有 img tag 中 src 符合 application-pdf.png 片段的
images = soup.find_all('img',{'src': re.compile('application-pdf\.png')})

for image in images:
    print(image.parent.prettify())

import requests
from bs4 import BeautifulSoup

# 對範例網站送出 request 並把回應的網頁內容送到解析器
url = 'https://afuntw.github.io/demo-crawling/demo-page/ex4/index1.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# 搜尋 id 是 first 的 h2 tag
h2 = soup.find_all('h2', id="first")
print(h2[0].text)

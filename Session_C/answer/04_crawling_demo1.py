import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://afuntw.github.io/demo-crawling/demo-page/ex1/index1.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
h1_answer = []

# 取得頁面中所有的 h1 tag 並將結果存入 h1_answer
h1 = soup.find_all('h1')
for tag in h1:
    h1_answer.append(tag.text)

print('Current URL: {}'.format(url))
print('Get h1 tags: {}'.format(h1_answer))
print()

# 取得頁面中的 a tag
links = soup.find_all('a', href=True)

# 依序對每個 a tag 做處理
for link in links:
    # 透過 urljoin 確認超連結是絕對位置
    new_url = urljoin(url, link['href'])

    # 對超連結送出 request 得到新的網頁
    new_response = requests.get(new_url)
    new_soup = BeautifulSoup(new_response.text, 'lxml')

    # 在新網頁中取得 h1 tag 並將結果存入 h1_answer
    new_h1 = new_soup.find_all('h1')
    for tag in new_h1:
        h1_answer.append(tag.text)

    print('Get new URL: {}'.format(new_url))
    print('Get h1 tags: {}'.format(h1_answer))
    print()

print('Final h1 tags answer: {}'.format(h1_answer))

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def recursive_h1_url(url, answer):
    print('Begin with URL: {}'.format(url))

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    links = soup.find_all('a', href=True)
    for link in links:
        # 透過 urljoin 確認超連結是絕對位置
        new_url = urljoin(url, link['href'])
        recursive_h1_url(new_url, answer)

    # 取得當前頁面中的 h1 tag 並將結果存入 answer
    h1 = soup.find_all('h1')
    for h1_tag in h1:
        answer.append(h1_tag)

    print('Get h1 tag: {}'.format(answer))
    print('End with URL: {}'.format(url))
    print()

def h1_recursive_url(url, answer):
    print('Begin with URL: {}'.format(url))

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    # 取得當前頁面中的 h1 tag 並將結果存入 answer
    h1 = soup.find_all('h1')
    for h1_tag in h1:
        answer.append(h1_tag)

    links = soup.find_all('a', href=True)
    for link in links:
        # 透過 urljoin 確認超連結是絕對位置
        new_url = urljoin(url, link['href'])
        h1_recursive_url(new_url, answer)

    print('Get h1 tag: {}'.format(answer))
    print('End with URL: {}'.format(url))
    print()

answer_1 = []
answer_2 = []
url = 'https://afuntw.github.io/demo-crawling/demo-page/ex1/index1.html'
print('========================================> recursive => get h1')
recursive_h1_url(url, answer_1)
print('========================================> get_h1 => recursive')
h1_recursive_url(url, answer_2)

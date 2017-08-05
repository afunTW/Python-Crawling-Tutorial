import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

wait_list = ['https://afuntw.github.io/demo-crawling/demo-page/ex2/index1.html']
viewed_list = []
h1_answer = []

# 當 wait list 裏面還有網址發生的情況
while wait_list != []:

    # 取出 wait list 裏面的第一個網址
    url = 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    print('Current URL: {}'.format(url))

    # 將當前頁面存入已經看過的清單
    

    # 取得當前頁面中的 h1 tag 並將結果存入 h1_answer
    h1 = soup.find_all('h1')
    for tag in h1:
        

    # 取得頁面中的 a tag
    links = 
    for link in links:

        # 透過 urljoin 確認超連結是絕對位置
        new_url = 

        # 新的 url 要符合的條件
        # 1. wait_list 裏面沒有出現
        # 2. viewed_list 也沒有出現
        # 之後再將新發現的超連結存入 wait list
        

    print('Get h1 tags: {}'.format(h1_answer))
    print('URL wait list: {}'.format(wait_list))
    print('URL viewed list: {}'.format(viewed_list))
    print()

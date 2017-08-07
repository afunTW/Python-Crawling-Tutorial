import requests
import re

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse

wait_list = ['https://afuntw.github.io/demo-crawling/demo-page/ex3/index1.html']
viewed_list = []
h2_answer = []

# 當 wait list 裏面還有網址發生的情況
while wait_list != []:

    # 取出 wait list 裏面的第一個網址
    url = wait_list.pop(0)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    print('Current URL: {}'.format(url))

    # 將當前頁面存入已經看過的清單
    viewed_list.append(url)

    # 取得當前頁面中的 h2 tag 並將結果存入 h2_answer
    h2 = soup.find_all('h2')
    for tag in h2:
        h2_answer.append(tag.text)

    # 取得頁面中的 a tag
    links = soup.find_all('a', href=True)
    for link in links:

        new_url = urljoin(url, link['href'])

        # 過濾錨點, 不需要再對相同的網頁送 request
        check_anchor = not re.match('#.*', link['href'])

        # 過濾程式碼
        check_code = not re.match('^javascript.*', link['href'])

        # 過濾協定, 只取 http 或是 https
        # Hint: 若原本 href 是相對路徑則沒有協定, 要先透過 urljoin 取得絕對路徑
        check_protocol = urlparse(new_url).scheme in ['http', 'https']

        # 實際過濾的判斷式
        if check_anchor and check_code and check_protocol:

            # 新的 url 要符合的條件
            # 1. wait_list 裏面沒有出現
            # 2. viewed_list 也沒有出現
            if new_url not in wait_list and new_url not in viewed_list:

                # 將新發現的超連結存入 wait list
                wait_list.append(new_url)

    print('Get h2 tags: {}'.format(h2_answer))
    print('URL wait list: {}'.format(wait_list))
    print('URL viewed list: {}'.format(viewed_list))
    print()

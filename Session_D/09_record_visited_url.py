import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

wait_list = ['https://afuntw.github.io/demo-crawling/demo-page/ex2/index1.html']
viewed_list = []
answer = []

# 當 wait list 裏面還有網址發生的情況
while wait_list != []:

    # 取出 wait list 裏面的第一個網址
    url = wait_list.pop(0)
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    print('Current website: ', url)

    # 將當前頁面存入已經看過的清單
    viewed_list.append(url)

    # 取得當前頁面中的 h1 tag 並將結果存入 answer
    h1 = soup.find_all('h1')
    for tag in h1:
        answer.append(tag.text)

    # 取得頁面中的 a tag
    links = soup.find_all('a')
    for link in links:

        # 如果 a tag 中有超連結
        if link.has_attr('href'):

            # 透過 urljoin 確認超連結是絕對位置
            new_url = urljoin(url, link['href'])

            # 新的 url 要符合的條件
            # 1. wait_list 裏面沒有出現
            # 2. viewed_list 也沒有出現
            if new_url not in wait_list and new_url not in viewed_list:

                # 將新發現的超連結存入 wait list
                wait_list.append(new_url)

    print('Answer: ', answer)
    print('Wait list: ', wait_list)
    print('Viewed list', viewed_list, '\n')

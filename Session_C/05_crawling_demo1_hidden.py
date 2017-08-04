import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

wait_list = ['https://afuntw.github.io/demo-crawling/demo-page/ex1/index1.html']
answer = []

# 當 wait list 裏面還有網址發生的情況
while wait_list != []:

    # 取出 wait list 裏面的第一個網址
    url = wait_list.pop(0)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    print('Current website: ', url)

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

            # 將新發現的超連結存入 wait list
            wait_list.append(new_url)

    print('Answer: ', answer)
    print('Wait list: ', wait_list, '\n')

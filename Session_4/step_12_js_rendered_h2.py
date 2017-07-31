import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# 對範例網站送出 request 並把回應的網頁內容送到解析器
url = 'https://afuntw.github.io/demo-crawling/demo-page/ex4/index1.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# 搜尋 id 是 first 的 h2 tag
h2 = soup.find_all('h2', id="first")
print('static get:', h2[0].text)



# Selenium
# 打開 Chrome 瀏覽器
driver = webdriver.Chrome('../webdriver/chromedriver')

# 將瀏覽器視窗最大化
driver.maximize_window()

# 等待時間設定為 10 秒, 每個 session 只需要呼叫一次這個 function
driver.implicitly_wait(10)

# 對目標網站送 request
driver.get(url)

# 搜尋 id 是 first 的 h2 tag
selenium_h2 = driver.find_element_by_id('first')
print('selenium get: ', selenium_h2.text)

# 關掉瀏覽器
driver.quit()

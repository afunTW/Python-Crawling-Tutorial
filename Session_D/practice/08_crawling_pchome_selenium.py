import os
from selenium import webdriver
from selenium.webdriver.common.by import By


# PC home 商用筆電
url = 'http://24h.pchome.com.tw/region/DHBE'

# 打開 Chrome 瀏覽器
driver = webdriver.Chrome(os.path.abspath('../webdriver/chromedriver'))

# 將瀏覽器視窗最大化


# 對目標網站送 request


# 取得任何位置的dl tag, id = Block12COntainer50 底下的所有 dd tag
items = 

# 逐一對每個 tag 處理
for item in items:

    # 品名在當前 tag 底下的 div 底下的 h5 底下的 a 裏面的 text
    title = 

    # 價格在當前 tag 底下的 div 底下的 ul 底下的 li 底下的第2層 span
    price = 

    # 如果品名與價格有任一是空值, 則不處理
    if title and price:
        print('{} - {}'.format(title, price))

# 關掉瀏覽器
driver.quit()

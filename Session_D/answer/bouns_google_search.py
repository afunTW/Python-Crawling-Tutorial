from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pprint import pprint


# google 首頁
url = 'https://google.com'

# 打開 Chrome 瀏覽器
driver = webdriver.Chrome('../webdriver/chromedriver')

# 瀏覽器視窗最大化
driver.maximize_window()

# 最大等待時間 10 s
driver.implicitly_wait(10)

# 對目標網站送 request
driver.get(url)

# 取得 google 搜尋 tag
search_input  = driver.find_element(By.ID, 'lst-ib')

# 在搜尋欄位上輸入 datasci
search_input.send_keys('datasci')

# 在搜尋欄位上按下 ENTER
search_input.send_keys(Keys.ENTER)

# 透過 XPath 取得所有網站標題與超連結
links = driver.find_elements(By.XPATH, '//h3[@class="r"]/a[@href]')

# 另外一種透過 copy XPath 取得的網站標題與超連結
# links = driver.find_elements(By.XPATH, '//*[@id="rso"]/div[2]/div/div/div/div/h3 | //*[@id="rso"]/div[1]/div/div/div/div/h3')

for link in links:
    try:
        # 取得網站標題
        title = link.text

        # 取得網站超連結
        url = link.get_attribute('href')

        # 組合並印出訊息
        title_url = (title, url)
        print(title_url)
    except Exception as e:
        print(e)
        driver.quit()
        continue

# 關掉瀏覽器
driver.quit()

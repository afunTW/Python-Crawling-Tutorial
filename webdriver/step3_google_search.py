from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pprint import pprint


url = 'https://google.com'
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(url)

search_input  = driver.find_element(By.ID, 'lst-ib')
print(search_input.get_attribute('outerHTML'))

search_input.send_keys('datasci')
search_input.send_keys(Keys.ENTER)
print(driver.current_url)

links = driver.find_elements(By.XPATH, "//h3[@class='r']/a[@href]")
# import time
# time.sleep(10)
# links = driver.find_elements(By.XPATH, "//a[@href]")
for link in links:
    try:
        title = link.text
        url = link.get_attribute('href')
        title_url = (title, url)
        print(title_url)
    except Exception as e:
        print(e)
        continue
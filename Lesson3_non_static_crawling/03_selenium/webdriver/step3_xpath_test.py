from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint


url = 'https://gushi.tw'
driver = webdriver.PhantomJS()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('file:///home/afun/github/dsc-crawling/Lesson3_non_static_crawling/03_selenium/webdriver/gushi.html')
# print(driver.find_element(By.XPATH, '//div').get_attribute('outerHTML'), '\n----------\n')
# print(driver.find_element(By.XPATH, '//div/div').get_attribute('outerHTML'), '\n----------\n')
# print(driver.find_element(By.XPATH, '//*[@id="menu-item-33737"]').get_attribute('outerHTML'), '\n---------\n')
# print(driver.find_element(By.XPATH, '//*[@id="menu-item-33737"]/..').get_attribute('outerHTML'), '\n---------\n')
# print(driver.find_element(By.XPATH, '//*[@id="menu-item-33737"]/../li[3]').get_attribute('outerHTML'), '\n---------\n')
# print(driver.find_element(By.XPATH, '//*[@id="menu-item-33737"]/../li[last()]').get_attribute('outerHTML'), '\n---------\n')
# print(driver.find_element(By.XPATH, '//*[@id="menu-item-33737"]/../li[position() > 2]').get_attribute('outerHTML'), '\n---------\n')
driver.quit()

from selenium import webdriver
from pprint import pprint


url = 'https://gushi.tw'
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(50)
driver.get(url)
pprint(driver.find_elements_by_class_name('start_animation'))
print()
pprint(driver.find_elements_by_css_selector('.start_animation'))
print()
pprint(driver.find_elements_by_css_selector('.t-inside.style-color-xsdn-bg.animate_when_almost_visible.bottom-t-top.start_animation'))
print()
pprint(driver.find_elements_by_xpath('//*[@id="index-184108"]/div/div/div[1]/div'))

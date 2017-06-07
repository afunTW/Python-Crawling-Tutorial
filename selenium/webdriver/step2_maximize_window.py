# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SearchWaitClick(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com.tw/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_search_wait_click(self):
        driver = self.driver
        driver.get(self.base_url + "/search?client=ubuntu&channel=fs&q=%E7%A0%94%E4%B9%8B%E6%9C%89%E7%89%A9&ie=utf-8&oe=utf-8&gfe_rd=cr&ei=JQY4WbbXLOL88weg7IzoDQ")
        driver.find_element_by_css_selector("h3.r > a").click()
        driver.find_element_by_xpath("//ul[@id='primary-menu']/li[3]/a/span/span").click()
        driver.find_element_by_xpath("//div[@id='content']/div[2]/div[6]/article/div/p/a/i").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

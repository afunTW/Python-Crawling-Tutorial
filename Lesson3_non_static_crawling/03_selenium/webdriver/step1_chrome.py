# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Step0OriginalFf(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com.tw/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_step0_original_ff(self):
        driver = self.driver
        driver.get(self.base_url + "/search?client=ubuntu&channel=fs&q=%E6%95%85%E4%BA%8B&ie=utf-8&oe=utf-8&gfe_rd=cr&ei=BrpoWeTTHZGC8AW25ZWYBw")
        driver.find_element_by_link_text(u"故事| 寫給所有人的歷史").click()
        driver.find_element_by_link_text(u"全部文章").click()
        driver.find_element_by_css_selector("div.t-overlay-content").click()
    
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

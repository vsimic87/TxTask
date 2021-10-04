from selenium import webdriver
import browser
import unittest


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(desired_capabilities=browser.Chrome)
        self.driver.maximize_window()
        self.driver.get("https://doodle.com/")

    def tearDown(self):
        self.driver.quit()
